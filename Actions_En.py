from pyautogui import *
import pyautogui
def Help():
    print("Help:")
    print("minibot.Help() for help")    
    print("minibot.Move(Cords-x, Cords-y) to move the mouse to the cords")
    print("minibot.Click(Cords-x, Cords-y) to click on cords")
    print("minibot.DoubleClick(Cords-x, Cords-y) to double click on cords")
    print("minibot.Press('key') to press the key")
    print("minibot.DoublePress('key', 'key2') to press the key plus key2")
    print("minibot.Write('tex') to write the text")
def Move(x,y):
    pyautogui.moveTo(x,y)
    print(f"The mouse has moved to {x},{y}.")
def Click(x,y):
    pyautogui.click(x,y)
    print(f"Click on {x},{y}.")
def DoubleClick(x,y):
    pyautogui.doubleClick(x,y)
    print(f"Clicked twice in {x},{y}.")
def Press(x):
    pyautogui.press(x)
    print(f"The {x} key has been pressed.")
def DoublePress(x,y):
    pyautogui.hotkey(x, y)
    print(f"Press and hold {x} plus {y}.")
def Write(text):
    pyautogui.write(text)
    print(f"Has been written {text}")
