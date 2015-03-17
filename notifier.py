import time
import pynotify
from pygame import mixer


pynotify.init("Pomodoro")
mixer.init()
mixer.music.load("") #path to sound.mp3

start = pynotify.Notification("Pomodoro Timer",
    """<i>The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. The technique uses a timer to break down work into intervals traditionally 25 minutes in length, separated by short breaks. These intervals are known as "pomodori", the plural of the Italian word pomodoro for "tomato". The method is based on the idea that frequent breaks can improve mental agility. <a href="http://en.wikipedia.org/wiki/Pomodoro_Technique">Learn more</a></i>""",
    "") #path to img.png

start.show()

work_len = raw_input("Enter number of minutes for pomodoro session: ")
work_in_seconds = int(work_len) * 60

pause_len = raw_input("Enter number of minutes between each pomodoro session: ")
pause_in_seconds = int(pause_len) * 60

pause = pynotify.Notification("Pomodoro Timer",
    "Take break for " + pause_len + " minutes",
    "") #path to img.png

work = pynotify.Notification("Pomodoro Timer",
    "Start working now",
    "") #path to img.png


while True:
    work.show()
    mixer.music.play()
    time.sleep(float(work_in_seconds))

    pause.show()
    mixer.music.play()
    time.sleep(float(pause_in_seconds))
