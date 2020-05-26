#include <SPI.h>
#include <Ethernet.h>

byte mac[] = { 0x98, 0x04F, 0xEE, 0x05, 0x0D, 0xEA };
byte ip[] = { 192, 168, 0, 42 };

vooid setup() {
  Ethernet.beging(mac, ip);
}

void loop() {
}
