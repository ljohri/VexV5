# cav-pid.py - Runs motors with constant angular velocity, using shaft encoders,
#              and a proportional integral derivative control loop.
#
# Almost all the heavy lifting done by cnr437@gmail.com, 
# (http://code.activestate.com/recipes/577231-discrete-pid-controller/)
# adopted to run on VEX robots by sam@robotmesh.com
#
# This file is licensed under the terms of the MIT license.

import vexcortex as vex
import sys

# You'll want this to be the encoder that the motor's on, or else you'll be
# very confused. Here I'm using a motor on port 1, and a quad encoder on port 7.
rightencoder = vex.digital_quad_encoder(7)
leftencoder = vex.digital_quad_encoder(4)
motor10 = vex.motor(10, True)
motor1 = vex.motor(1)

switch = vex.digital_input(12)
  
#The recipe gives simple implementation of a Discrete Proportional-Integral-Derivative (PID) controller. PID controller gives output value for error between desired reference input and measurement feedback to minimize error value.
#More information: http://en.wikipedia.org/wiki/PID_controller
#
#cnr437@gmail.com
#
#######	Example	#########
#
#p=PID(3.0,0.4,1.2)
#p.setPoint(5.0)
#while True:
#     pid = p.update(measurement_value)



class PID:
	"""
	Discrete PID control
	"""

	def __init__(self, P=2.0, I=0.0, D=1.0, Derivator=0, Integrator=0, Integrator_max=500, Integrator_min=-500):

		self.Kp=P
		self.Ki=I
		self.Kd=D
		self.Derivator=Derivator
		self.Integrator=Integrator
		self.Integrator_max=Integrator_max
		self.Integrator_min=Integrator_min

		self.set_point=0.0
		self.error=0.0

	def update(self,current_value):
		"""
		Calculate PID output value for given reference input and feedback
		"""

		self.error = self.set_point - current_value

		self.P_value = self.Kp * self.error
		self.D_value = self.Kd * ( self.error - self.Derivator)
		self.Derivator = self.error

		self.Integrator = self.Integrator + self.error

		if self.Integrator > self.Integrator_max:
			self.Integrator = self.Integrator_max
		elif self.Integrator < self.Integrator_min:
			self.Integrator = self.Integrator_min

		self.I_value = self.Integrator * self.Ki

		PID = self.P_value + self.I_value + self.D_value

		return PID

	def setPoint(self,set_point):
		"""
		Initilize the setpoint of PID
		"""
		self.set_point = set_point
		self.Integrator=0
		self.Derivator=0

	def setIntegrator(self, Integrator):
		self.Integrator = Integrator

	def setDerivator(self, Derivator):
		self.Derivator = Derivator

	def setKp(self,P):
		self.Kp=P

	def setKi(self,I):
		self.Ki=I

	def setKd(self,D):
		self.Kd=D

	def getPoint(self):
		return self.set_point

	def getError(self):
		return self.error

	def getIntegrator(self):
		return self.Integrator

	def getDerivator(self):
		return self.Derivator

vex.start()

class pidmotor:
    #Either runs a motor at a constant angular velocity, or holds it at
    #a position.
    def __init__(self, motornumber, setPoint, P=2, I=0.01, D=0.01):
        self.p1 = PID(P, I, D)
        self.p1.setPoint(setPoint)
        self.motor = vex.motor(motornumber)

    def run(self):
        while True:
            foo = self.p1.update(rightencoder.value())
            self.motor.run(foo)

#p2 = PID(2.0, 0.01, 0.01)
#p2.setPoint(10.0)

fuzz = pidmotor(1, 20)
sys.runInThread(fuzz.run())

"""
def right():
    while True:
        pid = p2.update(rightencoder.value())
        motor1.run(pid)
        print pid
        if switch.is_on():
            x = rightencoder.value()
            x += 10
            rightencoder.value(x)

def left():       
    while True:
        pid = p2.update(leftencoder.value())
        motor10.run(pid)
        print pid
        if switch.is_on():
            x = rightencoder.value()
            x += 10
            leftencoder.value(x)
"""

#sys.runInThread(right)
#sys.runInThread(left)