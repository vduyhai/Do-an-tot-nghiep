int LEDR = 6;
int LEDG = 7;

 
// Hàm setup chạy một lần duy nhất khi khởi động chương trình
void setup() {                
  // đặt 'led' là OUTPUT
  pinMode(LEDG, OUTPUT); 
  pinMode(LEDR, OUTPUT);    
   
}
 
// Hàm loop chạy mãi mãi sau khi kết thúc hàm setup()
void loop() {
  digitalWrite(LEDG, HIGH);   // bật đèn led sáng
  digitalWrite(LEDR, HIGH); 
  delay(1000);               // dừng chương trình trong 1 giây => thây đèn sáng được 1 giây
  digitalWrite(LEDG, LOW);    // tắt đèn led
  digitalWrite(LEDR, LOW);
  delay(1000);               // dừng chương trình trong 1 giây => thấy đèn tối được 1 giây
}
