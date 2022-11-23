najak3d | 2020-09-09 02:15:18 UTC | #1

We are using UrhoSharp, and are wanting to toggle the Texture of the material to toggle between two images -- Normal and Bold.

The first time we toggle the image, it works.  The 2nd time, it throws an "AccessViolationError".

It's acting as though it's disposing the Texture that gets replaced, so that we can't set that Texture again.  We aren't disposing of anything and are holding a reference to both textures, and not releasing the references.

Is there some sort of auto-dispose that occurs in Urho when you swap textures (i.e. if the previous texture is non-null, then maybe it calls Dispose()?).

-------------------------

Avagrande | 2020-09-09 02:14:50 UTC | #2

I had a similar issue with managing off-screen render buffers in Lua. Even when creating the texture with :new() function it would still delete the texture anyway once I assign it to anything and that thing gets removed. 

Form what I know Urho3d manages memory using the Scene so if you want to be absolutely sure, it might be worth it to create hidden nodes and give it the texture you want to use.

-------------------------

Modanung | 2020-09-09 02:14:50 UTC | #3

Sounds like a situation where you'll want to use [`SharedPtr`](https://urho3d.github.io/documentation/1.7.1/_conventions.html)s to keep the texture alive.

-------------------------

najak3d | 2020-09-08 01:01:11 UTC | #4

Avagrande, thank you, this worked for me.   So for cases where I need to swap the textures, I need to make sure that some node in the scene keeps a reference to the texture, and that prevents it from being disposed.

Note - I think Modanung's solution (SharedPtr) should also work -- except UrhoSharp does *not* expose the SharedPtr class, so I am unable to use it.

-------------------------

Modanung | 2020-09-08 17:06:38 UTC | #5

[quote="najak3d, post:4, topic:6373"]
I am unable to use it.
[/quote]

Is it impossible to switch to Urho3D?

-------------------------

najak3d | 2020-09-08 19:53:48 UTC | #6

Modanung - yes, we are unable to switch.  Our project is being developed using Xamarin and XAML forms for 3 platforms, all in C#.  UrhoSharp is currently the only recommended OpenGL graphics engine recommended for Xamarin Forms.  That's why we are here.

-------------------------

Modanung | 2020-09-08 20:05:32 UTC | #7

[quote="najak3d, post:6, topic:6373"]
That’s why we are here.
[/quote]

Here we recommend Urho3D.

-------------------------

najak3d | 2020-09-08 21:19:37 UTC | #8

Yeah, but Xamarin Forms apps MUST use UrhoSharp, not Urho3D.

Does Urho3D itself support C# programming? (where your app can be fully .NET/C# which uses Urho3D for it's rendering)   My understanding is that any C#/.NET app really needs to use UrhoSharp as well.

-------------------------

JTippetts1 | 2020-09-08 23:08:34 UTC | #9

The issue is that you're using this forum as a support forum for a product that is not from here, that is apparently obsolete and abandoned, and that most of the users here are not that familiar with. For example, this question. SharedPtrs are the means by which Urho3D manages the lifetime of resources. They're used internally, and they're intended to be used by the user. Had you been using SharedPtr, this question never would have needed to be asked, and the answer to this question has nothing at all to do with Urho3D itself, and everything to do with UrhoSharp not correctly exposing the basic lifetime-management tools that Urho3D employs. It's annoying to have the forums cluttered with issues and problems that are not relevant to Urho3D.

-------------------------

najak3d | 2020-09-09 00:45:19 UTC | #10

JTippetts1 - UrhoSharp may be updated in the future.  Currently it's the ONLY recommendation for Xamarin Forms for 3D graphics rendering support.  Egorbo made sure it works, and it does work.

So there are a number of people likely in my boat - as Xamarin Forms is quite mainstream, especially for those who want to write C#/.NET apps for all 3 main platforms -- Windows, Android, and iOS.

So for these users, it's good for them to know the "Urhosharp version of the solution". 

I hope this forum will continue to support me on this.  I think these answers will be helpful to others, and in the end, may drive some fixes and a re-release of UrhoSharp.

-------------------------

Modanung | 2020-09-09 02:13:18 UTC | #11



-------------------------

Modanung | 2020-09-09 02:16:56 UTC | #12

This thread is off-topic.

Try to get support from the people you are listening to, or listen to the people you are getting support from.

-------------------------

weitjong | 2020-09-09 03:56:36 UTC | #13

Instead of shutting the door for all the UrhoSharp related topics, I am considering creating another category for UrhoSharp in the forum so that people can segregate the topics easily. A topic will only get the responses from the community on best effort basis anyway. Having a separate category does not change anything else.

My only concern is the "amount of traffic" it would generate. As long as it does not exceed (from the past historical trend it should not) the quota of our free Discourse account then I am OK with it.

-------------------------

Modanung | 2020-09-09 04:49:30 UTC | #14

Maybe Xamarin should *open their door* instead?
[spoiler]...oh they have, but there's nobody home?[/spoiler]

Or will you track UrhoSharp issues too? Nobody here is going to provide "full support", and I don't think we should create categories that suggest we do.

-------------------------

weitjong | 2020-09-09 04:54:16 UTC | #15

The purpose of the category is to, well, just to put the topics in the respective category. We don't claim to provide support either way.

Frankly speaking I need the traffic, just not that much. Some of their issues *are* Urho3D issues too, not all of course.

-------------------------

Modanung | 2020-09-09 04:55:03 UTC | #16

[quote="weitjong, post:15, topic:6373"]
We don’t claim to provide support either way.
[/quote]

It doesn't take a claim to allude to a suggestion.

-------------------------

weitjong | 2020-09-09 04:55:47 UTC | #17

I disagree. We also don't claim we provide full support of Urho3D for free.

-------------------------

Modanung | 2020-09-09 04:56:52 UTC | #18

True... furthermore "we" doesn't speak. "We" does not exist, really.

-------------------------

weitjong | 2020-09-09 05:00:32 UTC | #19

Well, except I am the owner of the domain. So, I could say "we" to indicate I have the authority and final say here.

If you still want to discuss this further, I suggest you open a separate topic and invite all the members of the staff to discuss. Thanks.

-------------------------

Modanung | 2020-09-09 05:01:01 UTC | #20

Yes, but if this domain turns totalitarian, it's time to move.

-------------------------

weitjong | 2020-09-09 05:01:48 UTC | #21

True. But the forums is equally doom if we have to vote for smallish thing like this.

-------------------------

Modanung | 2020-09-09 05:02:50 UTC | #22

Then let's not. Things are fine as they are, AFAIC. :slight_smile: 
...and I appreciate what you do @weitjong.

-------------------------

weitjong | 2020-09-09 05:05:58 UTC | #23

I will see how many "likes" I get in the comment above where I suggested for category creation, before I make the decision. Like I said, I *am* considering still.

-------------------------

Modanung | 2020-09-09 05:12:31 UTC | #24

But then, how about an rbfx category? Or do those users respect this forum's topic too much to be present? Do you consider an UrhoSharp category because it "contains" "urho"?

-------------------------

weitjong | 2020-09-09 05:12:20 UTC | #25

This is different. RBFX is a complete fork.

-------------------------

Modanung | 2020-09-09 05:13:56 UTC | #26

UrhoSharp is too, effectively. It's got old bugs that will never be solved.

-------------------------

weitjong | 2020-09-09 05:16:47 UTC | #27

Again, I disagree. I could be wrong but I see UrhoSharp as a C# binding on top of Urho3D, although they may not have done a good job at it or need to make some changes that ended up breaking some of the underlying Urho3D logic. RBFX is nothing but.

Plus, RBFX has their forum already, right?

-------------------------

Modanung | 2020-09-09 05:19:20 UTC | #28

Yes, but - if I understand correctly - it's binding to a relic from the past. Which makes it dead fork.
...in *essence*.


But you'd have to ask Xamarin to be sure.

-------------------------

weitjong | 2020-09-09 05:20:43 UTC | #29

If we ever start to see people complaining RBFX issues mix with our Urho3D issues in this forum then we could have this discussion too, but not before it.

-------------------------

Modanung | 2020-09-09 05:21:41 UTC | #30

And by the time _sharpies_ learn how to start a forum, they're coding in C++.

You can't expect an open source stance from proprietary parasites.

-------------------------

Modanung | 2020-09-09 05:32:51 UTC | #31

https://www.youtube.com/watch?v=BMxO68BJcFY

-------------------------

1vanK | 2020-09-09 06:54:41 UTC | #32

I don't see anything wrong with creating a separate category for UrhoSharp with a note that we have nothing to do with UrhoSharp and cannot fix bugs in it :)

-------------------------

Modanung | 2020-09-10 08:46:49 UTC | #33

[quote="1vanK, post:32, topic:6373"]
I don’t see anything wrong with [...]
[/quote]

...creating a topic titled "off-topic" that welcomes people into a black hole? *So* generous. :slightly_smiling_face: 

Maybe we could make a faux category instead that merely links to the Xamarin forums?

-------------------------

Modanung | 2020-09-09 07:29:36 UTC | #34

It is not our problem that UrhoSharp is an unsupported corpse and dragging it in would be unhygienic.

-------------------------

1vanK | 2020-09-09 07:36:36 UTC | #35

What are your suggestions?

-------------------------

Modanung | 2020-09-09 07:38:29 UTC | #36

To stop repeating this discussion. It's beginning to look like necrophilia.

-------------------------

1vanK | 2020-09-09 07:41:07 UTC | #37

Do you agree that questions about UrhoSharp will come up over and over and over again? How can you change this? Better to keep them in a separate category with the note.

-------------------------

Modanung | 2020-09-09 07:47:06 UTC | #38

No, you help them to make the right decision.
> [spoiler]Stop humping that corpse[/spoiler]

Instead of making a room for sick activities.

-------------------------

