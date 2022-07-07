int EnA = 8;
int IN1 = 7;
int IN2 = 6;

void setup() {
  pinMode(EnA, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
}
void run(){
  digitalWrite(IN1, HIGH);
  digitalWrite(IN2, LOW);
  analogWrite(EnA, 255);
  delay(100);
}
void loop() {
  run();
  delay(1000);
}
