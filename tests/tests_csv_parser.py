import unittest

from exceptions.parsing_error import ParsingError
from parsers.csv_parser import CsvParser
from parsers.parser import Parser


class TestsCsvParser(unittest.TestCase):

    def setUp(self):
        self.parser = CsvParser()

    def test__given_a_csv_file__when_parsing_it__then_return_file_data(self):
        filepath = './tests/data/cookie_log.csv'
        try:
            file_data = self.parser.parse(filepath)
            self.assertIsNotNone(file_data)

        except ParsingError:
            self.fail()

    def test__given_not_a_csv_file__when_parsing_it__then_throw_parsing_error(self):
        filepath = './cookie_log.txt'
        try:
            self.parser.parse(filepath)
            self.fail("Failed to throw ParsingError")

        except ParsingError as e:
            self.assertEqual(Parser.NO_PARSER_FOUND, e.message)
            self.assertEqual(filepath, e.expression)
