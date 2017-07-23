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

// Define variables
int inByte = 0;


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

  if (Serial.available()) {
    digitalWrite(TEST_LED, HIGH);
  }
  
  

  if (buttonState == HIGH) {
    
    flash(3, 100);
  } 
  else if (Serial.available()) {
    
    inByte = Serial.read();
    int activeLED = inByte - '1';
    digitalWrite(LED[activeLED], HIGH);
    delay(250);
    digitalWrite(LED[activeLED], LOW);
    delay(100);
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

