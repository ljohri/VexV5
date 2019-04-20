#include "main.h"
#include "api.h"
#define ANALOG_SENSOR_PORT_RIGHT 5
#define ANALOG_SENSOR_PORT_MID 6
#define ANALOG_SENSOR_PORT_LEFT 7 
#define MAX_VAL 4095
#define BLACK  500
#define WHITE  900
#define TICK 5
#define ATTENUATION 0.1
#define TURN_ATTENUATION 0.7
#define GAIN_ATTENUATION 1.1
#define SPEED 150
#define STRAIGHT 0
#define LEFT 1
#define RIGHT 2
#define MAX_VOLTAGE 12000 
#define MOTORPORT_LEFT  20
#define MOTORPORT_RIGHT  13

typedef enum {
	straight=0,
	left_turn,
	right_turn,
	indeterminate_turn

} state_t;

pros::Motor* m_r;
pros::Motor* m_l;



static void line_follower();
static void drive( state_t dir, int speed);
static void camera_module();
void stop();

void on_center_button() {
	static bool pressed = false;
	pressed = !pressed;
	if (pressed) {
		pros::lcd::set_text(2, "I was pressed!");
	} else {
		pros::lcd::clear_line(2);
	}
}

/**
 * Runs initialization code. This occurs as soon as the program is started.
 *
 * All other competition modes are blocked by initialize; it is recommended
 * to keep execution time for this mode under a few seconds.
 */
void initialize() {
	pros::lcd::initialize();
	pros::lcd::set_text(1, "Hello PROS User!");
	pros::lcd::register_btn1_cb(on_center_button);
	
	pros::Motor drive_left(MOTORPORT_LEFT, pros::E_MOTOR_GEARSET_18, true, pros::E_MOTOR_ENCODER_DEGREES);
	pros::Motor drive_right(MOTORPORT_RIGHT, pros::E_MOTOR_GEARSET_18, false, pros::E_MOTOR_ENCODER_DEGREES);

	 

	pros::ADIGyro gyro (1);
	pros::delay(2000);
	double TURN = 90;
	double turn = 0;
	double turn_velocity_start = 50; 
	double turn_velocity = turn_velocity_start;
	printf("..... turn:%f", turn);
	while (true) 
	{
    	// Get the gyro heading
		turn = fabs(gyro.get_value())/10 ;
		turn_velocity = 2* turn_velocity_start * (TURN-turn)/90 ;

		if( TURN-turn < 0.1 ) 
		{
			turn_velocity = 0;
			printf(". turn:%f", turn);
			break;
		}
		drive_left.move_velocity(turn_velocity);
		drive_right.move_velocity(turn_velocity*(-1));
		if( turn_velocity == 0 )
			break;
		pros::delay(1);
	}
	printf("..... turn:%f", turn);
	pros::delay(10000*10);
	return ;

	
	

}

void camera_module()
{
	FILE *fp;
	char buf[50];
	if ( (fp = fopen("/usd/data1.txt","w")) == NULL)
	{
		perror("write file error: ");
		printf("write file open error %s:%d\n",__FILE__,__LINE__);
	}
	if( fp)
	{
		fprintf(fp, "hello world\n");
		fclose(fp);
	}

	if ( (fp = fopen("/usd/test.txt","r")) == NULL)
	{
		perror("read file error: ");
		printf("read file open error %s:%d\n",__FILE__,__LINE__);
		return ;
	}
	fread(buf,1,50,fp);
	printf(buf);
	fclose(fp);
	return ;
}

void line_follower()
{
	unsigned tm,val ;

	pros::ADIAnalogIn s_r (ANALOG_SENSOR_PORT_RIGHT);
	pros::ADIAnalogIn s_m (ANALOG_SENSOR_PORT_MID);
	pros::ADIAnalogIn s_l (ANALOG_SENSOR_PORT_LEFT);
	//tm= pros::millis();
  	//sensor.calibrate();
	//printf("Calibrated Reading:%d  Calibration time:%d\n", sensor.get_value_calibrated(),pros::millis()-tm )  ;
  	//std::cout << "Calibrated Reading:" << sensor.get_value_calibrated() << "Calibration time" << pros::millis()-tm;
	
	for( int i=0;i<2;i++)
	{
		tm= pros::millis();
		pros::delay(1000); 
		val= s_m.get_value();
		printf("hello world time:%u  l:%u m:%u r:%u\n", pros::millis()-tm,
		s_l.get_value(),s_m.get_value(),s_r.get_value() );
	}


 
	state_t dir ;

	m_r = new pros::Motor(13, pros::E_MOTOR_GEARSET_18, true, pros::E_MOTOR_ENCODER_DEGREES);
	m_l = new pros::Motor(20, pros::E_MOTOR_GEARSET_18, false, pros::E_MOTOR_ENCODER_DEGREES);

	 
	dir = straight;
	int speed = SPEED;
	drive(dir,speed);
	printf("should go straight-2\n");

	while ( s_m.get_value()  >  WHITE ); //keep going slow till you hit white with the middle sensor
	
	printf("h1. l:%u m:%u r:%u\n", 
		s_l.get_value(),s_m.get_value(),s_r.get_value() );

	int start_tm = pros::millis();
	for(;;)
	{
	
		if( pros::millis()-start_tm > 1000*10)
			stop();
		//continue in the same line
		if( s_m.get_value() < WHITE )
		{
			pros::delay(TICK);
			dir = straight;
			continue ;
		}
		dir=indeterminate_turn ; //middle sensor not on white 

		
		//have to wait for the left or right sensor 
		//to hit white, while continue stright
		unsigned  int r,l,m;
		
		int cnt;
		cnt=0;
		while(dir == indeterminate_turn)
		{
			m = s_m.get_value();
			r = s_r.get_value();
			l = s_l.get_value();
			if( r  < WHITE)
				dir = right_turn ;
			else if( l  < WHITE)
				dir = left_turn ;
			pros::delay(TICK);
			printf("dir:%d l:%u m:%u r:%u\n",dir, l,m,r);	
		}
		
		//printf("drive:%u\n",dir);
		drive(dir,speed); //now we will have right or the left sensor triggered
		
		while( m >  WHITE)
		{
			m = s_m.get_value();
			r = s_r.get_value();
			l = s_l.get_value();
		}  //wait for the turn to complete
		//printf("turn complete l:%u m:%u r:%u\n", l,m,r);	

		
		dir = straight;
		drive(dir,speed)	; //straighten the wheel	
	} 
}


void drive( state_t turn_dir, int speed)
{
	#if VELOCITY
	if( turn_dir == straight)
	{
		m_r->move_velocity(speed);
		m_l->move_velocity(speed);
	}
	else if( turn_dir == left_turn)
	{
		m_r->move_velocity(speed/2);
		m_l->move_velocity( 0);
	}
	else if( turn_dir == right_turn)
	{
		m_l->move_velocity(speed/2);
		m_r->move_velocity( 0);
	}
	#else
	printf("orig speed=%d\n",speed);
	speed = speed*(MAX_VOLTAGE/200);
	printf("Speed=%d\n",speed);
	if( turn_dir == straight)
	{
		m_r->move_voltage(speed);
		m_l->move_voltage(speed);
	}
	else if( turn_dir == left_turn)
	{
		m_r->move_voltage(speed);
		m_l->move_voltage( speed*(-1));
	}
	else if( turn_dir == right_turn)
	{
		m_l->move_voltage(speed);
		m_r->move_voltage( speed*(-1));
	}
	#endif
}

void stop()
{
	m_r->move_velocity(0);
	m_l->move_velocity(0);
	exit(0);
}

/**
 * Runs while the robot is in the disabled state of Field Management System or
 * the VEX Competition Switch, following either autonomous or opcontrol. When
 * the robot is enabled, this task will exit.
 */
void disabled() {}

/**
 * Runs after initialize(), and before autonomous when connected to the Field
 * Management System or the VEX Competition Switch. This is intended for
 * competition-specific initialization routines, such as an autonomous selector
 * on the LCD.
 *
 * This task will exit when the robot is enabled and autonomous or opcontrol
 * starts.
 */
void competition_initialize() {}
