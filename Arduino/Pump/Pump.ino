int Relay1 = 4;
int Relay2 = 5;

void setup() {
  pinMode(Relay1, OUTPUT);
  pinMode(Relay2, OUTPUT);

  digitalWrite(Relay1, LOW);
  digitalWrite(Relay2, LOW);
}

void loop() {
  digitalWrite(Relay1, HIGH);
  delay(3000);
  digitalWrite(Relay1, LOW);
  delay(1000);

//  digitalWrite(Relay2, HIGH);
//  delay(3000);
//  digitalWrite(Relay2, LOW);
//  delay(1000);
}
