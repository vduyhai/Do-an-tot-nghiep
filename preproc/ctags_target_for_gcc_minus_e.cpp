# 1 "D:\\Do-an-tot-nghiep\\Arduino\\DC_motor\\DC_motor\\src\\test\\test.ino"
int EnA = 8;
int IN1 = 7;
int IN2 = 6;

void setup() {
  pinMode(EnA, 0x1);
  pinMode(IN1, 0x1);
  pinMode(IN2, 0x1);
}
void run(){
  digitalWrite(IN1, 0x1);
  digitalWrite(IN2, 0x0);
  analogWrite(EnA, 255);
  delay(100);
}
void loop() {
  run();
  delay(1000);
}
