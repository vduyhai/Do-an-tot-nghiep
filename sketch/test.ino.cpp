#include <Arduino.h>
#line 1 "D:\\Do-an-tot-nghiep\\Arduino\\DC_motor\\DC_motor\\src\\test\\test.ino"
int EnA = 8;
int IN1 = 7;
int IN2 = 6;

#line 5 "D:\\Do-an-tot-nghiep\\Arduino\\DC_motor\\DC_motor\\src\\test\\test.ino"
void setup();
#line 10 "D:\\Do-an-tot-nghiep\\Arduino\\DC_motor\\DC_motor\\src\\test\\test.ino"
void run();
#line 16 "D:\\Do-an-tot-nghiep\\Arduino\\DC_motor\\DC_motor\\src\\test\\test.ino"
void loop();
#line 5 "D:\\Do-an-tot-nghiep\\Arduino\\DC_motor\\DC_motor\\src\\test\\test.ino"
void setup() {
  pinMode(EnA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
}
void run(){
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(EnA, 255);
  delay(100);
}
void loop() {
  run();
  delay(1000);
}

