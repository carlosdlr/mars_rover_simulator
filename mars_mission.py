#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: carlosdlr
"""

import shelve
import rover_data_initializer as initializer


def landing():
    print("landing on mars.......")
    initializer.initialize_locations()
    initializer.initialize_commands()
    with shelve.open('locations') as locations:
        print(format_location(locations['0'], "landed"))

def execute_commands(commands):
    check_command_validity(commands)
    with shelve.open('locations') as locations:
        current_postion =  locations['0']
        for command in commands:
            set_heading(current_postion, command)
            move_to(current_postion, command)
        print(format_location(current_postion, "current position"))  
                
                
def set_heading(current_postion, command):
    if current_postion["coordinates"]["heading"] == "NORTH":
        if command == 'R':
            current_postion["coordinates"]["heading"] =  "WEST"
        elif command == 'L':
            current_postion["coordinates"]["heading"] =  "EAST"
    elif current_postion["coordinates"]["heading"] == "SOUTH":    
        if command == 'R':
            current_postion["coordinates"]["heading"] =  "EAST"
        elif command == 'L':
            current_postion["coordinates"]["heading"] =  "WEST"
    elif current_postion["coordinates"]["heading"] == "WEST":    
        if command == 'R':
            current_postion["coordinates"]["heading"] =  "SOUTH"
        elif command == 'L':
            current_postion["coordinates"]["heading"] =  "NORTH"
    elif current_postion["coordinates"]["heading"] == "EAST":    
        if command == 'L':
            current_postion["coordinates"]["heading"] =  "SOUTH"
        elif command == 'R':
            current_postion["coordinates"]["heading"] =  "NORTH"        
            
def move_to(current_postion, command):
    if (current_postion["coordinates"]["heading"] == "NORTH") or (current_postion["coordinates"]["heading"] == "SOUTH"):
        if command == 'F':
            current_postion["coordinates"]["y"] += 2
        elif command == 'B':
            current_postion["coordinates"]["y"] -= 2           
    elif (current_postion["coordinates"]["heading"] == "EAST") or (current_postion["coordinates"]["heading"] == "WEST"):        
        if command == 'F':
            current_postion["coordinates"]["x"] += 2
        elif command == 'B':
            current_postion["coordinates"]["x"] -= 2
    
            
def check_command_validity(entered_commands):
    with shelve.open('commands') as commands:
     for command in entered_commands:
         commands[command]
 
def format_location(location, status):
    return location["desc"].format(status, location['coordinates']["x"], 
                                  location['coordinates']["y"],
                                  location['coordinates']["heading"])      


def start_mission():
    landing()
    while True:
         print("rover ready to start")
         direction = input("""Indicate a direction, F(Forward), B(Backward) L(Left), R(Right), Q(Quit): """).upper()
         if direction == 'Q':
             break
         else:
             try:
                 execute_commands(direction)
             except KeyError:
                 print("An invalid command was entered")    
                  
                
def main():                              
    start_mission()

if __name__ == "__main__":
    main()    

