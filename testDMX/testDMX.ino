#include <DmxSimple.h>

void setup() {

  Serial.begin(115200);

  /* DMX devices typically need to receive a complete set of channels

  ** even if you only need to adjust the first channel. You can

  ** easily change the number of channels sent here. If you don't

  ** do this, DmxSimple will set the maximum channel number to the

  ** highest channel you DmxSimple.write() to. */

  DmxSimple.maxChannel(14);
  DmxSimple.usePin(3);   // digital output for DMX serial data
  
  DmxSimple.write(0, 255);     // set fixture #1 master brightness to max
  DmxSimple.write(8, 255);    // set fixture #2 master brightness to max

  //DmxSimple.write(1, 255);     // set fixture #1 master brightness to max
  //DmxSimple.write(8, 255);    // set fixture #2 master brightness to max
  //Turn on to check if they master dimmer is automatically turned on if this command is sent
  Serial.println("DMX Manual Control");
  Serial.println();
  //Serial.println("Syntax:");
  Serial.println(" #c : use DMX channel number value between ranges: 1-512"); //Color Channel
  Serial.println(" #v  : set current channel to value between ranges: 0-255"); //Dimmness
  Serial.println("In format : 000c000v");

}
int value = 0;
int channel;

void loop() {

  int c;

  while (!Serial.available());
  c = Serial.read();
  if ((c >= '0') && (c <= '9')) {
    value = 10 * value + c - '0';
  } else {
    if (c == 'c') channel = value;
    else if (c == 'v') {

      DmxSimple.write(channel, value);
      Serial.print("Ch:");
      Serial.print(channel);
      Serial.print(" Value:");
      Serial.print(value);
      Serial.println();
    }
    value = 0;
  }
}
