int Relay1 = 4;
int Relay2 = 5;
int SS1 = 2;
int SS2 = 3;
int LEDR = 6;
int LEDG = 7;
int EN2 = A5;
int DIR2 = A4;
int PUL2 = A3;
int EN1 = A2;
int DIR1 = A1;
int PUL1 = A0;

void setup() {
  Serial.begin(9600);

  pinMode(PUL1,OUTPUT); 
  pinMode(DIR1,OUTPUT);
  pinMode(EN1,OUTPUT);
  
  pinMode(PUL2,OUTPUT); 
  pinMode(DIR2,OUTPUT);
  pinMode(EN2,OUTPUT);
  
  pinMode(SS1, INPUT);
  pinMode(SS2, INPUT);
  pinMode(Relay1, OUTPUT);
  pinMode(Relay2, OUTPUT);

  digitalWrite(EN1,LOW);
  digitalWrite(EN2,LOW);
  
  digitalWrite(LEDR, HIGH); 
  digitalWrite(LEDG, LOW); 

  digitalWrite(Relay1, LOW);
  digitalWrite(Relay2, LOW);
}

void Pour(String a){
  Serial.println(a);

  if (a == "coffee"){
    digitalWrite(Relay1, HIGH);
    delay(3000);
    digitalWrite(Relay1, LOW);
    delay(1000);
  }

  if (a == "tea"){
    Serial.println("x");

    digitalWrite(Relay2, HIGH);
    delay(3000);
    digitalWrite(Relay2, LOW);
    delay(1000);
  }  
}


void Blink(){
  digitalWrite(LEDR, HIGH); 
  delay(1000);               // dừng chương trình trong 1 giây => thây đèn sáng được 1 giây
  digitalWrite(LEDR, LOW);
  delay(1000); 
}
void loop() {
  if (Serial.available()){

    String order = Serial.readString();
    int index = order.lastIndexOf("_");
    int len = order.length();
    String cup = order.substring(0,index);
    String drink = order.substring(index+1,len);
    Serial.println(cup);
    Serial.println(drink);
    
    // Read type of cup
    if (cup == "plastic"){
      
      // Run Step1
      digitalWrite(DIR1,HIGH); // Enables the motor to move in a particular direction
      for (int a = 0; a < 1; a ++){
        for(int x = 0; x < 200; x++) {
          digitalWrite(PUL1,LOW); 
          delayMicroseconds(500); 
          digitalWrite(PUL1,HIGH); 
          delayMicroseconds(500); 
        }
      }
      
      // Read ss1
      while (1){
        int x = digitalRead(SS1);
        if (x == 0){
          Serial.println("SS1 have cup");
          break;
        }
        else {
          Serial.println("SS1 no cup");
        }
      }

        // Run Step2
      digitalWrite(DIR2,HIGH); 
      for(int b = 0; b < 10; b++) {
        for(int x = 0; x < 200; x++) {
        digitalWrite(PUL2,LOW); 
        delayMicroseconds(500); 
        digitalWrite(PUL2,HIGH); 
        delayMicroseconds(500); 
        }
      }
      
//        
        // Read ss2
      while (1){
        int y = digitalRead(SS2);
        if (y == 0){
          Serial.println("SS2 have cup");
          break;
        }
        else {
          Serial.println("SS2 don no cup");
        }
      }
//          
//      // Led Red blink 
////      Blink();
//
//          
//      // Pour dirnk
      Pour(drink);
//      }
//      
//    if (cup == "personal"){
//
//      // Den do nhap nhay
//
//      // Read SS2
//      int y = digitalRead(sensor2);
//      if (y == 0){
//        Serial.println("SS2 have cup");
//
//        // Led Red blink
//        
//        // Pour drink
//        // Pour(drink);
//      
//      }
//      else{
//        Serial.println("SS2 no cup");
//
//      }
    }
  }
}
