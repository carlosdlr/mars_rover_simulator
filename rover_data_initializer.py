#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: carlosdlr
"""

import shelve

def initialize_locations(): 
    locations = shelve.open('locations') 
    locations['0'] = {"desc": "{0} on mars location ({1}, {2}) heading {3}",
                  "coordinates": {
                      "x": 0,
                      "y": 0,
                      "heading": "NORTH"
                      }}
    locations.close()
    

def initialize_commands(): 
    commands = shelve.open('commands')
    commands["Q"] = "QUIT"
    commands["F"] = "FORWARD"
    commands["B"] = "BACKWARDS"
    commands["L"] = "LEFT"
    commands["R"] = "RIGHT"    
    commands.close()
