import random
import pyautogui as pt
import time 
animal=('dog','cat', )
time.sleep(10)
for i in range(100):
    a=random.choice(animal)
    pt.write("you are "+a)
    pt.press('enter')