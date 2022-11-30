int LEDR = 6;
int LEDG = 7;

 
// Hàm setup chạy một lần duy nhất khi khởi động chương trình
void setup() {                
  // đặt 'led' là OUTPUT
  pinMode(LEDG, OUTPUT); 
  pinMode(LEDR, OUTPUT);    
  Serial.begin(9600);
   
}
 
// Hàm loop chạy mãi mãi sau khi kết thúc hàm setup()
void loop() {
  if (Serial.available()){
    String order = Serial.readString();
    int index = order.lastIndexOf("_");
    int len = order.length();
    String cup = order.substring(0,index);
    String drink = order.substring(index+1,len);
    Serial.println(cup);
    Serial.println(drink);

    
  }
}
