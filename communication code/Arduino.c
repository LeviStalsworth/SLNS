#include <SPI.h>
#include <Ethernet.h>

//The mac address needs to be found on the shield sticker and galileo
byte mac[] = {0x90, 0xA2, 0xDA, 0x0f, 0x25, 0xE7};
//The mac address on shield

//ip Address for shield
byte ip[] = {192,168,1,113}; //We have to create a similar ip address
//ip Address for Galileo
byte ip2[] = {192,168,1,69};

//Use port 23 for telnet
EthernetServer server = EthernetServer(23);

void setup() {
  Serial.begin(9600);     //For visual feedback on what's going on
  while(!Serial){
    ;   //wait for serial to connect -- needed by Leonardo
  }

  Ethernet.begin(mac2,ip2,);
  delay(10000);
  Ethernet.begin(mac,ip); // init EthernetShield
  delay(10000);

  server.begin();
  if(server.available()){
    Serial.println("Client available");
  }
}

void loop() {
  // put your main code here, to run repeatedly:
  EthernetClient client = server.available();
  message = client.read();

  server.write(message);
  server.write("Testu ");
  Serial.println(message);

//  if (client == true){                    <----- This check screwed it up. Not needed.
//    Serial.println("Client Connected.");
//    server.write(client.read());        //send back to the client whatever     the client sent to us.
  }
int main() {

	setup();
	loop();
	return 0;
  }	