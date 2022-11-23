Andre_B | 2017-01-05 15:12:51 UTC | #1

Hi im working on a IOs graphical application that has a urho graphical window positioned at the middle of the screen and a scroll view with some buttons beneath it.

Now Urho stops the Update loop when the app looses input focus. 
This is all well and good except i don't want it to loose focus when sliding a simple scroll view.

Only after the sliding operation ends that Urho resumes its update loop. Press and holding also causes urho to stop doing update loops.

How do i mantain input focus while my slide view is operational?

EDIT: Anyone out there?

-------------------------

hdunderscore | 2017-01-06 10:09:29 UTC | #2

You can try SetPausedMinimized(false) 

https://urho3d.github.io/documentation/1.3/class_urho3_d_1_1_engine.html#ab3fc430d9c0e4fdbfefff85ae66eb65c

-------------------------

Andre_B | 2017-01-06 10:09:50 UTC | #3

The problem i was having was related to having Input.Enabled = false before which made it ignore my SetPausedMinimized(false).

But thank you anyways :slight_smile:

-------------------------

