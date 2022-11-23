codingmonkey | 2017-01-02 01:06:06 UTC | #1

Hi, folks!
I'm trying to do mirror node transformations but I found that it's not easy to do with inverted scale
invertedAxis = Vector3(-1,1,1); // mirroring by x - axis
node.worldScale = node.worldScale * invertedAxis;

because in Node::SetScale we got abs() function
[code]
void Node::SetScale(const Vector3& scale)
{
    scale_ = scale.Abs();
    MarkDirty();

    MarkNetworkUpdate();
}

for what purpose this is "abs" guard?

-------------------------

cadaver | 2017-01-02 01:06:06 UTC | #2

You would get flipped normals and inverted triangle winding, so be prepared to deal with that. I have added the abs() in relation to a physics related refactoring; I no longer remember exactly why but it's possible Bullet will not play nice with negative scale. I will test if leaving it out will not cause outright crashes or asserts, if not I'll remove it and it'll be left at user's responsibility to use negative scale at own risk.

EDIT: Bullet will remove objects with negative scale from simulation due to AABB violation, so scale will have to be abs():ed before passing to physics.

EDIT 2: scratch that, actually negative scale is fine, but editing the scale in editor, potentially at the point where there's just a minus sign in the edit field, will possibly cause NaN (?) or infinite be passed as the scale value, which will cause Bullet error.

-------------------------

codingmonkey | 2017-01-02 01:06:06 UTC | #3

>You would get flipped normals and inverted triangle winding, so be prepared to deal with that.
in my old little 2d shooter on unity with sprites i'm do flip rotation with negate of localScale 
but maybe this works only for 2d planes with cull - none and not for 3d models ?
well i guess that there is no ways to mirror geometry without these side effects:  flipped normals and inverted triangle winding
if only in 3d editor, you add mirror modificator and use this mirrored model for export.

-------------------------

cadaver | 2017-01-02 01:06:06 UTC | #4

Change to allow negative node scale has been pushed to master.

-------------------------

codingmonkey | 2017-01-02 01:06:06 UTC | #5

thanks, i will test this tomorrow but if it work only for 2d plane, you may restore "abs()" guard.

-------------------------

codingmonkey | 2017-01-02 01:06:07 UTC | #6

i'm tested this and actually it works normal, i guess. 
But after negate scale you will need change cull from ccw to CW and rotate model to up or somehow else
[url=http://savepic.ru/7653238.htm][img]http://savepic.ru/7653238m.png[/img][/url] 
also am not tested this with bullet, i'm think that not all objects in scene really needed to use it's own triangulated mesh they may use std colliders ( sphere, capsule, box) or low-poly model as collider instead. And these nodes with negative scales may placed as child in nodes with positives scale where bullet works fine.

-------------------------

