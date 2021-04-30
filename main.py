# Copyright© 2020. VL Some rights reserved.
# https://myworldbox.github.io/

import urllib.parse
import webbrowser
import pyautogui
import pandas
import time
import os

first = True
count = 0

list = pandas.read_csv('WhatAuto - Sheet1.csv').to_dict('list')

for number, body in zip(list['number'], list['body']):

    if count % 10 == 0:
        os.system("killall -9 'Google Chrome'")
        webbrowser.open(
            'https://web.whatsapp.com')
        time.sleep(12)

    webbrowser.open('https://web.whatsapp.com/send?phone=852_' + str(number) + '&text=' + urllib.parse.quote(body))
    count += 1

    if (first):
        time.sleep(10)
        first = False

    width, height = pyautogui.size()
    pyautogui.click(width / 2, height / 2)

    time.sleep(10)
    pyautogui.press('enter')
    time.sleep(10)
