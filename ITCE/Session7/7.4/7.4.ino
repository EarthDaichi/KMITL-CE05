void setup() {
  // put your setup code here, to run once:
  pinMode(A1,INPUT);
  pinMode(8,OUTPUT);
  pinMode(9,OUTPUT);
  pinMode(10,OUTPUT);
  pinMode(11,OUTPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int LDR=analogRead(A1);
  int LED=map(LDR,0,989,0,4);
  Serial.println(LDR);
  Serial.println(LED);
  switch(LED){
    case 0:
    digitalWrite(8,0);
    digitalWrite(9,0);
    digitalWrite(10,0);
    digitalWrite(11,0);
      break;
    case 1:
    digitalWrite(8,1);
    digitalWrite(9,0);
    digitalWrite(10,0);
    digitalWrite(11,0);
      break;
    case 2:
    digitalWrite(8,1);
    digitalWrite(9,1);
    digitalWrite(10,0);
    digitalWrite(11,0);
      break;
    case 3:
    digitalWrite(8,1);
    digitalWrite(9,1);
    digitalWrite(10,1);
    digitalWrite(11,0);
      break;
    case 4:
    digitalWrite(8,1);
    digitalWrite(9,1);
    digitalWrite(10,1);
    digitalWrite(11,1);
      break;
  }
}
