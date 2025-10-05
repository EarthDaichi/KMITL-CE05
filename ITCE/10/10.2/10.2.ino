#include <IRremote.hpp>
#include <LiquidCrystal_I2C.h>
LiquidCrystal_I2C lcd(0x27,16,2);
#define IR_REMOTE_PIN 4

unsigned long Level;

//trig:A0
//echo:A2
long duration;
int distance;

int LCD1(int SetLevel){
  lcd.setCursor(8,0);
  lcd.print(SetLevel);
  lcd.print("  ");
}

int Check(int level, int distance){
  if(distance <= level/4){delay(250);digitalWrite(3,1);delay(250);digitalWrite(3,0);}
  else if(distance <= level/2){delay(500);digitalWrite(3,1);delay(250);digitalWrite(3,0);}
  else if(distance <= (level*3)/4){delay(750);digitalWrite(3,1);delay(250);digitalWrite(3,0);}
  else if(distance <= level){delay(1000);digitalWrite(3,1);delay(250);digitalWrite(3,0);}
  else if(distance > level){digitalWrite(3,1);}
}

void setup(){
  pinMode(A0,OUTPUT);
  pinMode(A2,INPUT);
  pinMode(3,OUTPUT);
  IrReceiver.begin(IR_REMOTE_PIN,ENABLE_LED_FEEDBACK);
  Serial.begin(9600);
  lcd.init();
  lcd.backlight();
}

void loop(){
  lcd.setCursor(0,0);
  lcd.print("Level = ");
  if(IrReceiver.decode()){
    Serial.print(IrReceiver.decodedIRData.decodedRawData, HEX);
    IrReceiver.printIRResultShort(&Serial);
    IrReceiver.printIRSendUsage(&Serial);
    Level = IrReceiver.decodedIRData.decodedRawData;
    IrReceiver.resume();
  }

  digitalWrite(A0, LOW);
  delayMicroseconds(2);
  digitalWrite(A0, HIGH);
  delayMicroseconds(10);
  digitalWrite(A0, LOW);

  duration = pulseIn(A2,1,30000);
  distance = duration * 0.034 / 2;
  int timer;
  if(millis() >= timer){
    timer = millis()+300;
    lcd.setCursor(0,1);
    lcd.print("Distance = ");
    lcd.print(distance);
    lcd.print("   ");}

  switch(Level){
    case 0xBA45FF00:LCD1(10);Check(10,distance); break;
    case 0xB946FF00:LCD1(20);Check(20,distance); break;
    case 0xB847FF00:LCD1(30);Check(30,distance); break;
    case 0xBB44FF00:LCD1(40);Check(40,distance); break;
    case 0xBF40FF00:LCD1(50);Check(50,distance); break;
    case 0xBC43FF00:LCD1(60);Check(60,distance); break;
    case 0xF807FF00:LCD1(70);Check(70,distance); break;
    case 0xEA15FF00:LCD1(80);Check(80,distance); break;
    case 0xF609FF00:LCD1(90);Check(90,distance); break;
    case 0xE619FF00:LCD1(100);Check(100,distance); break;
    case 0xE31CFF00:LCD1(-1);Check(0,distance); break;
    default:LCD1(-1);
  }
}