from pyautogui import *
import pyautogui


def Help():
    print("Ayuda:")
    print("minibot.Help() para mostrar este menu")
    print("minibot.Move(Cords-x,Cords-y) para mover el raton a las cords")
    print("minibot.Click(Cords-x,Cords-y) para clickear en las cords")
    print("minibot.DoubleClick(Cords-x,Cords-y) para doble click en las cords")
    print("minibot.Press('tecla') para pulsar la tecla")
    print("minibot.DoublePress('tecla','tecla2') para pulsar la tecla mas la tecla2")
    print("minibot.Write('texto') para escribir el texto")


def Move(x, y):
    pyautogui.moveTo(x, y)
    print(f"El ratón se ha movido a {x},{y}.")


def Click(x, y):
    pyautogui.click(x, y)
    print(f"Se a clickeado en {x},{y}.")


def DoubleClick(x, y):
    pyautogui.doubleClick(x, y)
    print(f"Se a clickeado dos veces en {x},{y}.")


def Press(x):
    pyautogui.press(x)
    print(f"Se ha pulsado la tecla {x}.")


def DoublePress(x, y):
    pyautogui.hotkey(x, y)
    print(f"Se a pulsado la tecla {x} mas {y}.")


def Write(text):
    pyautogui.write(text)
    print(f"Se ha escrito {text}.")
