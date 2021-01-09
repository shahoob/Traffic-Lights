from gpiozero import LED
from gpiozero import Button
from time import sleep

red = LED(17);
yellow = LED(27);
green = LED(22);
button = Button(23);

count = 0;

while True:
    red.on();
    yellow.off();
    green.off();
    button.wait_for_press();
    red.off();
    yellow.off();
    green.on();
    sleep(1);
    button.wait_for_press();
    while (count < 5):
        count = count + 1;
        green.off();
        sleep(0.5);
        green.on();
        sleep(0.5);
    green.off();
    yellow.on();
    sleep(2);
    yellow.off();
    red.on();
        
