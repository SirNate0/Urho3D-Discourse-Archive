miz | 2017-01-02 01:14:12 UTC | #1

When I build a game for the raspberry pi, if you click around in the game the game doesn't 'block' these clicks. i.e you end up clicking on loads of stuff on the desktop and opening things while playing the game. To get around this I launch an empty Python Tkinter application behind the game to block the clicks. Although it works I feel like there has to be a better way to do this.

Another (maybe related issue) is when booting the game if you move the mouse Raspbians cursor image gets caught above the game grapics so it looks like there are 2 cursors (the Urho cursor works fine)

Anyone know how I could get around the problems?

-------------------------

miz | 2017-01-02 01:14:16 UTC | #2

If anyone is following this I am currently investigating accessing x11 stuff from c++ and seeing if I can disable OS input that way.

-------------------------

Modanung | 2017-01-02 01:14:16 UTC | #3

[quote="miz"]If anyone is following this...[/quote]
Will definitely keep this topic in mind. Please, do share your solution if you find one.

-------------------------

miz | 2017-01-02 01:14:17 UTC | #4

One option I've found is something called xinput - it's a command line tool that you can use to disable inputs so you can make a bash script that will use xinput to disable the inputs and open the game and then either call another bash script upon exiting the game to re-enable inputs or have some sort of thing running that checks whether the game process is still running and if it isn't enables the inputs again.


Also xinput is source code is available online and written in C so I'm also digging around to see what it's actually doing to see if I can do something similar without needing to use xinput i.e. do what xinput would be doing but from the game binary.

-------------------------

