  int LEDs[4] = {4,5,6,7};
  int LEDcount = 4;

void setup() {
  // put your setup code here, to run once:
  for(int i=0;i<LEDcount;i++) {
    pinMode(LEDs[i],OUTPUT);
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i=0;i<LEDcount;i++) {
    digitalWrite(LEDs[i],1);
    delay(500);
    digitalWrite(LEDs[i],0);
  }
}
