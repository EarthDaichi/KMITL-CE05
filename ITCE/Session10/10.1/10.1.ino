#include <LiquidCrystal_I2C.h>
#include <DHT.h>

LiquidCrystal_I2C lcd(0x27,16,2); 
#define DHTPIN 8
#define DHTTYPE DHT11
DHT dht(DHTPIN,DHTTYPE);

void setup() {
  // put your setup code here, to run once:
  lcd.init();
  lcd.backlight();
  dht.begin();
  pinMode(8,INPUT);
  pinMode(6,OUTPUT);
  pinMode(12,OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  float humidity = dht.readHumidity();
  float celsius = dht.readTemperature();
  lcd.setCursor(0,0);
  lcd.print("Humidity : ");
  lcd.print(humidity);
  lcd.print(" %");

  lcd.setCursor(0,1);
  lcd.print("Temp : ");
  lcd.print (celsius);
  lcd.print(" *C");

  if(humidity >= 94){digitalWrite(12,0);}else{digitalWrite(12,1);}
  if(celsius >=26){digitalWrite(6,1);}else{digitalWrite(6,0);}

}
