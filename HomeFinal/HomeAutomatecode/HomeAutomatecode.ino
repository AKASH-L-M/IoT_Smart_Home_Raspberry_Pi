#include <dht11.h>
#define DHT11PIN 4
dht11 DHT11;
int A[3] ={};

int ldrPin = A3;

int humidity = 0;
int temp = 0;
int intensity = 9680;

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  
  pinMode(ldrPin, INPUT);
}

void loop() {
  int chk = DHT11.read(DHT11PIN);
  A[0] = (int)DHT11.humidity;
  A[1] = (int)DHT11.temperature;

 
   A[2] = analogRead(ldrPin);

  for(int i = 0; i<3; i++){
    Serial.println(A[i]);
    delay(500);
  }
  delay(10000);
  
}
