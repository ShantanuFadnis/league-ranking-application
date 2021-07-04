""" Rank Table Processor Module """
from typing import List, Tuple

from utils.logger import init_logging_object  # type:ignore
from spark.executor import PySparkExecutor  # type:ignore

LOG = init_logging_object(__name__)


class RankTableProcessor:
    """class RankTableProcessor to hold data processing logic"""

    scorecards: List[Tuple[str, int]] = []

    @staticmethod
    def pre_process(row: str) -> None:
        """
        pre_process() - Method to do initial processing of data.
        @param row: str - A row from input text file
        @return: None
        """
        left, right = row.split(",")
        team_left, team_left_score = left.strip().rsplit(" ", 1)
        team_right, team_right_score = right.strip().rsplit(" ", 1)

        result = RankTableProcessor._get_winning_team(int(team_left_score), int(team_right_score))
        RankTableProcessor._update_scorecard(team_left, team_right, result)

    @staticmethod
    def _get_winning_team(score1: int, score2: int) -> str:
        """
        _get_winning_team() - Method to compare scores of both teams and return a decision.
        @param score1: int - Team 1 score
        @param score2: int - Team 2 score

        @return: str - Decision made on compairing two scores
        """
        decision = "TIE"
        if score1 > score2:
            decision = "LEFT"
        elif score1 < score2:
            decision = "RIGHT"
        return decision

    @classmethod
    def _update_scorecard(cls, left: str, right: str, result: str) -> None:
        """
        _update_scorecard() - Method to maintain a scorecard for each team.
        @param left: str - Team 1 name
        @param right: str - Team 2 name
        @param result: str - Decision made on compairing both team scores

        @return: None
        """
        left_pts = 0
        right_pts = 0
        if result == "TIE":
            left_pts, right_pts = 1, 1
        elif result == "LEFT":
            left_pts = 3
        elif result == "RIGHT":
            right_pts = 3
        cls.scorecards.append((left, left_pts))
        cls.scorecards.append((right, right_pts))

    @classmethod
    def calculate_rank(cls, out_file_path: str) -> None:
        """
        calculate_rank() - Method to calculate rank on the scorecards.
        Submits a spark job.

        @param out_file_path: str - Output data location
        """
        PySparkExecutor.submit(cls.scorecards, out_file_path)
