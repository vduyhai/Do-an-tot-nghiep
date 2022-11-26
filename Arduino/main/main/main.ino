int Relay1 = 2;
int Relay2 = 3;
int SS1 = 4;
int SS2 = 5;
int LEDR = 6;
int LEDG = 7;
int EN2 = 8;
int DIR2 = 9;
int PUL2 = 10;
int EN2 = 11;
int DIR2 = 12;
int PUL2 = 13;

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

  digitalWrite(EN2,HIGH);
  digitalWrite(LEDR, HIGH); 
  digitalWrite(LEDG, LOW); 

  digitalWrite(Relay1, LOW);
  digitalWrite(Relay2, LOW);
}

void Pour(String a){
  if (a == "coffee"){
    digitalWrite(Relay1, HIGH);
    delay(3000);
    digitalWrite(Relay1, LOW);
  }

  if (a == "tea"){
    digitalWrite(Relay2, HIGH);
    delay(3000);
    digitalWrite(Relay2, LOW);
  }  
}

void loop() {
  if (Serial.available()){
    String order = Serial.readString();

    int index = order.indexOf("_");
    int length = order.length;
    
    // Read type of cup
    if (cup == "plastic"){
      
      // Run Step1
//      digitalWrite(DIR1,HIGH); // Enables the motor to move in a particular direction
//      for(int x = 0; x < 200; x++) {
//        digitalWrite(PUL1,LOW); 
//        delayMicroseconds(500); 
//        digitalWrite(PUL1,HIGH); 
//        delayMicroseconds(500); 
//      }
      // Read ss1
      int x = digitalRead(sensor1);
      if (x == 0){
        Serial.println("SS1 have cup");
        
        // Run Step2
        digitalWrite(DIR2,HIGH); 
        for(int x = 0; x < 200; x++) {
          digitalWrite(PUL2,LOW); 
          delayMicroseconds(500); 
          digitalWrite(PUL2,HIGH); 
          delayMicroseconds(500); 
        }
        
        // Read ss2
        int y = digitalRead(sensor2);
        if (y == 0){
          Serial.println("SS2 have cup");
          
          // Led Red blink 
          
          // Pour dirnk
          // Pour(drink);
        }
        else{
          Serial.println("SS2 no cup");  
        }
      }

      // Ready
      digitalWrite(LEDG, HIGH); 
      digitalWrite(LEDL, LOW); 
      else{
        Serial.println("SS1 no cup");  
      }
    }
    if (cup == "personal"){

      // Den do nhap nhay

      // Read SS2
      int y = digitalRead(sensor2);
      if (y == 0){
        Serial.println("SS2 have cup");

        // Led Red blink
        
        // Pour drink
        // Pour(drink);
      
      }
      else{
        Serial.println("SS2 no cup");

      }
    }
  }
}
