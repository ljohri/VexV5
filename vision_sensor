'''
To use this example, you will need to configure the TARGETBLOB signature to match your target given your own target requirements and lighting conditions. It is highly unlikely that the blob the example author configured will match your intended target.

 

This program will wait passively while nothing that matches TARGETBLOB is in the frame. When something that matches TARGETBLOB is spotted, the program will determine whether the target is to the camera's left or right, then turn towards it until the target is in the middle of the camera's field of view.

 

Motor connections:

Port 15: right side drive motor (200 RPM)
Port 16: left side drive motor (200 RPM)
'''

import vex

#region config
brain          = vex.Brain();
vision_9       = vex.Vision(vex.Ports.PORT9)
sig_TARGETBLOB = vex.VisionSignature(1,101,3217,1659,-4681,-3869,-4275,2.3,0)
vision_9.set_brightness(50);
vision_9.set_signature(sig_TARGETBLOB)
motor_right    = vex.Motor(vex.Ports.PORT15, vex.GearSetting.RATIO18_1, True)
motor_left     = vex.Motor(vex.Ports.PORT16, vex.GearSetting.RATIO18_1, False)
dt             = vex.Drivetrain(motor_left, motor_right, 319.1764, 292.1, vex.DistanceUnits.MM)
#endregion config

screen_middle_x = None
linedup = None


# main thread
# Camera image is 316x212, so 316/2 is the middle
screen_middle_x = 316 / 2
linedup = False
# We're going to be turning, but don't
# need to do so quickly.
dt.set_velocity(5, vex.VelocityUnits.PCT)
while not linedup:
  # Snap a picture
  vision_9.take_snapshot(sig_TARGETBLOB)
  # Did we see anything that we were looking for?
  if vision_9.object_count > 0:
    # Largest thing to the left, right, or middle?
    if vision_9.largest_object.centerX < screen_middle_x - 5:
      # On the left, turn towards it
      dt.turn(vex.TurnType.LEFT)
    elif vision_9.largest_object.centerX > screen_middle_x + 5:
      # On the right, turn towards it
      dt.turn(vex.TurnType.RIGHT)
    else:
      # In the middle! We're done lining up.
      linedup = True
      dt.stop(vex.BrakeType.COAST)
  else:
    # Saw nothing, relax
    dt.stop(vex.BrakeType.COAST)