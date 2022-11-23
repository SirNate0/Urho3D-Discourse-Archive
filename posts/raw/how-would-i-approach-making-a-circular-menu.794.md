setzer22 | 2017-01-02 01:02:55 UTC | #1

I want to make a circular menu for my game. The behaviour should be as follows

[ul]
- When i click and hold in a point on the screen the menu will appear at that point. The menu consists of a donut-like shape with slices corresponding to particular buttons. 
- After that, dragging the mouse outwards in the direction of a button should highlight that particular button.
- In the end, after releasing the mouse the menu should become invisible again, and if a button was highlighted that counts as a button press for that particular button.
[/ul]

I have a pretty clear idea of how would I implement this with a basic Draw API, but no clue on how could I achieve this in Urho. Will subclass UIElement be of any help? Does it provide methods for drawing custom shapes? I can't see any on the documentation. 

Maybe I should better go off with avoiding UI and creating a component instead? What's the best way to draw a texture on the screen that way? Can I combine Urho3D and Urho2D classes to do so? I feels wrong to not use the UI for an UI component but I also feel like the UI API is not going to be of much help with this.

So basically I've thought of those two alternatives. Which would be better? Is any other alternative I might be missing?

Thank you!

-------------------------

devrich | 2017-01-02 01:02:56 UTC | #2

[quote="setzer22"]I want to make a circular menu for my game. The behaviour should be as follows

[ul]
- When i click and hold in a point on the screen the menu will appear at that point. The menu consists of a donut-like shape with slices corresponding to particular buttons. 
- After that, dragging the mouse outwards in the direction of a button should highlight that particular button.
- In the end, after releasing the mouse the menu should become invisible again, and if a button was highlighted that counts as a button press for that particular button.
[/ul][/quote]

I totaly love that design!! :smiley:

In pseudo format I can give you some idea on what direction to take with it:

1: in the menu icon's onMouseDown code ( or the scene's onMouseDown code if you prefer ) when the user holds down the mouse or a finger on the screen then start a global count down timer function to regularly count down from a "delay time" to zero
2: when that count down timer function reaches <= 0 then stop calling the timer function and set the [u][i]count-down-start variable back to the max-count-down variable[/i][/u] then call the function to open the menu 
2-B: put a line in the onMouseUp code to stop the count down timer and to set it's [u][i]count-down-start variable back to the max-count-down[/i][/u] variable ( reseting the count down for next time )
3: now that the menu has come up, nothing will automatically "hover or highlight" until the user moves while holding down on the menu which will naturally call the onMouseMove code ( you shouldn't have to do anything in onMouseMove )
4: In the objects of the menu; set each one to be their own independant object.  Now you can set each one to have their own independant sizes and shapes ( they can be anything even oddly looking shapes instead of pie pieces ) fonts and color schemes.
5: when the user "moves" over on top of one of the pie pieces then you have that object's onMouseOver code change the look and feel of the menu item to show that it is hovered over ( maybe make it wiggle slowly for effect )
6: when the user "move OFF" from one of the pie pieces then you have that object's onMouseIOut code change the look and feel of the menu item back to normal.

( 5: and 6: allow the menu items to act independantly based on their code and also allow for multiple menu choices to be selectable at the same time so be careful about menu item placement for mobile 'tap' operations unless you want to give the user the option of selecting more than one menu item at the same time )

7: when the user "lets go" then the object where their finger/mouse was will naturally call it's onMouseUp code which will let you put in there the animations/sounds to show that the user has selected that particular menu option and then to also start a timer that will make the menu disappear ( or return to it's icon'd posiiton ) after the "selected" animation completes

Sorry for the long post but hopefully something in all that helps :slight_smile:

-------------------------

jmiller | 2017-01-02 01:02:56 UTC | #3

I love radial menus and consider them one of the greatest UI constructs ever.  They make great multi-level menus too.

I'm no Urho UI buff yet, but I think there must be a few ways.

[url=http://urho3d.github.io/documentation/1.32/class_urho3_d_1_1_border_image.html]BorderImage[/url], [url=http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_sprite.html]Sprite[/url], [url=http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_button.html]Button[/url] ..are some that can hold textures so that might be something to play with.

[url=http://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_u_i_element.html]UIElement[/url] already offers:
OnHover, OnClickBegin, OnClickEnd, OnDrag, etc.

of course you can create elements dynamically, or preconstruct complete UI trees and load them (Editor has examples of this) with e.g. LoadXML, hook to your handlers, and selectively set visible/enabled.

food for thought?

-------------------------

