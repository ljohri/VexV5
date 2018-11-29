# VEX V5 Python-Project with Competition Template
#Imports
import sys
import vex
import math


#Variables
brain       = vex.Brain()
dev         = vex.Devices()
motor_right = vex.Motor(vex.Ports.PORT11, vex.GearSetting.RATIO18_1, True)
motor_left  = vex.Motor(vex.Ports.PORT20, vex.GearSetting.RATIO18_1, False)
motor_claw  = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO18_1, True)
motor_arm   = vex.Motor(vex.Ports.PORT2, vex.GearSetting.RATIO18_1, True)
con         = vex.Controller(vex.ControllerType.PRIMARY)
driveTrain  = vex.Drivetrain(motor_left, motor_right, 319.1764, 292.1, vex.DistanceUnits.CM)
con.set_deadband(10)
print("A welcome change!")

#Procedures
def pre_auton():
    # All activities that occur before competition start
    # Example: setting initial positions
    pass

#*******************************************************************************
def ToCm(value, units):
    if units=="FEET":
        return value*12*2.54
    if units=="INCHES":
        return value*2.54
def get_quadrant(x, y):
    quadrant = 0
    if x>0 and y>0:
        quadrant = 1
    if x<0 and y>0:
        quadrant = 2
    if x<0 and y<0:
        quadrant = 3
    if x>0 and y<0:
        quadrant = 4
    if x==0 and y==0:
        quadrant = 5
    if x==0 and y!=0:
        quadrant = 6
    if x!=0 and y==0:
        quadrant = 7
    return quadrant    
def get_angle(x, y):
    return math.atan(y/x)
def getMainMotorPower(x_axis, y_axis):
    return math.sqrt( (y_axis)*(y_axis) + (x_axis)*(x_axis)  )
def getSubordinateMotorPower(main_power, angle):
    half_pi=(3.14159265358979323846264)/2
    return (main_power*(angle/half_pi))
#*******************************************************************************
class autonomous_class:
    def goto():
        motor_arm.rotate_to(-60, vex.RotationUnits.DEG, 20, vex.VelocityUnits.PCT)
        motor_arm.stop(vex.BrakeType.HOLD)
        driveTrain.turn_for(vex.TurnType.RIGHT, 90, vex.RotationUnits.DEG, 20, vex.VelocityUnits.PCT)


    def autonomous():
        #autonomous_class.goto()
        print("Checkpoint 1: You are a failure")
        motor_arm.rotate_to(-390, vex.RotationUnits.DEG, 20, vex.VelocityUnits.PCT)
        print("Checkpoint 2: What is wrong with you!!!")
        driveTrain.drive_for(vex.DirectionType.FWD, ToCm(1, "FEET"), vex.DistanceUnits.CM, 20, vex.VelocityUnits.PCT)
        print("Checkpoint 3: What is wrong with you!!!")
        motor_arm.stop(vex.BrakeType.HOLD)
        driveTrain.turn_for(vex.TurnType.RIGHT, 100.5, vex.RotationUnits.DEG, 20, vex.VelocityUnits.PCT)
        driveTrain.drive_for(vex.DirectionType.FWD, ToCm(5.5, "FEET"), vex.DistanceUnits.CM, 40, vex.VelocityUnits.PCT)
        sys.sleep(1)
        driveTrain.drive_for(vex.DirectionType.REV, ToCm(3.35, "FEET"), vex.DistanceUnits.CM, 20, vex.VelocityUnits.PCT)
        driveTrain.turn_for(vex.TurnType.RIGHT, 102, vex.RotationUnits.DEG, 20, vex.VelocityUnits.PCT)
        driveTrain.drive_for(vex.DirectionType.REV, ToCm(2, "FEET"), vex.DistanceUnits.CM, 50, vex.VelocityUnits.PCT)
        motor_arm.rotate_to(0, vex.RotationUnits.DEG, 20, vex.VelocityUnits.PCT)
        driveTrain.drive_for(vex.DirectionType.REV, ToCm(10, "INCHES"), vex.DistanceUnits.CM, 50, vex.VelocityUnits.PCT)
        motor_arm.rotate_to(-200, vex.RotationUnits.DEG, 20, vex.VelocityUnits.PCT)
        driveTrain.drive_for(vex.DirectionType.REV, ToCm(3, "INCHES"), vex.DistanceUnits.CM, 40, vex.VelocityUnits.PCT)
#*******************************************************************************        
class driver_class:
    def drivercontrol():
        while True:
            #Maneuvering left and right
            y_axis  = con.axis3.position()
            x_axis  = con.axis4.position()
            quadrant = get_quadrant(x_axis, y_axis)
            
            max_power = 0.4
            if con.buttonB.pressing():
                max_power = max_power*2
            
            left_power=0
            right_power=0                
            
            if quadrant==5:
                left_power=0
                right_power=0
                
            if quadrant==6:
                left_power  = y_axis*max_power
                right_power = left_power
            
            if quadrant==7:
                if x_axis>0:
                    left_power  = x_axis*max_power
                    right_power = 0
                else:
                    right_power = (x_axis)*(-1)*max_power
                    left_power  = 0
            angle=0
            if quadrant==1:
                left_power  = getMainMotorPower(x_axis, y_axis)
                angle       = get_angle(x_axis, y_axis)
                right_power = getSubordinateMotorPower(left_power, angle)*max_power
                left_power  = int(left_power)*max_power
            if quadrant==2:
                right_power = getMainMotorPower(x_axis, y_axis)
                angle       = get_angle(x_axis*(-1), y_axis)
                left_power  = getSubordinateMotorPower(right_power, angle)*max_power
                right_power = int(right_power)*max_power
            if quadrant==3:
                right_power = getMainMotorPower(x_axis*(-1), y_axis*(-1))
                angle       = get_angle(x_axis*(-1), y_axis*(-1))
                left_power  = getSubordinateMotorPower(right_power, angle)*(-1)*max_power
                right_power = int(right_power)*(-1)*max_power
            if quadrant==4:
                left_power  = getMainMotorPower(x_axis, y_axis*(-1))
                angle       = get_angle(x_axis*(-1), y_axis*(-1))
                right_power = getSubordinateMotorPower(left_power, angle)*(-1)*max_power
                left_power  = int(left_power)*(-1)*max_power
                    
            motor_left.spin (vex.DirectionType.FWD, left_power, vex.VelocityUnits.PCT)
            motor_right.spin(vex.DirectionType.FWD, right_power, vex.VelocityUnits.PCT)
            
            print("Quadrant: ", quadrant)
            print("Left motor: ", motor_left.rotation())
            print("Right motor: ", motor_right.rotation())
            
            #Maneuvering the claw
            if con.buttonL1.pressing():
                motor_claw.spin(vex.DirectionType.FWD, 100, vex.VelocityUnits.PCT)
                print("You pressed L1! Congratulations!")
            elif con.buttonL2.pressing():
                motor_claw.spin(vex.DirectionType.REV, 85, vex.VelocityUnits.PCT)
                print("You pressed L2! Congratulations!")
            else:
                motor_claw.stop(vex.BrakeType.HOLD)
            
            #Maneuvering the arm
            if con.buttonR1.pressing():
                motor_arm.spin(vex.DirectionType.REV, 100*max_power*0.5, vex.VelocityUnits.PCT)
                print("You pressed R1! Congratulations!")
            elif con.buttonR2.pressing():
                motor_arm.spin(vex.DirectionType.FWD, 100*max_power*0.5, vex.VelocityUnits.PCT)
                print("You pressed R2! Congratulations!")
            else:    
                motor_arm.stop(vex.BrakeType.HOLD)
                
            sys.sleep(0.08)

#main section
autonomous_class.autonomous()
#driver_class.drivercontrol()
