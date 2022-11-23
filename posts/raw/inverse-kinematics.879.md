setzer22 | 2017-01-02 01:03:46 UTC | #1

Inverse Kinematics is a feature I would like to be added to Urho. 

I'm actually thinking of implementing this myself after finding no good open source libraries (with compatible licenses) that fullfill this task. I've been reading some papers on the subject, but it seems I'll need some time and practise to really understand this. 

In the meantime I'll make this post to see how many people is interested in this, and also if there's someone more capable than me also willing to implement the feature. 

Cheers :smiley:

-------------------------

franck22000 | 2017-01-02 01:03:46 UTC | #2

Definitely interested by this also. I might try to add it in the future but i think i have no more knowledge than you on the subject :slight_smile:

-------------------------

sabotage3d | 2017-01-02 01:03:46 UTC | #3

There are available open source solutions.
Check [ogre3d.org/forums/viewtopic.php?f=5&t=47172](http://www.ogre3d.org/forums/viewtopic.php?f=5&t=47172) for OpenTissue
And also there is SmarBody which is quite complex but the IK can be extracted easily: [smartbody.ict.usc.edu/](http://smartbody.ict.usc.edu/)
There is also a simple IK solver provided with Maya in the OpenMaya library .

-------------------------

codingmonkey | 2017-01-02 01:03:46 UTC | #4

I used to think about it. But without the use of any third-party libraries
For example: how to make a character (if it is close enough to the door) could take the door handle and open it.
door handle has a dummy-target for the skeleton.
If the character be close enough to handle of door, then all the arm bone (which arm will open the door) are switched to the Ragdoll-chain.
And this ragdoll-chain of bones must have two binding. ?ne binding to the shoulder of the character, and the second to bind to the palm of the hand of the character.
In the script, we can move the bone of palm and all ragdoll-chani (arm) should move (on the idea) behind it.
I think for this tech we should also use the blending of bone positions, between animated skeleton and switched ragdoll-parts of it.
At last may be we should use fully copied separated ragdoll-skeleton in same place with animated skeleton, and do this blending.

-------------------------

sabotage3d | 2017-01-02 01:03:46 UTC | #5

Smartbody already does this.

-------------------------

codingmonkey | 2017-01-02 01:03:46 UTC | #6

looking at this example. 
especially at refinement part.

He say's what there is no needed any of the library for this - this is simple trigonometry :slight_smile:

[gdcvault.com/play/1020583/An ... e-Approach](http://www.gdcvault.com/play/1020583/Animation-Bootcamp-An-Indie-Approach)

>Smartbody already does this.
I do not have anything against of this. But I think it's a big library-monster )

-------------------------

hdunderscore | 2017-01-02 01:03:46 UTC | #7

[quote="codingmonkey"]looking at this example. 
especially at refinement part.
[/quote]
Very interesting video, makes me want to go and try some of those things.

Smart body uses LGPL license, which is of course fine for personal projects but I'm not sure we'd want that in Urho master. OpenTissue has a more agreeable zlib license + is header only so it's probably not too difficult to whip up a test case (eg, on character demo) and see how it works out. I'd be interested to see the results if you do that :smiley:

-------------------------

sabotage3d | 2017-01-02 01:03:47 UTC | #8

If you want full IK like HumanIK in Maya it is not simple :slight_smile:

-------------------------

Mike | 2017-01-02 01:04:21 UTC | #9

I've ported Ogre+OpenTissue sample to Urho. I've done some quick tests in T-pose and A-pose and it seems to be promising.
[img]http://i.imgur.com/3ezQLWE.png?1[/img]
I'll investigate more real-life experiments to determine if it's worthy of going further with this library.

-------------------------

cadaver | 2017-01-02 01:04:21 UTC | #10

Cool! It seems that OpenTissue depends on Boost, which makes integration into Urho somewhat a negative, at least in the way we usually integrate dependencies, unless the needed portion of Boost can be "faked" like Assimp does. But sharing the code as an external add-on people can experiment with and integrate on their own, could still be valuable.

-------------------------

GoogleBot42 | 2017-01-02 01:04:21 UTC | #11

[quote="cadaver"]Cool! It seems that OpenTissue depends on Boost, which makes integration into Urho somewhat a negative, at least in the way we usually integrate dependencies, unless the needed portion of Boost can be "faked" like Assimp does. But sharing the code as an external add-on people can experiment with and integrate on their own, could still be valuable.[/quote]

That is too bad... I don't really like boost very much.  If the bindings could be faked that would be awesome!  But it does look promising so at the very least it should be an external Urho3D library so that others can use it if they are ok with including boost.  :slight_smile:

-------------------------

sabotage3d | 2017-01-02 01:04:21 UTC | #12

This one is a lot simpler no dependencies. And very easy to port.
It is shipped with maya and it is part of completely free open maya framework for real-time applications.

[code.google.com/p/gamekit/sourc ... ver/?r=173](https://code.google.com/p/gamekit/source/browse/branches/character-system/Loader/ik2Bsolver/?r=173)

And here is a guide on what it actually does.

[download.autodesk.com/global/doc ... d30e300476](http://download.autodesk.com/global/docs/maya2014/en_us/index.html?url=files/CSS_IK_solvers.htm,topicNumber=d30e300476)

-------------------------

Mike | 2017-01-02 01:04:22 UTC | #13

For Boost I simply extracted header files in OpenTissue folder, no bindings, no built library. Other dependencies like Atlas, GLUT... are not necessary and IK is only a small fraction of the library so we can later trim the fat.
I'm currently digging in the API to set the axes and limits, this part is not well documented.

@sabotage3d, thanks for the links, a 2 bones chain can be a good alternative to a full chain that is not always necessary. I'll try to integrate it today.

-------------------------

cadaver | 2017-01-02 01:04:22 UTC | #14

Mike: that sounds good; no need to add (cross-platform) Boost library build mechanism then.

-------------------------

Mike | 2017-01-02 01:04:23 UTC | #15

Maya ik2Bsolver also works great, is lightweight and easier to setup as it's only a 2D IK solver applied on pairs of bones.
Both libraries have their strengths and weaknesses and for now it's good to have both.

In both cases, I think I'll get rid of setting constraints/limits by simply clamping the rotations given by the solver.

Maybe I'll also give a look at this library released under BSD (which is unfortunately not documented at all and code is sparsely commented): [quelsolaar.com/confuse/index.html](http://www.quelsolaar.com/confuse/index.html)

-------------------------

sabotage3d | 2017-01-02 01:04:24 UTC | #16

I stuck upon this library as well it is mainly for robotics but it looks interesting. It is based on Jacobian inverse which is good in some cases.

[github.com/kouretes/NAOKinematics](https://github.com/kouretes/NAOKinematics)

-------------------------

