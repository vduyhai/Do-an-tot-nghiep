const int DIR = 6;
const int STP = 7;
const int stepsPerRevolution = 200;
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
   delayMicroseconds(100);
   digitalWrite(STP, LOW);
   delayMicroseconds(100);
   }
}
