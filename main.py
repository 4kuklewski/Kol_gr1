from plane import Plane
import time


plane = Plane()

while True:
	plane.move()
	angle = plane.getAngle()
	print "Current angle: ", angle
	correction = plane.getCorrection()
	correction = plane.setCorrection(correction)
	print "Applied correction: ", correction
	time.sleep(1)
	
