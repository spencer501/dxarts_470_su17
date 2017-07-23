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

const int TEST_LED = 13;

const int BUTTON = 2;


void setup() {

  Serial.begin(9600);

  for (int i=0; i < TOTAL_LED; i++) {
    pinMode(LED[i], OUTPUT);
  }

  pinMode(TEST_LED, OUTPUT);

  pinMode(BUTTON, INPUT);
}

void loop() {

  int buttonState = digitalRead(BUTTON);

  if (Serial.available() > 0) {
    digitalWrite(TEST_LED, HIGH);
  }
  
  if (buttonState == HIGH) {
    
    flash(3, 100);
  } 
  else if (Serial.available() > 0) {
    
    int activeLED = Serial.read() - 1;
    
    digitalWrite(LED[activeLED], HIGH);
    delay(175);
    digitalWrite(LED[activeLED], LOW);
    delay(100);

    Serial.print(activeLED + 1);
  }
}


void flash(int cycles, int duration) {

  for (int i=0; i < cycles; i++) {
  
    for (int i=0; i < TOTAL_LED; i++) {
      digitalWrite(LED[i], HIGH);
    }
    delay(duration);
    
    for (int i=0; i < TOTAL_LED; i++) {
      digitalWrite(LED[i], LOW);
    }
    delay(duration);
  }
}

