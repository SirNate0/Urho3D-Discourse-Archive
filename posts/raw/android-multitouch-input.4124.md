simonsch | 2018-03-26 14:24:06 UTC | #1

Hello,
another day another issue for me i can't resolve without your help.

I am trying to process touch input from my SDLActivity on android in urho for controlling camera movement. So far this is working as expected.

    SubscribeToEvent(E_TOUCHMOVE, URHO3D_HANDLER(RenderImpl, HandleTouchMove));

I used this to get touch callbacks, which works fine. In the function 'HandleTouchMove' then i proof

    Input *input = GetSubsystem<Input>();
    if (input->GetNumTouches() == 1) {
       ... One finger ....
    } else if(input->GetNumTouches() == 2){
       ... Two finger ....
    }
After logging what is happening, GetNumTouches returns 1 after the first touch, the double touch returns 2. Now the issues, the event seems to be firing on and on resulting on GetNumTouches being 1 even when no finger touches the display. 

I also proofed it on the Android Java part there is everything correct in finger recognition. Anyone knows something about this behaviour?

EDIT: Interesting, when i use the window button from the bottom bar. And then bring back the app to full screen i get a normal one finger touch event again. But again just one then the issue occurs again.

-------------------------

simonsch | 2018-03-27 09:12:53 UTC | #2

Solved it myself urho3d code was all fine, the problem was related to the SDLActivity where i used my standard onTouch Method, instead creating proper binding via the specific SDLSurface.

-------------------------

