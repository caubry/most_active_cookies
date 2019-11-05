import datetime
import re

from exceptions.input_error import InputError
from helpers.filesystem import path_exists


class InputValidation:
    INVALID_DATE_ERROR_MESSAGE = "Unexpected date, ensure it exists. (supported formats: [YYYY-MM-DD])"
    FILE_EXT_ERROR_MESSAGE = "Unexpected log file extension. (supported formats: [CSV])"
    FILE_NOT_FOUND_ERROR_MESSAGE = "File not found."

    @staticmethod
    def validate_date(date):
        try:
            return datetime.datetime.strptime(date, '%Y-%m-%d').date()
        except ValueError:
            raise InputError(date, InputValidation.INVALID_DATE_ERROR_MESSAGE)

    @staticmethod
    def validate_file_extension(filename):
        if re.search('^.*csv$', filename, re.IGNORECASE):
            return filename
        else:
            raise InputError(filename, InputValidation.FILE_EXT_ERROR_MESSAGE)

    @staticmethod
    def validate_file_exists(filepath):
        if not path_exists(filepath):
            raise InputError(filepath, InputValidation.FILE_NOT_FOUND_ERROR_MESSAGE)

        return filepath
