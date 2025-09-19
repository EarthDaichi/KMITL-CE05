int state = 0;
void setup() {
  // put your setup code here, to run once:
  pinMode(9,INPUT);
  pinMode(10,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(digitalRead(9)){
    state = !state;
  }
  digitalWrite(10,state);
  delay(200);
}
