import urllib2
from stockdata import *
def saveQuotes():
	symbol = raw_input("%-3s %-40s " % ("?","Enter The Symbol")).upper()
	url = "http://www.nseindia.com/content/equities/scripvol/datafiles/01-01-2015-TO-12-12-2015"+symbol+"EQN.csv"
	request_headers = {
		"Accept-Language": "en-US,en;q=0.5",
		"User-Agent": "Mozilla/5.0 (Windows NT 10.0; WOW64; rv:40.0) Gecko/20100101 Firefox/40.0",
		"Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
		"Referer": "http://www.nseindia.com",
		"Connection": "keep-alive" 
	}
	request = urllib2.Request(url, headers=request_headers)
	contents = urllib2.urlopen(request)
	output = open("data/"+symbol+".csv","wb")
	output.write(contents.read())
	output.close()
def testEquity():
	symbol = raw_input("%-3s %-40s " % ("?","Enter Symbol")).upper()
	stock = equityLearner(symbol)
	if not stock.isValid():
		print "%-3s %-40s %s" % ("","File Not Found",symbol+".csv")
		return
	print "#"*70
	print "%-3s %-40s " % ("1","Basic Info")
	print "%-3s %-40s " % ("2","Simple Moving Average Graph")
	print "%-3s %-40s " % ("3","Bollinger Band Graph")
	print "%-3s %-40s " % ("4","Current Simple Moving Average")
	print "%-3s %-40s " % ("5","Current Bollinger Bands")
	print "%-3s %-40s " % ("6","KNN Model")
	print "%-3s %-40s " % ("0","Exit to Main Menu")
	while True:
		print "#"*70
		option = int(raw_input("%-3s %-40s " % ("?","Enter Your Option")))
		if option == 1:
			currentPosition = stock.getBasicInfo()
			for key in currentPosition:
				print "%-3s %-40s %s" % ("*",key,currentPosition[key])
		elif option == 2:
			noDays = int(raw_input("%-3s %-40s " % ("?","No of Days")))
			stock.graphSimpleMovingAverage(noDays)
		elif option == 3:
			noDays = int(raw_input("%-3s %-40s " % ("?","No of Days")))
			stock.graphBollingerBands(noDays)
		elif option == 4:
			SMA = stock.getCurrentSimpleMovingAverage()
			print "%-3s %-40s %s" % ("","Simple Moving Average",SMA)
		elif option == 5:
			bands = stock.getCurrentBollingerBands()
			for key in bands:
				print "%-3s %-40s %s" % ("",key,bands[key])
		elif option == 6:
			stock.makeKNNModel()
		else:
			break
def main():
	while True:
		print "%-3s %-40s " % ("1","Test Equity")
		print "%-3s %-40s " % ("2","Download New Data")
		print "%-3s %-40s " % ("0","Exit")
		print "*"*70
		option = int(raw_input("%-3s %-40s " % ("?","Enter Your Option")))
		if option == 1:
			testEquity()
		elif option == 2:
			saveQuotes()
		else:
			exit("Exiting")
main()
'''
Convert Numpy array to DataFrame

data = numpy.array(['','Col1','Col2'],[0,'val1','val2'],[1,'val1','val2'])
pd.DataFrame(data[1:,1:], index=data[1:,0], columns=data[0,1:])
'''
'''
Standard Deviation

#std = self.dataFrame['Close Price'][i-5:i].std()
'''
'''
Dataframe to Numpy Array

dataset_array = dataset.values
print(dataset_array.dtype)
print(dataset_array)
'''
'''
Download Using Urllib
urllib.urlretrieve (url, full_path)
'''
'''
NSE URL
http://www.nseindia.com/content/equities/scripvol/datafiles/12-12-2014-TO-11-12-2015SBINEQN.csv
'''
'''
CSV with numpy

import numpy as np
csv = np.genfromtxt ('file.csv', delimiter=",")
second = csv[:,1]
third = csv[:,2]

>>> second
Out[1]: array([ 432.,  300.,  432.])

>>> third
Out[2]: array([ 1.,  1.,  0.])

'''
'''
Numpy mean , std

In [17]: import numpy

In [18]: arr = numpy.array([A_rank, B_rank, C_rank])

In [20]: numpy.mean(arr, axis=0)
Out[20]: 
array([ 0.7       ,  2.2       ,  1.8       ,  2.13333333,  3.36666667,
        5.1       ])

In [21]: numpy.std(arr, axis=0)
Out[21]: 
array([ 0.45460606,  1.29614814,  1.37355985,  1.50628314,  1.15566239,
        1.2083046 ])
'''
'''

Pandas col subtraction

import pandas as pd
df = pd.DataFrame(range(4), columns = ['col'])

print(df['col'] - df['col'].shift())
# 0   NaN
# 1     1
# 2     1
# 3     1
# Name: col

print(df['col'] + df['col'].shift())
# 0   NaN
# 1     1
# 2     3
# 3     5
# Name: col
If you wish NaN plus (or minus) a number to be the number (not NaN), use the add (or sub) method with fill_value = 0:

print(df['col'].sub(df['col'].shift(), fill_value = 0))
# 0    0
# 1    1
# 2    1
# 3    1
# Name: col

print(df['col'].add(df['col'].shift(), fill_value = 0))
# 0    0
# 1    1
# 2    3
# 3    5
# Name: col


import pandas as p
df = p.read_csv("data/HDIL.csv")
a = df[['High Price','Low Price']].values

class a:
 def __init__(self,w):
  self.w = w
  self.inc_w()
  self.print_w()
 def inc_w(self):
  self.w += 1
 def print_w(self):
  print self.w

def a(dic):
 dic['a'] = 1
d = {'a':2}
a(d)
d
'''