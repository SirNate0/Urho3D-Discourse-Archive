Mike | 2017-01-02 00:59:07 UTC | #1

I think we could use Billboards to easily instantiate 'cutouts' (2D planes used to fake 3D by always facing camera position).

For cutouts it's better to face camera position [code]node->LookAt(cameraNode->GetPosition());[/code] than camera axes (so that the cutout doesn't spin when camera rotates).

So adding 'faceCameraPosition' similar to faceCameraAxes would allow full control over the behavior of the Billboards.

-------------------------

cadaver | 2017-01-02 00:59:07 UTC | #2

It's likely better that we ditch the face camera boolean and the axes parameter, and move to an enum for the facing modes. In that case it would be easy to add.

However, what is the behavior you want when the camera flies over these objects? A straight LookAt() will cause the objects to tilt. Are you looking for rotation about the Y-axis (yaw) only?

-------------------------

Mike | 2017-01-02 00:59:07 UTC | #3

Yes, straight and only yaw rotation. To prevent from seeing a flat line when above, user can set a fixed incline (for example at 45?) so that it looks good from any angle.

-------------------------

Mike | 2017-01-02 00:59:07 UTC | #4

Many thanks for commit, this is really powerful and versatile. :smiley:

-------------------------

thebluefish | 2017-01-02 00:59:10 UTC | #5

This begs a question: What if the user wants a billboard that is fixed on some other axis? I can think of other instances where having some other orientation would be preferred. One such example would be a space sim, where there's no real specific orientation that is "up".

First, I think it would be better to use local transforms instead of world transform. That way if I position the billboard at a 30 degree angle on the X-axis, it still won't be limited.

Secondly, I think the API here should match closer to what Bullet Physics does for their 2D API:
[code]body->setLinearFactor(btVector3(1,0,1));
body->setAngularFactor(btVector3(0,1,0));[/code]

The billboard API could be something like:
[code]
billboard->setAngularLimit(Vector3(1,1,1)); // Able to freely rotate
billboard->setAngularLimit(0,1,0); // Rotate by the Y-axis only
[/code]

-------------------------

cadaver | 2017-01-02 00:59:11 UTC | #6

It had that API for a while, but that led into multiple attributes for the facing. One way to do it would be to have an enum specifying the facing mode (none, rotate, lookat) and a vector parameter for the axes. 

I'm not likely going to change the code anymore, but if you want to try it out in a pull request, that's fine.

-------------------------

