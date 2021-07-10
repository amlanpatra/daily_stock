import subprocess
import requests
import time
# me : 889863862
# stock group : -1001455798482


def send(x):
    url = "https://api.telegram.org/bot1727980585:AAHFRrTSekWIyq1zD_BkO0FjiXyzi7_EWFM/sendMessage?chat_id=-1001455798482&text="+x
    r = requests.get(url)
    print(r.text)
    time.sleep(5)


def sendc(x):
    url = "https://api.telegram.org/bot1727980585:AAHFRrTSekWIyq1zD_BkO0FjiXyzi7_EWFM/sendMessage?chat_id=-1001455798482&text=`"+x+"`&parse_mode=MARKDOWN"
    time.sleep(5)
    r = requests.get(url)
    print(r.text)


def start_dots(rangee, nameoftrend):
    for sending_dots in range(rangee):
        send(".")
    # for i in range(rangee):
    send(nameoftrend)
    send('.')


def send_file(name):
    url = 'curl -v -F "chat_id=889863862" -F document=@{} https://api.telegram.org/bot1727980585:AAHFRrTSekWIyq1zD_BkO0FjiXyzi7_EWFM/sendDocument'.format(
        name)
    subprocess.call(url, shell=True)
# curl -v -F "chat_id=-1001455798482" -F document=@/Users/amlanpatra/Desktop/Projects/stck_analysis_dev/ss.png https://api.telegram.org/bot1727980585:AAEWfPLYEB95CgoSbSQC5Sx58GCi9DvxGMA/sendDocument


# send_file('/Users/amlanpatra/Desktop/Projects/stck_analysis_dev/ss.png')


def psend(x):  # psend for personal send of messages
    url = "https://api.telegram.org/bot1727980585:AAHFRrTSekWIyq1zD_BkO0FjiXyzi7_EWFM/sendMessage?chat_id=889863862&text="+x
    # time.sleep(5)
    r = requests.get(url)
    print(r.text)


def psend_file(name):  # psend_file means personal sending of files
    url = 'curl -v -F "chat_id=889863862" -F document=@{} https://api.telegram.org/bot1727980585:AAHFRrTSekWIyq1zD_BkO0FjiXyzi7_EWFM/sendDocument'.format(
        name)
    subprocess.call(url, shell=True)


def test_send(x):
    url = "https://api.telegram.org/bot1889980295:AAFWdnU2dN6i0vYtgpF96jSzMgFYtS5FZqg/sendMessage?chat_id=889863862&text="+x
    # time.sleep(5)
    r = requests.get(url)
    print(r.text)

# 1889980295:AAFWdnU2dN6i0vYtgpF96jSzMgFYtS5FZqg        <=== test bot token
# 1194321406:AAGLxsBjGay252PCPXhTMl_CKipqc-25vMM        <== powerkey bot token
# 1713334304:AAHgY3CyRO-QYhBTUGuxI4DSt59qmHbj4Is        <== min5 bot token


def pkpsend(x):  # psend for personal send of messages through powerkey bot
    url = "https://api.telegram.org/bot1194321406:AAGLxsBjGay252PCPXhTMl_CKipqc-25vMM/sendMessage?chat_id=889863862&text="+x
    # time.sleep(5)
    r = requests.get(url)
    print(r.text)


def min5psend(x):  # psend for personal send of messages through min5 bot
    url = "https://api.telegram.org/bot1713334304:AAHgY3CyRO-QYhBTUGuxI4DSt59qmHbj4Is/sendMessage?chat_id=889863862&text="+x
    # time.sleep(5)
    r = requests.get(url)
    print(r.text)


"""
Old send()function using powershell. It is not in use as telegram api requests is more efficient

def file_send(x):
    import subprocess
    remaining_string = "Send-TelegramLocalDocument -BotToken 1727980585:AAEWfPLYEB95CgoSbSQC5Sx58GCi9DvxGMA -ChatID -1001455798482-File "
    input_file = open('file.txt', 'w')
    input_file.write(remaining_string + '"{}"'.format(x))
    input_file.close()
    subprocess.call("pwsh -File file.txt", shell=True)


def send(x):
    import subprocess
    # Only for stock bot me : 889863862  stock group :-1001346286579   powerkey channel :-1001241532406     new stock news channel : -1001455798482
    # need to give minus (-) before chat id in channels and groups
    remaining_string = "Send-TelegramTextMessage -BotToken 1727980585:AAEWfPLYEB95CgoSbSQC5Sx58GCi9DvxGMA -ChatID -1001455798482 -Message "

    input_file = open('input.txt', 'w')
    input_file.write(remaining_string + '"{}"'.format(x))
    input_file.close()
    print("Sleeping for 2 secs and then sending")
    time.sleep(2)
    subprocess.call("pwsh -File input.txt", shell=True)
"""
