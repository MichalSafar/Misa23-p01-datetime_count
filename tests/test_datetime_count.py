import unittest
from unittest.mock import MagicMock, call
import datetimecount.datetime_count


class CardTest(unittest.TestCase):
    def test_will_return_time_in_seconds(self):
        self.assertEqual(datetimecount.datetime_count.count_date_time(2008,4,12,20,44,3,2014,5,9,3,17,51,mode="seconds"), "191572428 seconds")

    def test_will_return_time_in_minutes(self):
        self.assertEqual(datetimecount.datetime_count.count_date_time(2008,4,12,20,44,3,2014,5,9,3,17,51,mode="minutes"), "3192873 minutes and 48 seconds")

    def test_will_return_time_in_hours(self):
        self.assertEqual(datetimecount.datetime_count.count_date_time(2008,4,12,20,44,3,2014,5,9,3,17,51,mode="hours"), "53214 hours, 33 minutes and 48 seconds")

    def test_will_return_time_in_days(self):
        self.assertEqual(datetimecount.datetime_count.count_date_time(2008,4,12,20,44,3,2014,5,9,3,17,51,mode="days"), "2217 days, 6 hours, 33 minutes and 48 seconds")

    def test_will_return_time_in_weeks(self):
        self.assertEqual(datetimecount.datetime_count.count_date_time(2008,4,12,20,44,3,2014,5,9,3,17,51,mode="weeks"), "316 weeks, 5 days, 6 hours, 33 minutes and 48 seconds")

    def test_will_return_time_in_years(self):
        self.assertEqual(datetimecount.datetime_count.count_date_time(2008,4,12,20,44,3,2014,5,9,3,17,51,mode="years"), "6 years, 3 weeks, 6 days, 6 hours, 33 minutes and 48 seconds")
    
    def test_count_date_communicates_with_count_date_time(self):
        """
        může být špatně - count_date_time() chci nahradit za MagicMock() a poté zkontrolovat jesli má hlášení (assert_has_calls).
        Tímto chci zkontrolovat jesli "count_date()" správně volá "count_date_time()"
        Nechci do "count_date()" dát datum a poté zkontrolovat jesli mám dobrý výsledek, protože to je kontrola dvou různých procesů
        jedním testem - komunikace mezi "count_date()" a "count_date_time()" a druhý test je správné spočítání času. Druhý test ale
        už  mám zkontrolovaný.
        """
        my_date = MagicMock()
        datetimecount.datetime_count.count_date_time(2002, my_date, my_date, my_date, my_date, my_date, 2002, my_date, my_date, my_date, my_date, my_date)
        datetimecount.datetime_count.count_date(2004,12, 1,2005,2, 4)
    
        my_date.assert_has_calls([call.__index__()])