import urllib.parse
import pyautogui
import webbrowser
import pandas
import time
import os

data = pandas.read_csv('auto - Sheet1.csv')
book = data.to_dict('list')

receiver = book['電話號碼 - Phone number']
message = book['message']

zipper = zip(receiver, message)
first = True
count = 0

for person, info in zipper:

    if count % 10 == 0:
        os.system("killall -9 'Google Chrome'")
        webbrowser.open(
            'https://web.whatsapp.com')
        time.sleep(12)

    webbrowser.open(
        'https://web.whatsapp.com/send?phone=852_' + str(person) + '&text=' + urllib.parse.quote(
            '成員: ' + str(count) + '\n\n' + info))
    count += 1

    if (first):
        time.sleep(10)
        first = False

    width, height = pyautogui.size()
    pyautogui.click(width / 2, height / 2)

    time.sleep(10)
    pyautogui.press('enter')
    time.sleep(10)
