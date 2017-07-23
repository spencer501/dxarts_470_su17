/*
 * Spencer Pease
 * DXARTS 470
 * 
 * Draft 1:
 * Create an array of LEDs that are controlled via external
 * serial communication
 */

// Define constants
const int LED_R = 6;
const int LED_Y = 5;
const int LED_G = 4;
const int LED_B = 3;

const int BUTTON = 2;


void setup() {

  pinMode(LED_R, OUTPUT);
  pinMode(LED_Y, OUTPUT);
  pinMode(LED_G, OUTPUT);
  pinMode(LED_B, OUTPUT);

  pinMode(BUTTON, INPUT);
  
}

void loop() {

  int buttonActive = digitalRead(BUTTON);

  if (buttonActive == HIGH) {
    
    digitalWrite(LED_R, HIGH);
    digitalWrite(LED_Y, HIGH);
    digitalWrite(LED_G, HIGH);
    digitalWrite(LED_B, HIGH);
    delay(100);
  }
  else {

    digitalWrite(LED_R, LOW);
    digitalWrite(LED_Y, LOW);
    digitalWrite(LED_G, LOW);
    digitalWrite(LED_B, LOW);
    delay(100);
  }

}

