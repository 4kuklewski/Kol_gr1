import random

class Plane:
	def __init__(self):
		self.angle = 0
		self.stdev = 1

	def move(self):
		self.angle += random.gauss(2, self.stdev)

	def getAngle(self):
		return self.angle

	def setCorrection(self, correction):
		correction = (correction/2. + self.stdev)
		self.angle -= correction
		return correction

	def getCorrection(self):
		# returns max possible correction for plane
		return self.angle
	
	
	


