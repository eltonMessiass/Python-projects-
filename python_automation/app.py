


import requests
# resp = requests.post('https://textbelt.com/text', {
#   'phone': '+258873549922',
#   'message': 'Hello world',
#   'key': 'textbelt',
# })



def send_message():
    resp = requests.post('https://textbelt.com/text',{
        'phone': '+258879989149',
        'message': 'Olá Malingas tudo bem? Isso é um teste. kkkkkkkkkkk.  Ass: Elton Messias',
        'key': 'textbelt',
    })

    print(resp.json())


#send_message()

import schedule

import time

#schedule.every().day.at('06:00').do(send_message)

schedule.every(10).seconds.do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)