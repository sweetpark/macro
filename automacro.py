import pyautogui
import sys
try:
    while 1:
        num =0
        num1=0
        selection = input("do you want continue? y/n")
        if selection == "y" or selection == "Y":
            print("Quitting")
            sys.exit()
        else :
            while num < 1000:
                num1 =0
                pyautogui.moveTo(3781,566, 3)
                pyautogui.click()
                while num1 <4:
                    pyautogui.moveRel(0, 15, 1)
                    pyautogui.click()
                    num1 = num1 +1
                pyautogui.moveTo(3850,152,3)
                pyautogui.click()
                num = num + 1
except KeyboardInterrupt:
    sys.exit()