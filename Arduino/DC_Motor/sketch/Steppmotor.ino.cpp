#include <Arduino.h>
#line 1 "D:\\Do-an-tot-nghiep\\Arduino\\Steppmotor\\Steppmotor\\Steppmotor.ino"
const int DIR = 9;
const int STP = 8;
const int stepsPerRevolution = 200;
#line 4 "D:\\Do-an-tot-nghiep\\Arduino\\Steppmotor\\Steppmotor\\Steppmotor.ino"
void setup();
#line 10 "D:\\Do-an-tot-nghiep\\Arduino\\Steppmotor\\Steppmotor\\Steppmotor.ino"
void loop();
#line 4 "D:\\Do-an-tot-nghiep\\Arduino\\Steppmotor\\Steppmotor\\Steppmotor.ino"
void setup() {
  pinMode(DIR, OUTPUT);
  pinMode(STP, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(DIR, HIGH);

  for(int x = 0; x <stepsPerRevolution; x++)
  {
   digitalWrite(STP, HIGH);
   Serial.println("OK");
   delay(1000);
   digitalWrite(STP, LOW);
   delay(1000);
   }
}

