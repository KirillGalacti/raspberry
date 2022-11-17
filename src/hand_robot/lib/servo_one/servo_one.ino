#include <Servo.h>
#include <Wire.h>

#define SLAVE_ADD_1 0x08
#define PIN 2

Servo myservo_1;
String pypos;

int pos = 0;

void setup(){
  Wire.begin(SLAVE_ADD_1);
  Wire.onReceive(receiveData);
  myservo_1.attach(PIN);
  Serials.begin(9600);
}

void loop(){

}

void receiveData(){
    if(Serial.available() ) //если команда принята, то
    {
    pypos = Serial.readString(); // принять полученную строку и перевести в строку
    Serial.println(" Angle: " + pypos);
    serial.println('\n');
    int pyposint = pypos.toInt();
    myservo.write(pyposint);
    Serial.flush();
    delay(15);
    }  
}
