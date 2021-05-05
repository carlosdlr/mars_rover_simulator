### Rover mission
This program simulates an autonomous vehicule on mars.

## Tech stack
For this solution is required python 3 and have rigths in the application directory
to create file.

## Solution description
When the application starts initialize 2 files to persist command configuration
and the initial position of the vehicule, the name of these files are:

commands.db -> contains the commands configuration.
locations.db -> contains the rover's initial position, this can be extended to
to store each rover's movement that allows to have historical information 
and replay rover's missions.

## To start the application
Just go to the application directory and execute this in the terminal:

python3 mars_mission.py


## To execute the unit tests
Just go to the application directory and execute this in the terminal:

!python3 -m unittest rover_tests.py

## Commands
F -> Move forward on current heading
B -> Move backwards on current heading 
L -> Rotate left by 90 degrees
R -> Rotate right by 90 degrees
