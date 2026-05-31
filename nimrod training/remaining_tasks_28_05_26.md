
# solenoids
currently testing a new solenoids (& different dimensions). starting with changing one.

- [ ] clamp solenoid onto platform (since holes are in wrong loc. now)
- [ ] update solenoid pulsing code to make sure all pucks fall in. (esp. columns 1 and 2 that often don't fall fast enough).

# calibration
- [ ] recalibrate red puck sequence

# main game
- update movement of robot in game to our calibrated sequences
- update button press for light up then restart
    - on getting start from thread, need to have it kill the existing game..?
- request explanation graphic of "press x seconds to reset" from amir/nevo (the graphic designer).
# future calibration - meeting w amir, his choice.
- screw in robot again
- recalibrate zero positions
- make some homing location for the robot.
# cleanup
- new non-gpt-ish readme.
- delete non-essential files
    - [X] cleanup arduino code
- explain ocp structure + how to cmake the solver.
- update todos in readme.md


## quality of life stuff 
- automatic identify ports so you don't need to do it yourself
