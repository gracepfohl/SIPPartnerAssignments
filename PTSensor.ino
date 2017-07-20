///////////////////////////////////////////////////
//Project 5.01 Read the phototransistor
int photoTran = A3;
int reading = 0;

void setup(){
  pinMode(photoTran,INPUT);
  Serial.begin(9600);
}

void loop(){
  reading = analogRead(photoTran);
  Serial.println(reading);
  delay(100);
}
///////////////////////////////////////////////////

  

