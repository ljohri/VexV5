#include "main.h"

/**
 * Runs the operator control code. This function will be started in its own task
 * with the default priority and stack size whenever the robot is enabled via
 * the Field Management System or the VEX Competition Switch in the operator
 * control mode.
 *
 * If no competition control is connected, this function will run immediately
 * following initialize().
 *
 * If the robot is disabled or communications is lost, the
 * operator control task will be stopped. Re-enabling the robot will restart the
 * task, not resume it from where it left off.
 */

static int dist_mm =0;
static int line_right_val, line_left_val, line_mid_val;

void opcontrol() {
	pros::Controller master(pros::E_CONTROLLER_MASTER);
	pros::Motor left_mtr(MOTORPORT_LEFT);
	pros::Motor right_mtr(MOTORPORT_RIGHT);

	left_mtr.move_absolute(100,100);
	pros::delay(2000);
	right_mtr.move_absolute(100,100);

	printf("hello world: debug");
	while (true) {
		pros::lcd::print(0, "%d %d %d", (pros::lcd::read_buttons() & LCD_BTN_LEFT) >> 2,
		                 (pros::lcd::read_buttons() & LCD_BTN_CENTER) >> 1,
		                 (pros::lcd::read_buttons() & LCD_BTN_RIGHT) >> 0);
		int left = master.get_analog(ANALOG_LEFT_Y);
		int right = master.get_analog(ANALOG_RIGHT_Y);

		left_mtr = left;
		right_mtr = right;
		pros::delay(20);
	}
}


void sensor_read( void* arg)
{
 	std::cout << "In sensor read\n" ;
 	pros::ADIUltrasonic ultra_sensor (PORT_PING, PORT_ECHO);
	int dist_prev=0; 
	pros::ADIAnalogIn line_left(ANALOG_SENSOR_PORT_LEFT);
	pros::ADIAnalogIn line_right(ANALOG_SENSOR_PORT_RIGHT);
	pros::ADIAnalogIn line_mid(ANALOG_SENSOR_PORT_MID);

	unsigned int  time = 0 ;
	unsigned int loop_var = 1;

 	for(;;)
 	{
		 if( loop_var == 0 )
			loop_var =1 ;

		if( loop_var%1000 == 0)
			std::cout << "Time since start (ms) : " << pros::millis() << std::endl ; 

		 //read distance in mm - 1 cm accuracy till ~2ft(?)	
		 dist_prev = dist_mm;
		 dist_mm = ultra_sensor.get_value();

		 if( abs(dist_mm-dist_prev) > 10 )
		 	std::cout << "dist is : " << dist_mm  << std::endl ; 
		 
		//read the line sensors
		
		int left_pr=0,mid_pr=0,right_pr=0 ;
	
		left_pr = line_left_val;
		line_left_val = line_left.get_value();

		right_pr = line_right_val;
		line_right_val = line_right.get_value();

		mid_pr = line_mid_val;
		line_mid_val = line_mid.get_value() ;

		if( abs(dist_mm-dist_prev) > 10 )
		 	std::cout << "dist is : " << dist_mm  << std::endl ; 

		if( abs(left_pr-line_left_val)>10)
			std::cout << "left line val : "	<< line_left_val << std::endl; 	

		if( abs(right_pr-line_right_val)>10)
			std::cout << "right line val : "	<< line_right_val << std::endl; 	

		if( abs(mid_pr-line_mid_val)>10)
			std::cout << "mid line val : "	<< line_mid_val << std::endl; 	

		pros::delay(10);
	}

}