#include<SoftwareSerial.h>
SoftwareSerial aGSM(9,10); //connect TX of GSM moduleto pin 9,connect RX of GSM to 10 pin of arduino
const int locker=4;
const int buzzer=8;
const int irsensor=7;
const int trigPin = 5;
const int echoPin = 6;
long duration;
int distance;
int doorstat;
String msg;


void setup() 
{
pinMode(trigPin , OUTPUT);
pinMode(echoPin , INPUT);

Serial.begin(9600);
aGSM.begin(9600);
delay(100);
pinMode(buzzer,OUTPUT);
pinMode(irsensor,INPUT);
pinMode(locker,OUTPUT);

}

void loop() 
{
  /*
   * Detect collision and Send SMS 
   */
  digitalWrite(trigPin, LOW);
  delayMicroseconds(10);
  digitalWrite(trigPin, LOW);
  duration = pulseIn(echoPin, HIGH);
  distance= duration*0.034/2;
  //Serial.println(distance);

   if(distance<5)
   {
    SendMessage();//Message 
    aGSM.println("ATD8281303005;");
   }
 /*
  * if anyone access the door send message to owner and wait forthe incoming message.
  * if the incoming message is "lock",do lock the car . 
  * and raise the alarm.
  */
doorstat=digitalRead(irsensor);
if (doorstat==HIGH)
{
  SendMessage2();
  aGSM.println("ATD9846600013;");
  RecieveMessage();
msg=aGSM.read();
if(msg=="LOCK");
{
  digitalWrite(locker,HIGH); //Relay cut 
  alarm();
  
}
  
  
}
}
void SendMessage()//message when accident occures
{
  aGSM.print("AT+CMGF=1");
  delay(1000);
  aGSM.print("AT+CMGS=\"+919846600013\"\r");
  aGSM.println("Accident alert ");delay(100);
  aGSM.println((char)26);delay(1000);
}

void SendMessage2()//lock
{
  aGSM.println("AT+CMGF=1");
  delay(1000);
  aGSM.println("AT+CMGS=\"+919846600013\"\r");
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
  aGSM.println("AT+CNMI=2,2,0,0,0"); delay(1000);
 }

