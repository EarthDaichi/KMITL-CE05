int num[10][7] = {
 {1,1,1,1,1,1,0}, // 0
 {0,1,1,0,0,0,0}, // 1
 {1,1,0,1,1,0,1}, // 2
 {1,1,1,1,0,0,1}, // 3
 {0,1,1,0,0,1,1}, // 4
 {1,0,1,1,0,1,1}, // 5
 {1,0,1,1,1,1,1}, // 6
 {1,1,1,0,0,0,0}, // 7
 {1,1,1,1,1,1,1}, // 8
 {1,1,1,1,0,1,1}  // 9
};//abcdefg

void setup() {
  // put your setup code here, to run once:
  for(int i=2;i<9;i++){
    pinMode(i,OUTPUT);
  }
  pinMode(A1,INPUT);
  Serial.begin(9600);
}

void loop() {
  // put your main code here, to run repeatedly:
  int VR = analogRead(A1);
  int level = map(VR,120,950,0,9);
  Serial.println(VR);
  Serial.println(level);
  for(int i=2;i<9;i++){
   digitalWrite(i,num[level][i-2]);
  }
}
