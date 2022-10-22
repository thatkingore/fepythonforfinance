
import datetime
from datetime import date
import calendar

# Predicting Future Day

future_date = datetime.date(2022, 11, 14)
print(calendar.day_name[future_date.weekday()])
future_date = datetime.date(2022, 11, 15)
print(calendar.day_name[future_date.weekday()])
future_date = datetime.date(2022, 11, 16)
print(calendar.day_name[future_date.weekday()])
future_date = datetime.date(2022, 11, 17)
print(calendar.day_name[future_date.weekday()])
future_date = datetime.date(2022, 11, 18)
print(calendar.day_name[future_date.weekday()])

# Using Calendars

cal = calendar.TextCalendar(calendar.SUNDAY)
calen = cal.formatmonth(2020, 10, 0, 0)
print(calen)

# Today's Date

today = date.today()
print("Today is " + str(today))
print("Today is " + str(today.day))
print("The month is " + str(today.month))
print("The year is " + str(today.year))

days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
print("Today is " + str(days[today.weekday()]) + "(" + str(today.weekday()) + ")")

# The Time Right Now
from datetime import datetime

the_time = datetime.now()
print("The date and time right now is " + str(the_time))
print("The time right now is " + str(datetime.time(datetime.now())))

# Date Formatting

now = datetime.now()
print("Today's date is " + str(now.strftime("%A")) + ", " + str(now.strftime("%B")) + " " + str(now.strftime("%d")) + " " + str(now.strftime("%Y")))

# Time Formatting

print("12-Hour format time is " + str(now.strftime("%I:%M:%S %p")))
print("24-Hour format time is " + str(now.strftime("%H:%M:%S")))

# Local Data and Time

print("Again, today's date is " + str(now.strftime("%x")))
print("And the time is " + str(now.strftime("%X")))
print("The local date and time is " + str(now.strftime("%c")))

