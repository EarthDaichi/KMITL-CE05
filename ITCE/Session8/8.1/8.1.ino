int state = 0;

void setup()
{
 pinMode(10,OUTPUT);
 pinMode(2,INPUT);
}

void loop()
{
  if(digitalRead(2)){
    state = !state;
  }
  if(state)
  {
  	analogWrite(10,255);
  }
  else{
    analogWrite(10,0);
  }
}