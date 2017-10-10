from datetime import date as d_date, timedelta

year, month, day = input().split()
date = d_date(int(year), int(month), int(day))
date += timedelta(days=int(input()))
print(date.year, date.month, date.day)
