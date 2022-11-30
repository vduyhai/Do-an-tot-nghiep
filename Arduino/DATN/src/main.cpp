#include <Arduino.h>
int PUL2 = 13; 
int DIR2 = 12; 
int EN2 = 11;

void setup() {
  Serial.begin(9600);

  pinMode(PUL2,OUTPUT); 
  pinMode(DIR2,OUTPUT);
  pinMode(EN2,OUTPUT);
  digitalWrite(EN2,HIGH);
}

void loop() {
  if (Serial.available()){
    String order = Serial.readString();
    if (order == "tea"){
      digitalWrite(DIR2,HIGH); // Enables the motor to move in a particular direction
      for(int x = 0; x < 200; x++) {
        digitalWrite(PUL2,LOW); 
        delayMicroseconds(500); 
        digitalWrite(PUL2,HIGH); 
        delayMicroseconds(500); 
      }
    }
  }
}
