import time
import keyboard

def press_f5():
    """
    Pressiona a tecla F5 a cada 2 segundos.
    """
    while True:
        keyboard.press('F5')
        keyboard.release('F5')
        time.sleep(2)

if __name__ == "__main__":
    press_f5()
