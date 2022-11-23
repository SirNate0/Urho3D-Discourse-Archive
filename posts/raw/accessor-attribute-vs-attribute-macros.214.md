weitjong | 2017-01-02 00:58:55 UTC | #1

After checking out this morning commits from Lasse, I become a little confuse myself about the usage of these two macros when registering an object's attributes. In the last commit I observe the ATTRIBUTE macro is used for "Face Camera Axes" attribute in BillboardSet class. However, that new attribute does have a setter accessor, which like most of the other setter does two things: assign the instance variable and mark the object for network replication. This implies that setting the "Face Camera Axes" attribute alone using OnSetAttribute() will not mark the instance for network replication. Is that intentional?

With this in mind, I scan through the code for attribute registration in other classes (ParticleEmitter and Text3D) included in the last commit and find that there are a number of existing attributes which are also just being registered using ATTRIBUTE macro although apparently they have setter that do the marking as described above. If this is intentional then I am simply missing a big picture because I cannot see the rationale when to use one over the other. For instance in BillBoard and ParticileEmitter classes:

    ACCESSOR_ATTRIBUTE(BillboardSet, VAR_BOOL, "Face Camera", GetFaceCamera, SetFaceCamera, bool, true, AM_DEFAULT);
    ATTRIBUTE(BillboardSet, VAR_VECTOR3, "Face Camera Axes", faceCameraAxes_, Vector3::ONE, AM_DEFAULT);

Both attributes are AM_DEFAULT and their setter are similar. Can someone (Lasse, I am looking at you :slight_smile:) enlighten me?

While I am at it, I think we could refactor the code to make Serializable class to have a virtual MarkNetworkUpdate() method. And then in the OnSetAttribute() method, we could call that virtual MarkNetworkUpdate() method when detecting the attribute being set has the AM_NET bit, regardless of whether it is being set using setter accessor or instance offset. This way we can remove all the MarkNetworkUpdate() calls in all the setter methods in all the code base; and even remove the setter methods themselves if that is only what they do in addition to setting the attribute value.

-------------------------

cadaver | 2017-01-02 00:58:55 UTC | #2

If you look at Component::OnSetAttribute() and Node::OnSetAttribute(), both call MarkNetworkUpdate(), so that part should be covered both with accessor and non-accessor attributes.

My rationale has been to use non-accessor attributes whenever the setter does not have range validity checks or other side-effects than MarkNetworkUpdate(). However I don't guarantee that I've followed that 100% :slight_smile: In case of the "Face Camera" attribute in BillboardSet, I think I've used the accessor form unnecessarily. This possibly is because earlier changing the flag had a side-effect (dirtying a bounding box or such) which is no longer necessary. Text3D *does* have that side-effect, so in that class the accessor form is necessary.

I wouldn't oppose making a virtual MarkNetworkUpdate(), because it would clean up Node / Component code (though at a small performance cost), and checking for the attribute actually being a net attribute is a good idea.

However I don't think we can actually remove MarkNetworkUpdate() from setters, because then direct function calls to them wouldn't trigger the network update.

-------------------------

weitjong | 2017-01-02 00:58:55 UTC | #3

Thanks for your reply. It is clearer to me now. I agree that MarkNetworkUpdate() cannot be removed from setters in any case, I have not thought through it earlier.

I will raise this as an Issue first in GitHub as I am in the middle of another refactoring. I will come back to it later if it has not been taken care of by then.

-------------------------

