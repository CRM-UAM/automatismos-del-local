/*
  Example for different sending methods
  
  https://github.com/sui77/rc-switch/
  
*/

#define SW_1_ON  5575987
#define SW_1_OFF 5575996

#define SW_2_ON  5576131
#define SW_2_OFF 5576140

#define SW_3_ON  5576451
#define SW_3_OFF 5576460

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
