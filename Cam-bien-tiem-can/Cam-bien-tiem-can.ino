#define sensor 2

void setup() 
{
  pinMode(sensor, INPUT);
  Serial.begin(9600);

}

void loop() {
  if (digitalRead(sensor)==1)
  {
    Serial.println("phat hien vat can");
    
    }
  else 
  {
    Serial.println("khong co vat can");
    }   
}
