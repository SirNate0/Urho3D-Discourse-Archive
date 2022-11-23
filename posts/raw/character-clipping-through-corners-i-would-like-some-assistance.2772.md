TheTophatDemon | 2017-03-18 02:07:13 UTC | #1

EDIT: Disabling gravity seems to eliminate the problem, but only when the character is off the floor.

I have a project set up with a character controller that clips through the corners of the level's geometry.
You can waltz right on through most (interior) corners just by walking into them while turning. If you don't manage to walk through, the character will still jitter around.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/56b828633f9f55ee7f6fb8631387b526c05da101.png" width="690" height="408">
I find this corner here the most blasphemous, so use that for testing.

The level geometry is a static rigid body with a triangle mesh collider, and the character has the angular factor disabled and a cylinder collision shape. My character is driven by setting its velocity manually for better control. I do not have much experience with physics engines yet, so I would appreciate some pointers (heh) on how to handle this.
I have already tried using swept collision for the character as well as messing with the collision margins for both the character and the level.

You can take a look at my project files here:
https://drive.google.com/file/d/0BzyMN5S2kRTHLVRLSmRTSU81Yzg/view?usp=sharing
You might have to re-set the include directories if you want to compile it yourself.

-------------------------

Lumak | 2017-02-10 20:45:33 UTC | #4

I downloaded your zip file and tried it and verified that the player drops off at the particular corner you mentioned along with other full wall corners that I tested.
Then I changed your "playerstart" cylinder to capsule:
> 		<component type="CollisionShape" id="16778942">
> 			<attribute name="Shape Type" value="Capsule" />
> 			<attribute name="Size" value="4 14 4" />

and the penetration problem stopped. I couldn't tell you if there is a problem with Bullet's cylinder collision or not but it's leaning that way.

-------------------------

TheTophatDemon | 2017-02-09 04:01:59 UTC | #5

Thank you very much, sir! Changing it to a capsule seems to have worked. I had originally planned on using a capsule, but it gave me trouble when working with slopes. However, that problem seems to have magically disappeared.

I might also add that the corner shown below triggers a "btAssert(!fuzzyZero())" in Debug Mode. It doesn't do that in Release, however, so I guess it's not to be worried about yet.
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/d1b39b12120ae5d136406af3de36eabdad39ec59.png" width="690" height="387">

-------------------------

TheTophatDemon | 2017-02-25 23:13:31 UTC | #6

I've come across a similar problem in one of my other projects, but I found out that if I introduced a second collision shape to the character controller (in this case, a sphere) and put it near the midsection the character no longer clips through the wall.

-------------------------

