#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_ADXL345_U.h>
#include <OneWire.h>
#include <DallasTemperature.h>

Adafruit_ADXL345_Unified accel = Adafruit_ADXL345_Unified(12345);


#define ONE_WIRE_BUS 4
OneWire oneWire(ONE_WIRE_BUS);
DallasTemperature tempSensor(&oneWire);

float baseGravity = 9.81; 

const int currentPin = 34;
const int voltagePin = 35;

float prevVibration = 0;
float currentOffset = 2.20; 

void setup() {
  Serial.begin(115200);
  Wire.begin(21, 22);

  if (!accel.begin()) {
    Serial.println("ADXL345 not detected! Check SDA/SCL lines.");
    while (1);
  }

  accel.setRange(ADXL345_RANGE_16_G);
  tempSensor.begin();


  float gravitySum = 0;
  for (int i = 0; i < 50; i++) {
    sensors_event_t event;
    accel.getEvent(&event);
    gravitySum += sqrt(event.acceleration.x * event.acceleration.x +
                       event.acceleration.y * event.acceleration.y +
                       event.acceleration.z * event.acceleration.z);
    delay(10);
  }
  baseGravity = gravitySum / 50.0;


}

float getVibration() {
  float sum = 0;
  const int samples = 15;

  for (int i = 0; i < samples; i++) {
    sensors_event_t event;
    accel.getEvent(&event);

    float currentG = sqrt(
      event.acceleration.x * event.acceleration.x +
      event.acceleration.y * event.acceleration.y +
      event.acceleration.z * event.acceleration.z
    );

    float rawVibe = abs(currentG - baseGravity);
    sum += rawVibe;
    delay(4);
  }

  float vibration = sum / samples;

  vibration = (vibration * 0.3) + (prevVibration * 0.7);
  prevVibration = vibration;


  if (vibration < 0.15) vibration = 0.00;

  return vibration;
}


float getTemperature() {
  tempSensor.requestTemperatures();
  float temp = tempSensor.getTempCByIndex(0);

  if (temp == -127 || temp == 85) {
    return -1; 
  }
  return temp;
}


float getCurrent() {
  float sum = 0;

  for (int i = 0; i < 20; i++) {
    int raw = analogRead(currentPin);
    float v = raw * (3.3 / 4095.0);
    sum += v;
    delay(2);
  }

  float voltage = sum / 20;

  float current = (voltage - currentOffset) / 0.185;

  // Remove noise
  if (abs(current) < 0.15) current = 0;
  if (current > 5 || current < -5) current = 0;

  return current ;
}


float getVoltage() {
  int raw = analogRead(voltagePin);
  float v_out = raw * (3.3 / 4095.0);

  float voltage = v_out * 5; 

  return voltage;
}


void loop() {

  float vibration = getVibration();
  float temperature = getTemperature();
  float voltage = getVoltage();
  float current = getCurrent();


  // Skip bad temperature readings
  if (temperature == -1) {
    return;
  }

  Serial.print(vibration); Serial.print(",");
  Serial.print(temperature); Serial.print(",");
  Serial.print(current); Serial.print(",");
  Serial.println(voltage);

  delay(500);
}