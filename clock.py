import datetime
import time
import playsound  # pip install playsound==1.2.2

ALARM_TIME = "07:30"  # format HH:MM (24-hour)

print(f"Alarm set for {ALARM_TIME}")

while True:
    now = datetime.datetime.now().strftime("%H:%M")
    if now == ALARM_TIME:
        print("Wake up!")
        playsound.playsound("alarm.mp3")  # path to sound file
        break
    time.sleep(1)
