
#include<Universal_GPS.h>
GPS_Init(10,11);
 int butt;
const int but=15;
const int buzzer=9;

void setup()
{
pinMode(butt,INPUT_PULLUP);  
pinMode(buzzer,OUTPUT);
gps.begin(4800);
pinMode(6,OUTPUT);digitalWrite(6,HIGH);
Serial.begin(9600);digitalWrite(buzzer,HIGH); delay(1000); 
digitalWrite(buzzer,LOW);
}

void loop()
{
  butt=digitalRead(but);
  if(butt==LOW)
  {
    digitalWrite(buzzer,HIGH);
    delay(1000);
    digitalWrite(buzzer,LOW);
   
    SendMessage();
    delay(1000);
   ton();
    
   }
}
 

  void SendMessage()
{
  Serial.println("AT+CMGF=1");//Sets the GSM Module in Text Mode
  delay(1000);//Delay of 1000 milli seconds or 1 second
  Serial.println("AT+CMGS=\"+917034403461\"\r");//Replace x with mobile number 
  delay(1000);
  Serial.println("Please help me");
  String data=GetGPS();
  Serial.println(data);//the SMS text you want to send
  delay(100);
  Serial.println((char)26);//ASCII code of CTRL+Z
  delay(1000);
  }
  void ton()
  { 
    digitalWrite(buzzer,HIGH);
    delay(1000);
    digitalWrite(buzzer,LOW);
    delay(1000);
    
    digitalWrite(buzzer,HIGH);
    delay(1000);
    digitalWrite(buzzer,LOW);
    delay(1000);
    
    digitalWrite(buzzer,HIGH);
    delay(1000);
    digitalWrite(buzzer,LOW);
    delay(1000);

    
  }


