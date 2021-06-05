void setup() {
 
pinMode(13,OUTPUT);

}

void loop() {
tone(10,500);
delay(2000);
noTone(10);
delay(2000);
tone(10,1000);
delay(5000);
}
