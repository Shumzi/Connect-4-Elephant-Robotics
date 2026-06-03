
# pucks not falling good
currently testing a new solenoids (& different dimensions). starting with changing one.

- [ ] clamp solenoid onto platform (since holes are in wrong loc. now)
- [ ] update solenoid pulsing code to make sure all pucks fall in. (esp. columns 1 and 2 that often don't fall fast enough).
    - parameters to play with: 
        1. voltage
        2. how many ms for a puck w x pucks above it?
- [ ] maybe changing column width in perspex can fix everything 
- [ ] meeting w omer about mechanics. (maybe w eyal as well).

# calibration
- [ ] recalibrate red puck sequence

# main game
- update movement of robot in game to our calibrated sequences (i.e. update robot.py to use the locations from angles.json)
- update button press for light up then restart
    - on getting start from thread, need to have it kill the existing game..?
- meeting to decide how to reset (or just decide yourself)
- request explanation graphic of "press x seconds to reset" from amir/nevo (the graphic designer).
# future calibration - meeting w amir, his choice.
- ideas -
    - recalibrate zero positions
    - make some homing location for the robot.
# cleanup
- new non-gpt-ish readme.

## quality of life stuff 
- automatic identify ports instead of config.yaml so you don't need to do it yourself
