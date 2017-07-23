/*
 * Spencer Pease
 * DXARTS 470
 * 
 * Draft 1:
 * Create an array of LEDs that are controlled via external
 * serial communication
 */

// Define constants
const int LED[] = {3, 4, 5, 6};
const int TOTAL_LED = 4;

const int BUTTON = 2;


void setup() {

  for (int i=0; i < TOTAL_LED; i++) {
    pinMode(LED[i], OUTPUT);
  }

  pinMode(BUTTON, INPUT);
}

void loop() {

  int buttonState = digitalRead(BUTTON);

  for (int i=0; i < TOTAL_LED; i++) {
    digitalWrite(LED[i], buttonState);
  }

  delay(100);
}

