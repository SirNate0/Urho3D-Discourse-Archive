orefkov | 2017-10-16 11:52:03 UTC | #1

I work on some mobile game (Urho3DPlayer + AngelScript) and test it on device (GLES), and computer DX9 and OGL.
In DX9 version no problem. On GLES and OGL I have glitches. Some screenshots.
This is screen from mobile, in 50% the game start as shown, and that result is good for me. Look at "stone" material on "portal"
![Mobile-2|281x500](upload://k4rIgVLumO9sb2SX7XvSnAUTDlw.jpg)
But in ~50% runs - game start as
![Mobile-1|281x500](upload://NuFBbDOTWQjJHFxocRb5oiEM16.jpg)
Stone above portal is dark.

On computer in DX9 game always start as shown:
![Scene DX9|279x500](upload://oYs2AE9xp4RugxSeWgZEWWvQ9zI.png)
In OGL game always start as
![Scene OpenGL|280x500](upload://pF4v1AprP5aQiurzh3WHGdIotWu.png)
but if I move camera down, at some moment picture changed to
![Scene OpenGL-down|279x500](upload://bCbGanMqjsza4SgZ4p6CzPs3oVN.png)

Also on mobile if I add more models, sometimes portal looks like an exploding:
![Mobile-3|281x500](upload://eWvOrdR3oxkaj9byHibOWalfcAm.jpg)
but sometimes all good.

For portal I use DiffNormal technique, other model simple Diff techique.
What could be the problem?

-------------------------

JTippetts | 2017-10-16 14:44:50 UTC | #2

Are you sure you are actually supplying tangents for the portal? Sometimes you can get those kinds of glitches if a shader expects some bit of data, such as tangents, but that data isn't provided. In which case, it just uses whatever old bit of data is there. Sorta like using an uninitialized array. Double check that your portal model has been exported with tangents, since it is using the DiffNormal technique.

-------------------------

orefkov | 2017-10-16 14:47:45 UTC | #3

Many thanks. Really, on export from Blender, forgot toggle "Tangent" check box. Early exported with tangents, and all work fine. At some moment I was change portal's model and export without tangent.

-------------------------

