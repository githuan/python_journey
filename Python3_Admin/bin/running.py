#!/usr/bin/env python3.7
#title           :running.py
#description     :Gets environement value and alert.
#author          :Thuan Q Nguyen
#date            :20190121
#version         :0.1
#usage           :
#notes           :
#python_version  :3.7.2
#==============================================================================

import os

stage = os.getenv("STAGE", default="dev").upper()

output = f"We're running in {stage}"

if stage.startswith('PROD'):
    output = "DANGER!!! - " + output

print(output)
