#include<SoftwareSerial.h>
SoftwareSerial aGSM(9,10); //connect TX of GSM moduleto pin 9,connect RX of GSM to 10 pin of arduino
const int locker=2;
const int buzzer=8;
const int irsensor=7;
const int trigPin = 5;
const int echoPin = 6;
long duration;
int distance;
int doorstat;
String textMessage;

void setup() 
{
pinMode(trigPin , OUTPUT);
pinMode(echoPin , INPUT);


aGSM.begin(9600);
delay(1000);
pinMode(buzzer,OUTPUT);
pinMode(irsensor,INPUT_PULLUP);
pinMode(locker,OUTPUT);digitalWrite(locker,HIGH); delay(1000);digitalWrite(locker,LOW);
aGSM.println("AT+CMGD=1,4"); 
delay(1000);

}

void loop() 
{ 

  
  
  if(aGSM.available()>0)
  { aGSM.println("AT+CMGF=1");delay(1000);
    aGSM.println("AT+CMGR=1");delay(100);
    textMessage = aGSM.readString();
    delay(100);
    if(textMessage.indexOf("LOCK")>=0)
  {
    
    alarm();  alarm(); 
    digitalWrite(locker,HIGH); //Relay cut 
    delay(1000);
    alarm();
    textMessage = "";   
    aGSM.println("AT+CMGD=1,4"); 
    delay(1000);
  }
  } 
    
  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin,LOW);
  duration = pulseIn(echoPin, HIGH);
  distance= duration*0.034/2;
  if(distance<5)
   {
    alarm();
    alarm();
  
    SendMessage();//Message 
 
   }


  
doorstat=digitalRead(irsensor);
if (doorstat==LOW)
{
  alarm();
  SendMessage2();
}
           
}

void SendMessage()//message when accident occures
{
  aGSM.println("AT+CMGF=1");
  delay(1000);
  aGSM.println("AT+CMGS=\"+919846600013\"\r");delay(1000);
  aGSM.println("Accident alert ");delay(100);
  aGSM.println((char)26);delay(2000);
  aGSM.println("AT+CSQ");delay(1000);aGSM.println("AT+CREG?");delay(1000);
  aGSM.println("ATD9846600013;");delay(10000);aGSM.println("ATH");
}

void SendMessage2()//lock
{
  aGSM.println("AT+CMGF=1");
  delay(1000);
  aGSM.println("AT+CMGS=\"+919846600013\"\r");delay(1000);
  aGSM.println("Car Theft alert");delay(100);
  aGSM.println((char)26);delay(1000);
}

void alarm() //Alarm
{
  digitalWrite(buzzer,HIGH);delay(250);
  digitalWrite(buzzer,LOW);delay(250);
   digitalWrite(buzzer,HIGH);delay(250);
  digitalWrite(buzzer,LOW);delay(250);
   digitalWrite(buzzer,HIGH);delay(250);
  digitalWrite(buzzer,LOW);delay(250);
   digitalWrite(buzzer,HIGH);delay(250);
  digitalWrite(buzzer,LOW);delay(250);
   digitalWrite(buzzer,HIGH);delay(250);
  digitalWrite(buzzer,LOW);delay(250);
   digitalWrite(buzzer,HIGH);delay(250);
  digitalWrite(buzzer,LOW);delay(250);
     
}

 void  RecieveMessage()
 {
  
  aGSM.println("AT+CNMI=2,2,0,0,0\r");  
  delay(1000);
 }


