import subprocess
import pyautogui
from PIL import ImageChops
from pynput.keyboard import Key, Controller
from pyscreenshot import grab
import time


def main():
    time_check()
    if 0 <= time_now_wday < 5:
        open_teams()
        check_updates()
        class_join()
    else:
        print("Weekend or Wrong time")
        quit()


def time_check():
    global time_now_hr, time_now_wday, time_now_min

    time_now = str(time.localtime())
    time_now_split = time_now.split(", ")

    time_now_hr_raw = str(time_now_split[3])
    time_now_hr_split = time_now_hr_raw.split("=")
    time_now_hr = int(time_now_hr_split[1])

    time_now_min_raw = str(time_now_split[4])
    time_now_min_split = time_now_min_raw.split("=")
    time_now_min = int(time_now_min_split[1])

    time_now_wday_raw = str(time_now_split[6])
    time_now_wday_split = time_now_wday_raw.split("=")
    time_now_wday = int(time_now_wday_split[1])


def open_teams():
    subprocess.call(r'start "" "C:\Users\divij\desktop\Microsoft Teams"', shell=True)
    time.sleep(20)

    pyautogui.press("win")
    time.sleep(2)
    pyautogui.press("win")
    time.sleep(1)

    pyautogui.FAILSAFE = False
    pyautogui.click(1915, 540, duration=.5)
    pyautogui.click(1915, 1080, duration=1)
    pyautogui.click(1915, 1080)
    pyautogui.click(980, 540, duration=.25)
    pyautogui.FAILSAFE = True
    time.sleep(1)


def check_updates():
    time.sleep(1)
    im = grab(bbox=(1550, 800, 1850, 825))
    while True:
        time.sleep(1.5)

        diff = ImageChops.difference(grab(bbox=(1550, 800, 1850, 825)), im)
        bbox = diff.getbbox()
        if bbox is not None:
            break
        else:
            pyautogui.click(940, 540, duration=.25)
            pyautogui.click(980, 540, duration=.25)


def class_join():
    keyboard = Controller()

    pyautogui.click(1700, 1000, duration=1.5)

    time.sleep(1)
    pyautogui.keyDown('win')
    pyautogui.press('up')
    pyautogui.keyUp('win')
    time.sleep(.5)

    pyautogui.click(700, 930, duration=3)  # time.sleep(300)
    pyautogui.click(1270, 105, duration=5)
    time.sleep(4)
    if (time_now_hr >= 12) or (time_now_hr == 11 and time_now_min >= 45):
        keyboard.type("Good Afternoon")
    else:
        keyboard.type("Good Morning")
    keyboard.press(Key.enter)
    keyboard.release(Key.enter)


main()
