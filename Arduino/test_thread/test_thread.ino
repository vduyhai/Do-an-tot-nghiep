
int Relay1 = 4;
int Relay2 = 5;
int LEDR = 6;

void Blink(){
  digitalWrite(LEDR, HIGH); 
  delay(1000);               // dừng chương trình trong 1 giây => thây đèn sáng được 1 giây
  digitalWrite(LEDR, LOW);
  delay(1000); 
}

void Pour(){  
  digitalWrite(Relay1, HIGH);
  digitalWrite(LEDR, HIGH);
  delay(1000); 
  digitalWrite(LEDR, LOW);
  delay(1000); 
  digitalWrite(LEDR, HIGH); 

  delay(1000);
  digitalWrite(Relay1, LOW);
}
void setup() {
  pinMode(Relay1, OUTPUT);
  digitalWrite(LEDR, HIGH); 
}


void loop() {
  
  Pour();

}
