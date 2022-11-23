brokensoul | 2020-04-23 00:46:53 UTC | #1

I launched a empty Urho3d app, with just a black window, and it is using 100mb (more or less) of ram, i'm just curious why.

-------------------------

SirNate0 | 2020-04-23 03:13:04 UTC | #2

Loading the executable itself into memory maybe?

-------------------------

George1 | 2020-04-23 06:45:30 UTC | #3

It's nothing to worry about.  I have run simulation with 60k objects without issues about memory.  The below example use the same amount of ram( e.g about 100mb).  Most Urho examples use the same amount of ram.  It won't grow more!

![4|690x381](upload://g5MIbAYUqzyz1awCKD2vuq39tDW.gif)

-------------------------

brokensoul | 2020-04-23 16:38:08 UTC | #4

Thanks :slightly_smiling_face:

-------------------------

