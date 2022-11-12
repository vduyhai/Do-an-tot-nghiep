int led1 = 6;
int led2 = 7;

 
// Hàm setup chạy một lần duy nhất khi khởi động chương trình
void setup() {                
  // đặt 'led' là OUTPUT
  pinMode(led1, OUTPUT); 
  pinMode(led2, OUTPUT);    
   
}
 
// Hàm loop chạy mãi mãi sau khi kết thúc hàm setup()
void loop() {
  digitalWrite(led1, HIGH);   // bật đèn led sáng
  digitalWrite(led2, HIGH); 
  delay(1000);               // dừng chương trình trong 1 giây => thây đèn sáng được 1 giây
  digitalWrite(led1, LOW);    // tắt đèn led
  digitalWrite(led2, LOW);
  delay(1000);               // dừng chương trình trong 1 giây => thấy đèn tối được 1 giây
}
