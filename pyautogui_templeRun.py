import pyautogui


def clicks(num):
    #pyautogui.PAUSE = 0

    if   num == 5:
        pyautogui.press('up')


    elif num == 1:
        pyautogui.click()
    elif num == 3:
        pyautogui.press('down')
    elif num == 3:
        pyautogui.press('down')


    elif num == 2:
        pyautogui.press('right')
    elif num == 4:
        pyautogui.press('left')

    return num

