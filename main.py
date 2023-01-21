import ctypes
import os
import datetime
import time


def change_wallpaper(code):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, os.path.join(os.getcwd(), "wallpapers", f"{code}.jpg"), 3)


def check_time_and_change_wallpaper():
    current_time = datetime.datetime.now().hour
    if current_time >= 5 and current_time < 6:
        change_wallpaper("1")
    elif current_time >= 6 and current_time < 9:
        change_wallpaper("2")
    elif current_time >= 9 and current_time < 12:
        change_wallpaper("3")
    elif current_time >= 12 and current_time < 16:
        change_wallpaper("4")
    elif current_time >= 16 and current_time < 18:
        change_wallpaper("5")
    elif current_time >= 18 and current_time < 20:
        change_wallpaper("6")
    else:
        change_wallpaper("7")


if __name__ == '__main__':
    check_time_and_change_wallpaper()
    while True:
        check_time_and_change_wallpaper()
        time.sleep(30)
