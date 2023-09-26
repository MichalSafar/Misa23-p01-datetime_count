import datetime

def count_date(codate1_year, codate1_month, codate1_day, codate2_year, codate2_month, codate2_day):
    """
    format: count_date(end_year, end_month, end_day, begin_year, begin_month, begin_day)
    """
    date1 = datetime.date(year = codate1_year, month = codate1_month, day = codate1_day)
    date2 = datetime.date(year = codate2_year, month = codate2_month, day = codate2_day)
    
    return print((date1 - date2))

def count_time(time1_hour, time1_minute, time1_second, time2_hour, time2_minute, time2_second):
    """
    format: count_time(end hour, end minute, end second, start hour, start minute, start second)
    """
    time1 = datetime.timedelta(hours = time1_hour, minutes = time1_second, seconds = time1_second)
    time2 = datetime.timedelta(hours = time2_hour, minutes = time2_minute, seconds = time2_second)
    return print((time1 - time2))

count_time(20, 22, 0, 8, 16, 0)