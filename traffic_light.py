
#set up
from pymata4 import pymata4
import time 
board = pymata4.Pymata4()
#green light
board.set_pin_mode_digital_output(7)
#yellow light
board.set_pin_mode_digital_output(6)
#red light
board.set_pin_mode_digital_output(5)

def turn_green():
    """
    Function: turn_green
    This function will turn the green light on
    inputs: NA
    outputs: digital pin output
    """
    board.digital_pin_write(5,0)
    board.digital_pin_write(6,0)
    board.digital_pin_write(7,1)

def turn_off():
    """
    Function: turn_off
    This function will turn off all lights
    inputs: NA
    outputs: digital pin output
    """
    board.digital_pin_write(5,0)
    board.digital_pin_write(6,0)
    board.digital_pin_write(7,0)

def turn_red():
    """
    Function: turn_red
    This function will execute the sequence for the red light
    inputs: NA
    outputs: digital pin output
    """
    board.digital_pin_write(6,1)
    time.sleep(3)
    board.digital_pin_write(6,0)
    board.digital_pin_write(5,1)


def main():
    #initial input:
    cars = 0
    while cars <= 0:
        print("how many cars:")
        cars = int(input())

    board.digital_pin_write(5,1)
    while cars > 0:
        turn_green()
        for i in range(1,4):
            print("number of cars:", cars)
            time.sleep(1)
            cars -= 1
            if cars ==0:
                break
        turn_off()
        turn_red()
        time.sleep(3)
    print("no cars at traffic light")
    turn_off()
    board.shutdown()
    

if __name__ == "__main__":
    main()