from unittest import TestCase
from unittest.mock import patch
from src.main import App, AppExceptions


class RankAppTest(TestCase):
    maxDiff = None

    @patch("src.main.App.execute")
    def test_init_with_correct_files(self, mock_execute):
        mock_execute.return_value = None
        app = App("tests/fixtures/test_data/in.txt", "output")
        self.assertEqual(app.in_file_path, "tests/fixtures/test_data/in.txt")
        self.assertEqual(app.out_file_path, "output")

    def test_init_with_incorrect_input_file(self):
        with self.assertRaises(AppExceptions):
            App("abc", "pqr")

    @patch("src.main.RTP.pre_process")
    @patch("src.main.RTP.calculate_rank")
    def test_execute(self, mock_calculate_rank, mock_pre_process):
        mock_pre_process.return_value = None
        mock_calculate_rank.return_value = None
        app = App("tests/fixtures/test_data/in.txt", "output")
        app.execute()
        mock_pre_process.assert_called_with("Foo 10, Bar 3")
        mock_calculate_rank.assert_called_with("output")
