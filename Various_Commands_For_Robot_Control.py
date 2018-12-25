# VEX V5 Python-Project with Competition Template
# 
# Start Robot from Blue box from 2nd square and facing West
#
#Imports
import sys
import vex
import math

#Variables
dev         = vex.Devices()
motor_right = vex.Motor(vex.Ports.PORT11, vex.GearSetting.RATIO18_1, True)
motor_left  = vex.Motor(vex.Ports.PORT20, vex.GearSetting.RATIO18_1, False)
motor_claw  = vex.Motor(vex.Ports.PORT10, vex.GearSetting.RATIO18_1, True)
motor_arm   = vex.Motor(vex.Ports.PORT2, vex.GearSetting.RATIO18_1, True)
con         = vex.Controller(vex.ControllerType.PRIMARY)
driveTrain  = vex.Drivetrain(motor_left, motor_right, 319.1764, 292.1, vex.DistanceUnits.CM)
con.set_deadband(10)

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

sleep_between_functions = 2
first_turn = 78
first_distance = 5 # feet
cap_turn = -180
podium_turn = 160
podium_distance1 = 1 # feet
podium_reverse_turn = 180
podium_distance2 = 3 # feet

class autonomous_class_s:

    def goto():
        motor_arm.rotate_to(-60, vex.RotationUnits.DEG, 20, vex.VelocityUnits.PCT)
        motor_arm.stop(vex.BrakeType.HOLD)
        driveTrain.turn_for(vex.TurnType.RIGHT, 45, vex.RotationUnits.DEG, 20, vex.VelocityUnits.PCT)
        driveTrain.drive_for(vex.DirectionType.FWD, ToCm(2, "FEET"), \
                             vex.DistanceUnits.CM, 20, vex.VelocityUnits.PCT)


    def goto_podium():
        driveTrain.turn_for(vex.TurnType.LEFT, podium_turn, vex.RotationUnits.DEG, 20, vex.VelocityUnits.PCT)
        driveTrain.drive_for(vex.DirectionType.FWD, ToCm(podium_distance1, "FEET"), \
                             vex.DistanceUnits.CM, 20, vex.VelocityUnits.PCT)
        driveTrain.turn_for(vex.TurnType.LEFT, podium_reverse_turn, vex.RotationUnits.DEG, 20, vex.VelocityUnits.PCT)
        driveTrain.drive_for(vex.DirectionType.FWD, ToCm(podium_distance2, "FEET"), \
                             vex.DistanceUnits.CM, 20, vex.VelocityUnits.PCT)

    def turn_over_cap():
        # bring arm down
        motor_arm.rotate_to(5, vex.RotationUnits.DEG, 20, vex.VelocityUnits.PCT)
        motor_arm.stop(vex.BrakeType.HOLD)

        # turn over cap
        driveTrain.drive_for(vex.DirectionType.FWD, ToCm(8, "INCHES"), \
                             vex.DistanceUnits.CM, 30, vex.VelocityUnits.PCT, False)
        motor_arm.rotate_to(cap_turn, vex.RotationUnits.DEG, 50, vex.VelocityUnits.PCT)

    def goto_cap():
        # turn and go drive to cap
        driveTrain.turn_for(vex.TurnType.RIGHT, first_turn, vex.RotationUnits.DEG, 20, vex.VelocityUnits.PCT)
        driveTrain.drive_for(vex.DirectionType.FWD, ToCm(first_distance, "FEET"), \
                             vex.DistanceUnits.CM, 20, vex.VelocityUnits.PCT)

    def starting_arm_up():
        # move arm up
        motor_arm.rotate_to(-60, vex.RotationUnits.DEG, 20, vex.VelocityUnits.PCT)
        sys.sleep(2)
        motor_arm.stop(vex.BrakeType.HOLD)

    def autonomous():
        autonomous_class_s.starting_arm_up()
        sys.sleep(sleep_between_functions)
        autonomous_class_s.goto_cap()
        sys.sleep(sleep_between_functions)
        autonomous_class_s.turn_over_cap()
        sys.sleep(sleep_between_functions)
        autonomous_class_s.goto_podium()


#main section
autonomous_class_s.autonomous()
