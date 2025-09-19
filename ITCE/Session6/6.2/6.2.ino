void setup() {
  // put your setup code here, to run once:
  pinMode(7,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(4,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i=4;i<8;i++){
    digitalWrite(i,1);
    delay(500);
    digitalWrite(i,0);
  }
}