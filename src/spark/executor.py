"""PySpark Job"""
from typing import List, Tuple

from pyspark.sql import SparkSession, Row
from pyspark.sql import functions as F
from pyspark.sql.window import Window


class PySparkExecutor:
    """PySparkExecutor class to hold Spark logic"""

    @staticmethod
    def submit(scorecards: List[Tuple[str, int]], output: str) -> None:
        """
        Submit Spark Job
        @param scorecards: list - Scorecards from RankTableProcessor
        @param output: str - Output data location for spark job

        @return: None
        """
        spark = SparkSession.builder.master("local[*]").appName("RankApp").getOrCreate()
        raw_dataframe = spark.createDataFrame(scorecards, schema=["team", "points"]).repartition(2)
        dataframe_with_total_points = raw_dataframe.groupBy("team").agg(F.sum("points").alias("points"))
        window = Window.partitionBy().orderBy(F.desc("points"))
        final = (
            dataframe_with_total_points.withColumn("rank", F.rank().over(window))
            .withColumn("suffix", F.when(dataframe_with_total_points.points == 1, "pt").otherwise("pts"))
            .sort("rank", "team")
            .select("rank", "team", "points", "suffix")
        )
        result_df = final.rdd.map(lambda row: Row(f"{row[0]}. {row[1]}, {row[2]} {row[3]}")).toDF().coalesce(1)
        result_df.coalesce(1).write.mode("overwrite").format("text").save(output)
        spark.stop()
