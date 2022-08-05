#include <Arduino.h>
#line 1 "D:\\Do-an-tot-nghiep\\Arduino\\Sensor\\sensor\\sensor.ino"
const int sensor = 5;

#line 3 "D:\\Do-an-tot-nghiep\\Arduino\\Sensor\\sensor\\sensor.ino"
void setup();
#line 8 "D:\\Do-an-tot-nghiep\\Arduino\\Sensor\\sensor\\sensor.ino"
void loop();
#line 3 "D:\\Do-an-tot-nghiep\\Arduino\\Sensor\\sensor\\sensor.ino"
void setup() {
  pinMode(sensor, INPUT);
  Serial.begin(9600);
}

void loop() {
  int x = digitalRead(sensor);
  Serial.println(x);
  delay(100);
}

