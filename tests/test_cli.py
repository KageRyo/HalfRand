import csv
import tempfile
import unittest
from pathlib import Path

from halfrand.cli import main


class CliTests(unittest.TestCase):
    def test_writes_csv(self):
        with tempfile.TemporaryDirectory() as directory:
            output = Path(directory) / "values.csv"
            self.assertEqual(main(["3", "--seed", "7", "--output", str(output)]), 0)
            with output.open(newline="", encoding="utf-8") as stream:
                rows = list(csv.reader(stream))
        self.assertEqual(rows[0], ["index", "value"])
        self.assertEqual(len(rows), 4)

    def test_reports_invalid_configuration(self):
        self.assertEqual(main(["1", "--step", "-1"]), 2)
