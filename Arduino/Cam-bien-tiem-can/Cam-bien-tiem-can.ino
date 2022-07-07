#include <cvzone.h>
#define sensor 2
#define led 13
#define relay 7
int lvl;

void setup() 
{
  pinMode(sensor, INPUT);
  pinMode(relay,OUTPUT);
  pinMode(led, OUTPUT);
  Serial.begin(9600);
  digitalWrite(relay,LOW);

}

void loop() {
//  lvl = analogRead(sensor);
//  Serial.println(lvl);
//  delay(1000); 
  digitalWrite(relay,HIGH);
  delay(5000);
  digitalWrite(relay,LOW);
  delay(1000);
  
}
