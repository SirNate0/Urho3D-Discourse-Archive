rifai | 2017-01-02 01:00:35 UTC | #1

hi,
I'm trying to make a loading screen. 
I load "loading screen" UI file and make it visible, load scene from XML, & hide "loading screen". 
But, I have a problem. UI didnt show up until scene is completely loaded. 

I dont use loadAsync. Do I have to use loadAsync?  I dont need loading progress, I just want to show static loading screen.

-------------------------

gunnar.kriik | 2017-01-02 01:00:35 UTC | #2

How about you create the loading UI first (without loading rest of the scene), and then wait a few frame updates, and then load the rest of the Scene? Then you could also use loadAsync if you wish to animate the loading screen, but I have not tested this myself, but it should work in theory.  :slight_smile:

-------------------------

thebluefish | 2017-01-02 01:00:35 UTC | #3

If you don't use loadasync, it's going to block until it's finished loading. Meaning it's not going to draw that frame, you need to have drawn something the previous frame. On the other hand you can use loadAsync, and there should be an event for when the async load has finished. You can hide the static load screen by listening to this event. Whether you want progress or not is up to you, but you can do anything during this load time that you want.

-------------------------

Mike | 2017-01-02 01:00:35 UTC | #4

There's a sample here: [url]http://discourse.urho3d.io/t/simple-splash-screen/127/5%20screen#p652[/url].

-------------------------

