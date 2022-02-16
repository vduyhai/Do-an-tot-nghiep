#include <cvzone.h>
#define sensor 2
#define led 13
SerialData serialData;

int sendVals[2];

void setup() 
{
  pinMode(sensor, INPUT);
  pinMode(led, OUTPUT);
  Serial.begin(9600);

}

void loop() {
  int Val = digitalRead(sensor);
  Serial.println(Val);
}
