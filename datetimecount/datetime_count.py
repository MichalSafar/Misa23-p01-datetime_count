import datetime

def count_date_time(
        begin_year, begin_month, begin_day, begin_hour, begin_minute, begin_second,
        end_year, end_month, end_day, end_hour, end_minute, end_second, mode="seconds"):
    """
    the count_date_time() wrap up in print() func -> print(count_date_time(xx,yy,zzz .....))
    begin_xyz - the beginning date from which the period should be calculated.\n
    end_xyz - the ending date which the period should be calculated to.\n
    begin_year, end year - Fill 4-digit number of the year\n
    begin_month, end_month - Fill 1-9 or 10-12 number for the month.\n
    begin_day, end_day - Fill 1-9 or 10-31 number for the day.\n
    begin_hour, end_hour - Fill 0-23 number for the hour.\n
    begin_minute, end_minute - Fill 0-59 number for the minute.\n
    begin_second, end_second - Fill 0-59 number for the second.\n
    \n
    mode -> "seconds" - default value and it will return calculated time difference in seconds.\n
            "minutes" - calculated time in minutes and the rest in seconds.\n
            "hours"   - time will be in hours, minutes and the rest of time period in seconds.\n
            "days"    - the time period will include days, hours, minutes and seconds.\n
            "weeks"   - the same as "days" but include number of weeks.\n
            "year"    - difference in two datetimes will be in years, weeks, days, minutes, and seconds.
    """
    begin_date = datetime.datetime(begin_year, begin_month, begin_day, begin_hour, begin_minute, begin_second)
    end_date = datetime.datetime(end_year, end_month, end_day, end_hour, end_minute, end_second)
    begin_date = begin_date.timestamp()
    end_date = end_date.timestamp()
    if mode == "seconds":
        time_difference = end_date - begin_date
        return f"{int(time_difference)} seconds"
        #return int(time_difference)
    elif mode == "minutes":
        minutes = (end_date - begin_date)//60
        seconds = (end_date - begin_date)%60
        return f"{int(minutes)} minutes and {int(seconds)} seconds"
    elif mode == "hours":
        hours = (end_date - begin_date)/60//60
        minutes = (end_date - begin_date)//60%60
        seconds = (end_date - begin_date)%60%60
        return f"{int(hours)} hours, {int(minutes)} minutes and {int(seconds)} seconds"
    elif mode == "days":
        days = (end_date - begin_date)//60//60/24
        hours = (end_date - begin_date)//60//60%24
        minutes = (end_date - begin_date)//60%60
        seconds = (end_date - begin_date)%60%60
        if hours != 0 or minutes != 0 or seconds != 0:
            return f"{int(days)} days, {int(hours)} hours, {int(minutes)} minutes and {int(seconds)} seconds"
        else:
            return f"{int(days)} days"
    elif mode == "weeks":
        weeks = (end_date - begin_date)//60//60//24/7
        days = (end_date - begin_date)//60//60/24%7
        hours = (end_date - begin_date)//60//60%24
        minutes = (end_date - begin_date)//60%60
        seconds = (end_date - begin_date)%60%60
        return f"{int(weeks)} weeks, {int(days)} days, {int(hours)} hours, {int(minutes)} minutes and {int(seconds)} seconds"
    elif mode == "years":
        years = (end_date - begin_date)//60//60//24/365
        weeks = (end_date - begin_date)//60//60//24%365/7
        days = (end_date - begin_date)//60//60/24%365%7
        hours = (end_date - begin_date)//60//60%24
        minutes = (end_date - begin_date)//60%60
        seconds = (end_date - begin_date)%60%60
        return f"{int(years)} years, {int(weeks)} weeks, {int(days)} days, {int(hours)} hours, {int(minutes)} minutes and {int(seconds)} seconds"
    
def count_date(begin_year, begin_month, begin_day, end_year, end_month, end_day):
    """
    format: count_date(beginning_of_period-year, beg_of_period-month, beg_of_period-day, end_of_period-year, end_of_period-month, end_of_period-day)
    """
    count_date_time(begin_year=begin_year, begin_month=begin_month, begin_day=begin_day, begin_hour=1, begin_minute=0, begin_second=0,
                    end_year=end_year, end_month=end_month, end_day=end_day, end_hour=0, end_minute=0, end_second=0, mode="days")
def count_time(begin_hour, begin_minute, begin_second, end_hour, end_minute, end_second):
    count_date_time(begin_year=2000, begin_month=1, begin_day=1, begin_hour=begin_hour, begin_minute=begin_minute, begin_second=begin_second,
                    end_year=2000, end_month=1, end_day=1, end_hour=end_hour, end_minute=end_minute, end_second=end_second, mode="hours")

#print(count_date_time(2008,4,12,20,44,3,2014,5,9,3,17,51,mode="seconds"))
#print(count_date_time(2008,4,12,20,44,3,2014,5,9,3,17,51,mode="minutes"))
#print(count_date_time(2008,4,12,20,44,3,2014,5,9,3,17,51,mode="hours"))
#print(count_date_time(2008,4,12,20,44,3,2014,5,9,3,17,51,mode="days"))
#print(count_date_time(2008,4,12,20,44,3,2014,5,9,3,17,51,mode="weeks"))
#print(count_date_time(2008,4,12,20,44,3,2014,5,9,3,17,51,mode="years"))



#count_date(2002,4,12,2007,12,22)

#count_time(11,5,0,19,20,20)