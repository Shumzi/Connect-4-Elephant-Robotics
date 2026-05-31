# robot coordinates
the `coords.json` contains both cartesian & angles, used for calibration. in the final run of the game, we'll use `angles.json` with all the linear transformations baked in, to make sure the system is deterministic (since IK isn't).

for linear movements, we'll save all the values as a list of coords/angles in the json. that way list\[x\] == linear movement #x out of y (y depends on how fine you want your movement).

see scripts/