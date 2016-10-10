from plane import Plane
import time


plane = Plane()

while True:
	plane.move()
	angle = plane.getAngle()
	print "Current angle: ", angle
	correction = plane.getCorrection()
	plane.setCorrection(correction)
	print "Applied correction: ", plane.getAppliedCorrection()
	time.sleep(1)
	
