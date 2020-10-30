from gpiozero import LED
from gpiozero import Button
from time import sleep

leda = LED(17);
ledb = LED(27);
ledc = LED(22);
button = Button(23);

count = 0;

while True:
    leda.on();
    ledb.off();
    ledc.off();
    button.wait_for_press();
    leda.off();
    ledb.off();
    ledc.on();
    sleep(1);
    button.wait_for_press();
    while (count < 5):
        count = count + 1;
        ledc.off();
        sleep(0.5);
        ledc.on();
        sleep(0.5);
    ledc.off();
    ledb.on();
    sleep(2);
    ledb.off();
    leda.on();
        
