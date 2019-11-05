import datetime
import unittest

from most_active_cookies import MostDailyActiveCookies


class TestsMostActiveCookies(unittest.TestCase):

    def setUp(self):
        dummy_data = [
            {
                'cookie': 'AtY0laUfhglK3lC7',
                'timestamp': '2018-12-09T14:19:00+00:00'
            },
            {
                'cookie': '5UAVanZf6UtGyKVS',
                'timestamp': '2018-12-09T10:13:00+00:00'
            },
            {
                'cookie': '5UAVanZf6UtGyKVS',
                'timestamp': '2018-12-09T07:25:00+00:00'
            },
            {
                'cookie': 'AtY0laUfhglK3lC7',
                'timestamp': '2018-12-09T06:19:00+00:00'
            },
            {
                'cookie': 'SAZuXPGUrfbcn5UA',
                'timestamp': '2018-12-08T22:03:00+00:00'
            }
        ]

        self.most_active_cookies = MostDailyActiveCookies(dummy_data)

    def test__given_cookie_log_data__and_date__when_one_cookie_only_is_active__then_return_it(self):
        date = '2018-12-08'
        date = self.__get_date(date)
        expected_cookie = 'SAZuXPGUrfbcn5UA'
        cookies = self.most_active_cookies.get_for_date(date)
        self.assertEqual([expected_cookie], cookies)

    def test__given_cookie_log_data__and_date__when_multiple_cookies_are_active__then_return_them(self):
        date = '2018-12-09'
        date = self.__get_date(date)
        expected_cookies = ['AtY0laUfhglK3lC7', '5UAVanZf6UtGyKVS']
        cookies = self.most_active_cookies.get_for_date(date)
        self.assertEqual(expected_cookies, cookies)

    def test__given_cookie_log_data__and_date__when_date_is_not_in_log__then_return_empty(self):
        date = '2018-12-07'
        date = self.__get_date(date)
        cookies = self.most_active_cookies.get_for_date(date)
        self.assertEqual([], cookies)

    def test__given_wrong_cookie_log_data_format__when_retrieving_most_active_daily_cookies__then_return_empty(self):
        dummy_data = [
            {
                'cookie': 'AtY0laUfhglK3lC7',
                'date': '2018-12-09T14:19:00+00:00'
            }]

        most_active_cookies = MostDailyActiveCookies(dummy_data)
        date = '2018-12-09'
        date = self.__get_date(date)
        cookies = most_active_cookies.get_for_date(date)
        self.assertEqual([], cookies)

    @staticmethod
    def __get_date(date):
        # This is currently wrong as we are putting datetime under test.
        # Given more time, I would wrap it into another class.
        return datetime.datetime.strptime(date, '%Y-%m-%d').date()
