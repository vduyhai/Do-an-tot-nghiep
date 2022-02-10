#include <cvzone.h>
#define sensor 2
SerialData serialData;

int sendVals[2];

void setup() 
{
  pinMode(sensor, INPUT);
  Serial.begin(9600);

}

void loop() {
  int Sensor = digitalRead(sensor);
  sendVals[0] = Sensor;
  if (digitalRead(sensor)==1)
  {
    serialData.Send(sendVals);
    Serial.println("phat hien vat can");
    
    }
  else 
  {
    serialData.Send(sendVals);
    Serial.println("khong co vat can");
    }   
}
