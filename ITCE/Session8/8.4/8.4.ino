#include <Servo.h>
Servo myservo;

void setup() {
  // put your setup code here, to run once:
  myservo.attach(9);
  pinMode(A0,INPUT);
  pinMode(9,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int VR = analogRead(A0);
  int VRM = map(VR,0,1024,1,180);
  Serial.println(VR);
  Serial.println(VRM);
  myservo.write(VRM);
}
