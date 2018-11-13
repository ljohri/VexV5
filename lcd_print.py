# VEX IQ Python-Project
import sys
import vexiq

# Use vexiq.lcd_write to print to the LCD.
# first param is the text to write
# second param is the row, 1 to 5.  Default 1
# thirs param is the column, 1 to 25.  Default 1

vexiq.lcd_write('LCD write row 1')  # Defaults to row 1, column 1 if last parameters aren't provided

vexiq.lcd_write('Hello world', 2)   # Prints on row 2

# Counting number on row 3
for i in range(10) :
    vexiq.lcd_write(i, 3, 5)        # Prints on row 3, column 5
    sys.sleep(1)
    
# Horizontally Scrolling text
for i in range(1, 20) :
    vexiq.lcd_write(' Done', 5, i)
    sys.sleep(0.1)