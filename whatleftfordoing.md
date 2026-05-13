current pomodoro - explain what's left in open-loop calibration.

started ~1:30
breaked for 50min w bitbat
# calibration
- reset red puck calibration - already made easier calibration seq.
- if ylw stack misses sometimes - reset that too.
- run overnight.
# gutter
- [X] drill holes - KINDA...
- [ ] one more hole for the tl column (+ nut on other side)
- [ ] screw solenoids in place. might need more advice from ppl.
- [ ] update solenoid pulsing code to make sure all pucks fall in. (esp. columns 1 and 2 that often don't fall fast enough).
- (10.5.26) - left top column is too loose for 2 red puck on each other (get stuck). need another screw through all?
# main game
- update movement of robot in game to our calibrated sequences
- update button press for light up then restart
    - on getting start from thread, need to have it kill the existing game..?
- request explanation graphic of "press x seconds to reset"
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
