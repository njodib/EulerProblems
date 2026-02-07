'''
You are given the following information, but you may prefer to do some research for yourself.

1 Jan 1900 was a Monday.
Thirty days has September,
April, June and November.
All the rest have thirty-one,
Saving February alone,
Which has twenty-eight, rain or shine.
And on leap years, twenty-nine.
A leap year occurs on any year evenly divisible by 4, but not on a century unless it is divisible by 400.
How many Sundays fell on the first of the month during the twentieth century (1 Jan 1901 to 31 Dec 2000)?
'''

def is_leap_year(year):
    return year%4 == 0 and (year%100 != 0 or year%400 == 0)
def days_in_month(month, year):
    match month:
        case 1 | 3 | 5 | 7 | 8 | 10 | 12: return 31
        case 4 | 6 | 9 | 11: return 30
        case 2: return 29 if is_leap_year(year) else 28

# days of week which month begins
day = 1 # 1 Jan 1900 was a Monday
sunday_the_first = 0
for year in range(1900, 2001):
    for month in range(1, 13):
        day = (day + days_in_month(month, year)) % 7
        if year >= 1901 and day == 0:
            sunday_the_first += 1
print("sunday the first count 20th century:", sunday_the_first)