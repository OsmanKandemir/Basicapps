import sys
import os



class DataMSameFiles:
	def __init__(self,first,second,third = None):
		files = {
				"File1" : first,
				"File2" : second
		}
		for firsts,seconds in files.items():
			print firsts,seconds

		self.first = first
		self.second = second
	def FirstFile(self,first,second = None):
		return self.first
	def SecondFile(self,second,first = None):
		return self.secondfile
	def OpenFile(self,thirdfile):
		with open(self.first,"rw+") as one1:
			print one1.readlines()
		with open(self.second,"rw+") as two2:
			print two2.readlines()
	

deneme = DataMSameFiles("First.txt","Second.txt")
print deneme.OpenFile(thirdfile = None)
