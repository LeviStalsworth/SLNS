//This code displays the light intensity on a LCD 16*2 screen

/* 
 * ON PUBLIC DOMAIN
 * Author         : Nitish Dash
 * Name           : LDR Light Level Display on 16X2 LCD
 * Created        : 12/27/2014
 * Webpage        : http://goo.gl/Er9y4l
 * Author Email   : nitishdash95@gmail.com
 * Author Website : http://www.nitishdash.com/
 **** DONOT COPY AND PLAGIARATE WITHOUT THE AUTHOR'S PERMISSIONS ****
 */
  
#include <LiquidCrystal.h>
LiquidCrystal lcd(12, 11, 5, 4, 3, 2);
const int level_pin = 0;

void setup() { //initialise for at least 2s
  lcd.begin(16, 2);
  lcd.print("INITIALISING");
  delay(500);
  lcd.print(".");
  delay(500);
  lcd.print(".");  
  delay(500);
  lcd.print(".");
  delay(500);
  lcd.print("."); 
  Serial.begin(9600); // Serial monitor begins to read in data 
  delay(500);
}
void loop()
{
 int sensorValue = analogRead(A0);
 double dV = sensorValue;
 double le = (dV/1023)*100;
 int level = le;
 
 lcd.clear();
 lcd.setCursor(0, 0);
 lcd.print("LIGHT LEVEL:");
 lcd.print(level);
 lcd.print("%");
 lcd.setCursor(0, 1);
  
 if ((level >= 0) && (level <= 5))
 {
  lcd.print("VERY DARK"); 
 }
 else if ((level > 5) && (level <= 10))
 {
  lcd.print("DARK"); 
 }
 else if ((level > 10) && (level <= 50))
 {
  lcd.print("BRIGHT"); 
 }
 else
 {
  lcd.print("VERY BRIGHT"); 
 }

Serial.println(analogRead(level_pin)); // Printed data to the Serial Monitor
  
 delay(500); 
}
//</liquidcrystal.h>
