import pyautogui as pag
import random
import time
import keyboard


def main():

    print("Press the 'end' key to start MouseAFK")

    while True:
        if keyboard.is_pressed('end'):
            # print("a key is pressed")
            move_cursor()      

def move_cursor():
    print('Bring mouse cursor to the top left of the monitor to stop the program')
    while True:
        # coordinates on the monitor
        x = random.randint(600,700)
        y = random.randint(200,600)

        # moving the cursor and adding a delay
        pag.moveTo(x,y,0.5)
        time.sleep(2)

if __name__ == '__main__':
    main()


