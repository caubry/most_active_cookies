"""Get the most daily active cookies CLI
Usage:
    most_active_cookies.py [FILE] (-d) [DATE]
    most_active_cookies.py -h|--help
    most_active_cookies.py -v|--version

Arguments:
    FILE  Path to the CSV log file
    DATE  Date in UTC time zone, needs FILE, --d to be present

Options:
    -d            Date in UTC time zone
    -h --help     Show this screen
    -v --version  Show version
"""
from docopt import docopt

from exceptions.input_error import InputError
from most_active_cookies import MostDailyActiveCookies
from parsers.csv_parser import CsvParser
from validations.input_validation import InputValidation

if __name__ == '__main__':
    arguments = docopt(__doc__, version='1.0')
    file_arg = arguments['FILE']
    date_arg = arguments['DATE']

    if not file_arg or not date_arg:
        print(arguments)
        exit(1)

    try:
        date = InputValidation.validate_date(date_arg)
        file = InputValidation.validate_file_extension(file_arg)
        file = InputValidation.validate_file_exists(file)

        csv_parser = CsvParser()
        data = csv_parser.parse(file)
        most_active_cookies = MostDailyActiveCookies(data)
        cookies = most_active_cookies.get_for_date(date)

        for cookie in cookies:
            print(cookie)

    except InputError as e:
        print(e)
