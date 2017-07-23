/*
 * Spencer Pease
 * DXARTS 470
 * 
 * Draft 1:
 * Create an array of LEDs that are controlled via external
 * serial communication
 */

// Define constants
#define LED_PIN_R 6
#define LED_PIN_Y 5
#define LED_PIN_G 4
#define LED_PIN_B 3

#define BUTTON_PIN 2


void setup() {

  pinMode(LED_PIN_R, OUTPUT);
  pinMode(LED_PIN_Y, OUTPUT);
  pinMode(LED_PIN_G, OUTPUT);
  pinMode(LED_PIN_B, OUTPUT);

  pinMode(BUTTON_PIN, INPUT);
  
}

void loop() {

  int buttonActive = digitalRead(BUTTON_PIN);

  if (buttonActive == HIGH) {
    
    digitalWrite(LED_PIN_R, HIGH);
    digitalWrite(LED_PIN_Y, HIGH);
    digitalWrite(LED_PIN_G, HIGH);
    digitalWrite(LED_PIN_B, HIGH);
    delay(100);
  }
  else {

    digitalWrite(LED_PIN_R, LOW);
    digitalWrite(LED_PIN_Y, LOW);
    digitalWrite(LED_PIN_G, LOW);
    digitalWrite(LED_PIN_B, LOW);
    delay(100);
  }

}

