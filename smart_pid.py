# cav-pid.py - Runs motors with constant angular velocity, using shaft encoders,
#              and a proportional integral derivative control loop.
#
# Almost all the heavy lifting done by cnr437@gmail.com, 
# (http://code.activestate.com/recipes/577231-discrete-pid-controller/)
# adopted to run on VEX robots by sam@robotmesh.com
# further adopted to run on VexV5 by ljohri@gmail.com
#
# This file is licensed under the terms of the MIT license.

import sys
import vex
import math
from vex import *
from math import *
  
#The recipe gives simple implementation of a Discrete Proportional-Integral-Derivative (PID) controller. PID controller gives output value for error between desired reference input and measurement feedback to minimize error value.
#More information: http://en.wikipedia.org/wiki/PID_controller
#
#cnr437@gmail.com
#
####### Example #########
#
#p=PID(3.0,0.4,1.2)
#p.setPoint(5.0)
#while True:
#     pid = p.update(measurement_value)
print('start')


con     = vex.Controller(vex.ControllerType.PRIMARY)

motor_right = vex.Motor(vex.Ports.PORT11, vex.GearSetting.RATIO18_1, True)
motor_left = vex.Motor(vex.Ports.PORT20, vex.GearSetting.RATIO18_1, False)
dt          = vex.Drivetrain(motor_left, motor_right, 319.1764, 292.1, vex.DistanceUnits.MM)
arm = vex.Motor(vex.Ports.PORT2, vex.GearSetting.RATIO18_1, False)
arm.reset_rotation()

arm.rotate_to (30, RotationUnits.DEG, 30, vex.VelocityUnits.PCT,True)
arm.stop()

#encoder_right = vex.Encoder(brain.three_wire_port.e)
#encoder_left = vex.Encoder(brain.three_wire_port.b)
#encd  = vex.Encoder(brain.three_wire_port.d)
#encd.reset_rotation()
#encoder_right.reset_rotation()
#encoder_left.reset_rotation()
'''
pid_right = pidmotor(motor_right, encoder_right)
pid_left  = pidmotor(motor_left, encoder_left)

sys.run_in_thread(pid_right.run())
sys.run_in_thread(pid_left.run())
'''

while True:
    
    direction = vex.DirectionType.FWD
    y_axis = con.axis3.position()
    x_axis = con.axis4.position()
 
    angle_rad = math.atan2(y_axis, x_axis) 
    angle_deg = math.degrees(angle_rad)
    r = math.sqrt(y_axis*y_axis+x_axis*x_axis)
 

    if( angle_deg >=0 and angle_deg <= 90 ):
        vel_right = r*(1-math.cos(angle_rad))
        vel_left = r
    elif( angle_deg > 90 and angle_deg <= 180) :
        theta_prime = math.pi - angle_rad;
        vel_left = r*(1-math.cos(theta_prime))
        vel_right = r
    elif( angle_deg > 180 and angle <= math.pi*1.5) :    
        theta_prime = math.pi*1.5 - angle_rad;
        vel_left = r*(1-math.cos(theta_prime))
        vel_right = r
        dierction = vex.DirectionType.REV
    else:
        theta_prime = math.pi*2 - angle_rad;
        vel_right = r*(1-math.cos(theta_prime))
        vel_left = r
        direction = vex.DirectionType.REV
    
    if( x_axis > 0 or y_axis > 0 ):
        print('r=',r, 'angle=',angle_deg,'vel_left=',vel_left, 'vel right=',vel_right)
        

    if( con.buttonB.pressing() == True ):
        if( vel_right <= 10):
            motor_right.stop()
        else:
            motor_right.spin(direction,vel_right)
        
        if( vel_left <= 10):
            motor_left.stop()
        else:
            motor_left.spin(direction,vel_left)
    else :
        r = r/4
        
        dt.set_velocity(r, vex.VelocityUnits.PCT)
        print( r,angle_deg-90,direction )
        if( r < 10 ):
            dt.stop()
        elif( angle_deg <= 80 and angle_deg >= 0 ):
            dt.turn_for(vex.TurnType.RIGHT, angle_deg, vex.RotationUnits.DEG,r, vex.VelocityUnits.PCT)
        elif(angle_deg > 95 and angle_deg <= 180  ) :
            dt.turn_for(vex.TurnType.LEFT, angle_deg-90,vex.RotationUnits.DEG,r, vex.VelocityUnits.PCT)
        else :    
            dt.drive(direction)
    if(con.buttonX.pressing() == True):
        dt.drive_for(vex.DirectionType.FWD, 200, vex.DistanceUnits.MM, 30, vex.VelocityUnits.PCT, True) 
    
    if   ( con.buttonR1.pressing() == True ) :
        arm.spin(vex.DirectionType.FWD,30,  vex.VelocityUnits.PCT)
    elif ( con.buttonR2.pressing() == True) :
        arm.spin(vex.DirectionType.REV,30,  vex.VelocityUnits.PCT)
    else :
        arm.stop(vex.BrakeType.HOLD)
    
    
    sys.sleep(.05)
    



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


class pidmotor:
    #Either runs a motor at a constant angular velocity, or holds it at
    #a position.
    def __init__(self, my_motor, my_encoder, setPoint=0, P=2, I=0.01, D=0.01):
        self.p1 = PID(P, I, D)
        self.p1.setPoint(setPoint)
        self.motor = my_motor

    def target_velocity( self, my_vel):
        self.p1.setPoint(my_vel)
    def run(self):
        while True:
            foo = self.p1.update(my_encoder.value())
            self.motor.run(foo)
            pass

#p2 = PID(2.0, 0.01, 0.01)
#p2.setPoint(10.0)



#endregion config

