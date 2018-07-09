
const int L1= 9, L2=10,F=11;

char c;
void setup() {
  pinMode(L1,OUTPUT);
  pinMode(L2,OUTPUT);
  pinMode(F,OUTPUT);
  Serial.begin(9600);

}

void loop() {

//digitalWrite(9,HIGH); digitalWrite(10,HIGH);digitalWrite(11,HIGH);

if(Serial.available()>0)
{
  c=Serial.read();
  Serial.println(c);

   if(c=='a')
  digitalWrite(L1,HIGH);
  
  if(c=='b')
  digitalWrite(L1,LOW);
  if(c=='c')
  digitalWrite(L2,HIGH);
  
  if(c=='d')
  digitalWrite(L2,LOW);
  if(c=='e')
  digitalWrite(F,HIGH);
  
  if(c=='f')
  digitalWrite(F,LOW);


}
}
