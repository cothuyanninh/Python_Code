import datetime as dt
import math

firstDay = input("Moi nhap so ngay dau tien: ")
firstDays = dt.datetime.strptime(firstDay, '%d%m%Y').date()
sencondDay = input("Moi nhap so ngay thu hai: ")
sencondDays = dt.datetime.strptime(sencondDay, '%d%m%Y').date()
days = (sencondDays - firstDays)
print(days)
