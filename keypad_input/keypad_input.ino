#include <Keypad.h>

//------------------------

const byte ROWS1 = 4; //four rows
const byte COLS1 = 4; //four columns
char* keys1[ROWS1][COLS1] = {
  {"a4","b4","c4","d4"},
  {"a3","b3","c3","d3"},
  {"a2","b2","c2","d2"},
  {"a1","b1","c1","d1"}
};
byte rowPins1[ROWS1] = {5, 4, 3, 2}; //connect to the row pinouts of the keypad
byte colPins1[COLS1] = {9, 8, 7, 6}; //connect to the column pinouts of the keypad

Keypad keypad1 = Keypad( makeKeymap(keys1), rowPins1, colPins1, ROWS1, COLS1 );

//------------------------

const byte ROWS2 = 4; //four rows
const byte COLS2 = 4; //four columns
char* keys2[ROWS2][COLS2] = {
  {"e4","f4","g4","h4"},
  {"e3","f3","g3","h3"},
  {"e2","f2","g2","h2"},
  {"e1","f1","g1","h1"}
};
byte rowPins2[ROWS2] = {5, 4, 3, 2}; //connect to the row pinouts of the keypad
byte colPins2[COLS2] = {9, 8, 7, 6}; //connect to the column pinouts of the keypad

Keypad keypad2 = Keypad( makeKeymap(keys2), rowPins2, colPins2, ROWS2, COLS2 );

//------------------------

const byte ROWS3 = 4; //four rows
const byte COLS3 = 4; //four columns
char* keys3[ROWS3][COLS3] = {
  {"a8","b8","c8","d8"},
  {"a7","b7","c7","d7"},
  {"a6","b6","c6","d6"},
  {"a5","b5","c5","d5"}
};
byte rowPins3[ROWS3] = {5, 4, 3, 2}; //connect to the row pinouts of the keypad
byte colPins3[COLS3] = {9, 8, 7, 6}; //connect to the column pinouts of the keypad

Keypad keypad3 = Keypad( makeKeymap(keys3), rowPins3, colPins3, ROWS3, COLS3 );


//------------------------


const byte ROWS4 = 4; //four rows
const byte COLS4 = 4; //four columns
char* keys4[ROWS4][COLS4] = {
  {"e8","f8","g8","h8"},
  {"e7","f7","g7","h7"},
  {"e6","f6","g6","h6"},
  {"e5","f5","g5","h5"}
};
byte rowPins4[ROWS4] = {5, 4, 3, 2}; //connect to the row pinouts of the keypad
byte colPins4[COLS4] = {9, 8, 7, 6}; //connect to the column pinouts of the keypad

Keypad keypad4 = Keypad( makeKeymap(keys4), rowPins4, colPins4, ROWS4, COLS4 );

//------------------------

void setup() {
  Serial.begin(9600);
}

void loop() {
  char key1 = keypad1.getKey();
  char key2 = keypad2.getKey();
  char key3 = keypad3.getKey();
  char key4 = keypad4.getKey();

  if (key1 != NO_KEY || key2 != NO_KEY || key3 != NO_KEY || key4 != NO_KEY){
    Serial.println(key1);
    Serial.println(key2);
    Serial.println(key3);
    Serial.println(key4);
  }
}
