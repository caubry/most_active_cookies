import datetime


class MostDailyActiveCookies:

    def __init__(self, cookie_log_data):
        self.cookie_log_data = cookie_log_data

    def get_for_date(self, date):
        daily_cookies = self.__get_daily_cookies(date)
        length = len(daily_cookies)
        result = []

        if length == 0:
            return result

        max_cookies_seen = max(daily_cookies.values())

        for cookie in daily_cookies:
            cookies_seen = daily_cookies[cookie]
            if cookies_seen == max_cookies_seen:
                result.append(cookie)

        return result

    def __get_daily_cookies(self, date):
        daily_cookies = {}

        for row in self.cookie_log_data:

            cookieId = row.get('cookie')
            dateStr = row.get('timestamp')

            if not cookieId or not dateStr:
                return daily_cookies

            logged_date = datetime.datetime.fromisoformat(dateStr).date()

            if date > logged_date:
                break

            if logged_date == date:
                if not daily_cookies.get(cookieId):
                    daily_cookies[cookieId] = 0

                daily_cookies[cookieId] += 1

        return daily_cookies
