int state = 0;

void setup(){
 pinMode(10,OUTPUT);
 pinMode(9,INPUT);
 pinMode(8,INPUT);
 pinMode(7,INPUT);
}

void loop(){
  if(digitalRead(9)){
  	state=0;
  }
  if(digitalRead(8)){
  	state=1;
  }
  if(digitalRead(7)){
  	state=2;
  }
  if(state ==0){
    analogWrite(10,0);
  }
  else if(state ==1){
  	analogWrite(10,125);
  }
  else if(state ==2){
  	analogWrite(10,255);
  }
    
}