# Project 6: Countdown Timer Python Project

import time

def countdown_timer(seconds):
    print("🔃 Countdown started...\n")
    while seconds >0:
        mins,secs=divmod(seconds,60) 
        time_format='{:02d}:{:02d}'.format(mins,secs)
        print(time_format,end='\r')
        time.sleep(1)
        seconds -=1
    print("⏰ 00:00 \n Time's Up")    

total_seconds=int(input("Enter time in second for countdown : "))
countdown_timer(total_seconds)    