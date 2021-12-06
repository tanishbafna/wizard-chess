#include <Keypad.h>

//------------------------

const byte ROWS = 8; //four rows
const byte COLS = 8; //four columns
char* keys[ROWS][COLS] = {
  {"a8","b8","c8","d8","e8","f8","g8","h8"},
  {"a7","b7","c7","d7","e7","f7","g7","h7"},
  {"a6","b6","c6","d6","e6","f6","g6","h6"},
  {"a5","b5","c5","d5","e5","f5","g5","h5"},
  {"a4","b4","c4","d4","e4","f4","g4","h4"},
  {"a3","b3","c3","d3","e3","f3","g3","h3"},
  {"a2","b2","c2","d2","e2","f2","g2","h2"},
  {"a1","b1","c1","d1","e1","f1","g1","h1"}
};

byte rowPins[ROWS] = {9, 8, 7, 6, 5, 4, 3, 2}; //connect to the row pinouts of the keypad
byte colPins[COLS] = {17, 16, 15, 14, 13, 12, 11, 10}; //connect to the column pinouts of the keypad

Keypad keypad = Keypad( makeKeymap(keys), rowPins, colPins, ROWS, COLS );

//------------------------

void setup() {
  Serial.begin(9600);
}

void loop() {
  char key = keypad.getKey();

  if (key != NO_KEY){
    Serial.println(key);
  }
  
}
