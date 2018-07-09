int butt=15;
const int temp=A4;
const int buzzer=9;
const int motor=6;

float tempC;
int tempdata;
void setup()
{
pinMode(A4,INPUT);  
pinMode(buzzer,OUTPUT);
pinMode(motor,OUTPUT);
digitalWrite(motor,LOW);
Serial.begin(9600);
digitalWrite(buzzer,HIGH);
delay(1000);
digitalWrite(buzzer,LOW);
}
void(*resetFunc)(void)=0;
void loop()
{
  tempdata=analogRead(temp);
  //Serial.println(tempdata);
  //delay(1000);
  tempC=tempdata*.488;
  Serial.println(tempC);
  if(tempC>45)
  {delay(500);
  if(tempC>45)
   {
    digitalWrite(buzzer,HIGH);
    delay(1000);
    digitalWrite(buzzer,LOW);
    butt=digitalRead(15);
    
    if(butt==LOW)
    {
      resetFunc();
      }
    Serial.println("AT+CMGF=1");//Sets the GSM Module in Text Mode
  delay(1000);//Delay of 1000 milli seconds or 1 second
  Serial.println("AT+CMGS=\"+919744187435\"\r");//Replace x with mobile number 
  delay(1000);
  Serial.println("Fire Emergency,KR market,5th avenu delhi ");//the SMS text you want to send
  Serial.println(tempC);
  delay(1000);
  Serial.println((char)26);//ASCII code of CTRL+Z
  delay(1000);
    
    digitalWrite(motor,HIGH);
    delay(1000);
   ton();
    
   }
}
 
}
  void SendMessage()
{
  
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

    
    digitalWrite(buzzer,HIGH);
    delay(1000);
    digitalWrite(buzzer,LOW);
    delay(1000);
  }


