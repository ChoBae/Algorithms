# datetime 사용
import datetime as da
month = int(input())
day = int(input())

def findday(m, d):
    day = ["MON", "TUE", "WED", "THU", "FRI", "SAT", "SUN"]
    #weekday() -> 날짜를 숫자로 리턴해줌 0-> 월요일 6-> 일요일
    return day[da.date(2020, m, d).weekday()]

print(findday(month, day))

import calendar
print(calendar.calendar(2021))