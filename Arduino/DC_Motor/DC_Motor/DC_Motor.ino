#define in1 8
#define in2 9
#define enA 7

#define MAX_SPEED 255 //từ 0-255
#define MIN_SPEED 0
int i = 0;
void setup()
{
  Serial.begin(9600);
  pinMode(enA, OUTPUT);
  pinMode(in1, OUTPUT);
  pinMode(in2, OUTPUT);
}

void chaymotor()
{
//    for(i=0;i<=255;i++){
  Serial.println(i);
  if (i == 0){
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW);
    analogWrite(enA, 255); 
    delay(100);
    }
  else{
    analogWrite(enA, 0);
    digitalWrite(in1, HIGH);
    digitalWrite(in2, LOW); 
    }
  i += 1;        
} 
 
void loop() 
{
    chaymotor();
    delay(1000);
}
