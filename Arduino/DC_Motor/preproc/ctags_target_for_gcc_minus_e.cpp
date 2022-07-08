# 1 "D:\\Do-an-tot-nghiep\\Arduino\\Steppmotor\\Steppmotor\\Steppmotor.ino"
const int DIR = 9;
const int STP = 8;
const int stepsPerRevolution = 200;
void setup() {
  pinMode(DIR, 0x1);
  pinMode(STP, 0x1);
  Serial.begin(9600);
}

void loop() {
  digitalWrite(DIR, 0x1);

  for(int x = 0; x <stepsPerRevolution; x++)
  {
   digitalWrite(STP, 0x1);
   Serial.println("OK");
   delay(1000);
   digitalWrite(STP, 0x0);
   delay(1000);
   }
}
