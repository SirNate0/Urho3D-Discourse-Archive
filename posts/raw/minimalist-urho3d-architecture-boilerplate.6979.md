nickwebha | 2021-08-28 17:56:08 UTC | #1

Hey, everyone.

I am working on a [minimalist architecture boilerplate](https://github.com/nickwebha/urho3d-architecture/) and blog post to go along with it explaining the "Urho3D way" to n00bs. It is not meant to show off all the subsystems but to show one example of a potential basic architecture (the thing I personally struggled with the most). The project will remain small is scope.

What do you guys think of it overall as [it stands now](https://github.com/nickwebha/urho3d-architecture/tree/c48304dbf72845a0bdcb1fd6cde5d49dd6da8939/)? This is more of an alpha version than anything else; I expect a lot to change. With the help of your feedback, I want to get this blog post live with the v1.0 of the code.

At least one thing I am unsure about is how [the player is handled](https://github.com/nickwebha/urho3d-architecture/blob/c48304dbf72845a0bdcb1fd6cde5d49dd6da8939/source/world.cpp#L64). Any suggestions there would be most appreciated. Maybe it is fine as it is? Not sure of the ideal way to handle that one.

One final note: Comments will be added once the code base settles down a bit.

Thanks for your time and input!

*I would like to recognize [Miegamicis](https://discourse.urho3d.io/u/miegamicis/) for his [new project template](https://discourse.urho3d.io/t/new-project-template/). His is meant to be more "complete" than mine so if you want a more fleshed-out starting off point go with that.*

-------------------------

Modanung | 2021-08-28 20:10:07 UTC | #2

In my book, the `Player` is (often) not the `Controllable`. This makes it easier for the `Player` to momentarily switch to a different `Controllable` - be it some vehicle, crane, turret or possessed creature - and to switch out the `Player` for some `Autopilot`.

-------------------------

nickwebha | 2021-08-29 15:35:37 UTC | #3

[quote="Modanung, post:2, topic:6979"]
the `Player` is (often) not the `Controllable`... and to switch out the `Player` for some `Autopilot`
[/quote]
This is a good point. I am going to have to think about the best way to go about this.

-------------------------

JTippetts1 | 2021-08-29 16:11:34 UTC | #4

There is stuff in there that is just not needed. Not every game even needs a Player. Things such as https://github.com/nickwebha/urho3d-architecture/blob/master/include/objectMovement.hpp are just completely unnecessary, given how single-case it is (applying impulses along axes in the physics sim, which not every game is even going to enable). Not even really sure what the point of cylinders is, given the fact that in the source you are creating StaticModels and setting their attributes.

If you want to write boilerplate, pare it down to commonalities. Minimalist means minimalist, so you should eliminate your special-case thingies like cylinders and objectMovement, that you implemented for your own project and that have no reason for being a part of any 'minimal boilerplate' project.

My recommendation is that you do more projects with Urho, learn more about how it is structured and how to use it, before attempting to write something for other people to use. Otherwise, it's just the blind leading the blind.

-------------------------

Modanung | 2021-08-29 19:04:26 UTC | #5

IDE wizards are a great format for this as well, allowing for convenient modularity.

https://gitlab.com/luckeyproductions/tools/QtCreatorUrho3DWizards

-------------------------

nickwebha | 2021-09-04 18:52:14 UTC | #6

*Sorry for the late reply. A rough few days.*

[quote="JTippetts1, post:4, topic:6979"]
it’s just the blind leading the blind
[/quote]
I do not disagree. I just would like to see a resource out there that I had found lacking. The samples are **truly** wonderful but they do not answer the larger architecture problem. With the help of the community this could be a valuable learning tool for multiple systems and how to put them to together in a coherent way (as opposed to the isolation of each sample). I have been reading a few books ([Game Programming Books](https://gameprogrammingpatterns.com/), for one) and they are really helping.

[quote="JTippetts1, post:4, topic:6979"]
There is stuff in there that is just not needed.
[/quote]
This is a question that still needs answering (which falls on me): How much is too much and how much is too little. A lot of games do not need a `player` but I had to go somewhere with it and I decided `player` is the more common first project.

[quote="JTippetts1, post:4, topic:6979"]
Not even really sure what the point of cylinders is
[/quote]
[quote="JTippetts1, post:4, topic:6979"]
eliminate your special-case thingies like cylinders and objectMovement
[/quote]
I do not like the way `objectMovement` is implemented, for example, as it does so little and could-- should, even-- be inside the `player` class itself but I wanted to show off creating components and could not think of another, less complex way. I liked the idea [Modanung](https://discourse.urho3d.io/u/Modanung/) had and could make it viable to switch the "player" around which would make it more generic and have more use cases. Something that lets the player control any object they wanted at any time using the same component(s).

With appropriate comments it should be easy for people to remove stuff they do not need.

[quote="JTippetts1, post:4, topic:6979"]
My recommendation is that you do more projects with Urho
[/quote]
You might be right. I have been leaning on the community a bit much; Maybe more time is needed. If that is deemed to still be the case after some revisions then I can shelf this for a while and come back to it later to it when I am more knowledgeable. Right now, though, I still think there will be value here.

I am leaving out a lot for the sake of "boilerplate" but putting some stuff in that is not strictly necessary just to demonstrate its use beyond the samples (again, as part of an architecture).

I am not blindly moving forward but hoping to hear back from more experienced peopled than myself. If that does not happen then I may put it all on hold for now (but I hope not).

[quote="Modanung, post:5, topic:6979"]
IDE wizards are a great format for this as well, allowing for convenient modularity.

https://gitlab.com/luckeyproductions/tools/QtCreatorUrho3DWizards
[/quote]
This link looks great and something to study. Thank you.

-------------------------

lebrewer | 2021-08-31 15:45:37 UTC | #7

[quote="JTippetts1, post:4, topic:6979"]
Otherwise, it’s just the blind leading the blind.
[/quote]

A bit too rough, eh? I found his content to be extremely useful and helps overcome a lot of doubts and challenges when beginning to work with Urho. Any documentation, any guide, any tutorial is going to be useful, regardless of the knowledge level of the writer. Everyone ends up improving the community together, at different levels.

@nickwebha thanks a lot for putting the time and the effort on this, I really appreciate this and I'm sure other beginners will appreciate this kind of content.

-------------------------

Modanung | 2021-09-03 11:30:14 UTC | #8

Looking at those wizards again, public domain seemed more appropriate: CC0 now.

Despite having served me well, they are not perfect. Let me know if you'd like write access to the repository. Maybe it would me nice to transplant parts of @Miegamicis' template.

-------------------------

