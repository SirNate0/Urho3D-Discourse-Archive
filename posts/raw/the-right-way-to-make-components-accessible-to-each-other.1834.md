lizardperson | 2017-01-02 01:10:32 UTC | #1

Hello, this is my first post here. 
I've found Urho3d recently and so far it seems like an engine I could get really comfortable to work with.
Currently, the most head scratching thing that stops me from working is the structuring of the game logic. I've read the forum and apparently the common way is to group code inside classes derived from LogicComponent. 
What I can't figure out is the right way to make other components accessible from the LogicComponent. By the right way I mean the one that won't break some engine's functionality down the road. For example, if I have Node and attached to it StaticModel and LogicComponent, how to register pointer to StaticModel inside LogicComponent the way it will be valid after deserialization? 
I guess it definitely won't work with manual binding during creation of components like:
[code]myLogicComponent->bindModel(model);[/code]
I can look it up through the parent node inside LogicComponent's OnNodeSet method and bind it that way:
[code]MyLogicComponent::OnNodeSet()
{
	staticmodelptr_ = this->GetNode()->getComponent(StaticModel::GetTypeStatic())
}[/code]
but this is supposed to work only when LogicComponents are added the last, seems kind of sloppy, also I can't find if components are initialized in the original order during deserialization, if not this method won't work as well.

Maybe I shouldn't store pointer to the needed component in the member variable at all and instead search it through the parent node every time I need an access to it, but it feels non-optimal.
Am I missing some other way?

-------------------------

thebluefish | 2017-01-02 01:10:32 UTC | #2

Typically you would do this in LogicComponent::DelayedStart(). It is called on the first scene update, which ensures that all other nodes and components have been loaded already.

-------------------------

lizardperson | 2017-01-02 01:10:32 UTC | #3

I should have looked at LogicComponent members list closer, that's exactly what I was looking for, thank you.

-------------------------

jmiller | 2017-01-02 01:10:32 UTC | #4

Pointers can also be conveniently reacquired at end of Scene load, when Serializable::ApplyAttributes() is called on each Serializable.

[github.com/urho3d/Urho3D/blob/m ... le.cpp#L60](https://github.com/urho3d/Urho3D/blob/master/Source/Samples/19_VehicleDemo/Vehicle.cpp#L60)

VehicleDemo gets the nodes by ID and components by type, but both can be acquired by GetNode(id)/GetComponent(id) wherever they are.

-------------------------

lizardperson | 2017-01-02 01:10:33 UTC | #5

Thank you as well, carnalis, it's helpful. All samples I've seen were self contained in one class, without usage of custom components, didn't notice this one.
Also, documentation describes ApplyAttributes just like you "Called after scene load or a network update.", but there's a page in the [url=http://urho3d.wikia.com/wiki/Creating_your_own_C%2B%2B_components]unofficial  wiki[/url] which mentions that it also "will be called whenever the user changes an attribute on the editor (or the code changes it programatically)", is this accurate?

-------------------------

jmiller | 2017-01-02 01:10:33 UTC | #6

Yes, that seems to be true.
(and just so you don't miss it, there's a new wiki in the works [[b]edit: see gawag reply[/b]])

-------------------------

Modanung | 2017-01-02 01:10:33 UTC | #7

[quote="carnalis"](and just so you don't miss it, there's a [url=https://urho3d.miraheze.org/wiki/Main_Page]new wiki[/url] in the works)[/quote]
There's also an [url=https://github.com/urho3d/Urho3D/wiki]official wiki[/url] in the works linked to by the Urho3D home page and mentioned on the wiki carnalis linked to.

-------------------------

lizardperson | 2017-01-02 01:10:33 UTC | #8

I see, thanks!

-------------------------

gawag | 2017-01-02 01:10:34 UTC | #9

*cough*
[quote="carnalis"]Yes, that seems to be true.
(and just so you don't miss it, there's a [url=https://urho3d.miraheze.org/wiki/Main_Page]new wiki[/url] in the works)[/quote]

That wiki is paused to concentrate on the official wiki. There may be no need for it anymore or it may cover different topics not covered in the official one. I placed notes on the two unofficial wiki regarding that and just made the one on the Miraheze wiki bigger and added a sentence to it to make that clearer.

About that component questions: Someone else wrote that article and I'm not that familiar with that area. Maybe there's something in the documentation? Here is a bit about attributes and components: [urho3d.github.io/documentation/1 ... ation.html](http://urho3d.github.io/documentation/1.5/_attribute_animation.html)

-------------------------

