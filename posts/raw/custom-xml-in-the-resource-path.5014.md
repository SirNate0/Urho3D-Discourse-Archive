Leith | 2019-03-10 12:17:34 UTC | #1

I like to describe certain information per character model.
The editor hates this being in the resource path, but the editor hates linux either way.
Am I doing it wrong?

[code]
<Outer>
<AnimationSet>
    <Comment>
    Player and NonPlayer Animation Descriptors align with hardcoded semantic enumerations
    which is to say, their index has a meaning for the character
    </Comment>

    <Descriptor Name="Models/Derrick/zombie idle.ani" Looping="true" LayerID="0"/>
    <Descriptor Name="Models/Derrick/zombie walk.ani" Looping="true" LayerID="0"/>
    <Descriptor Name="Models/Derrick/zombie run.ani" Looping="true" LayerID="0"/>
    <Descriptor Name="Models/Derrick/zombie crawl.ani" Looping="true" LayerID="0"/>
    <Descriptor Name="Models/Derrick/zombie running crawl.ani" Looping="true" LayerID="0"/>
    <Descriptor Name="Models/Derrick/zombie attack.ani" Looping="false" LayerID="0"/>
    <Descriptor Name="Models/Derrick/zombie biting.ani" Looping="false" LayerID="0"/>
    <Descriptor Name="Models/Derrick/zombie scream.ani" Looping="false" LayerID="0"/>
    <Descriptor Name="Models/Derrick/zombie dying.ani" Looping="false" LayerID="0"/>
    <Descriptor Name="Models/Derrick/zombie death.ani" Looping="false" LayerID="0"/>
    
    <Comment>
    The following bone descriptors are required to locate bones for foot ik
    </Comment>

    <Bone Name="Left Foot"  Value="LeftFoot" />
    <Bone Name="Right Foot" Value="RightFoot" />
    <Bone Name="Pelvis"     Value="Hips" />

    <Comment>
    Ragdoll Bodyparts are defined with respect to the character bindpose
    </Comment>

    <BodyPart Name="Hips"   Shape="Box"     Size=".3,.15,.2"   Position="0,0.05,0"  Orientation="0,0,0" />
    <BodyPart Name="Spine1" Shape="Box"     Size=".35,.35,.25" Position="0,0.1,0"   Orientation="0,0,0" />
    <BodyPart Name="Head"   Shape="Capsule" Size=".25,.35,0"   Position="0,0.125,0" Orientation="0,0,0" />

    <Comment>
    Ragdoll Joint Constraints
    </Comment>
    <Joint Name="Neck" BodyPart="Head" ParentPart="Spine1" Type="ConeTwist" Axis="-1,-0,0" ParentAxis="-1,0,0" HighLimit="0,30,0" LowLimit="0,0,0" />

</AnimationSet>
</Outer>
[/code]

-------------------------

lezak | 2019-03-10 13:31:22 UTC | #2

[quote="Leith, post:1, topic:5014"]
The editor hates this being in the resource path
[/quote]

What exactly do You mean by this?

-------------------------

Modanung | 2019-03-10 13:57:39 UTC | #3

The editor and my Linux Mint machine get along fine. @Leith What distro you on (again?)?

-------------------------

Leith | 2019-03-10 21:49:18 UTC | #4

I'm on the master branch from git, with editor from the public branch (as the one in the master branch is totally unstable on linux tessa - selecting a scene object will crash the application)
Editor attempts to parse my custom xml file (as its in the resource path) and complains loudly :)

-------------------------

weitjong | 2019-03-11 00:38:02 UTC | #5

You are not making any sense!

-------------------------

Leith | 2019-03-11 02:56:39 UTC | #6

I will try at some point today to record a video of the masterbranch editor crashing on select, and the 1.7 editor complaining about my custom xml files - I know, I can just change the file extension to hide those files from the editor...

-------------------------

weitjong | 2019-03-11 03:09:18 UTC | #7

Can you first answer Modanung question? Also don’t expect the Editor to handle the custom things(whatever that means) for you.

-------------------------

Leith | 2019-03-11 03:11:08 UTC | #8

I did answer - I said Linux Mint Tessa (which is 19.1) - I did not check the kernel version, but that is the distro I am using ;)

-------------------------

weitjong | 2019-03-11 03:23:19 UTC | #9

Yes. That’s much clearer answer. Thanks.

-------------------------

Leith | 2019-03-11 03:26:02 UTC | #10

No problem :) I apologize for not being more clear in the first place, you shouldn't need to read between the lines for the answer to a direct and simple question!

-------------------------

weitjong | 2019-03-11 04:15:23 UTC | #11

The reason I asked because we could easily try the same exact distro in a virtual machine to verify or reproduce the editor issue that you claim to have.

-------------------------

Leith | 2019-03-11 04:19:26 UTC | #12

I could try harder to trap it, now I have some hands-on experience in hacking the sourcecode, but that sounds like a 99.9% better way to go about it :slight_smile: Hacking the sourcecode is bad - but so far mostly is restricted to additional debug information. There's a bit of overwhelming spew, but it is more verbose. Works in a few small corner cases.

-------------------------

weitjong | 2019-03-11 04:42:23 UTC | #13

You are allowed to customize the project to suit your particular use case, but if you break it along the way then you have to be upfront of what you have changed so you don’t waste other time trying to support you, thinking you are using vanilla version.

-------------------------

Leith | 2019-03-11 04:50:12 UTC | #14

So far my only core change, was to auto-initialize Attributes to their default values (as we defined them), plus the networking fix I offered for out of order node restructure - anything else I added, is already up for removing, because its just debug stuff that I don't need right now
ok there was one more small change, but I suspect it was not needed - will review before PR.

-------------------------

