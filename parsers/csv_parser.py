from helpers.filesystem import read_csv_file
from parsers.parser import Parser


class CsvParser(Parser):

    # Given more time, I'd have validate fieldnames/headers on the CSV file
    def parse(self, filepath, fieldnames=None):
        if self.can_handle_file(filepath, '.csv'):
            return read_csv_file(filepath, fieldnames)
        else:
            super(CsvParser, self).parse(filepath)
