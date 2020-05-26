/*
 UDPSendReceiveString:
 This sketch receives UDP message strings, prints them to the serial port
 and sends an "acknowledge" string back to the sender

 A Processing sketch is included at the end of file that can be used to send
 and received messages for testing with a computer.

 created 21 Aug 2010
 by Michael Margolis

 This code is in the public domain.
 */


#include <Ethernet.h>
#include <EthernetUdp.h>
#include <DmxSimple.h>
#include <stdio.h>
#include <errno.h>
#include <stdlib.h>

char *str;
char chanStr[3];
char valStr[3];
int valDMX[4];
int count;
//char delim = " ";
int ild;
int jild;
int nild;
int charsArr[4][3];
char thing;
char testArr[23];
int l;
int titty[23];
int failono;

// Enter a MAC address and IP address for your controller below.
// The IP address will be dependent on your local network:
byte mac[] = {
  0xDE, 0xAD, 0xBE, 0xEF, 0xFE, 0xED
};
IPAddress ip(192, 168, 1, 177);

unsigned int localPort = 5004;      // local port to listen on

// buffers for receiving and sending data
char packetBuffer[UDP_TX_PACKET_MAX_SIZE];  // buffer to hold incoming packet,
char ReplyBuffer[] = "acknowledged";        // a string to send back
int todFail;
//char chan[];
//char val[];

// An EthernetUDP instance to let us send and receive packets over UDP
EthernetUDP Udp;

void setup() {
  // You can use Ethernet.init(pin) to configure the CS pin
  //Ethernet.init(10);  // Most Arduino shields
  //Ethernet.init(5);   // MKR ETH shield
  //Ethernet.init(0);   // Teensy 2.0
  //Ethernet.init(20);  // Teensy++ 2.0
  //Ethernet.init(15);  // ESP8266 with Adafruit Featherwing Ethernet
  //Ethernet.init(33);  // ESP32 with Adafruit Featherwing Ethernet
  DmxSimple.maxChannel(14);
  DmxSimple.usePin(3);   // digital output for DMX serial data
  
  DmxSimple.write(0, 255);     // set fixture #1 master brightness to max
  DmxSimple.write(8, 255);    // set fixture #2 master brightness to max
  
  
  // start the Ethernet
  Ethernet.begin(mac, ip);

  // Open serial communications and wait for port to open:
  Serial.begin(9600);
  while (!Serial) {
    ; // wait for serial port to connect. Needed for native USB port only
  }

  // Check for Ethernet hardware present
  if (Ethernet.hardwareStatus() == EthernetNoHardware) {
    Serial.println("Ethernet shield was not found.  Sorry, can't run without hardware. :(");
    while (true) {
      delay(1); // do nothing, no point running without Ethernet hardware
    }
  }
  if (Ethernet.linkStatus() == LinkOFF) {
    Serial.println("Ethernet cable is not connected.");
  }

  // start UDP
  Udp.begin(localPort);
}

void loop() {
  // if there's data available, read a packet
  int packetSize = Udp.parsePacket();
  if (packetSize) {
    //Serial.print("Received packet of size ");
    //Serial.println(packetSize);
    //Serial.print("From ");
    Udp.beginPacket(Udp.remoteIP(), Udp.remotePort());
    //Serial.println(failono);
    //Serial.println(Udp.remoteIP());
    Udp.write(ReplyBuffer);
    failono = Udp.endPacket();
    Serial.println(failono);
    
    IPAddress remote = Udp.remoteIP();
    for (int i=0; i < 4; i++) {
      //Serial.print(remote[i], DEC);
      if (i < 3) {
        //Serial.print(".");
      }
    }
    //Serial.print(", port ");
    //Serial.println(Udp.remotePort());	

    // read the packet into packetBufffer
    Udp.read(packetBuffer, UDP_TX_PACKET_MAX_SIZE);

    //charsArr[0][0] = packetBuffer[0];
    for(jild = 0; jild < 4; jild++) {
      for(nild = 0; nild < 3; nild++) {
        charsArr[jild][nild] = '0';
      }
    }
    jild = 2;
    nild = 0;
    //Serial.println("fuckoff were here now");
    for(ild = 0; ild < UDP_TX_PACKET_MAX_SIZE; ild++) {
      if(packetBuffer[ild] != ' ') {
        charsArr[nild][jild] = packetBuffer[ild];
       /* Serial.print(" char ");
        Serial.print(charsArr[nild][jild]);
        Serial.print(" nild = ");
        Serial.print(nild);
        Serial.print(" jild = ");
        Serial.print(jild);*/
        //Serial.println(packetBuffer[ild]);
        jild--; 
      }
      else {
        if(charsArr[nild][0] == '0'){
          valDMX[nild] = (charsArr[nild][2]-'0') + ((charsArr[nild][1]-'0')*10);
        }
        else if(charsArr[nild][0] == '0' && charsArr[nild][1] == '0') {
          valDMX[nild] = (charsArr[nild][2]-'0');
        }
        else {
          valDMX[nild] = (charsArr[nild][0]-'0') + ((charsArr[nild][1]-'0')*10) + ((charsArr[nild][2]-'0')*100);
        }
        nild++;
        jild = 2;
      }
      if (nild > 3) {
        break;
      }
      
    }
    /*Serial.println();
    //Serial.println(ild);
    //l = charsArr[0];
    //valDMX[0] = atoi(l);
    //valDMX[0] = atoi(charsArr[0]);
    //thing = charsArr[0][0];
    //valDMX[0] = atoi(thing);
    //valDMX[1] = atoi(charsArr[1]);
    Serial.print("charsArr1[]: ");
    //Serial.println(charsArr[1]);
    //valDMX[2] = atoi(charsArr[2]);
    //valDMX[3] = atoi(charsArr[3]);*/
    Serial.println("Contents:");
    Serial.println(packetBuffer);
    //Serial.print("light ");
    //Serial.print(valDMX[0]);
    //Serial.print(", r ");
    //Serial.print(valDMX[1]);
    //Serial.print(", g ");
    //Serial.print(valDMX[2]);
    //Serial.print(", b ");
    //Serial.print(valDMX[3]);

    DmxSimple.write(((valDMX[0]-1)*7)+1, 155);
	  DmxSimple.write(((valDMX[0]-1)*7)+2, valDMX[1]);
    DmxSimple.write(((valDMX[0]-1)*7)+3, valDMX[2]);
    DmxSimple.write(((valDMX[0]-1)*7)+4, valDMX[3]);

    /*
    DmxSimple.write(packetBuffer[0], 150);
    DmxSimple.write(2, 155);
    DmxSimple.write(3, 255);
    DmxSimple.write(4, 0);
    */
  }
  delay(10);
}
