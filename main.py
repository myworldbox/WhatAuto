''' pywhatkit is shitty as hell
import pywhatkit
import datetime

x = datetime.datetime.now()
pywhatkit.sendwhatmsg('+85212345678', 'fuck', x.hour, 1+x.minute)
'''

import pyautogui
import webbrowser
import pandas
import time
import os

data = pandas.read_csv('auto.csv')
book = data.to_dict('list')

receiver = book['receiver']
message = book['message']

zipper = zip(receiver, message)
first = True
count = 0

for person, info in zipper:

    time.sleep(4)
    webbrowser.open('https://web.whatsapp.com/send?phone=' + person + '&text=' + info)
    count += 1

    if first:
        time.sleep(6)
        first = False

    width, height = pyautogui.size()
    pyautogui.click(width / 2, height / 2)
    time.sleep(9)
    pyautogui.press('enter')
    time.sleep(8)

    if count == 5:
        os.system("killall -9 'Google Chrome'")
        count = 0