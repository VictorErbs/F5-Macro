import time
import keyboard

def press_f5():
    while True:
        keyboard.press('F5')
        keyboard.release('F5')
        time.sleep(2)

press_f5()