void setup() {
  // put your setup code here, to run once:
  pinMode(A1,INPUT);
  pinMode(3,OUTPUT);
  pinMode(4,OUTPUT);
  pinMode(5,OUTPUT);
  pinMode(6,OUTPUT);
  pinMode(7,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  for(int i=3;i<8;i++){
    digitalWrite(i,0);
  }
  int VR=analogRead(A1);
  Serial.println(VR);
  VR=map(VR,0,1000,1,5);
  if(VR==1){
    digitalWrite(3,1);
  }
  else if(VR==2){
    digitalWrite(4,1);
  }
  else if(VR==3){
    digitalWrite(5,1);
  }
  else if(VR==4){
    digitalWrite(6,1);
  }
  else if(VR==5){
    digitalWrite(7,1);
  }
}
