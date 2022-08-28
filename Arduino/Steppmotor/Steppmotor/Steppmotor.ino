const int DIR = 4;
const int STP = 5;
const int EN = 6;
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
    digitalWrite(EN, LOW);
    digitalWrite(STP, HIGH);
    Serial.println("OK");
    delayMicroseconds(100);
    digitalWrite(STP, LOW);
    delayMicroseconds(100);
   }
}
