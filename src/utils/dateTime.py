from datetime import datetime, timedelta
from email.utils import formatdate, parsedate
import time


time_delt1 = timedelta(days=2)
# timedelta(days=270, hours=9, minutes=18)


print(round(time_delt1.total_seconds() * 1000))
print(round(time_delt1.days))



# timestamp is number of seconds since 1970-01-01
timestamp = time_delt1.total_seconds()

# convert the timestamp to a datetime object in the local timezone
dt_object = datetime.fromtimestamp(timestamp)

# current date and time
now = datetime.now()

# convert from datetime to timestamp
ts = datetime.timestamp(now)


print("dt_object =", dt_object)

print("------------------ \n")

currentDateAndTime = datetime.now()

print("The current year is ", currentDateAndTime.year)  # Output: The current year is  2022
print("The current month is ", currentDateAndTime.month)  # Output: The current month is  3
print("The current day is ", currentDateAndTime.day)  # Output: The current day is  19
print("The current hour is ", currentDateAndTime.hour)  # Output: The current hour is  10
print("The current minute is ", currentDateAndTime.minute)  # Output: The current minute is  49
print("The current second is ", currentDateAndTime.second)  # Output: The current second is  18




def convert_timestamp_to_date(sec: int):
    sec = sec % (24 * 3600)
    hour = sec // 3600
    sec %= 3600
    minu = sec // 60
    sec %= 60
    print("seconds value in hours:", hour)
    print("seconds value in minutes:", minu)
    return "%02d:%02d:%02d" % (hour, minu, sec)


n = 20000
print("Time in preferred format :-", convert_timestamp_to_date(n))



def formatdate_timestime_now():
    return formatdate(timeval=None, localtime=False, usegmt=True)


def formatdate_parsedate_now(date):
    print(date)
    rs1 = datetime.datetime(parsedate(date))
    rs2 = time.mktime(parsedate(date))
    rs3 = parsedate(date)
    print(rs1,rs2,rs3)



rs_time = formatdate_timestime_now()
print(type(rs_time))
print(rs_time)



# Convert the date and time string to a datetime object
datetime_object = datetime.strptime(rs_time, '%a, %d %b %Y %H:%M:%S %Z')

# Print the datetime object
print(type(datetime_object))
print(type(datetime.now()))
print(datetime_object)
print(datetime.now())


def get_difference_in_minutes(start_date, end_date):
  """
  Esta función devuelve la diferencia en minutos entre dos fechas.

  Args:
    start_date: La fecha de inicio.
    end_date: La fecha de finalización.

  Returns:
    La diferencia en minutos entre las dos fechas.
  """

  # Obtenga la diferencia en segundos entre las dos fechas.
  difference_in_seconds = (end_date - start_date).total_seconds()

  # Devuelva la diferencia en minutos.
  return difference_in_seconds // 60

start_date = datetime(2023, 7, 21, 12, 0, 0)
end_date = datetime(2023, 7, 21, 12, 30, 0)

difference_in_minutes = get_difference_in_minutes(start_date, end_date)

print(difference_in_minutes)

