__author__ = 'T Jeremiah - October 2015'

from bs4 import BeautifulSoup
import urllib2, pprint

page = urlopen('http://www.wunderground.com/history/airport/KNYC/2015\
/11/1/MonthlyCalendar.html')
soup = BeautifulSoup(page)
dates = soup.find_all('a',attrs={'class':'dateText'})
actuals = {}
forecasts = {}

for date in dates:
    highs = date.parent.parent.parent.parent.find('span',attrs={'class':'high'})
    lows =  date.parent.parent.parent.parent.find('span',attrs={'class':'low'})
    if not date.has_attr('href'):
        actuals[int(date.get_text().strip())] = [highs.get_text(),lows.get_text()]
    else:
        if int(date.get_text().strip()) <= 17:
            forecasts[int(date.get_text().strip())] = [highs.get_text(),lows.get_text()]
print 'Todays highs and lows: '
pprint.pprint(actuals)
print '\nWeeks forecasted highs and low: '
pprint.pprint(forecasts)
