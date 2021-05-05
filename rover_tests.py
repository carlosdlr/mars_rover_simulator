#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: carlosdlr
"""

from rover_data_initializer import *
from mars_mission import *
import shelve
import unittest

class TestMarsMission(unittest.TestCase):
    def test_locations_initialization(self):
        initialize_locations()
        with shelve.open('locations') as locations:
            self.assertEqual(len(locations), 1)
            
    def test_commands_initialization(self):
        initialize_commands()
        with shelve.open('commands') as commands:
            self.assertEqual(len(commands), 5)
            
    def test_check_command_not_valid(self):
        commands = "FBLLRZ"
        self.assertRaises(KeyError, check_command_validity, commands)
    
    def test_format_location_empty(self):
        location = {}
        self.assertRaises(KeyError, format_location, location, 'fail')
        
    def test_format_location_not_empty(self):
        current_postion = {"desc": "{0} on mars location ({1}, {2}) heading {3}",
                  "coordinates": {
                      "x": 5,
                      "y": 7,
                      "heading": "WEST"
                      }}
        self.assertEqual(format_location(current_postion, "current position"),
                         "current position on mars location (5, 7) heading WEST")
     
    def test_set_heading(self):
        current_postion = {"desc": "{0} on mars location ({1}, {2}) heading {3}",
                  "coordinates": {
                      "x": 5,
                      "y": 7,
                      "heading": "WEST"
                      }}
        set_heading(current_postion, 'R')
        self.assertEqual(current_postion["coordinates"]["heading"], "SOUTH")