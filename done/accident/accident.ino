
#include<Servo.h>
Servo myservo;



const int breaker=6;
const int buzzer=7;
const int trigPin = 12;
const int echoPin = 13;
long duration;
int distance=0;
String msg;


void setup() 
{
  myservo.attach(breaker);
  myservo.write(0);delay(2000);
pinMode(trigPin , OUTPUT);
pinMode(echoPin , INPUT);

Serial.begin(9600);

delay(1000);
pinMode(buzzer,OUTPUT);
digitalWrite(buzzer,HIGH);delay(300);
digitalWrite(buzzer,LOW);


}

void loop() 
{
  

  digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin,LOW);
  duration = pulseIn(echoPin, HIGH);
  distance= duration*0.034/2;
  
   if(distance<5)
   { 
    //Serial.println("less thsnz5");
    digitalWrite(trigPin, LOW);
  delayMicroseconds(2);
  digitalWrite(trigPin, HIGH);
  delayMicroseconds(10);
  digitalWrite(trigPin,LOW);
  duration = pulseIn(echoPin, HIGH);
  distance= duration*0.034/2;
  if(distance<5)
  {
    myservo.write(90);
    delay(2500);
    

/////////////////////
  Serial.println("AT+CMGF=1");
  delay(1000);
  Serial.println("AT+CMGS=\"+918113969354\"\r");delay(1000);
  Serial.println("Accident alert ");delay(1000);
  Serial.println((char)26);delay(1000);
/////////////////////
    alarm();
 
   myservo.write(0);delay(2500);
   }
   }


  //Serial.println(distance);
   else if (distance<100)
   {
    
    digitalWrite(buzzer,HIGH);
    myservo.write(90);
   delay(1000);
  digitalWrite(buzzer,LOW);
   delay(2000);
   myservo.write(0);
   delay(2500);
   }
   
}

/*void SendMessage()//message when accident occures
{
  Serial.println("AT+CMGF=1");
  delay(1000);
  Serial.println("AT+CMGS=\"+918907089522\"\r");delay(1000);
  Serial.println("Accident alert ");delay(1000);
  Serial.println((char)26);delay(1000);
}

*/

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


