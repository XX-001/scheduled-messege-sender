from credentials import mobile_number
import requests
import schedule
import time

def send_message():
    resp = requests.post("https://textbelt.com/text", {
        "phone" : mobile_number,
        "message" : "Hey, You are Genius",
        "key": "textbelt"
    })
    print(resp.json())

schedule.every().day.at("10:00").do(send_message)

while True:
    schedule.run_pending()
    time.sleep(1)