from datetime import date
from datetime import timedelta

y, m, d = [int(i) for i in input().split()]
days = int(input())
a = date(y, m, d)
a += timedelta(days)
print(a.year, a.month, a.day)


