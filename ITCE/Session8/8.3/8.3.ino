void rotate(){
  for(int j=0;j<121;j++){
    for(int i=8;i<12;i++){
      digitalWrite(i,1);
      delay(3);
      digitalWrite(i,0);
    }
  }
}

void setup() {
  // put your setup code here, to run once:
  pinMode(7,INPUT);
  for(int i=8;i<12;i++){
    pinMode(i,OUTPUT);
    digitalWrite(i,0);
    }
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(7)){
    rotate();
  }
}
