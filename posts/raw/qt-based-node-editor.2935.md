sabotage3d | 2017-03-21 16:51:38 UTC | #1

Hey guys I found this the other day. It seems like pretty decent node based editor if anyone is interested this is the repo: https://github.com/paceholder/nodeeditor

-------------------------

1vanK | 2017-03-21 18:28:50 UTC | #2

Qt lib has (L)GPL and commercical licenses only

-------------------------

TheSHEEEP | 2017-03-22 06:10:20 UTC | #3

[quote="1vanK, post:2, topic:2935, full:true"]
Qt lib has (L)GPL and commercical licenses only
[/quote]
Indeed. But... what about it?

-------------------------

cadaver | 2017-03-22 08:10:54 UTC | #4

Qt LGPL license is not a problem as long as you link dynamically. Because of its size and involved build process, it's not a good match for a Urho core dependency, but for user applications it's a perfectly fine choice.

-------------------------

TheSHEEEP | 2017-03-22 08:58:56 UTC | #5

Yeah, that's true. Qt does not make a good core dependency for a library that you want to link against in an own project.

-------------------------

sabotage3d | 2017-03-22 13:19:41 UTC | #6

I think the idea of a node based editor is more for game editor rather than embedding it in your game.

-------------------------

rku | 2017-03-22 13:44:30 UTC | #7

Is that why [my request](http://discourse.urho3d.io/t/profiler-rework-and-profiling-tool/2726/13?u=rku) on integrating qt profiler was ignored? I would appreciate the answer so i know where i should concentrate my efforts - Urho3D or Atomic.

-------------------------

cadaver | 2017-03-22 14:11:58 UTC | #8

Can't speak for others, but I have given myself permission to not comment one way or other if something doesn't particularly interest me. In this case you've met a bit of bad luck. You could consider just going directly to PR and see if you get stronger reactions then. If the existing real-time profiler (within Urho window) functionality gets broken, then that is a negative, which would point against merging it.

-------------------------

Enhex | 2017-03-22 17:56:49 UTC | #9

Another argument against Qt other than the LGPL license is that it isn't standard C++ with the use of MOC.

A new modern GUI library I tried recently is Nana:
https://github.com/cnjinhao/nana

Modern C++, Boost license, got all the features I want such as automatic layout, skinning, multi-window, docking, tabs, etc., without the bloat of full C++ frameworks like Qt that include more than just GUI.

-------------------------

sabotage3d | 2017-03-22 20:37:45 UTC | #10

I think the topic is about cool node based editor not Qt vs other GUI libraries.

-------------------------

TheSHEEEP | 2017-03-24 06:10:16 UTC | #11

[quote="Enhex, post:9, topic:2935, full:true"]
Another argument against Qt other than the LGPL license is that it isn't standard C++ with the use of MOC.[/quote]
A common, and wrong, misconception about Qt.

From the author of moc himself:
> I have read this many times, but this is simply false. The macros understood by moc to annotate the code are simply standard C++ macros defined in a header. They should be understood by any tool that can understand C++. When you write Q_OBJECT, it is a standard C++ macro that expands to some function declarations. When you write signals: it is just a macro that expands to public:. Many other Qt macros expand to nothing. The moc will then locate these macros and generate the code of the signal emitter functions, together with some additional introspection tables.

> The fact that your code is also read by another tool than the compiler does not make it less C++. I've never heard that you are not using vanilla C++ if you use tools like gettext or doxygen, which will also parse your code to extract some information.

I recommend the whole article, it debunks most of those old myths: https://woboq.com/blog/moc-myths.html

But anyway, I also got that this is just about the node editor the OP posted.
Speaking of which, I do like node editors for graphical work, so that is nice.
What I found utterly horrible is stuff like Unreal Engine's Blueprints.

-------------------------

godan | 2017-03-26 13:12:00 UTC | #12

@TheSHEEEP what is it about Unreal's Blueprints that you don't like? I'd be super interested to hear more, since I work a lot with node editors (although not Blueprints in particular).

-------------------------

TheSHEEEP | 2017-03-26 16:35:22 UTC | #13

[quote="godan, post:12, topic:2935, full:true"]
@TheSHEEEP what is it about Unreal's Blueprints that you don't like? I'd be super interested to hear more, since I work a lot with node editors (although not Blueprints in particular).
[/quote]
I just think they are extremely inefficient, lead to horrible code (I saw the code some of those produce when compiled) and become completely spaghetti-like for any real project.
You cannot beat the efficiency of just writing code.

They might be fine for prototyping, and are easier to get into than learning to code (I'll never agree that clicking together nodes is programming) but that's about it.

Of course, there are exceptions, like material editors, or what Iogram does.
But those work only because of the limited complexity.

-------------------------

Sinoid | 2017-03-27 05:57:48 UTC | #14

Personally, I use this node based editor http://algoholic.eu/qnodeseditor-qt-nodesports-based-data-processing-flow-editor/ as it was the easiest to adjust to an external arbitrary graph and the cleanest in implementation (even if I wasn't a fan of the code). It did help that I love the author's QSexyTooltip as well.

Code production is arguable. I won't weigh in there, but it can be done well. At least I'd like to think my approach does it well. (bias alarm)

-------------------------

godan | 2017-03-28 15:29:33 UTC | #15

@TheSHEEEP Yep, I mostly agree. I think it is a big mistake to try to implement a programming language in a node editor. While functions actually work quite well, logical flow and variables are horrible! Having to use 4-5 nodes just to do a simple comparison or sort is no good...although kind of a necessary evil when using such a platform.

However, I disagree that node editors can't be used for complex things - in fact, I think they are often better at that sort of stuff than doing simple things. Depends a lot on the implementation, though. Also, I think it *should* be possible to get decent, human readable, source code out of a node editor. It's something I'm researching.

-------------------------

slapin | 2017-04-05 09:44:55 UTC | #16

Also AI stuff is good with node editor.
The main reason these exist is to allow non-programmers to write some logic.
There are some data structures like behavior tree, which go well into node concept.
Also stuff like animation trees. If done well, these structures cooperate well with
written code, but you do not consider these structures as code per se, just some
data structure with nice editor. Making something serious (i.e. algorithmic code) with
node editors is proven ineffective a long time ago, node editors should operate with high-level
task-specific content. But if done right, these tools are very useful.

-------------------------

TheSHEEEP | 2017-04-05 09:55:45 UTC | #17

Well, that's something I can surely agree with.

-------------------------

