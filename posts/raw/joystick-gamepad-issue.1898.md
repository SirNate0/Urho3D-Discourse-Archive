G392 | 2017-01-02 01:11:20 UTC | #1

I added a few lines to the PhysicsStressTest sample to be able to control the camera with a game controller and made a few [b]for[/b] loops 
to test what value each Button/Axis had, as I noticed they didn't have the same as those I could see in jstest-gtk ([github.com/Grumbel/jstest-gtk](https://github.com/Grumbel/jstest-gtk)) 
(Which isn't the problem). The controller I used is a sixaxis PS3 controller which works just fine in other games and as I mentionned works with jstest.
I am testing for input with: 
[code]GetSubsystem<Input>()->GetJoystickByIndex(0)->GetButtonDown(i);
GetSubsystem<Input>()->GetJoystickByIndex(0)->GetAxisPosition(i);[/code]
My problem now; when I wanted to use the (R2) and (L2) triggers to make the camera move up and down while controlling the speed at which it did,
 :confused:  I found out two things: 
    ? Those two don't have a 'Button' in Urho3D.
    ? Their 'AxisPosition' values either are 1 or 0.
I understand why the axes of most buttons would be ignored by the game engine, but surely it isn't normal that those two work that way currently?
:blush: Or could I be doing something wrong? I observed this with the yaourt urho3d and urho3d-git builds (Linux Manjaro).

-------------------------

Modanung | 2017-02-11 12:26:55 UTC | #2

Here's are all the SIXAXIS buttons mapped (as over bluetooth) to an enum:
```
enum SixaxisButton {  SB_SELECT, SB_LEFTSTICK, SB_RIGHTSTICK, SB_START,
                      SB_DPAD_UP, SB_DPAD_RIGHT, SB_DPAD_DOWN, SB_DPAD_LEFT,
                      SB_L2, SB_R2, SB_L1, SB_R1,
                      SB_TRIANGLE, SB_CIRCLE, SB_CROSS, SB_SQUARE,
                      SB_PS };
```
Detecting the triggers (L2/R2) works fine here with GetButtonDown. In [url=https://luckeyproductions.itch.io/hexon]heXon[/url] these trigger the ejection seat.
I'm running Xunbuntu btw.

-------------------------

Modanung | 2017-01-02 01:11:27 UTC | #3

Then again... for me they do have the same values as shown in [b]jstest-gtk[/b]. Do they say Sony and is the PS3 logo visible on the central button? Did you change the mapping?

-------------------------

G392 | 2017-01-02 01:11:27 UTC | #4

Yup, it's an official PS3 controller with the sony/playstation logos (Model: CECHZC2U)
and is seen as such in lsusb and jstest-gtk.  
I didn't change any mapping. I only read values. 
lsusb:
[color=#666666]Bus 005 Device 005: ID 054c:0268 Sony Corp. Batoh Device / PlayStation 3 Controller[/color]
jstest-gtk:
[color=#666666]Sony PLAYSTATION(R)3 Controller 
Device: /dev/input/js0
Axes:27
Buttons:19[/color]
[code]Button		In Urho3D 		In jstest-gtk

     x			0				14
     ?			1				13
     ?			2				15
     ?			3				12
Select			4				0
    PS			5				16
 Start			6				3
    L3			7				1
    R3			8				2
    L1			9				10
    R1			10			  11
    UP			11			  4
  DOWN			12			  6
  LEFT			13			  7
 RIGHT			14			  5


(Axis)

    Axis	In Urho3D		In jstest-gtk

 left(x)		0				 0
 left(y)		1				 1
right(x)		2				 2
right(y)		3				 3
      L2 	  4* 			  12
      R2		5*			   13

*Can only have 0 or 1 as value.[/code] I've confirmed this on two computers, with two PS3 controllers. I've also tested Urho3D with a PS4 controller and saw that there was no problem; every button, hat and axis worked as it should, including the triggers.  :neutral_face:
[quote]Then again... for me they do have the same values as shown in jstest-gtk.[/quote]
I wonder if my problem could be that I'm running this on Arch-based Linux Manjaro, instead of Debian/Ubuntu?

-------------------------

Modanung | 2017-01-02 01:11:28 UTC | #5

Right, I just realized I use the controllers over bluetooth most of the time.
When I play over usb the mapping matches yours. In jstest-gtk everything still looks the same as over bluetooth though.
Which comes down to a: Yea, same problem here. Maybe post an issue on this? Might be SDL related.

-------------------------

