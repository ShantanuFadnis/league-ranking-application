"""Rank Table Application"""
import os
import sys
from utils.logger import init_logging_object  # type:ignore
from processors import RankTableProcessor as RTP  # type:ignore


LOG = init_logging_object(__name__)


class AppExceptions(Exception):
    """AppExceptions for this App"""


class App:
    """Main Application"""

    def __init__(self, in_file_path: str, out_file_path: str) -> None:
        """
        Instantiation of App to store input file path.
        @param in_file_path: str - Input file path
        @param out_file_path: str - Output file path
        @return: None
        """
        if not os.path.exists(in_file_path):
            raise AppExceptions("File does not exist!")
        self.in_file_path = in_file_path
        self.out_file_path = out_file_path

    def execute(self):
        """
        execute() - Method to execute App and processing of input file.
        """
        with open(self.in_file_path, "r", encoding="UTF-8") as file:
            while True:
                row = file.readline().strip()
                if len(row) == 0:
                    break
                RTP.pre_process(row)
        RTP.calculate_rank(self.out_file_path)


if __name__ == "__main__":
    try:
        app = App(sys.argv[1], sys.argv[2])
        app.execute()
    except AppExceptions as err:
        print(err)
