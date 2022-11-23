OMID-313 | 2017-01-02 01:15:29 UTC | #1

Hi all,

I've set up Urho3D on Raspberry Pi 3.
When I want to run a game, I type the following in the terminal:

[code]pi@raspberrypi:~/Urho3D-1.5/build/bin $ ./Urho3DPlayer Data/Scripts/NinjaSnowBar.as[/code]

Then something happens:
During the game, when I'm clicking, it sometime causes the game window to close suddenly.
Then I see that many many terminal windows have been opened, while I was clicking in the game !!!
Also, sometimes the game closes suddenly on click, and I see no window at all, not even the terminal that I had opened!

How can I solve this clicking issue !!?

-------------------------

jmiller | 2017-01-02 01:15:30 UTC | #2

Seems like unexpected behavior to me. :unamused: 

Would there be console (F1) messages coinciding with these? These would normally also be written to the standard urho log (naturally, the last lines would be of particular interest).
Urho3DPlayer -log debug might output something useful as well?

-------------------------

slapin | 2017-01-02 01:15:30 UTC | #3

This looks like recent changes in RPi port, where it works directly with /dev/input*.
I don't know if that is true, though.

-------------------------

weitjong | 2017-01-02 01:15:30 UTC | #4

Our RPI port is designed to run directly from the text mode. The game engine does not expect there is any desktop environment underneath the "layer" where the application runs. Notice that our RPI port also does not interact with the DE in any meaningful way. It just takes the whole screen. You cannot maximize or minimize the app, for example. If you don't know how to configure your RPI to boot straight into text mode then simply kill the X server in a virtual console before running Urho3D app. The frame rate is much better this way anyway.

-------------------------

OMID-313 | 2017-01-02 01:15:31 UTC | #5

[quote="weitjong"]Our RPI port is designed to run directly from the text mode. The game engine does not expect there is any desktop environment underneath the "layer" where the application runs. Notice that our RPI port also does not interact with the DE in any meaningful way. It just takes the whole screen. You cannot maximize or minimize the app, for example. If you don't know how to configure your RPI to boot straight into text mode then simply kill the X server in a virtual console before running Urho3D app. The frame rate is much better this way anyway.[/quote]

Thanks @weitjong for your reply.
I boot into text mode (CLI), and this has solved the problem. So far so good.
Thanks.

-------------------------

