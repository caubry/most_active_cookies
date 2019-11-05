import unittest

from parameterized import parameterized

from exceptions.input_error import InputError
from validations.input_validation import InputValidation


class TestsInputValidation(unittest.TestCase):

    @parameterized.expand([["csv"], ["CSV"], ["cSv"]])
    def test__given_a_csv_log_file_path__when_validating_its_ext__then_return_file_path(self, ext):
        log_file_path = 'cookie_log.{ext}'.format(ext=ext)
        try:
            file_path = InputValidation.validate_file_extension(log_file_path)
            self.assertEqual(log_file_path, file_path)

        except InputError:
            self.fail()

    @parameterized.expand([["txt"], ["yaml"], ["json"]])
    def test__given_not_a_csv_log_file_path__when_validating_its_ext__then_throw_input_error(self, ext):
        log_file_path = 'cookie_log.{ext}'.format(ext=ext)
        try:
            InputValidation.validate_file_extension(log_file_path)
            self.fail("Failed to throw InputError")

        except InputError as e:
            self.assertEqual(InputValidation.FILE_EXT_ERROR_MESSAGE, e.message)
            self.assertEqual(log_file_path, e.expression)

    def test__given_an_existing_log_file_path__when_validating_its_existence__then_return_file_path(self):
        log_file_path = './tests/data/cookie_log.csv'
        try:
            file_path = InputValidation.validate_file_exists(log_file_path)
            self.assertEqual(log_file_path, file_path)

        except InputError:
            self.fail()

    def test__given_an_unknown_log_file_path__when_validating_its_existence__then_throw_input_error(self):
        log_file_path = './cookie_test.csv'
        try:
            InputValidation.validate_file_exists(log_file_path)
            self.fail("Failed to throw InputError")

        except InputError as e:
            self.assertEqual(InputValidation.FILE_NOT_FOUND_ERROR_MESSAGE, e.message)
            self.assertEqual(log_file_path, e.expression)

    @parameterized.expand([["2018-12-09"], ["2019-02-01"], ["2022-12-30"]])
    def test__given_expected_date_format__when_validating_it__then_return_date(self, expected_date):
        expected_format = '%Y-%m-%d'
        try:
            date = InputValidation.validate_date(expected_date)
            self.assertEqual(expected_date, date.strftime(expected_format))

        except InputError:
            self.fail()

    @parameterized.expand([["2022-02-31"], ["2022-12-33"]])
    def test__given_unreachable_date__when_validating_it__then_throw_input_error(self, date):
        try:
            InputValidation.validate_date(date)
            self.fail("Failed to throw InputError")

        except InputError as e:
            self.assertEqual(InputValidation.INVALID_DATE_ERROR_MESSAGE, e.message)
            self.assertEqual(date, e.expression)

    @parameterized.expand([["2018-12-0"], ["2018-12-00:00:00:00"], ["2018-12"], ["2018:12:09"]])
    def test__given_unexpected_date_format__when_validating_it__then_throw_input_error(self, date):
        try:
            InputValidation.validate_date(date)
            self.fail("Failed to throw InputError")

        except InputError as e:
            self.assertEqual(InputValidation.INVALID_DATE_ERROR_MESSAGE, e.message)
            self.assertEqual(date, e.expression)
