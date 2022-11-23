grokko | 2021-05-26 18:16:05 UTC | #1

Hi,
  I'd like to detect a Mouse button up event and the sdk has little for this. I've looked for the source code in the URHO branch for events like E_MOUSEBUTTONUP but its not button specific...

Grokko

-------------------------

grokko | 2021-05-26 18:51:49 UTC | #2

SOLVED...

You add a event handler to your code SubscribeToEvent(E_MOUSEBUTTONUP...myEvent()). 

Then the  proper Event data sent to myEvent is...
int button = eventData[UIMouseClick::P_BUTTON].GetInt();

all the mouse up buttons are there!

grokko

-------------------------

