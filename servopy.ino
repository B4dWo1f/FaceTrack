#include <Servo.h>
Servo myservo; 
const int servoPin=5;

void setup(){
  Serial.begin(9600);
  Serial.setTimeout(50);
  myservo.attach(servoPin);
}

void loop()
{
  int pos, t;
  String input_data;
  if(Serial.available())  // if data available in serial port
    { 
    // Read input data from python
    input_data = Serial.readStringUntil('\n');
    pos = input_data.toFloat();
    // Calculate pulse and send to servo
    t = deg2ms(pos);
    myservo.writeMicroseconds( t );
    delay(100);
    }
}

float deg2ms(float alpha){
  int t;
  //  Return lenght of the HIGH pulse (in microseconds) to move the servo to
  // a certain angle. The angles are defined as:
  //         0
  //   [servo] 90
  //        180
  t = 700+(2500-700)*(1-(alpha/180));
  return t;
}
