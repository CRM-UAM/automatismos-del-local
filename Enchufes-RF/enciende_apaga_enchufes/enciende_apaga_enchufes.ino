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

  Serial.begin(9600);
  
  // Transmitter is connected to Arduino Pin #10  
  mySwitch.enableTransmit(10);

  // Optional set pulse length.
  mySwitch.setPulseLength(184);
  
  // Optional set number of transmission repetitions.
  mySwitch.setRepeatTransmit(15);

  delay(1000);
  
}

void loop() {
  mySwitch.send(SW_2_ON, 24);
  delay(1000);  
  mySwitch.send(SW_2_OFF, 24);
  delay(1000);
}
