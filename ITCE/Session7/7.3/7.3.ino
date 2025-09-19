void setup() {
  // put your setup code here, to run once:
  pinMode(A1,INPUT);
  pinMode(10,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  
  int Level=map(VR,0,1023,0,255);
  Serial.println(VR);
  Serial.println(Level);
  analogWrite(10,Level);
}
