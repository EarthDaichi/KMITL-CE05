int interrupting = 0;

void setup() {
  // put your setup code here, to run once:
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(2,INPUT_PULLUP);
  attachInterrupt(0,INTR,RISING);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(interrupting==0){
  	digitalWrite(8,1);
    delay(1000);
    digitalWrite(8,0);
    delay(500);
  }
  else if(interrupting==1){
    for(int i=0;i<5;i++){
      digitalWrite(9,1);
      delay(2000);
      digitalWrite(9,0);
      delay(2000);
    }
    interrupting=0;
  }
}

void INTR(){
  interrupting=1;
}