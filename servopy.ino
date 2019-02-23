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
    input_data = Serial.readStringUntil('\n'); // read data until newline  
    pos = input_data.toFloat();
    t = deg2ms(pos);
    myservo.writeMicroseconds( t );
    delay(100);
    }
}

float deg2ms(float alpha){
  int t;
  // Return the microseconds to wait for the servo to be in
  //a certain angle. The angles are defined as:
  //       0
  // [servo] 90
  //      180
  t = 700+(2500-700)*(1-(alpha/180));
  return t;
}
