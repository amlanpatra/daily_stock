# while transferring code the path of the image must be noted.
import pyautogui as auto
import time
import subprocess
import tsend
# time.sleep(10)


def send_stock_ss(x, chart_duration='15'):
    x = x.lower()
    auto.write(chart_duration, duration=.25)
    auto.press("enter")
    time.sleep(.25)
    auto.write(x, duration=.5)
    time.sleep(1.5)
    auto.press("down")
    auto.press("enter")
    time.sleep(8)
    path = '/Users/amlanpatra/Desktop/Projects/stck_analysis_dev/images/{}.png'.format(
        x)
    ss = auto.screenshot()
    ss.save(r'{}'.format(path))
    tsend.psend_file(path)
    subprocess.call(
        "rm -rf {}".format(path), shell=True)
