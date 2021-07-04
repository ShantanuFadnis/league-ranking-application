from unittest import TestCase
from unittest.mock import patch
from src.processors import RankTableProcessor


class RankTableProcessorTest(TestCase):
    maxDiff = None

    def setUp(self):
        RankTableProcessor.scorecards.clear()

    @patch("src.processors.RankTableProcessor._get_winning_team")
    @patch("src.processors.RankTableProcessor._update_scorecard")
    def test_pre_process(self, mock_update_scorecard, mock_get_winning_team):
        mock_update_scorecard.return_value = None
        mock_get_winning_team.return_value = "RIGHT"
        RankTableProcessor.pre_process("Foo 10, Bar 150")
        mock_get_winning_team.assert_called_with(10, 150)
        mock_update_scorecard.assert_called_with("Foo", "Bar", "RIGHT")

    def test_get_winning_team(self):
        test_cases = [
            {
                "input": (10, 30),
                "output": "RIGHT",
            },
            {
                "input": (30, 10),
                "output": "LEFT",
            },
            {
                "input": (10, 10),
                "output": "TIE",
            },
        ]
        for test_case in test_cases:
            res = RankTableProcessor._get_winning_team(test_case["input"][0], test_case["input"][1])
            self.assertEqual(res, test_case["output"])

    def test_update_scorecard(self):
        test_cases = [
            {"left": "Foo", "right": "Bar", "result": "LEFT"},
            {"left": "Foo", "right": "Bar", "result": "RIGHT"},
            {"left": "Foo", "right": "Bar", "result": "TIE"},
        ]
        expected_scorecards = [("Foo", 3), ("Bar", 0), ("Foo", 0), ("Bar", 3), ("Foo", 1), ("Bar", 1)]
        for test_case in test_cases:
            RankTableProcessor._update_scorecard(test_case["left"], test_case["right"], test_case["result"])
        self.assertEqual(expected_scorecards, RankTableProcessor.scorecards)

    @patch("src.processors.PySparkExecutor.submit")
    def test_calculate_rank(self, mock_submit):
        mock_submit.return_value = None
        test_cases = [
            {"left": "Foo", "right": "Bar", "result": "LEFT"},
            {"left": "Foo", "right": "Bar", "result": "RIGHT"},
            {"left": "Foo", "right": "Bar", "result": "TIE"},
        ]
        for test_case in test_cases:
            RankTableProcessor._update_scorecard(test_case["left"], test_case["right"], test_case["result"])
        RankTableProcessor.calculate_rank("output")
        mock_submit.assert_called_with(
            [("Foo", 3), ("Bar", 0), ("Foo", 0), ("Bar", 3), ("Foo", 1), ("Bar", 1)], "output"
        )
