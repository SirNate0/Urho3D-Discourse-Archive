mightymarcus | 2017-01-02 01:09:51 UTC | #1

I'm playing with the engine to get more into it, and I wanted to start with something really simple (hehe), a 3D background scrolling vertically with a top down camera and a 3D Object flying over the background like in a vertical scrolling shooter. Now it doesn't fit well in the concept of a vertical scroller (and looks horrible) when the 3D Object is rendered in 3D perspective, so I want the 3D Object to be rendered with an orthographic view (or as would the camera always be on top of the ship but then I would need a camera for each enemy, projectile etc. too i guess).

So I came up with the idea to mix orthographic with perspective view. The orthographic camera should only view the game objects like ships, rockets, power ups maybe off the screen and should render it then on the screen where the game objects should be. Maybe to a render target texture that makes up the screen (a transparent texture).

Now I really don't know how to start. Would be nice if someone could point me in the right direction.

UPDATE:

Another idea is to have both cameras on the same positions, one excludes the game objects and the other excludes the background. They have both the same viewport, the viewport that gets the game objects should be transparent. Is this possible?

UPDATE:

Now I tried with viewmask settings and RenderPathCommand, and after all I managed to have the orthographic camera output in front of the perspective camera. Only thing is: the objects are on the wrong positions.

And I even don't no what exactly I did, actually I wanted to change the clear color of viewport 2 to transparent, but I didn't knew how.

renderer->SetViewport(1, orthoViewport);
RenderPath* orthoPath = orthoViewport->GetRenderPath();
orthoPath->SetCommand(0, RenderPathCommand()); <---- but this worked  :smiling_imp:

-------------------------

