const int DIR = 9;
const int STP = 8;
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
   delay(1000);
   digitalWrite(STP, LOW);
   delay(1000);
   }
}
