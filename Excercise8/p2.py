#. Print the dates between March-2017 to April-2017 using datetime

from datetime import date
march = date(2017,3,1)
april = date(2017, 4,30)
total = april - march
print("days= ",total.days)
