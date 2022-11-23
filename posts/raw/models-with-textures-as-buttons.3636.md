stark7 | 2017-10-05 06:54:52 UTC | #1

I need to create a UI with nodes and models with textures as buttons, this is because I want access to the Actions that the nodes benefit from as well as materials - for this my plan was to create a ray picking component and keep track of time and calls "RaycastEnd" on my target to perform a button action of some kind - just like the UI Button is doing it right now.

Is there already somewhere a component that will allow me to make nodes/models behave as buttons?


EDIT: 
I am currently following this pattern until something else happens :D:
https://discourse.urho3d.io/t/detect-mouse-touch-event-in-separate-objects/1278

-------------------------

stark7 | 2017-10-05 15:06:43 UTC | #2

Follow-up question:

I am adding a child node with a model to my camera Node only I can't seem to be able to see it rendered. I tried various positions and rotations with no results. Are the camera children nodes ignored when rendering?

EDIT: Looks like this might be a monologue thread:

The camera component seems to be outside the scene and it's children are not rendered because there is no octree outside the scene:
https://discourse.urho3d.io/t/my-first-experience-and-problems-with-urho3d/838/10

-------------------------

