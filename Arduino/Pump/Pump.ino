int Relay1 = 2;
int Relay2 = 3;

void setup() {
  pinMode(Relay1, OUTPUT);
  pinMode(Relay2, OUTPUT);

  digitalWrite(Relay1, HIGH);
  digitalWrite(Relay2, HIGH);
}

void loop() {
  digitalWrite(Relay1, LOW);
  delay(3000);
  digitalWrite(Relay1, HIGH);
  delay(3000);
}
