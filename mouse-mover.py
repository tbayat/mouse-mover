import pyautogui as pag
import time
import random

current_pos = pag.position() #cursor current location
print(current_pos)
monitor_size = pag.size() #size of screen
print(monitor_size)
afk_counter = 0 # time that u dont move your mouse
while True :
    if current_pos == pag.position() :
        afk_counter += 1
    else :
        afk_counter = 0
        current_pos = pag.position()
    if afk_counter > 5 :
        x = random.randint(0,1511)
        y = random.randint(0,981)
        pag.moveTo(x,y,1)
        current_pos = pag.position()
    print(f"AFK counter : {afk_counter}")
    time.sleep(1) #delay between count afk