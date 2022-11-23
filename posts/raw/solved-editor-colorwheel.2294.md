TheComet | 2017-01-02 01:14:33 UTC | #1

I see the option under "edit->color wheel" but it doesn't do anything. Am I missing something? How do I edit colour values using the color wheel in the editor?

-------------------------

1vanK | 2017-01-02 01:14:33 UTC | #2

Example of using:
1) Create light source
2) Select light component
3) Alt+w -> Light color

-------------------------

TheComet | 2017-01-02 01:14:33 UTC | #3

I can't get it to work...

1) Create light source
2) Click on light source
3) alt+w -> light color
4) context menu disappears, nothing else happens.

Is this the intended behaviour?

-------------------------

pqftgs | 2017-01-02 01:14:33 UTC | #4

On my laptop the color wheel gets created partially offscreen.  With less resolution it's not visible at all.

-------------------------

1vanK | 2017-01-02 01:14:33 UTC | #5

Data\UI\EditorColorWheel.xml
[code]
	<attribute name="Position" value="1026 364" />[/code]

-------------------------

codingmonkey | 2017-01-02 01:14:33 UTC | #6

>Is this the intended behaviour?
of course not. 
I yesterday compile last master, and check the colorWheel a few minutes ago and it's works fine, I mean as expected. 
what build of engine you are use? own custom or what? actually I do not know that may produce this issue. try to change hot keys mode to: blender mode and try use it again

-------------------------

cadaver | 2017-01-02 01:14:33 UTC | #7

Just removed the hardcoded position from colorwheel dialog (master branch), and added centering on creation. It was probably hardcoded for full HD resolution.

-------------------------

TheComet | 2017-01-02 01:14:33 UTC | #8

[quote="1vanK"]Data\UI\EditorColorWheel.xml
[code]
	<attribute name="Position" value="1026 364" />[/code][/quote]
Lol yeah, that would do it, I have a 1024x768 screen  :smiley:

-------------------------

