# Traffic Lights
A simple project for having the leds that re-assemble the traffic lights.

## NOTE
This is only for Raspberry Pi Computers

## Setup

### Wiring


| LED Color | Hardware Pin | GPIO |
|-----------|--------------|------|
| Red       | 11           | 17   |
| Yellow    | 13           | 27   |
| Green     | 15           | 22   |

You can also wire them into a single rgb led!

#### IMPORTANT

In every wire to the - pin, add 220ohm resistor before the wire being passed.
Not doing this will:
Not letting the leds light up.

### Installation

Since this masterpiece is done with python, You may need to check it before you run the .py files.
By running:
```
python
```
Or:
```
python3
```
If you see this:
```
python: Command not found
```
Then your need to install it yourself.
If it was this:
```
python3: Command not found
```
Then you can use `python` instead of `python3`. Which runs `python` 2.
So `python3` is recommended

## Usage

To run:
```
python main.py
```
Or
```
python3 main.py
```

### Hardware Usage

To control the traffic lights, just press the button.
