ucupumar | 2017-01-02 01:12:48 UTC | #1

I've been implemented ribbon trail on Urho3D and made a [url=https://github.com/urho3d/Urho3D/pull/1418]pull request[/url]. 
My implementation consists of two types of trail, face camera and bone type. Face camera trail is always facing camera just like billboard. Bone trail will emit trail between child and it's parent, it's pretty useful for sword slashing effect. Also, I've been adding column option too to minimize artifacts.

Face camera trail:
[img]https://cloud.githubusercontent.com/assets/5253453/15984497/92b5d1ae-2ff7-11e6-8d1f-113f0fff8c07.png[/img]

Bone trail:
[img]https://cloud.githubusercontent.com/assets/5253453/15984499/953d8ffc-2ff7-11e6-9a4b-efa9c0a45aa6.png[/img]

-------------------------

rasteron | 2017-01-02 01:12:52 UTC | #2

Looks nice ucupumar! :slight_smile:

-------------------------

namic | 2017-01-02 01:12:52 UTC | #3

Thank you!

-------------------------

Lumak | 2017-01-02 01:12:53 UTC | #4

Thank you for this. I had plans to code this and now I just can use yours.

-------------------------

1vanK | 2017-01-02 01:12:53 UTC | #5

Hm, at first sight it seems, that it can be used for [docs.unity3d.com/Manual/class-LineRenderer.html](http://docs.unity3d.com/Manual/class-LineRenderer.html) with small modifications

-------------------------

ucupumar | 2017-01-02 01:12:55 UTC | #6

Thanks for all the nice replies!
[quote="1vanK"]Hm, at first sight it seems, that it can be used for [docs.unity3d.com/Manual/class-LineRenderer.html](http://docs.unity3d.com/Manual/class-LineRenderer.html) with small modifications[/quote]
If I understand it correctly, you can use ribbon trail as line renderer if you set the tail lifetime to infinity. But I don't think I have implement infinity lifetime yet. Maybe I'll add that tomorrow.

I actually plan to add batch support like Ogre ribbon trail. For now, each trail is rendered in individual draw call, so if you render trail a lot, you'll get some a performance hit.

-------------------------

ucupumar | 2017-01-02 01:13:13 UTC | #7

Sorry to inform you, I just realized RibbonTrail not supposed to emit infinite tail, so it's better to implement real Line renderer to do that specific things. If you really need that feature now, feel free to modify my code and start to create own LineRenderer class.  :unamused:

-------------------------

