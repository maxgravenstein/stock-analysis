import datetime as dt
import matplotlib.pyplot as plt
import matplotlib.dates as mdates

dates = [2010-7-19, 2010-7-20, 2010-7-21, 2010-7-22, 2010-7-23]
x = dt.datetime.strptime(row[0][0:10], '%Y-%m-%d').date()
y = range(len(dates))
#plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
#plt.gca().xaxis.set_major_locator(mdates.DayLocator())
#plt.plot(x,y)
#plt.gcf().autofmt_xdate()

print(x,y)