import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.neighbors import KNeighborsRegressor
class KNNModel:
	def __init__(self,dataFrame):
		self.dataFrameKNN = {}
		self.KNNWeightage = {'Avg-High Ratio':100,'Avg-Low Ratio':100,'Deliverable Qty':300,'Turnover':100,'Growth':150,'Trend':100,'Output':100}
		self.valid = True
		self.KNNModelHash = {}
		self.dataFrameKNN = pd.DataFrame()
		self.dataFrameKNN['Avg-High Ratio'] = dataFrame['High Price'][1:] - dataFrame['Average Price'][1:]
		self.dataFrameKNN['Avg-Low Ratio'] = dataFrame['Average Price'][1:] - dataFrame['Low Price'][1:]
		self.dataFrameKNN['Deliverable Qty'] = dataFrame['Deliverable Qty'][1:]
		self.dataFrameKNN['Turnover'] = dataFrame['Turnover in Lacs'][1:]
		self.dataFrameKNN['Growth'] = dataFrame['Close Price'][1:]-dataFrame['Prev Close'][1:]
		self.dataFrameKNN['Trend'] = dataFrame['Turnover in Lacs'][1:]
		self.dataFrameKNN['Output'] = dataFrame['High Price'][1:]-dataFrame['Prev Close'][1:]
		self.KNNModelHash['mean'] = self.dataFrameKNN['Output'].mean()
		self.KNNModelHash['std'] = self.dataFrameKNN['Output'].std()
		for key in self.dataFrameKNN:
			self.normalizeKNNModel(key)
		#trainData has the data to be trained, but the last data is the testData
		trainData =	self.dataFrameKNN[['Avg-High Ratio','Avg-Low Ratio','Deliverable Qty','Growth']][:-1].values
		testData = self.dataFrameKNN[['Avg-High Ratio','Avg-Low Ratio','Deliverable Qty','Growth']][-1:].values
		#trainOutput contains the output corresponding to train Data but the first one is garbage
		trainOutput = self.dataFrameKNN['Output'][1:].values
		KNNModel = KNeighborsRegressor(n_neighbors=3,weights = 'distance')
		KNNModel.fit(trainData[100:400],trainOutput[100:400])
		prediction = KNNModel.predict(trainData[400:450])
		weightage = self.KNNWeightage['Output']
		for i in range(50):
			prediction[i] = ((prediction[i]*self.KNNModelHash['std'])+self.KNNModelHash['mean'])/weightage
			trainOutput[400+i] = ((trainOutput[400+i]*self.KNNModelHash['std'])+self.KNNModelHash['mean'])/weightage
			print "%-40s %-40s " %(prediction[i],trainOutput[400+i])
	def normalizeKNNModel(self,key):
		weightage = self.KNNWeightage[key]
		self.dataFrameKNN[key] = (self.dataFrameKNN[key] - self.dataFrameKNN[key].mean())*weightage/self.dataFrameKNN[key].std()	

class equityLearner:
	def __init__(self,quoteFile):
		try:
			self.dataFrame = pd.read_csv("data/"+quoteFile+".csv")
			self.dataFrameKNN = {}
			self.KNNWeightage = {'Avg-High Ratio':100,'Avg-Low Ratio':100,'Deliverable Qty':300,'Turnover':100,'Growth':150,'Trend':100,'Output':100}
			self.valid = True
			self.KNNModelHash = {}
		except Exception:
			self.valid = False
	def isValid(self):
		return self.valid
	def getBasicInfo(self):
		lastRow = self.dataFrame.values[-1]
		index = self.dataFrame.columns
		currentPosition = {}
		for i in range(len(index)):
			currentPosition[index[i]] = lastRow[i]
		return currentPosition
	def getCurrentSimpleMovingAverage(self):
		mean = self.dataFrame['Close Price'].tail().mean()
		return mean
	def getCurrentBollingerBands(self):
		mean = self.dataFrame['Close Price'].tail().mean()
		std = self.dataFrame['Close Price'].tail().std()
		bollingerUP = (mean+(2*std))
		bollingerLOW = (mean-(2*std))
		return {'upperBand':bollingerUP,'lowerBand':bollingerLOW}
	def graphBollingerBands(self,noDays):
		bollingerUP = []
		bollingerLOW = []
		for i in range(0,5):
			mean = self.dataFrame['Close Price'][0:i].mean()
			std = self.dataFrame['Close Price'][0:i].std()
			bollingerUP.append(mean+(2*std))
			bollingerLOW.append(mean-(2*std))
		for i in range(5,len(self.dataFrame)):
			mean = self.dataFrame['Close Price'][i-5:i].mean()
			std = self.dataFrame['Close Price'][i-5:i].std()
			bollingerUP.append(mean+(2*std))
			bollingerLOW.append(mean-(2*std))
		self.dataFrame['bollingerUP'] = pd.DataFrame(bollingerUP,range(len(self.dataFrame)))
		self.dataFrame['bollingerLOW'] = pd.DataFrame(bollingerLOW,range(len(self.dataFrame)))
		self.dataFrame[['Close Price','bollingerLOW','bollingerUP']][-noDays:].plot()
		plt.show()
	def graphSimpleMovingAverage(self,noDays):
		SMA = []
		for i in range(0,5):
			SMA.append(float(self.dataFrame['Close Price'][i]))
		for i in range(5,len(self.dataFrame)):
			mean = self.dataFrame['Close Price'][i-5:i].mean()
			SMA.append(mean)
		self.dataFrame['SMA'] = pd.DataFrame(SMA,range(len(self.dataFrame)))
		self.dataFrame[['Close Price','SMA']][-noDays:].plot()
		plt.show()
	def makeKNNModel(self):
		KNNModel(self.dataFrame)