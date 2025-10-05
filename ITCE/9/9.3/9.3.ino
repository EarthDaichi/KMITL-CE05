#include <LiquidCrystal.h>
LiquidCrystal lcd(12,11,5,4,3,2);

void setup() {
  // put your setup code here, to run once:
  pinMode(A1,INPUT);
  pinMode(A3,INPUT);
  Serial.begin(9600);
  lcd.begin(16,2);
}

void loop() {
  // put your main code here, to run repeatedly:
  float VR = analogRead(A1);
  int LDR = analogRead(A3);
  Serial.println(LDR);
  lcd.setCursor(0,0);
  lcd.print("VR ");
  lcd.setCursor(4,0);
  lcd.print(VR/100);
  lcd.setCursor(0,1);
  lcd.print("LDR ");
  lcd.setCursor(4,1);
  lcd.print(LDR);
  if(VR<1000){
  	lcd.setCursor(8,0);
  	lcd.print(" ");}
  if(LDR<100){
  	lcd.setCursor(6,1);
    lcd.print(" ");}
  if(LDR<10){
  	lcd.setCursor(5,1);
    lcd.print("  ");}
}
