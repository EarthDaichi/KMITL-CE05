#include <Adafruit_GFX.h>
#include <Adafruit_LEDBackpack.h>
Adafruit_7segment matrix = Adafruit_7segment();

void setup() {
  // put your setup code here, to run once:
  pinMode(A1,INPUT);
  pinMode(A3,INPUT);
  Serial.begin(9600);
  matrix.begin(0x70);
}

void loop() {
  // put your main code here, to run repeatedly:
  int VR = analogRead(A1);
  int mVR = VR/100;
  int LDR = analogRead(A3)/10;
  int mLDR = map(LDR,0,67,0,99);
  Serial.println(LDR);
  matrix.writeDigitNum(0,mVR/10,1);
  matrix.writeDigitNum(1,mVR%10,0);
  matrix.writeDigitNum(3,mLDR/10,0);
  matrix.writeDigitNum(4,mLDR%10,0);
  matrix.drawColon(1);
  matrix.writeDisplay();
}
