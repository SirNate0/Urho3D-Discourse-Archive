rogerdv | 2017-01-02 01:02:07 UTC | #1

Is there some way to make UI elements "consume" the click events? I found that when I click in an element, the app receives and uses the click, moving the character to the clicked coords.  The desired behaviour is to process the click in the ui event handler and ignore it.

-------------------------

hdunderscore | 2017-01-02 01:02:08 UTC | #2

Simplest way would be to check on the click event:
[code]if (ui.focusElement is null)
{
   //... do stuff
}[/code]

-------------------------

rogerdv | 2017-01-02 01:02:09 UTC | #3

If I underestand correctly, this means that I have to move a lot of code that handles left/right click on the scene from SceneUpdate event to UIMouseClick event, which is quite annoying, because I would be handling mouse over in a place and clicks in another. Why doesnt UI handles discarding the clicks on UIElements?

-------------------------

