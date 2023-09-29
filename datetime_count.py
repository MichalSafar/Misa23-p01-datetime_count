import datetime

def count_date_time(
        begin_year, begin_month, begin_day, begin_hour, begin_minute, begin_second,
        end_year, end_month, end_day, end_hour, end_minute, end_second, mode = "date_and_time"):
    begin_date = datetime.datetime(begin_year, begin_month, begin_day, begin_hour, begin_minute, begin_second)
    end_date = datetime.datetime(end_year, end_month, end_day, end_hour, end_minute, end_second)
    begin_date = begin_date.timestamp()
    end_date = end_date.timestamp()
    if mode == "seconds":
        time_difference = end_date - begin_date
        return print(f"{int(time_difference)} seconds")
    elif mode == "minutes":
        minutes = (end_date - begin_date)//60
        seconds = (end_date - begin_date)%60
        return print(f"{int(minutes)} minutes and {int(seconds)} seconds")
    elif mode == "hours":
        hours = (end_date - begin_date)/60//60
        minutes = (end_date - begin_date)//60%60
        seconds = (end_date - begin_date)%60%60
        return print(f"{int(hours)} hours, {int(minutes)} minutes and {int(seconds)} seconds")
    elif mode == "days":
        days = (end_date - begin_date)//60//60/24
        hours = (end_date - begin_date)//60//60%24
        minutes = (end_date - begin_date)//60%60
        seconds = (end_date - begin_date)%60%60
        if hours != 0 or minutes != 0 or seconds != 0:
            return print(f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes and {int(seconds)} seconds")
        else:
            return print(f"{int(days)} days")
    
count_date_time(2002,1,20,8,20,0,2007,1,12,11,15,2,mode="seconds")
count_date_time(2002,1,20,8,20,0,2007,1,12,11,15,2,mode="minutes")
count_date_time(2002,1,20,8,20,0,2007,1,12,11,15,2,mode="hours")
count_date_time(2002,1,20,8,20,0,2007,1,12,11,15,2,mode="days")

def count_date(begin_year, begin_month, begin_day, end_year, end_month, end_day):
    """
    format: count_date(beginning_of_period-year, beg_of_period-month, beg_of_period-day, end_of_period-year, end_of_period-month, end_of_period-day)
    """
    count_date_time(begin_year=begin_year, begin_month=begin_month, begin_day=begin_day, begin_hour=1, begin_minute=0, begin_second=0,
                    end_year=end_year, end_month=end_month, end_day=end_day, end_hour=0, end_minute=0, end_second=0, mode="days")

count_date(2002,4,12,2007,12,22)

def count_time(begin_hour, begin_minute, begin_second, end_hour, end_minute, end_second):
    count_date_time(begin_year=2000, begin_month=1, begin_day=1, begin_hour=begin_hour, begin_minute=begin_minute, begin_second=begin_second,
                    end_year=2000, end_month=1, end_day=1, end_hour=end_hour, end_minute=end_minute, end_second=end_second, mode="hours")
    
count_time(11,5,0,19,20,20)