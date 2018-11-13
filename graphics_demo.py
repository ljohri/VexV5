# VEX V5 Python Project
import sys
import vex
import math
from vex import *

#region config
brain    = vex.Brain();
bumper_a = vex.Bumper(brain.three_wire_port.a)
#endregion config

tau = math.pi * 2

DELAY = 0.001 # Delay in seconds between each draw call

def checkerboard():
    for x in range(10):
        for y in range(5):
            brain.screen.draw_rectangle(x*48, y*48, 24, 24, Color.WHITE)
            brain.screen.draw_rectangle(x*48+24, y*48+24, 24, 24, Color.WHITE)
            #sys.sleep(DELAY)

def lined_circle():
    angle1 = 0
    angle2 = 0
    brain.screen.draw_circle(240, 120, 100, Color.YELLOW)
    brain.screen.set_pen_color(Color.BLUE)
    for x in range(12, 0, -1):
        for y in range(x):
            brain.screen.draw_line(240-100*math.sin(angle1), 120-100*math.cos(angle1), 240-100*math.sin(angle2), 120-100*math.cos(angle2))
            angle2 += tau/12
            #sys.sleep(DELAY)
        angle1 += tau/12
        angle2 = angle1
    
checkerboard()
lined_circle()