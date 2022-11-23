gabdab | 2017-01-02 01:07:36 UTC | #1

[SOLVED] Something in my code is wrong .
Models work perfectly inside the editor and inside urho3d samples .
Check this image for further infos :
[url]https://cloud.githubusercontent.com/assets/6640045/10447977/814a1aec-7189-11e5-94cb-b96f3845aa0c.jpg[/url]
[WAS]
I am trying to export an animated model which I 
[b]previously succesfully exported 
[/b] with [b]reattiva blender exporter [/b]
but model shows up with no animations inside Urho3D.
What might be the cause ?
I cross tested new model and old animations and problem seems to be in new exported animations , which by the way are identical to the olds (on blender side)..
No errors output from reattiva blender exporter .
Same -no animation- problem exporting as ogre .xml .

-------------------------

codingmonkey | 2017-01-02 01:07:36 UTC | #2

I know one bug of exporter. if you have few >1 armatures on object. 

"It's all about empty *.ani files (or tiny sized) then you try export complex model with several armatures (in my case) "

[github.com/urho3d/Urho3D/issues/576](https://github.com/urho3d/Urho3D/issues/576)

Is it your situation?

-------------------------

gabdab | 2017-01-02 01:07:36 UTC | #3

[SOLVED] check first post
The same as hjmediastudios describes in that issue .
As I said model and animations exported fine last time , I still have the old model which plays well .
This time , same exporting scenario , no animations playing .
A basic human skeleton (2 arms etc.) with an orc model .

-------------------------

