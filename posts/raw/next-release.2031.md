cadaver | 2017-01-02 01:12:25 UTC | #1

For core devs: Urho has accumulated new features and fixes quite a bit since last release. Should it already be time for 1.6, what significant work do you still have that you'd want in?

For myself, I have [github.com/urho3d/Urho3D/issues/1370](https://github.com/urho3d/Urho3D/issues/1370) in queue, plus clearing the recent pull requests which shouldn't take long.

-------------------------

yushli | 2017-01-02 01:12:25 UTC | #2

Look forward to the new release. 
I'd like to point out some issues I just have about the build system.
I am using windows 7, VS2015 64bit, with git bash as the command console. I clone the latest master branch, and start the clean build. It configures successfully. But when trying to run make in the bash, when building tolua++, it complains a workable c++ compiler can't be found. If I run make from VS command console, tolua++ compiles fine, but then when generating the libversion info it will causes error. If now I switch back to bash console, make runs fine. It seems like that
1. in bash console, tolua++ can not find the c++ compiler.
2. in VS console, it finds the correct c++ compiler, but can't run git to get the desired libversion info.
3. in bash console, it can get the libversion info. 

Not sure if it is just my machine or a general bug. Right now I can use both consoles to go on.

-------------------------

1vanK | 2017-01-02 01:12:25 UTC | #3

[quote="yushli"]Look forward to the new release. 
I'd like to point out some issues I just have about the build system.
I am using windows 7, VS2015 64bit, with git bash as the command console. I clone the latest master branch, and start the clean build. It configures successfully. But when trying to run make in the bash, when building tolua++, it complains a workable c++ compiler can't be found. If I run make from VS command console, tolua++ compiles fine, but then when generating the libversion info it will causes error. If now I switch back to bash console, make runs fine. It seems like that
1. in bash console, tolua++ can not find the c++ compiler.
2. in VS console, it finds the correct c++ compiler, but can't run git to get the desired libversion info.
3. in bash console, it can get the libversion info. 

Not sure if it is just my machine or a general bug. Right now I can use both consoles to go on.[/quote]

try execute in bash console:
[code]
set "PATH=%PATH%;c:\Program Files (x86)\Microsoft Visual Studio 14.0\Common7\Tools\;c:\Windows\System32;"
call vsvars32.bat
[/code]

and it will see VS

-------------------------

namic | 2017-01-02 01:12:25 UTC | #4

[github.com/urho3d/Urho3D/issues/1167](https://github.com/urho3d/Urho3D/issues/1167)

-------------------------

Lumak | 2017-01-02 01:12:26 UTC | #5

Sweet! I was going to start merging all my code changes from 1.4 to 1.5 but if 1.6 is near ready, I'll just wait for that and skip 1.5.

When is the expected release date?

-------------------------

cadaver | 2017-01-02 01:12:26 UTC | #6

"When it's done."

I know weitjong has the refactor-buildsystem branch going on, we very likely want that in first.

-------------------------

Lumak | 2017-01-02 01:12:27 UTC | #7

All good. I procrastinated merging my changes to 1.5 forever so waiting isn't a problem.

-------------------------

weitjong | 2017-01-02 01:12:28 UTC | #8

[quote="cadaver"]"When it's done."

I know weitjong has the refactor-buildsystem branch going on, we very likely want that in first.[/quote]

I have a number of things I plan to do in that branch. Most of them have already been documented in the GitHub issue tracker. However, I am not sure "when it will be done".  :wink:

-------------------------

cadaver | 2017-01-02 01:12:28 UTC | #9

It's fine by me if it takes time; if you hit some significant stall just shout out and we can reconsider, but in general I'd say that as the work is already started, it's better to get in the build system related changes before release, rather than wait to next version. And for those who are impatient the master branch can always be pulled for a reasonably well-working version :slight_smile:

-------------------------

dragonCASTjosh | 2017-01-02 01:12:28 UTC | #10

Personally i want to make some improvements with the PBR but i dont think its big enough to hold back a release

-------------------------

cosmy | 2017-01-02 01:12:29 UTC | #11

I would like to update some old dependencies.

-------------------------

Lumak | 2017-01-02 01:12:35 UTC | #12

I've been wondering about this for sometime and thought I should bring it up before release.
I wonder if we can add a source directory for a complete project, i.e. using Hexon as an example

   \Urho3D\Source\CompleteProject\Hexon\

Developers can contribute their completed project that they want to open source, and these project will not be tools or a simple samples.

*Edit - Never mind. Scratch this idea.  I'd imagine the size of the repository once ppl start adding full projects.

-------------------------

cadaver | 2017-01-02 01:12:35 UTC | #13

Complete project(s) are a great idea, but the engine repo should be just the engine. Will just need to link prominently (e.g. from the doxygen documentation & website)

EDIT: probably the best & strongest way to signal that you'd want a project included as a link, is to simply make a pull request towards Urho's documentation. The file in question is Docs/Urho3d.dox, at the bottom.

-------------------------

Modanung | 2017-01-02 01:12:38 UTC | #14

Would that mean adding a [b]Projects using Urho3D:[/b] list to the [url=http://urho3d.github.io/documentation/1.5/_external_links.html]External links[/url]?

-------------------------

1vanK | 2017-01-02 01:12:38 UTC | #15

[quote="Modanung"]Would that mean adding a [b]Projects using Urho3D:[/b] list to the [url=http://urho3d.github.io/documentation/1.5/_external_links.html]External links[/url]?[/quote]

We can create special wiki page for it, and every can add own projects there

-------------------------

cadaver | 2017-01-02 01:12:38 UTC | #16

[quote="Modanung"]Would that mean adding a [b]Projects using Urho3D:[/b] list to the [url=http://urho3d.github.io/documentation/1.5/_external_links.html]External links[/url]?[/quote]
That'd be the place in the documentation. The preference would be for projects that are good for learning.

-------------------------

yushli | 2017-01-02 01:12:38 UTC | #17

Sample projects, especially the finishing games, are good sources for learning. I myself learn a lot from these projects, such as FlappyUrho, Dissolving, selection outline, Hexon, etc etc. We really need a good place to display them and give the authors the well deserved recognition.

-------------------------

Lumak | 2017-01-02 01:12:39 UTC | #18

Yes, having a web site that can provide links to completed projects would work. I'm afraid that w/o something like this, all those work would get lost eventually.

-------------------------

Modanung | 2017-01-02 01:12:39 UTC | #19

[quote="cadaver"]The preference would be for projects that are good for learning.[/quote]
Does that exclude closed-source projects from being listed?

-------------------------

yushli | 2017-01-02 01:12:39 UTC | #20

Add a showcase section for these would be nice.

-------------------------

cadaver | 2017-01-02 01:12:39 UTC | #21

[quote="Modanung"][quote="cadaver"]The preference would be for projects that are good for learning.[/quote]
Does that exclude closed-source projects from being listed?[/quote]

The Urho repo external links .dox page should IMHO list open source projects only; as that's what is already there (e.g. the Blender exporter). Other (closed) projects could be listed anywhere else.

-------------------------

weitjong | 2017-01-02 01:12:39 UTC | #22

This is rather off topic but we do have a "showcases" category in our website's news entry. Currently it is only myself who is updating the news entry and I have not been doing that lately. Over there I suppose there is no limitation of what could be listed. If I really want to and if I have enough time, it is also possible to have a permanent "ShowCase" section in our main home page.

-------------------------

Lumak | 2017-01-02 01:12:41 UTC | #23

I downloaded 1.5 to get an early start on preparation for 1.6 release.  I noticed that cmake revision is now 3.2.3 and I had 3.2.2 with urho 1.4. 
I went to cmake site to get a never version and noticed that they're up to 3.6.0rc1 and the latest 3.5.2. 

Will we be upgrading to 3.5.2 before release or should I just stick with 3.2.3?

-------------------------

Lumak | 2017-01-02 01:12:41 UTC | #24

I'm not favoring the new samples build option.  It's either all or none build option now. I much preferred the older way where you can comment out the ones you don't want to build.
I'm sure I can just drop the old cmakelist.txt and it will revert back to the old way.

-------------------------

weitjong | 2017-01-02 01:12:41 UTC | #25

3.2.3 will be the new minimal version required to build Urho3D. You can always and actually recommended to install any newer version than that on your system. As for the samples, if you don't mind to dirty your hand to comment off the code in the past, you may as well enhance the code to have a white or black list variables. Now to think about it, actually we do already have a blacklist/exclusion-list :slight_smile:.

-------------------------

Lumak | 2017-01-02 01:12:41 UTC | #26

I'll look into this blacklist that you've mentioned - have to get more familiar with 1.5.  In regards to cmake, I typically don't deviate on the build tools other than what's delivered with the release.  Because you know, if something goes wrong you'll pay the price and time trying to figure out what's wrong. I'm good with 3.2.3.

-------------------------

weitjong | 2017-01-02 01:12:41 UTC | #27

I hope I could find some time to start work on the refactor-buildsystem later. The 3.2.3 is set as minimal version for all the host systems (not just for Windows) in that branch. As I said before, that version is the minimal required. We are forced to choose that version because of the Linux host system that used by by our CI only has the highest 3.2.3 being back-ported to Ubuntu 12.04 LTS, or otherwise we would have chosen the latest version available. Personally I install the latest version available in the my OS package manager.

-------------------------

TheComet | 2017-01-02 01:12:45 UTC | #28

I was hoping I could finish work on my inverse kinematic contribution. I'm currently in the middle of exam hell though. My finals are over in 4 weeks, from there I estimate it will take perhaps a week, maybe two, to finish this.

[url]http://discourse.urho3d.io/t/inverse-kinematics/1819/1[/url]

-------------------------

cadaver | 2017-01-02 01:12:50 UTC | #29

I now have one more thing for my list, graphics API agnostic headers. It's not critical, but would be nice to have. [github.com/urho3d/Urho3D/issues/1422](https://github.com/urho3d/Urho3D/issues/1422)

-------------------------

weitjong | 2017-01-02 01:13:15 UTC | #30

I don't know about the progress of others, but I want to report that I am not sure when I could finish my work on the "refactor-buildsystem" branch. The more I dig, the more things come up on my to do list, and I am having a little problem with prioritization  :wink: .

-------------------------

TheComet | 2017-01-02 01:13:15 UTC | #31

I have run into some unforeseeable problems with IK and applying angles to AnimatedModel. On the plus side, exams are done.

-------------------------

cadaver | 2017-01-02 01:13:15 UTC | #32

[quote="weitjong"]I don't know about the progress of others, but I want to report that I am not sure when I could finish my work on the "refactor-buildsystem" branch. The more I dig, the more things come up on my to do list, and I am having a little problem with prioritization  :wink: .[/quote]
Thanks for the heads-up! In that case it makes sense to start moving toward release with no more big features going in.

-------------------------

yushli | 2017-01-02 01:13:15 UTC | #33

Will ParticleEffect clone method be implemented in this release?

-------------------------

weitjong | 2017-01-02 01:13:16 UTC | #34

[quote="cadaver"][quote="weitjong"]I don't know about the progress of others, but I want to report that I am not sure when I could finish my work on the "refactor-buildsystem" branch. The more I dig, the more things come up on my to do list, and I am having a little problem with prioritization  :wink: .[/quote]
Thanks for the heads-up! In that case it makes sense to start moving toward release with no more big features going in.[/quote]
The only slight complication is that a few of my commits are actually bug fixes and so does a few new items in my todo list. I actually quite surprise how our buildsystem works so well  :laughing: with them.

-------------------------

cadaver | 2017-01-02 01:13:16 UTC | #35

Would it make sense to merge those fixes (including the upcoming ones if critical) where possible or appropriate before release, even though the branch in total isn't completed yet? There's certainly no absolute hurry for a release.

-------------------------

weitjong | 2017-01-02 01:13:16 UTC | #36

Yes, I think so. It should be possible to quickly cherry-pick those just before the release. I made no promise on those still unimplemented though cause they could be related to other more breaking changes I have in mind. Let me know ahead your release plan and I will see to it.

-------------------------

cadaver | 2017-01-02 01:13:16 UTC | #37

I have vacation until end of July and I'd like to mostly keep it as vacation :slight_smile: so I'd aim for beginning half of August to prepare the release, if that's OK. That also lets the Graphics API changes get a bit more testing, hopefully.

-------------------------

jenge | 2017-01-02 01:13:30 UTC | #38

@cadaver I am in the process of updating Atomic with Urho changes since September of last year, this should help with testing the renderer changes.  Great work on that by the way, saving a fair amount of code duplication while simplifying  :smiley:

-------------------------

cadaver | 2017-01-02 01:13:30 UTC | #39

Thanks, that should certainly help. I just typed the initial changelog from commits and it was quite massive. :slight_smile:

-------------------------

jenge | 2017-01-02 01:13:33 UTC | #40

@cadaver Happy to report success on Windows (D3D9/D3D11), Mac, Linux, Android, iOS, and WebGL here, great work!  I won't be landing this to the master branch quite yet, though great to have the rendering agnostic stuff in! Updating to SDL 2.0.4 also fantastic, really cool that SDL is compiled for emscripten from source now... was using the -s USE_SDL=2 version :slight_smile:  THANKS!

-------------------------

cadaver | 2017-01-02 01:13:33 UTC | #41

Thanks for the quick test report! I will still run some personal sanity check builds but otherwise we're getting very ready to go.

-------------------------

slapin | 2017-07-08 05:52:08 UTC | #43

Well, there are some unfixed bugs like IK bug by @TheComet et al. would these be included in release notes?

-------------------------

cadaver | 2017-07-08 10:08:08 UTC | #44

1.7 release is indeed waiting for the IK bugfix PR. It and all other changes will be included in the changelog when it's time.

Now, my personal opinion is that releases in Urho are not important. Using the current master branch "head" is the best way to get the newest features, and it's rarely broken.

Though, in the case of this release, we've agreed that post 1.7, we would start introducing use of C++11 more, so in that sense it's more important than usual.

-------------------------

TheComet | 2017-07-10 16:17:15 UTC | #45

So sorry, I feel bad for postponing the IK fixes for this long (I only *just* finished all of my finals and still have an overdue report to complete). Can this still wait a few days?

-------------------------

cadaver | 2017-07-10 16:58:36 UTC | #46

Yes, there's no absolute hurry now. Somewhere in July is quite perfect for me personally as I have my summer holiday now.

-------------------------

ucmRich | 2017-07-17 06:22:43 UTC | #47

Looking forward to the 1.7 release for the improved C++11 support - are there any plans to start C++14 support down the line somewhere too?

-------------------------

Eugene | 2017-07-17 15:18:24 UTC | #48

The problem is that even Visual Studio 2015 doesn't support C++14 standard completely. To be honest, neither C++11...

-------------------------

cadaver | 2017-07-17 15:44:49 UTC | #49

Note that 1.7 is going to be just like the current master, which doesn't use C++11 much yet, or mandatorily. So even C++11 work starts only more heavily after that.

-------------------------

ucmRich | 2017-07-19 06:37:35 UTC | #50

I have been spending some time reading through the docs as I get a chance. I was wondering if there is going to be any major fundamental difference between the released v1.6 and the upcoming release of v1.7 -- Specifically; I am going to start out with LUA so for instance would any functions (or LUA-specific capabilities) be changed or deleted between 1.6 and 1.7 ?

Also, if i may, i'm pretty new to git and GitHub - I understand that the HEAD is where the latest up-to-date bug-fixes and changes are but how much has advanced since the Aug 2016 v1.6 release?

_INFO: I am developing using gEdit on Linux Mint 18.2 -- my target platforms are going to be Ubuntu-derivatives of Linux as well as Android 5+ devices, (don't care about iOS or windows or html, atm) also plan to get on the pi eventually...._

-------------------------

Eugene | 2017-07-19 07:03:35 UTC | #51

You could check all breaking changes here:
https://urho3d.github.io/documentation/HEAD/_porting_notes.html

> but how much has advanced since the Aug 2016 v1.6 release

Who knows? You shall revise every commit for the last year to find it out.
AFAIK, @cadaver usually do this work before release.

-------------------------

weitjong | 2017-07-19 07:11:44 UTC | #52

Assuming you are in the HEAD of master branch, execute: "git diff 1.6" or "git difftool 1.6" if you have configured a GUI tool, like "meld". Could usually use [GitHub web interface](https://github.com/urho3d/Urho3D/compare/1.6...master), however, this time round the diffs are too big to be displayed all.

-------------------------

ucmRich | 2017-07-19 08:23:48 UTC | #53

Sweet, thanks guys :slight_smile:

I've been reading tutorials and watching videos trying to get my head around git. many thanks for the git commands, i think that's perfect for what i need :+1:

-------------------------

cadaver | 2017-07-19 09:34:11 UTC | #54

What I do is I just basically go through all commit messages and try to condense them, then sort into a few categories, like editor, build system, bugfixes. New important features usually go into the very top. Not very scientific :) For breaking changes, the "porting notes" is indeed most important.

-------------------------

QBkGames | 2017-07-26 03:05:30 UTC | #55

How do you go about contributing to the engine, do you just pull from GitHub and push back your changes? Is there a core reviewer/moderator/QA you have to go through first (or after)?
What system is in place to prevent code pollution (anyone just changing anything)?

-------------------------

Eugene | 2017-07-26 09:01:18 UTC | #56

[quote="QBkGames, post:55, topic:2031"]
do you just pull from GitHub and push back your changes?
[/quote]

Some devs just push changes, I prefer to use PRs to check changes by CI first.

[quote="QBkGames, post:55, topic:2031"]
What system is in place to prevent code pollution (anyone just changing anything)?
[/quote]

Anyone cannot push changes to the main repo directly. All garbage is caught during PR review.

-------------------------

QBkGames | 2017-07-27 03:18:13 UTC | #57

Thanks for the reply.
I didn't quite understand "check changed by CI first" as I'm not sure what CI stands for (and I'm supposing PR = Peer Review).
Given that I'm new here, I would like to confirm what I have in mind with the people in charge of the project, before doing any work. How do I go about that? Do I just post a proposal here, or open an new conversation thread?

-------------------------

slapin | 2017-07-27 03:21:56 UTC | #58

These are not about crippled corporate ClearCase terms. These are terms for
CI=Continuous Integration and PR=pull request (git thing, but in this particular case - github thing).

So what are you selling?

-------------------------

QBkGames | 2017-07-29 09:50:36 UTC | #59

Something small to start with.

I would like to combine all Random related functionality (which is now in 2 places: Random and MathDefs), into a single static class (so is also looks more OO). So then you would use something like:
_Random::GetInt(int range)_
_Random::GetFloat()_, etc

Also, I need some extra functionality for my game, which I think might be useful to others and thus should  be in the engine, such as getting a random point inside a Rect or Circle areas, etc.

How's my offer? Are you buying it :) ?

-------------------------

slapin | 2017-07-28 01:24:57 UTC | #60

I think you could send PRs via github one small feature at time and see how it goes, it is easier to discuss when the code is unleashed.

-------------------------

SirNate0 | 2017-07-29 03:39:01 UTC | #61

Personally I prefer such functions as just functions - I don't like putting functions in classes just to do it (e.g. Java's Math class), especially when it is a case like this where it adds 5 characters to the name (::Get) yet gives no extra clarity. And in this case I think you could get the same benefits just by using namespace Random...
Then again, I'm neither a huge fan of OO programming nor have I looked at the files in question, so perhaps there is relevant state to be put in class Random, or something else I'm missing.
Regardless, moving it all into one header seems like a good idea.

-------------------------

Eugene | 2017-07-29 08:08:06 UTC | #62

Note that your changes shall not break existing code until extreme necessity.
Good test for it is to _never_ change samples when you edit Urho core.

-------------------------

QBkGames | 2017-07-29 10:09:25 UTC | #63

We could keep existing functions as simple wrappers that call functions of the new Random class and if there is a mechanism to mark functionality as deprecated (?), than we can use that on them.

(Talking about samples, they are still running in 800x600 window, that's so '90. We are in XXI century, they should run in at least 1280x720).

-------------------------

QBkGames | 2017-07-29 10:07:46 UTC | #64

Anyway, I'm currently working on a big project and have a tight deadline, so I don't have time to play around.

Is there someone in charge who can just tell me to go ahead with it or to forget about it?

-------------------------

cadaver | 2017-07-29 14:46:25 UTC | #65

In theory I'd be the authority as the original author, but in practice I've been slipping in to a degree of semi-retirement already and do not promise to have an opinion on every proposed change. So, it comes down to whoever of the core devs is interested / has a strong opinion on the matter. But it may turn out that no-one has, so if the prospect of this would offend you, then it's safer to not contribute.

In general, the nature of PRs is that you risk doing "wasted" work. And yes, I agree too that tangible code is easier to review than just a forum post.

-------------------------

QBkGames | 2017-07-30 00:22:43 UTC | #66

Cadaver, thanks for clarifying the situation. I started getting the feeling that it's best for me in my current situation (and stress level) to just keep to my own thing, and leave the contributing for later on when I have more time.

So, for now I'll just stick to reporting bugs and maybe making suggestion.

-------------------------

1vanK | 2017-08-04 10:30:02 UTC | #67

What about replacing
```
template<class T>
```
to
```
template<typename T>
```
(MathDefs.h for example)

-------------------------

Eugene | 2017-08-04 10:34:09 UTC | #68

I'd like to replace in the opposite way. So, it's probably better to avoid replacing at all...

-------------------------

1vanK | 2017-08-04 10:35:46 UTC | #69

What do you mean by "replace in the opposite way"?

-------------------------

TheComet | 2017-08-04 10:49:00 UTC | #70

Not sure where to ask this, but one of the things that really confused me when I first started using Urho3D was trying to understand what SharedPtr does. I think this is a terrible name for this class because I confused it with how std::shared_ptr works.

A far better name in my opinion would be ```Ref``` or ```Reference``` or even ```StrongRef```. The same goes for ```WeakPtr``` which I think would better be named ```WeakRef```.

Is renaming this still viable this far into the project? I realise it's a huge change, but I also realise that this wouldn't be the first time Urho3D renamed something (the last example I can think of was renaming ```OBJECT()``` to ```URHO3D_OBJECT()```.

Thoughts?

-------------------------

Eugene | 2017-08-04 11:18:11 UTC | #71

[quote="1vanK, post:69, topic:2031, full:true"]
What do you mean by “replace in the opposite way”?
[/quote]

I mean, use `class` instead on `typename`. That's pretty holywarable point of C++.

[quote="TheComet, post:70, topic:2031"]
A far better name in my opinion would be Ref or Reference or even StrongRef
[/quote]
Too generic name, IMO. And SharedPtr and WeakPtr is not a reference in C++ meaning.
`IntrusivePtr` is more fair but I doubt it worth.

-------------------------

yushli1 | 2017-08-04 11:25:54 UTC | #72

SharedPtr is better than other names. The same is WeakPtr. 
Looks like there are many different opinions and preferences. We may need Cadaver to at least examine the final decisions before any major changes happen.

-------------------------

TheComet | 2017-08-04 11:44:38 UTC | #73

If you look at other projects, they all use "Ref" to refer to an intrusive reference counted object.

Python's ```Py_INCREF``` and ```Py_DECREF```, Gtk's ```reference()``` and ```unreference()```, I remember the JNI also calling it references.

Even Urho3D uses the word "reference", the objects implement _Urho3D::RefCounted_ after all. Incrementing the reference count is known as "holding a reference" and I think the object that does this (in this case, SharedPtr) should be named after what it actually does.

If I go and talk to a colleague and say "yeah it's a shared pointer", this will raise a lot of questions. What do you mean by "shared"? If on the other hand I say "yeah it's a reference to an object" then it is immediately clear what this means.

-------------------------

1vanK | 2017-08-04 11:58:39 UTC | #74

[quote="Eugene, post:71, topic:2031"]
I mean, use class instead on typename. That’s pretty holywarable point of C++.
[/quote]

But "typename" was added specifically for this case.

For example
```
template <class T>
inline T Sign(T value) { return value > 0.0 ? 1.0 : (value < 0.0 ? -1.0 : 0.0); }
```
T can be float, double... How does this relate to a class?

-------------------------

TheComet | 2017-08-04 12:03:46 UTC | #75

@cadavar What files do I need to create/edit to have an entry about inverse kinematics on this page?
https://urho3d.github.io/documentation/1.6/index.html

-------------------------

S.L.C | 2017-08-04 12:31:08 UTC | #76

@TheComet I suppose we can have it both ways:

    template < class T > using WhateverAlias = SharedPtr< T >;

As for the `class` vs `typename` debate. I do agree with @1vanK to some degree. For example, I use both. `class` when I'm likely to specify a non primitive type and `typename` when I'm definitely going to specify a primitive type. Somehow using `class` for both is confusing to me.

-------------------------

Eugene | 2017-08-04 12:44:39 UTC | #77

[quote="1vanK, post:74, topic:2031"]
But “typename” was added specifically for this case.
[/quote]

Nope. `typename` was added for dealing with nested template types. And some dumb in committee somewhy decided that it is good idea to allow using both words in the template declaration.

[quote="TheComet, post:73, topic:2031"]
they all use “Ref” to refer to an intrusive reference counted object
[/quote]
C++ has explicitly specified meaning of the word "reference". If you call something "reference" in the C++, you must guarantee that it is non-zero. RefHolder is ok: it isn't reference, but holder. Holder may hold nothing, but reference mayn't refer to nowhere.

-------------------------

1vanK | 2017-08-04 12:58:06 UTC | #78

>> And some dumb in committee

nice argumentation...

-------------------------

Eugene | 2017-08-04 13:06:24 UTC | #79

[quote="1vanK, post:78, topic:2031"]
nice argumentation…
[/quote]

They can have allowed only one word, either class or typename. It's ok. But they allowed both... Damn, I hate such situations. It's f~n mess in the language.

-------------------------

1vanK | 2017-08-04 13:09:08 UTC | #80

it just backward compatible

EDIT: Just explain why you like class and not typename

-------------------------

Eugene | 2017-08-04 13:19:57 UTC | #81

[quote="1vanK, post:80, topic:2031"]
it just backward compatible
[/quote]

I can accept this excuse for most of C++ problems (e.g. `class` and `struct` similarity), but not for this, because both `class` and `typename` were introduced in the C++98.

[quote="1vanK, post:80, topic:2031"]
Just explain why you like class and not typename
[/quote]
Just my preference without any pros or cons. Maybe because it's shorther.

-------------------------

1vanK | 2017-08-04 14:48:46 UTC | #82

[quote="Eugene, post:81, topic:2031"]
I can accept this excuse for most of C++ problems (e.g. class and struct similarity), but not for this, because both class and typename were introduced in the C++98.
[/quote]

Do you mean templates not existed before adding "typename" keyword?

-------------------------

Mike | 2017-08-04 14:54:00 UTC | #83

[quote="TheComet, post:75, topic:2031"]
@cadavar What files do I need to create/edit to have an entry about inverse kinematics on this page?
[/quote]


This is this [file](https://github.com/urho3d/Urho3D/blob/master/Docs/Reference.dox) (content) :unicorn:
and this [one](https://github.com/urho3d/Urho3D/blob/master/Docs/Urho3D.dox) (menu)

-------------------------

TheComet | 2017-08-04 14:50:34 UTC | #84

Can... Can that file be split up into smaller files?

-------------------------

cadaver | 2017-08-04 14:51:42 UTC | #85

You will see the main index in beginning of Urho3D.dox (under the heading mainpage). Add links there to make them show up on the "front page".

-------------------------

TheComet | 2017-08-04 14:59:32 UTC | #86

Where would be the best place to add the IK user guide? There seem to be two main places where things are documented (the .dox files and the [official wiki](https://github.com/urho3d/urho3d/wiki)). I even see someone created an empty page for it in the wiki.

-------------------------

cadaver | 2017-08-04 15:33:09 UTC | #87

I'd recommend a sparse but sufficient guide to the .dox files, similar to graphics, UI etc. pages. Additional examples can then be put to the wiki.

-------------------------

slapin | 2017-08-04 16:23:36 UTC | #88

I'd say when doing some changes like this, please make sure these work with gcc-4.7-4.9. I will be really thankful. Yes, these can do c++11 but there are some limitations. And yes, that makes Urho more cross-platform.

-------------------------

slapin | 2017-08-04 16:28:04 UTC | #89

Yes, if you follow C++ debates, especially recent ones, there are many strange things suggested.
If there were less sane old league people in there, we'd have it much worse than now.

-------------------------

1vanK | 2017-08-04 16:52:19 UTC | #90

travis check every commit (I do not known used version of gcc)

-------------------------

TheComet | 2017-08-04 19:25:49 UTC | #91

Can I add animated gifs to aid my explanations?

-------------------------

weitjong | 2017-08-05 02:27:30 UTC | #92

I see no point to use ancient GCC version as any excuse to hold us back. We can scrap the Travis CI even if/when we have outgrown it.

-------------------------

weitjong | 2017-08-05 02:33:25 UTC | #93

We have upgraded our Travis CI setup to be ready for C++11 development one or two months ago.

-------------------------

Eugene | 2017-08-05 07:44:53 UTC | #94

[quote="slapin, post:88, topic:2031"]
that makes Urho more cross-platform
[/quote]

May you please list platforms supported by gcc-4.9 and not supported by gcc-5x-6x-7x?

-------------------------

Modanung | 2017-08-05 09:56:13 UTC | #95

[**Repology**](https://repology.org/) aims to do exactly that.

-------------------------

TheComet | 2017-08-05 10:08:42 UTC | #96

If you want to support Gentoo, those guys are still stuck on gcc-4.9 because some third party libraries still haven't adapted to the C++11 ABI change. :stuck_out_tongue:

-------------------------

weitjong | 2017-08-05 13:59:04 UTC | #97

The 4.8.1 is the first GCC version that has full support of C++11 standard. So, using 4.9 should be fine and that's part of the plan. But don't think we will give a damn on 4.7.x and 4.8.0.

-------------------------

slapin | 2017-08-05 11:49:39 UTC | #98

It is not about "theoretical" support, it is about vendor-provided SDKs for platforms
and other stuff like this, i.e. nobody made new compiler for the platform because
they already have new platform with new stuff and users of older platforms should
save themselves.
Not that I'm insist, but I'd ask about not breaking compatibility just to add new compiler
feature. gcc-4.7,4.8,4.9 do support a lot of C++11 stuff. 
The actual status: https://gcc.gnu.org/gcc-4.7/cxx0x_status.html

If any of No's are planned to be used in short term, please let me know, so I could yell
about them. Also I do not ask for something ridiculous , as 4.7-4.9 versions of gcc
are not so ancient. These are actually quite common in use.

Of course I don't mean that if something is really cool and improves development speed x2
and older compilers would block. I just talk about using new stuff because it is new, not because it is good.

-------------------------

weitjong | 2017-08-05 12:18:00 UTC | #99

Those that want to stay with ancient compiler, can of course just stay with the old version of Urho3D and other 3rd-party libs. We are not forcing anyone to upgrade with us.

-------------------------

S.L.C | 2017-08-05 16:20:07 UTC | #100

Out of curiosity. Will there be a series of macros available where various other features could be identified at compile time? For example, the presence of c++14/17 etc. And some individual features from these versions that are likely to have a bit of importance. Like extended `constexpr` from c++14. And various other type traits that are likely to make certain code simpler and/or easier for a compiler to do some optimizations.

Basically, have a header like `Config.h` which tests against various features and makes them identifiable as macros. To be honest, this doesn't sound very friendly and I'm a bit skeptical about having macros be a big part of a project. Especially when c++11 will be agreed as the primary standard. So I'm just curious if there'll be something like this.

But c++14 did add a few useful features that are supported even by "older" compilers like GCC 4.9.x. And would be a shame to have to go through various workarounds due to some "limitations" in c++11 or things that were simply not included but possible. No to mention the plethora of things that were removed from c++11 with more recent standards.

-------------------------

cadaver | 2017-08-05 17:05:59 UTC | #101

The .dox pages don't use images at all so far, so it would be more keeping in tradition if you didn't. These would be good for the wiki I believe. If you absolutely need to add images though, I don't think we will reject the PR just because of that.

-------------------------

