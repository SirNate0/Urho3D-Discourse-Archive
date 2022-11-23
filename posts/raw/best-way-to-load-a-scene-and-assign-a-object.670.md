vivienneanthony | 2017-01-02 01:02:00 UTC | #1

Hello,
It's been a while but I'm getting back into the coding. Basically, what I was thinking of doing, is modifying my code to add object component. I have to take a full scan of a scene node and check for the existent of collion and rigidbody component. Creating if none exist.  Additionally, assign a object component on all scene nodes except lights and zone.

Does that sound accurate?
[code]
   if (extension != ".xml")
                {
                    scene_ -> Load(dataFile);
                }
                else
                {
                    scene_ ->LoadXML(dataFile);
                }[/code]

So, I possibly have to stick the code or function right after this.

Vivienne

-------------------------

