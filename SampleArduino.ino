
#include <Servo.h>
Servo servoLeft;
Servo servoRight;

void setup() 
  // put your setup code here, to run once: these are pins
 {
  servoLeft.attach(13);
  servoRight.attach(12);
 }
void loop()
{
  // put your main code here, to run repeatedly:
 servoLeft.writeMicroseconds(1700);
 servoRight.writeMicroseconds(1300);
 delay(5000);
 exit(0);
}

