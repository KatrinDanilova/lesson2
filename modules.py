import datetime
import locale
import ephem
from answers import get_answer, answers

print(locale.setlocale(locale.LC_ALL, ''))

mars = ephem.Mars(datetime.date.today())
print(ephem.constellation(mars))
print(mars.ra)
print(ephem.next_full_moon(datetime.date.today()))
print(ephem.next_new_moon(datetime.date.today()))



print(datetime.date.today())
print(datetime.datetime.now())
print(datetime.datetime.utcnow())

d = datetime.date(2005, 7, 4)
t = datetime.time(12, 30)
print(datetime.datetime.combine(d, t))

dt = datetime.datetime.strptime("21/11/06 16:30", "%d/%m/%y %H:%M")
print(dt)

dt = datetime.datetime(2006, 11, 21, 16, 30)

tt = dt.timetuple()
print(tt.tm_wday)

ic = dt.isocalendar()
print(ic)

print(dt.strftime("%A, %d %B %Y %I:%M%p"))

mydate = datetime.datetime.now()
mydate = datetime.datetime.now()
print(mydate.strftime("%A %d.%m.%Y"))

year = datetime.timedelta(days=365)
ten_years = 10 * year
print(ten_years)
print(ten_years.days)

print(answers)
print(get_answer("Как дела?", answers))