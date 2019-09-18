#include <dht.h>
#include <Time.h>
dht DHT;

#define DHT11_PIN 7
double chk;
unsigned long timer;
int measurement_delay = 2000;
void setup() {
  Serial.setTimeout(50);
  Serial.begin(9600);
  timer = millis();
}

void loop()
{
  if (millis() - timer > measurement_delay) {
    timer = millis();
    float temp = DHT.temperature;
    float hum = DHT.humidity;
    to_print(temp, hum);
  }
}

void to_print(float var1, float var2) {
  Serial.print(var1);
  Serial.print(",");
  Serial.println(var2);
}
