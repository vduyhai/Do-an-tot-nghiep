int sensor1 = 2;
int sensor2 = 3;

void setup() {
  pinMode(sensor1, INPUT);
  pinMode(sensor2, INPUT);
  Serial.begin(9600);
}

void loop() {
  int x = digitalRead(sensor2);
  Serial.println(x);
//  int y = digitalRead(sensor2);
//  Serial.println("ss2", y);
  delay(1000);
}
