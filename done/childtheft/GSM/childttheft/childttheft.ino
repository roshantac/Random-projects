#include<Universal_GPS.h>
//athulbalan02@gmail.com
GPS_Init(10,11);


String textMessage;
const int buzzer = 9;//buzzer connected to 

void setup() {
  
  pinMode(buzzer, OUTPUT);// Set buzzer as OUTPUT
  pinMode(6, OUTPUT);
  digitalWrite(6, HIGH);
   digitalWrite(buzzer, HIGH);delay(300);
     digitalWrite(buzzer, LOW);
  Serial.begin(9600);
  delay(2000);
  Serial.println("AT+CMGF=1\r");   // AT command to set Serial to SMS mode
  delay(100);
  Serial.println("AT+CNMI=2,2,0,0,0\r");// Set module to send SMS data to serial out upon receipt 
  delay(100);
}

void loop(){
  if(Serial.available()>0)
  {
    textMessage = Serial.readString();
       
    delay(100);
  } 
  if(textMessage.indexOf("BUZON")>=0)
  {
    
    digitalWrite(buzzer, HIGH);digitalWrite(6, HIGH);
   
    textMessage = "";   
  }
  if(textMessage.indexOf("BUZOFF")>=0){
    
    // Turn off buzzer and save current state
    digitalWrite(buzzer, LOW);digitalWrite(6, LOW);
    textMessage="";
    
   
  }
  if(textMessage.indexOf("STAT")>=0)
  {
    
    sendSMS();

 
  }
}  

// Function that sends SMS
void sendSMS()
{
  // AT command to set Serial to SMS mode
  Serial.println("AT+CMGF=1"); 
  delay(1000);
  Serial.println("AT+CMGS=\"+917909190966\"\r");
  delay(1000);
  String s=GetGPS();
  Serial.println(s); 
  delay(100);
  Serial.println((char)26); 
 
  delay(1000);  
   Serial.println("AT+CNMI=2,2,0,0,0\r");
  delay(100);
}
