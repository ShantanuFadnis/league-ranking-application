from unittest import TestCase
import glob

from src.spark.executor import PySparkExecutor


class TestPySparkExecutor(TestCase):
    def test_submit(self):
        data = [
            ("Lions", 1),
            ("Snakes", 1),
            ("Tarantulas", 3),
            ("FC Awesome", 0),
            ("Lions", 1),
            ("FC Awesome", 1),
            ("Tarantulas", 3),
            ("Snakes", 0),
            ("Lions", 3),
            ("Grouches", 0),
        ]
        PySparkExecutor.submit(data, "output")
        self.assertListEqual(list(open(glob.glob("output/*.txt")[0])), list(open("tests/fixtures/out.txt")))
