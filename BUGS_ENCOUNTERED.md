In this doc, we'll describe some of the main bugs we had during the development process and what we did to solve them.

# the ever-breaking pump
the pump that is used to hold the pucks by suction kept having its gates broken. Possibly bc we connected the wires with a breadboard and the wires often were in the air, causing some weird voltage issues.
Solution:
1. Gave it to amir to fix a bunch of times
2. try 

# non-deterministic slow robot movement
at seemingly random, when we required a linear movement from the robot (e.g. for picking up pucks or placing them in the columns), the robot would generate some very slow and sometimes very wacky (in angles terms) positions, where the motors would move much more than another Inverse Kinematics (IK) solution could bring. It was clear we needed to rid ourselves of this. Solution:
1. Instead of relying on pymycobot's internal linear movement, we wrapped our own linear interpolator with a variable mm distance between points in cartesian space (see in `hardware/robot.py` the func `get_coords_interpolated`).  
2. In our calibration process (at `system_tests/calibrate_robot_locations.py`), we make sure to have an `angles.json` that includes all our positions (including the linear interpolation movements) in angle (i.e. motor) space. this requires us to physically move the robot to the cartesian position it calculated, then mark the angles at that point.  
this way, the risks generated from both the interpolation alg and in IK of pymycobot are mitigated to just the calibration process which we compute (hopefully) once offline.

# puck dispenser
## solenoids
the solenoids caused many headaches for our resident programmer wannabe-machanic. They'd get stuck at times, sometimes they wouln't open, and sometimes they'd fry. Specifically, the solenoids turn on based on the value sent via a MOSI line, that at one point wasn't periodically sending a reset. So, one time when some noise got into the system and was left on for the weekend, the MOSI line left a bunch of the solenoids on all that time and fried them.  
solution:  
1. swapped out the coils from some other set of solenoids we found that didn't have the correct pin size but still fit on the old one's casings.
2. tested current draw on the coils, looks ok (~400mA on ~18v).

## puck jams
The outer perspex pane of the board was warped (either because I screwed it in wrong or just over time), so when we tried releasing the pucks to the gutter they would often get stuck. Either they'd:  
1. Fall in between the panes
2. Whiplash upwards instead of falling down and create a jam (this would happen on the middle columns since at the edges there's only one direction to fall into)
3. fall into the slide but get stuck there instead of sliding down, causing a jam.

Solution (in same order as problems):  
1. Fastened the outer pane, first with clamps for an easy test, and soon by adding holes so the screws go through all 3 panes instead of just the inner 2.
2. Albeit not the most elegant solution, but we pulse our opening and closing of solenoids so the pucks fall one at a time. So we didn't fix the whiplash problem (that'd require redisigning the gutter or adding more mechanisms), we just gave the pucks enough time so it doesn't matter.
3. Turns out the slide wasn't fully pushed into the third pane, so also here - add screws through all 3 panes.

# General conclusions
1. Calibration isn't simple. Working a lot on making an easy calibration sequence pays off, both pyschologically and also in real time saved, since the calibration never works first time anyways. Didn't expect that process to turn into a full mini-project.
2. Mocks and tests: If I'd known this project would take >200h, I'd spend more time fleshing out the design, tests and mocks for the system. I thought the whole thing would take 100h tops, so after building intial mocks I started slacking off. Where did I pay the price for that? Possibly the mental load of not being sure if I might have random bugs show up at different places, bringing me to where I am now, having to use a pomodoro timer to get myself to even just write about the project (before I've even finished with it).
3. Psychological hump of mechanics: as a programmer working on a mechanical project, often I felt stuck when in reality I just needed to be willing to change modes to a mechanic or know to put the project on hold till a mechanic could help me screw in something or drill something for me. It's one thing to context switch between repos you're working on, but to change engineering hats to one you're unfamiliar with is especially unintuitive.
4. Building jigs is good: When I started testing out the actual movements of the robot, Oron helped me design and assemble a jig to screw the robot to approximate the setup in the final exhibit while staying in the office. 4.5h That let me test at my desk instead of sitting in front of the exhibit uncomfortably while mechanics walk by me, feeling like a lost child.  
5. Psychological load: Unsurprisingly, the conclusions I arrived at all relate to the mental load of making the project, not the specific techniques use for assembly or the code structure, or if so - only in regards to how it makes the engineer more comfortable to do his work. When you're doing a project that takes over 50h, even sitting most of the time without a normal desk will be what can break you from finishing. The fact that I'm having a hard time doing my final debugging is all done in front of the exhibit and not my jig is a testament to that.
6. Projects are just many small chunks: While there were a few large chunks of time wasted, namely - 
    1. manually trying to calibrate for ~7h instead of spending more time on making the calibration itself more convinient, though you can't really know how bad it'll be in advance so I'll give myself a pass on that one. 
    2. spending ~8h on making an async restart when you're not even sure if it works, and even so it's mostly a nice to have. I think the fact that I didn't set a limit on how long to spend on this &/| didn't see it through on the other hand is what made it sour, not necessarily the big chunk of time. 
Other than that, there were multiple >5h sprints that were well spent - soldering stuff, reading code, building jigs, etc.
In the end, I can't point to one thing that made the project taxing to work on. I can only point to momentum and how easy it is to work on it, and how defined my task is. So in conclusion: when working on a big project:
1. Keep momentum running, even with small side tasks.
2. Make the project easy for you to work on - make jigs, pcbs, helper code, sometimes spend more time on code when you see that manually doing the works is taxing. Often it'll pay off in absolute time as well.
3. make the tasks defined, if not it outcome then at least in time.
4. Keep others in the loop, know to ask for help.

assuming all this is done, big projects hopefully become a part of life and not a daily struggle.
