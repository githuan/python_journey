#!/usr/bin/env python3.7
#title           :stopwatch_v2.py
#description     :Build a timer with specific modules from (time package)
#author          :Thuan Q Nguyen
#date            :20190118
#version         :0.2
#usage           :
#notes           :
#python_version  :3.7.2
#==============================================================================

from time import localtime, mktime, strftime

start_time = localtime()
print(f"Timer started at {strftime('%X', start_time)}")

# Wait for user to stop timer
input("Press 'Enter' to stop timer ")

stop_time= localtime()
difference = mktime(stop_time) - mktime(start_time)

print(f"Timer stopped at {strftime('%X', stop_time)}")
print(f"Total time: {difference} seconds")
