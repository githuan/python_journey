#!/usr/bin/env python3

## Import module as namesapce
import helpers
helper.display('Not a warning')


## Import all into current namespace
from helpers import *
display('Not a warning')


## Import specific items into current namespace
from helpers import display
display('Not a warning')