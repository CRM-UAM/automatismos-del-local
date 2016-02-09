/*
  Example for different sending methods
  
  https://github.com/sui77/rc-switch/
  
*/

#define SW_1_ON  4527411
#define SW_1_OFF 4527420

#define SW_2_ON  4527555
#define SW_2_OFF 4527564

#define SW_3_ON  4527875
#define SW_3_OFF 4527884

#include <RCSwitch.h>

RCSwitch mySwitch = RCSwitch();

void setup() {

  Serial.begin(19200);
  
  // Transmitter is connected to Arduino Pin #10  
  mySwitch.enableTransmit(10);

  // Optional set pulse length.
  mySwitch.setPulseLength(184);
  
  // Optional set number of transmission repetitions.
  mySwitch.setRepeatTransmit(15);

  delay(1000);
  
}

int enchufes_ON = true;

void enciendeTodo() {
  mySwitch.send(SW_1_ON, 24);
  delay(100);
  mySwitch.send(SW_2_ON, 24);
  delay(100);
  mySwitch.send(SW_3_ON, 24);
  delay(100);
  enchufes_ON = true;
}

void apagaTodo() {
  mySwitch.send(SW_1_OFF, 24);
  delay(100);
  mySwitch.send(SW_2_OFF, 24);
  delay(100);
  mySwitch.send(SW_3_OFF, 24);
  delay(100);
  enchufes_ON = false;
}

int hayLuz() {
  return (analogRead(A0) > 450);
}

void loop() {
  Serial.println(analogRead(A0));
  if(enchufes_ON == false && hayLuz()) {
    enciendeTodo();
  } else if(enchufes_ON == true && !hayLuz()) {
    delay(3000);
    if(!hayLuz()) apagaTodo();
  }
  delay(1000);
}
