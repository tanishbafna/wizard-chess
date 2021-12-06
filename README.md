# wizard-chess

Wizard Chess is a Python application with an Arduino plugin to take input from a physical matrix chess board and output a real-time graphical dashboard with several informational features.

<p align="center">
  <img src="https://github.com/tanishbafna/wizard-chess/blob/main/examples/dashboard.png?raw=True" width="350" title="hover text">
  <img src="https://github.com/tanishbafna/wizard-chess/blob/main/examples/analysis.png?raw=True" width="350" alt="accessibility text">
</p>

![Dashboard](https://github.com/tanishbafna/wizard-chess/blob/main/examples/dashboard.png?raw=True)
![Analysis](https://github.com/tanishbafna/wizard-chess/blob/main/examples/analysis.png?raw=True)

## Installation

1. Clone this repository to your local machine.
2. Make sure you have Python 3.7 or higher.
3. `cd` into the main directory and run `pip3 install -r requirements.txt`.
4. Make sure you have Arduino IDE installed.
5. Connect the Arduino to your local machine and upload `keypad_input/keypad_input.ino` to it. (If it throws a library error then unpack `keypad_input/Keypad.zip` in your `Arduino/libraries` directory).

## Testing the Code w/o Arduino
1. Run `chess_integrated.py` and input White and Black player names along with the time control (Eg: 5+0 for 5 minutes).
2. Simultaneously run `examples/test_game.py` and input any number between 1-4 (1 being the shortest and 4 being the longest game).
3. Ensure the entire game plays out on the graphical dashboard. 
4. Once game has ended, press Enter in the terminal window running `chess_integrated.py` to see the post-analysis graph.

## Running the Code with Arduino
1. Connect the Arduino via USB and run `keypad_input/serial_read.py`.
2. Run `chess_integrated.py` and input White and Black player names along with the time control (Eg: 5+0 for 5 minutes).
