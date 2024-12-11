from credentials import mobile_number
import schedule
import requests
import time

def send_message():
    resp = requests.post("https://textbelt.com/text", {
        'phone': mobile_number,
        'message': "Yurtta sulh, cihanda sulh.",
        'key': 'textbelt',
    })
    print(resp.json())

schedule.every().day.at('06:00').do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)