const int sensor = 5*;

void setup() {
  pinMode(sensor, INPUT);
  Serial.begin(9600);
}

void loop() {
  int x = digitalRead(sensor);
  Serial.println(x);
  delay(100);
}
