#include <dht.h>
#include <Time.h>
dht DHT;

#define DHT11_PIN 7
double chk;
void digitalClockDisplay();

void setup(){
  Serial.setTimeout(50)
  Serial.begin(9600);
}

void loop()
{
  chk = DHT.read11(DHT11_PIN);
  Serial.print("Temperature = ");
  Serial.println(DHT.temperature);
  Serial.print("Humidity = ");
  Serial.println(DHT.humidity);
  delay(1500);
}

