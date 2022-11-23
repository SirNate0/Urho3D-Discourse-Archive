yushli | 2017-01-02 01:06:33 UTC | #1

What is the best way to determine whether a 2d/3d object is clicked or touched, and receive the corresponding events from this object? e.g., how to support writing code as follows:

var obj1 = createObject();
obj1.addEventListener("mousedown", function(){...});

-------------------------

cadaver | 2017-01-02 01:06:33 UTC | #2

The typical pattern is that you do a raycast in top-level application code as a response to the mouseclick event, and if the raycast hits an object, call some function in the object's component(s) to handle the click. The top-level application code should also verify first that the mouse cursor isn't over a UI element.

You can also do the handling with events by using the following pattern, similar to how a node's physics collisions are handled:

- The component or script object which is supposed to handle the click subscribes to a custom event with its own node as the specific sender (ie. SubscribeToEvent(node, "MouseClicked", "HandleMouseClicked") in pseudocode)
- When the raycast hits a certain object, the top-level application code makes the object's node send the "MouseClicked" event.
- The component handles the event.

For a raycasting example, see e.g. 08_Decals sample.

-------------------------

