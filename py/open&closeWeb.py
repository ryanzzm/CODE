#!/usr/bin/python
import time
import webbrowser
import os
import datetime

#first run...
#check time to locate next full hour
currentDateTime = datetime.datetime.now() #full date and time
currentYear = currentDateTime.year
currentMonth = currentDateTime.month
currentDay = currentDateTime.day
currentHour = currentDateTime.hour
currentMin = currentDateTime.minute
currentSec = currentDateTime.second


#time.sleep(3600-currentMin*60-currentSec)
waitTime = 60-currentSec
print("wait: %d" % waitTime)
time.sleep(waitTime)


i = 1
while i == 1 :
    currentDateTime = datetime.datetime.now() #full date and time
    currentYear = currentDateTime.year
    currentMonth = currentDateTime.month
    currentDay = currentDateTime.day
    currentHour = currentDateTime.hour
    currentMin = currentDateTime.minute
    currentSec = currentDateTime.second
    currentWeekNumber = currentDateTime.isocalendar()[1] # week number of the year
    currentWeekdayNumber = currentDateTime.isocalendar()[2] # weekday number of the week
    print(currentMin)
    print(currentWeekNumber)
    print(currentSec)
    #if currentHour > 10 and currentHour < 15 and currentWeekdayNumber < 6 :
    if currentMin > 40 and currentMin < 58 and currentWeekdayNumber < 6 :
        print(currentMin)
        print("in")
        webbrowser.open_new_tab('https://www.youtube.com/watch?v=X_hsmVjI4BU')  # Go to example.com
        #time.sleep(120)
        time.sleep(10)
        print(currentSec)
        os.system("TASKKILL /F /IM chrome.exe")
        #time.sleep(3480)
        print(currentSec)
        time.sleep(50)
        print(currentSec)
    else:
        #time.sleep(3600)
        print(currentMin)
        print("over")
        time.sleep(60)
       
