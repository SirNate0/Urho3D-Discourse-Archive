mustacheemperor | 2019-03-09 00:08:50 UTC | #1

Edit: I see another post was recently locked 

Hello,
In my application I have Node *A* with given scale (.525f, .42f, .0462f). Node A itself is locally scaled to Vector3.One, but is scaled to that world scale by its own parent in this context. I'd like to attach Node *B* to Node A as a child. When I set Node B as a child of Node A, its scale is modified by the parent scale, as expected. However, if I use SetWorldScale to force Node B back to its original scale, that doesn't happen. Instead Node B is scaled to some new set of values seemingly still modified by the parent. This doesn't seem like expected behavior, am I doing something wrong? I've included a detailed snippet below showing the problem. My head is really spinning on this one and I'd greatly appreciate the advice. 

    Node nodeA = Scene.AddChild();
    nodeA.SetWorldScale(new Vector3(3.2f,.2f,.2f);
    Node nodeB = Scene.AddChild();
    nodeB.SetWorldScale(Vector3.One);

    var originalWScale = nodeB.WorldScale;
    var originalLScale = nodeB.Scale;

    nodeB.ChangeParent(nodeA);

    System.Diagnostics.Debug.WriteLine($"Pre Reset: {originalScale} {originalLocalScale} {nodeB.WorldScale} {nodeB.Scale}");
Pre Reset: (0.9999999, 0.9999999, 0.9999999) (1, 1, 1) (0.525, 0.4199999, 0.0462) (1, 1, 1)

    this.Node.SetWorldScale(originalScale);
    System.Diagnostics.Debug.WriteLine($"Post Reset: {originalScale} {originalLocalScale}{nodeB.WorldScale} {nodeB.Scale});
Post Reset: (0.9999999, 0.9999999, 0.9999999) (1, 1, 1) (0.9999999, 9.090908, 0.11) (1.904762, 21.64502, 2.380952)

**I set nodeB's world scale, which should be unmodified by its place in the hierarchy, to (.999,.999,.999). The very next line, nodeB's world scale is (0.9999999, 9.090908, 0.11). I'm mystified.**

Apologies if this is the wrong forum for this topic. I understand this is primarily Urho3D discussion, but google results for UrhoSharp problems take me here with some regularity and I see UrhoSharp related discussions both being closed as off topic and answered by helpful people. If there's an alternative place to ask this please let me know.

-------------------------

Leith | 2019-03-09 03:15:02 UTC | #2

Ooh this looks like a bug - the scenegraph was not updated after being "dirtied" and before being queried again - I assume the second query occurs in the same frame?

-------------------------

Modanung | 2019-03-10 16:48:10 UTC | #3

[quote="mustacheemperor, post:1, topic:5010"]
nodeA.SetWorldScale(new Vector3(3.2f,.2f,.2f);
[/quote]

No need to create a pointer here, you can leave out the `new` keyword.

[quote="mustacheemperor, post:1, topic:5010"]
I understand this is primarily Urho3D discussion, but google results for UrhoSharp problems take me here with some regularity and I see UrhoSharp related discussions both being closed as off topic and answered by helpful people.
[/quote]

[details=Rant]
I worship Urho3D and like helping out people interested in it, but I absolutely detest Microsoft and its widely accepted spyware products... and if they can buy a company for $500 million, have it puke C# all over an open source project and leave in bugs that have been fixed up-stream they can do their own tech-support at the [Xamarin forums](https://forums.xamarin.com/).
[/details]
Indeed, *do not expect support for UrhoSharp here.*  

If you want to create things with Urho and write in C# it's probably wiser to use **[rbfx](https://github.com/rokups/rbfx)**. @rku where could people go with **rbfx**-related questions, btw?

-------------------------

rku | 2019-03-09 14:58:08 UTC | #4

Urho3D gitter is where i can be found for a quick word. Github issues also work.

-------------------------

I3DB | 2019-03-09 16:30:51 UTC | #5

[quote="Modanung, post:3, topic:5010"]
[spoiler]I worship Urho3D and like helping out people interested in it, but I absolutely detest Microsoft and its widely accepted spyware products… and if they can buy a company for $500 million, have it puke C# all over an open source project and leave in bugs that have been fixed up-stream they can do their own tech-support at the [Xamarin forums](https://forums.xamarin.com/).[/spoiler] Indeed, *do not expect support for UrhoSharp here.*
[/quote]

Some people ...
strive to extricate and expunge anyone or anything that differs in deed or word in any way from their own personal views.

Some people ...
strive to create communities, where people are working on the same things, generally going in the same directions, but taking different approaches, using skills they have to move forward in their own ways.

Indeed most people are just trying to find a bit of help and don't have all the perfect words, or perfect characteristics, or perfect biases, that align perfectly here so they can get help.

---------
I wonder about this board and the goals of the people who are sheperding this engine and this board.

Are you trying to build community and help people who have interest in using Urho3D?

Are you trying to chase away anyone who doesn't share your biases?

Do you want to see a community of Urho3D users, regardless of how they choose to use Urho3D?

Or is the goal to kill off interest in Urho3D because someone might not share your biases?

It's sort of like someone has an 8 cylinder engine they want to use, they found experts who only offer support for the 8 cylinder engine when it's stuffed in a Ford F-150, due to biases against all other automobiles. Anyone who admits their 8 cylinder is not in a Ford is out of luck.

Is this Urho3D?

-------------------------

Modanung | 2019-03-09 20:02:35 UTC | #6

Beyond my personal opinion there are several technical and sociodynamic reasons to point those with UrhoSharp questions to the Xamarin forums or rbfx.

Each project has their own repositories, with it their own developers, bugs, issues, features, ways of proper use and pitfalls. The questions and (known) causes of errors are connected to this.
Atomic Game Engine also had its own forums and its users did not come here expecting support.

If UrhoShark is a dead fish, consider switching to **rbfx** and feed it through use, feedback and maybe even development. Looking at the [graph](https://github.com/rokups/rbfx/graphs/contributors) @rku's been putting quite some effort into it and I believe one of the (maybe main) motivations for him to start that fork of Urho3D was to add C# support, which was out of the question for Urho3D and - as far as I'm concerned - still is. Not-containing-C# is exactly one of those things that *defines* Urho3D just like not requiring _boost_.

@rku How do you like this logo? 

[![rbfx](https://luckeyproductions.nl/images/rbfx.svg)](https://github.com/rokups/rbfx)
https://discourse.urho3d.io/t/setting-the-worldscale-of-a-node-with-a-parent-producing-confusing-results/5010/4

-------------------------

rku | 2019-03-09 18:42:45 UTC | #7

Logo looks too complicated ^_^

-------------------------

Modanung | 2019-03-09 18:53:43 UTC | #8

Better?  

![rbfx](https://luckeyproductions.nl/images/rbfx_2.svg)

-------------------------

rku | 2019-03-09 19:17:40 UTC | #9

Totally! Do you think a cogwheel would look better than star there?

-------------------------

Modanung | 2021-06-03 12:37:53 UTC | #10

![rbfx](https://luckeyproductions.nl/images/rbfx_3.svg)

-------------------------

rku | 2019-03-09 20:11:42 UTC | #11

Thanks! This is a great start and logo was indeed needed. I suck at art but this is already very workable even for likes of me :)

-------------------------

I3DB | 2019-03-09 20:34:02 UTC | #12

@mustacheemperor  How's your experience getting help with UrhoSharp?

-------------------------

Modanung | 2019-03-10 15:14:24 UTC | #13

[![UrhoConvert|333x210](upload://oID5Dj5kcMD2G5PSwWaiSMiTtdz.png)](https://global.discourse-cdn.com/standard17/uploads/urho3d/original/2X/a/ad3fb49e1041689202260bb2677b780ae2439fa5.png)

@I3DB Feeling better?

-------------------------

Leith | 2019-03-10 09:50:02 UTC | #14

Man, I felt this, but maybe it was just my bias, and not the lack of help I received.
Perhaps I asked the wrong questions - maybe I phrased them badly, I don't know.
The engine mostly works, and does not need me to nitpick, but that is what I do best - I can find the flaws and talk about them, sometimes I can be wrong too, this (should be) ok.
I'm not walking the well-trodden path toward urho dev, because the editor is broken in my working universe mostly. I can and should adopt scripting, outside the need for the editor. I know how cool warm-starting is, and how it can benefit me, without the need for the editor.

-------------------------

Modanung | 2019-03-10 16:31:54 UTC | #15

@mustacheemperor Could you maybe try to reproduce the issue using Urho3D?

-------------------------

