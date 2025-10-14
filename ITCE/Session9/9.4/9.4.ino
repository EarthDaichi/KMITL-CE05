#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);

void setup() {
  // put your setup code here, to run once:
  pinMode(A1,INPUT);
  pinMode(A3,INPUT);
  pinMode(A4,OUTPUT);
  pinMode(A5,OUTPUT);
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
}

void loop() {
  // put your main code here, to run repeatedly:
  float VR = analogRead(A1);
  int LDR = analogRead(A3);
  Serial.println(LDR);
  lcd.setCursor(0,0);
  lcd.print(VR/100);
  lcd.setCursor(0,1);
  lcd.print(LDR);
  delay(200);
  lcd.clear();
}
