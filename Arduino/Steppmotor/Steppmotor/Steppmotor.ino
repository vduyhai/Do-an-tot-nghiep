const int stepPin = 13; 
const int dirPin = 12; 
const int enPin = 11;

void setup() {
  pinMode(stepPin,OUTPUT); 
  pinMode(dirPin,OUTPUT);
  pinMode(enPin,OUTPUT);
  digitalWrite(enPin,HIGH);
  
}

void loop() {
  
  digitalWrite(dirPin,HIGH); // Enables the motor to move in a particular direction
  for(int x = 0; x < 200; x++) {
    digitalWrite(stepPin,LOW); 
    delayMicroseconds(500); 
    digitalWrite(stepPin,HIGH); 
    delayMicroseconds(500); 
  }
}
