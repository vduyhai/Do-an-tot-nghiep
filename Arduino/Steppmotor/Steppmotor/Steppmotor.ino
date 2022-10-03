//const int DIR = 4;
//const int STP = 5;
//const int EN = 6;
//const int stepsPerRevolution = 200;
//void setup() {
//  pinMode(DIR, OUTPUT);
//  pinMode(STP, OUTPUT);
//  Serial.begin(9600);
//}
//
//void loop() {
//  digitalWrite(DIR, HIGH);
//
//  for(int x = 0; x <stepsPerRevolution; x++)
//  {
//    digitalWrite(EN, LOW);
//    digitalWrite(STP, HIGH);
//    Serial.println("OK");
//    delayMicroseconds(100);
//    digitalWrite(STP, LOW);
//    delayMicroseconds(100);
//   }
//}

#include <Stepper.h>

const int steps_per_rev = 200; //Set to 200 for NIMA 17
#define IN1 8
#define IN2 9
#define IN3 10
#define IN4 11
#define enA 7
#define enB 6

Stepper motor(steps_per_rev, IN1, IN2, IN3, IN4);


void setup()
{
  motor.setSpeed(60);
  Serial.begin(9600);
  pinMode(enA, OUTPUT);
  pinMode(enB, OUTPUT);

}

void loop() 
{
  Serial.println("Rotating Clockwise...");
  motor.step(steps_per_rev);
  delay(500);

  Serial.println("Rotating Anti-clockwise...");
  motor.step(-steps_per_rev);
  delay(500);
}
