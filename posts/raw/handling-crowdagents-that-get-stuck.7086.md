GodMan | 2021-12-04 01:26:23 UTC | #1

So I have some crowd agents that get stuck sometimes. For example if I jump down a ledge the agents have a path leading up to the ledge and the ground below it. However if I have multiple agents that stand by the ledge that I jumped off of. One of the agents sometimes falls to the ground below. This agent will not move anymore even though he is on the navigation mesh still. 

Just seeking some suggestions on a solution. Maybe re-spawning agents that are stuck? I tried periodically checking the agents velocity to see if he was moving still, and if not re-spawn the agent. This did not work very well though.

-------------------------

GodMan | 2021-12-05 04:37:54 UTC | #2

So I have made some changes to my crowd navigation. I discovered that my player class was always setting the players position for the crowd agents to often. I set this propagation to have a delay, and not update every loop of the game. This seems to make a big improvement.

More changes coming.

-------------------------

