rusty | 2017-09-10 11:27:37 UTC | #1

I have created a simple GUI in XML with a slider. It displays "as expected" however, it won't drag the slider control. No matter what I do, the slider or even the scroll bar doesn't move. Even after fiddling about with the range attribute.

I haven't seen any C++ examples of Slider/scrollbar usage and I was wondering if perhaps I have to subscribe to events before the slider or scrollbar control will respond. Do I have have to manually intercept drag start and end events and set the scrollbar value myself?

If the control should move by itself without registering for events; what could the cause be?

-------------------------

weitjong | 2017-09-10 04:40:29 UTC | #2

You probably didn't set the range properly. There are samples using Slider and Scrollbar although indirectly (ListView uses ScrollView whcih in turn uses ScrollBar).

-------------------------

rusty | 2017-09-10 13:03:42 UTC | #3

The range was set properly - the control was not even gaining focus when the mouse moved over it.

I have since last evening, after sleeping on the problem a little, fixed the cause. The code is for a demo for my book, and in the base class for my application, I was somehow grabbing the grabbing the mouse. It was code left over from when  I copied over one of the samples to get my own basic application working.

-------------------------

