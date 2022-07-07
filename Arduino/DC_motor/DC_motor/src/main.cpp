#include <Arduino.h>
#define EnA 6
#define IN1 7
#define IN2 8

void setup() {
  pinMode(EnA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
}

void loop() {
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(EnA, 255);
  delay(1000);
}