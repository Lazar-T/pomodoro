import time
import pynotify

pynotify.init("Pomodoro")

start = pynotify.Notification("Pomodoro Technique",
    """<i>The Pomodoro Technique is a time management method developed by Francesco Cirillo in the late 1980s. The technique uses a timer to break down work into intervals traditionally 25 minutes in length, separated by short breaks. These intervals are known as "pomodori", the plural of the Italian word pomodoro for "tomato". The method is based on the idea that frequent breaks can improve mental agility. <a href="http://en.wikipedia.org/wiki/Pomodoro_Technique">Learn more</a></i>""",
  "", #path to img.png
)

start.show()

work_len = raw_input("Enter number of minutes for pomodoro session: ")
work_in_seconds = int(work_len) * 60

pause_len = raw_input("Enter number of minutes between each pomodoro session: ")
pause_in_seconds = int(pause_len) * 60

pause = pynotify.Notification("Take break for " + pause_len + " minutes")
work = pynotify.Notification("Start working now")

while True:
    work.show()
    time.sleep(float(work_in_seconds))
    pause.show()
    time.sleep(float(pause_in_seconds))
