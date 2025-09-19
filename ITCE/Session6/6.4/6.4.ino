int LEDs[4] = {4,5,6,7};
int LEDcount = 4;
int state = 0;
void setup() {
  // put your setup code here, to run once:
  for(int i=0;i<LEDcount;i++) {
    pinMode(LEDs[i],OUTPUT);
  }
  pinMode(13,INPUT_PULLUP);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(13)==0){
    state = !state;
  }
  if(state==1){
    for(int i=LEDcount;i>=0;i--) {
      digitalWrite(LEDs[i],1);
      delay(500);
      digitalWrite(LEDs[i],0);
    }
  }
  else if(state==0){
    for(int i=0;i<LEDcount;i++) {
      digitalWrite(LEDs[i],1);
      delay(500);
      digitalWrite(LEDs[i],0);
    }
  }
}