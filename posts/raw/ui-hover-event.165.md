Xero | 2017-01-02 00:58:33 UTC | #1

Do hover events exist in urho, ie. in a user interface, if a player hovers over a button text would appear below it?

-------------------------

cadaver | 2017-01-02 00:58:33 UTC | #2

There aren't hover begin/end events as such, so for checking if an element is being hovered, you have to poll its hover state by using the function UIElement::IsHovering().

Then there is the ToolTip UI element which will show automatically after a configured time. It's used in the editor toolbars. The ToolTip itself doesn't render anything, so you need to add the content you want to display (image, text etc.) as a child UI element to it.

-------------------------

Xero | 2017-01-02 00:58:33 UTC | #3

perfect! Forgot about ToolTip UI element.

-------------------------

cadaver | 2017-01-02 00:58:33 UTC | #4

Now there are also actual hover events :slight_smile: Though haven't tested them much.

-------------------------

friesencr | 2017-01-02 00:58:33 UTC | #5

When i was looking at the drag cancel stuff I noticed there wasn't a drag start event.  Presently I am checking for a ui.dragElement.

-------------------------

cadaver | 2017-01-02 00:58:33 UTC | #6

There should be (E_DRAGBEGIN).

-------------------------

