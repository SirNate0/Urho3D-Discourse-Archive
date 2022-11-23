att | 2017-01-02 00:57:56 UTC | #1

hello, 
I use the Editor to create game scene, but I found it is not easy to set up position for game object in perspective projection.
Is it support orthographic projection?

thank you.

-------------------------

weitjong | 2017-01-02 00:57:56 UTC | #2

Welcome to our forum.

The Editor currently does not support or work in orthographic mode although the camera class itself from Urho3D library does support orthographic projection. This may not result in exactly what you want, you can try to pop out the console by pressing F1 and then on the console command line keying this command: camera.orthographic=true

-------------------------

cadaver | 2017-01-02 00:57:57 UTC | #3

I believe Chris has been experimenting with orthographic camera in the editor, the problem is that the movement no longer works as expected (as movement in Z-direction in orthographic mode only adjusts what is being clipped and what not, not the actual viewing position) and may be unintuitive.

Though I checked that Unity does the exact same thing, so the easy way would be just to add a checkbox for ortho mode and let users struggle with the controls :wink:

-------------------------

friesencr | 2017-01-02 00:57:57 UTC | #4

Yup I tried orthographic again after seeing this post.  

I used the camera 'zoom' to simulate moving forwards and back when the camera is in orthographic mode and it worked pretty well.  I need to figure out some better maths for setting the value so that it has a more linear feel.  I am kind of thinking having 'wasd' still change the position but then the mousewheel can manipulate the zoom instead on both projections.  Having some zoom is better then naught from my experience.

Any opinions?

-------------------------

cadaver | 2017-01-02 00:57:57 UTC | #5

The orthographic window size is quite an important parameter. If the size was adjustable both via zoom controls and via editor settings LineEdit, it'd be superb.

I don't know how ortho mode should interact with multiple viewports, should it be possible to enable per viewport?

-------------------------

friesencr | 2017-01-02 00:57:58 UTC | #6

I could see myself perspective in one view to get the feel of a level and then using perspective top down to functionally place the items.  This wouldn't be my default workflow but situational.  The way i have been testing is to follow blender and using NUMPAD5 for a toggle.  Its pretty easy to make something to make something per viewport by shoving it in that wierd "ViewportContext" class that i wrote.  The biggest issue, like always, goes to the interface and ux.

I had initially writen every viewport to have its own small menu at the top write corner of every viewport that became visible when you hovered near it.  It had a drop down for orthographic and set the camera to front/back/side etc...  That would be a good place for zoom.  I did't like the menu very much so it didn't make the cut.  I will try it again.  Maybe I ate some bad cheese the day I worked on the menu.

-------------------------

friesencr | 2017-01-02 00:58:01 UTC | #7

Ok.  The skimpy featured version merged into master now.  NUMPAD5 to toggle.  There is some bits that change the orthographic size based on how far the thing in the middle of the screen is from the camera.  Its kind of cheesy to assume this for the user, but it was a far more bizarre experience without it.  I don't know if the automatic orthographic size will work well for everyone, so please test and give me feedback.

Thanks.

-------------------------

