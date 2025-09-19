unsigned long t_A1;
unsigned long t_A0;

void setup() {
  // put your setup code here, to run once:
  pinMode(A0,INPUT); //VR
  pinMode(A4,INPUT); //LDR
  pinMode(5,OUTPUT); //r
  pinMode(6,OUTPUT); //r
  pinMode(7,OUTPUT); //r
  pinMode(8,OUTPUT); //g
  pinMode(9,OUTPUT); //g
  pinMode(10,OUTPUT); //g
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  if(millis()>=t_A0){
    t_A0 = 1000+millis();
    int A0=analogRead(A0); //VR
    int A0M=map(A0,0,1000,1,3);
    Serial.println(A0);
    Serial.println(A0M);
    switch(A0M){
      case 1:
      digitalWrite(5,1);
      digitalWrite(6,0);
      digitalWrite(7,0);
      break;
      case 2:
      digitalWrite(5,1);
      digitalWrite(6,1);
      digitalWrite(7,0);
      break;
      case 3:
      digitalWrite(5,1);
      digitalWrite(6,1);
      digitalWrite(7,1);
      break;
    }
  }
  if(millis()>=t_A1){
    t_A1 =1000+millis();
    int A1=analogRead(A4); //LDR
    int A1M=map(A1,0,989,0,4);
    Serial.println(A1);
    Serial.println(A1M);
    switch(A1M){
      case 1:
      digitalWrite(8,1);
      digitalWrite(9,0);
      digitalWrite(10,0);
      break;
      case 2:
      digitalWrite(8,1);
      digitalWrite(9,1);
      digitalWrite(10,0);
      break;
      case 3:
      digitalWrite(8,1);
      digitalWrite(9,1);
      digitalWrite(10,1);
      break;
    }
  }
}
