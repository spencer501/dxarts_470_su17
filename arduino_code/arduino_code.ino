/*
   Spencer Pease
   DXARTS 470

   Draft 2:
   Create an array of solenoids that are controlled via external
   serial communication
*/

// Define constants
const int TOTAL_SOLENOID = 4;
const int SOLENOID[TOTAL_SOLENOID] = {3, 4, 5, 6};

const int BUTTON = 13;
const int LED = 12;


void setup() {

  Serial.begin(9600);

  for (int i = 0; i < TOTAL_SOLENOID; i++) {
    pinMode(SOLENOID[i], OUTPUT);
  }

  pinMode(BUTTON, INPUT);
  pinMode(LED, OUTPUT);
}

void loop() {

  int buttonState = digitalRead(BUTTON);

  if (buttonState == HIGH) {

    cascade(1, 250);
//    pulse(1, 500);
    delay(1000);
  }
  else if (Serial.available() > 0) {

    int activeSolenoid = Serial.read();

    digitalWrite(SOLENOID[activeSolenoid], HIGH);
    delay(50);
    digitalWrite(SOLENOID[activeSolenoid], LOW);
    delay(60);
  }
}


void cascade(int cycles, int duration) {

  for (int i = 0; i < cycles; i++) {

    for (int i = 0; i < TOTAL_SOLENOID; i++) {

      digitalWrite(SOLENOID[i], HIGH);
      delay(50);
      digitalWrite(SOLENOID[i], LOW);
      delay(duration);
    }
  }
}

void pulse(int cycles, int duration) {

  for (int i = 0; i < cycles; i++) {

    for (int i = 0; i < TOTAL_SOLENOID; i++) {

      digitalWrite(SOLENOID[i], HIGH);
    }

    delay(duration);

    for (int i = 0; i < TOTAL_SOLENOID; i++) {

      digitalWrite(SOLENOID[i], LOW);
    }

    delay(duration);
  }
}

