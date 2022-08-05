# 1 "D:\\Do-an-tot-nghiep\\Arduino\\Sensor\\sensor\\sensor.ino"
const int sensor = 5;

void setup() {
  pinMode(sensor, 0x0);
  Serial.begin(9600);
}

void loop() {
  int x = digitalRead(sensor);
  Serial.println(x);
  delay(100);
}
