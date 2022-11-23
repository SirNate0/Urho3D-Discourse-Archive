elemusic | 2017-01-02 01:02:59 UTC | #1

hi,i'm new to Urho3D,before that i use unity3d.

right now i want to rewrite some of my game from unity3d to Urho3D.

in unity3d i use two camera,one for 2D with clear flag 'depth only',and one for 3d just normal.

well in Urho3D i don't know how to make a viewport like this.i have seen 09_MultipleViewports example.
it shows me how to create two viewport,but i can't find some function how to set the 2D,say the second viewport with transparent.
when rendering two viewport,the small one always render a rectangle area,and the empty area is always black.
i need the black area to be transparent just like unity3d did,so what shall i do?

-------------------------

codingmonkey | 2017-01-02 01:02:59 UTC | #2

I think this problem has been discussed 
here: [topic756.html](http://discourse.urho3d.io/t/how-to-layer-scenes/740/1)

-------------------------

elemusic | 2017-01-02 01:02:59 UTC | #3

thank you,that works. :smiley:

-------------------------

