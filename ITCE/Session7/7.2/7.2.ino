void setup() {
  // put your setup code here, to run once:
  pinMode(A1,INPUT);
  pinMode(13,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  digitalWrite(13,0);
  delay(300);
  int VR=analogRead(A1);
  VR=map(VR,0,1000,1,4);
  Serial.println(VR);
  digitalWrite(13,1);
  if(VR==1){
    delay(500);
  }
  else if(VR==2){
    delay(1000);
  }
  else if(VR==3){
    delay(1500);
  }
  else if(VR==4){
    delay(2000);
  }
}
