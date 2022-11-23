codingmonkey | 2017-01-02 01:04:04 UTC | #1

Hi folks! Today i'm try to add cup of flexibility to editor in case of manipulation objects of scene.
I'm adds some blender basic shortkeys
key R - rotate
key G - grab(move)
key S - scale

 
these keys also have an circular-switching between local/global space on double press

also i'm adds, some restore  

alt + R - to reset object rotation
alt + G - to reset object position to (0,0,0)
alt + S - to reset object scale to (1,1,1)

there is short video example:
[video]http://youtu.be/Q66eAFIRZvw[/video]

but I have this strange sound when i press the alt+key
is editor issue or system?

add:
key F - focus on selected object(s) center. double clicks on F-key move the camera more closer
alt + F - move camera away from focused on selected object(s) center. double clicks on F-key move the camera more far away

still have this noised sound like default system "beep" :frowning: 
I guess that this sound plays then the usual window in win7/8 not have a menu or something like this.

-------------------------

cadaver | 2017-01-02 01:04:05 UTC | #2

The sound is played by the operating system. Actually it doesn't seem to make a difference whether the window procedure in SDL_windowsevents.c returns TRUE or FALSE for the alt-keypress (ie. whether to pass on the key event to the default handler)

So for now I'd suggest to just ignore the sound, or tweak your system sound preferences so that the alert bell is not played.

-------------------------

codingmonkey | 2017-01-02 01:04:05 UTC | #3

> just ignore the sound
 :smiley:

>or tweak your system sound preferences so that the alert bell is not played.
yes, but maybe for urho editor window may create some faked accelerator(keys) to avoid this? I guess that this is name for this thing.

I'm update my Urho fork and create brunch for this shortkeys if someone wants to play with it
[github.com/MonkeyFirst/Urho3D/tree/shortkeys](https://github.com/MonkeyFirst/Urho3D/tree/shortkeys)

-------------------------

cadaver | 2017-01-02 01:04:05 UTC | #4

The window message in question was WM_SYSCOMMAND, SC_KEYMENU subcommand. When it is "handled" by SDL the sounds will no longer appear. This change is now committed to the master branch.

-------------------------

codingmonkey | 2017-01-02 01:04:06 UTC | #5

Thanks, cadaver )

-------------------------

