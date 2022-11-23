Sir_Nate | 2017-01-02 01:09:40 UTC | #1

I've added some stuff to thebluefish's integration of libRocket, such as (basic) input support -- it's not complete, not all keys are supported, e.g., but you can now type in elements and click buttons, etc. Basic event support has been added (libRocket -> Urho3D), but a lot of work still needs to be done.

You can find it at [url]https://github.com/SirNate0/libRocket-Urho3D[/url], but I don't promise to maintain any backwards compatibility as I update it :wink:. You should also note that I've focused on the 2D document, not the 3D one, so there may be (serious) bugs in that one. I may eventually try for a full integration to Urho, like a separate UI subsystem, but that remains to be seen...

-------------------------

thebluefish | 2017-01-02 01:09:42 UTC | #2

Very nice :slight_smile:

Though it's usually important to adhere to existing licenses, to ensure that your code isn't blatantly breaking them. However I've long abandoned this project, so I'm not going to make a fuss over it. Don't let my bad habits get you in trouble, and just make sure to keep an eye on that sort of stuff in the future so that you don't piss someone off who [b]does[/b] care  :laughing:

-------------------------

rasteron | 2017-01-02 01:09:42 UTC | #3

This looks interesting Sir Nate but having to try your updated build from bluefish, I got it passed CMake with the

 [code]-URHO3D_ROCKET=1[/code] 

option, but I'm getting compile errors.

-------------------------

