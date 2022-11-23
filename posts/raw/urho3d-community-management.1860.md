Lunarovich | 2017-01-02 01:10:49 UTC | #1

Hello! As a newcomer to Urho3D, the first thing I've noticed is that there is no
- facebook page/group
- twitter account
- youtube page

IMO, those are needed not only to attract new users, but also to keep alive and strengthen the current user base. Personally, I like, in my free time, to watch videos or read about other's achievements using a certain software, for example. 

So, I think that it would be really nice if we had a proper Urho3D community management. What do you think? Should we and how could we develop an Urho3D community beyond the frontiers of this forum?

-------------------------

hdunderscore | 2017-01-02 01:10:49 UTC | #2

Building the community is definitely important (and I think urho has a pretty active and helpful community atm), although it's a time consuming thing to do too. We have a decently active IRC channel on freenode, that's probably the most active thing we got going on unofficially.

Gitter is another option we could throw onto the table.

-------------------------

cadaver | 2017-01-02 01:10:49 UTC | #3

To put a bit bluntly, Urho3D is a developer-oriented and somewhat hard to use engine. That is unlikely to change, except with a lot of effort.

If someone is turned away from Urho3D due to the lack of those things you listed, it's probably for the better (the same could be said of the periodically reappearing 'roadmap' discussion.)

That said, if there is willingness from someone here to devote time to e.g. making a Facebook page, I have nothing against it. However there is a risk involved should the person responsible lose interest. Right now the github project is in good health, as well as these forums, and they have evolved naturally. Any expansion to other channels should be similarly natural.

-------------------------

Lunarovich | 2017-01-02 01:10:49 UTC | #4

Thanks for the answer. I will join the IRC channel.

What about fb page and twitter? At the basic level, those are not too time consuming or too difficult to manage?

[b]EDIT[/b] I've written the above before I saw the cadaver's reply. OK, I understand that Urho3D is a developer-centered engine. However, only difficulty I've found was how to get the first project up and running. Afterwards, everything seems easy and logical. And I should mention you that I come from the world of javascript and GUI game dev and that I'm learning c++ along the way. 

IMO, there are lot of developers who are code-centered and who would like to use Urho3D but have never heard about it, I suppose. I've just twitted about it. I would like to put up a fb page, but since I'm a new comer, don't want to be imposing or else.

-------------------------

thebluefish | 2017-01-02 01:10:51 UTC | #5

[quote="Lunarovich"] I would like to put up a fb page, but since I'm a new comer, don't want to be imposing or else.[/quote]

Community management is typically a dedicated job. If other people haven't yet expressed interest in doing this, I don't see why we should turn away a newcomer   :wink:

-------------------------

Lunarovich | 2017-01-02 01:10:51 UTC | #6

OK. I've just created a FB page. If the admins/devs find it intrusive, I will delete it. 

[url]https://www.facebook.com/Urho3D/[/url]

If not, I have a question. I would like to proceed to creating some galeries on the page. I would like to take pictures that users post to this forum. Now, I suppose that no one would complain. Just in case, is it OK to simply take photos and post them on the FB page with proper credits given to authors?

-------------------------

cadaver | 2017-01-02 01:10:51 UTC | #7

On the Showcase forum, there is a special rule that by posting there you agree that the content may be republished by the Urho website (urho3d.github.io). This can be expanded to include the FB page. Otherwise you generally can't publish things without permission.

The "About" text on the FB page seems to be clipped. The "Inspired by" part is not important, so it can be removed.

-------------------------

Lunarovich | 2017-01-02 01:10:51 UTC | #8

Ok. Thanks. I removed the inspired part. The text was effectivly truncated. I will proceed to the galery creation.

-------------------------

gawag | 2017-01-02 01:10:53 UTC | #9

[quote="cadaver"]To put a bit bluntly, Urho3D is a developer-oriented and somewhat hard to use engine. That is unlikely to change, except with a lot of effort.[/quote]
(Could be worth an own thread but:) What do you mean by that? Is that some kind of design decision like "Focus on performance instead of ease of use"?
It's a Game Engine and not just a Graphics Engine like Ogre which makes it already easier as Ogre IMHO. The only other engine I know a bit is CrystalSpace and that was pretty broken (at least back then).
Or opposed to Unity or Unreal with these editors where you click stuff together like in the Blender Game Engine? Those are weird.
Also we could try improving the usability, that has always been one of my main concerns (thus all the wiki work) and I'm currently a bit working on that. Could someone name things that could be improved without sacrificing performance? (better a new thread if someone has ideas)

[quote="cadaver"]If someone is turned away from Urho3D due to the lack of those things you listed, it's probably for the better (the same could be said of the periodically reappearing 'roadmap' discussion.)[/quote]
What's wrong with a "there might by X, Y and Z coming"-roadmap? Fake promises? That the implementation is too uncertain? PBR looks pretty good currently for example, other things that are in a prototype state but look promising could be named too.

About social media:
I myself am not using Facebook at all, Twitter only rarely and passively (but a lot of Youtube). Are developers using those or is there a general aversion from developers?
I'm tending to something in that direction though. I used the "Message Wall" in the old Unofficial Wiki as some kind of blog ([github.com/damu/wiki](https://github.com/damu/wiki), not much in there yet though).
I would appreciate some kind of connectivity, "hubbing", news page or whatever you wanna call it. Not sure about what to use though as I'm not really a social media guy (I don't like Facebook but I'm >=neutral to all others).
I would participate, if we find something good. It should be reliable about displaying all posts, not like Facebook which I heard is weird in that way. Notifications with subscribeable topics would be good too.

BTW: there are some Youtube channels with Urho stuff: codemonkey ([youtube.com/results?search_query=urho3d](https://www.youtube.com/results?search_query=urho3d)
Oh Twitter seems also having a lot: [twitter.com/search?q=Urho3D](https://twitter.com/search?q=Urho3D)

*starts super secured Tor Browser to go to the Facebook page*
Suggestions about what to use? What are your opinions about the available options? Is Facebook usable and less bad as I think?

-------------------------

cadaver | 2017-01-02 01:10:53 UTC | #10

The developer-orientedness comes from a simple lack of resources, it's not intentional but simply the reality of the situation. For example, the editor was greatly improved by a number of people, but many of them became inactive.

To "lift" Urho3D to the tier of truly user-first engines (such as Unity) requires a huge leap in effort, so I'd rather have the community resources reflect that reality.

Now our active userbase seems to be mostly people who understand this and are OK with it, with just a few notable exceptions. Creating more active (social) media presence can draw in more people who are more novice-level, and who expect that Urho3D gets regular and extensive new features, while they contribute nothing back, and while we don't have the actual developer resources to respond to those requests.

For the "roadmap" thing, yes it could easily become outdated or too optimistic and therefore be "fake" like you say, whereas the Github issue tracker (mostly) reflects the reality of development. PBR is now listed there as a future issue that will be worked on.

-------------------------

Lunarovich | 2017-01-02 01:10:54 UTC | #11

[quote]Also we could try improving the usability, that has always been one of my main concerns (thus all the wiki work) and I'm currently a bit working on that. Could someone name things that could be improved without sacrificing performance? (better a new thread if someone has ideas)[/quote]

The most difficult thing for me, that kept me for months away from Urho3D, was the fact that I did not know how to start the damn thing :slight_smile: If I was provided with a working example of c++ minimal "hello world" that I could simply compile, modify and see effects, I would certainly start using Urho3D earlier. 

I'm not talking about already existing compiled examples in the static, pre-compiled version of the engine. I'm not talking about script examples that you can modify and run with the player. I'm talking about a possible pre-provided Code::blocks c++ project, for example, that I can simply download from the internet, bundled with the needed libraries and jump straight in. 

I had to spand a day to figure out just how to compile the engine and setup a first working minimal project. I admit, I come from the world of JS development, and things are obviously much simpler there. However, if we had a simple bundled project that can be compiled and run, then even newcomers to C++ could start bashing Urho3D right away :slight_smile:  

Now, for the advancement of FB page. I'm still in the process of gathering materials for galeries. You can see collections of images I gathered so far here: [url]https://www.pinterest.com/darkodraskovic/[/url]. Just look for the boards prefixed with Urho3D. This way I can have a platform independent collection of images that we can use for any other purpose. 

[quote]I would appreciate some kind of connectivity, "hubbing", news page or whatever you wanna call it. Not sure about what to use though as I'm not really a social media guy (I don't like Facebook but I'm >=neutral to all others).[/quote]

I don't like FB myself either and fully subscribe to this: [url]https://www.youtube.com/watch?v=BBUNNbgrXQM[/url]. However, FB is became a necessity these days, specially if you want to get visibility. Sure, we can have the same or even better functionality on other platforms. However, there are no groups like this ([facebook.com/groups/IndieGameDevs/](https://www.facebook.com/groups/IndieGameDevs/)) on other platforms that have nearly 60k members and growing. 

P.S. I was amazed to see how mayn Urho3D mobile published games are out there.

-------------------------

gawag | 2017-01-02 01:10:54 UTC | #12

[quote="cadaver"]The developer-orientedness comes from a simple lack of resources, it's not intentional but simply the reality of the situation. For example, the editor was greatly improved by a number of people, but many of them became inactive.
To "lift" Urho3D to the tier of truly user-first engines (such as Unity) requires a huge leap in effort, so I'd rather have the community resources reflect that reality.[/quote]
Could you give some more examples of required stuff for "user-first" engines besides the editor? More like other external tools like material and particle editors or more as in engine behavior and API changes?
The things bothering me are not a "huge leap", maybe that's because I'm coming from Ogre and CrystalSpace and not those giant Unity/Unreal things.

[quote="cadaver"]
Creating more active (social) media presence can draw in more people who are more novice-level, and who expect that Urho3D gets regular and extensive new features, while they contribute nothing back, and while we don't have the actual developer resources to respond to those requests.[/quote]
Hm, I'm not sure how much it is expected to get regular new features. If the engine can kinda do what other modern engines can do (in the result, like: effects (PBR,...), physic,...) and if it fits the needs of the people who want to use it, I don't think they have a real demand for new stuff. If there's really some professional team with special needs like a better, specialized level editor for their dedicated level designers, they may create their own tool anyway. 
If a more or less novice comes in (after searching for "game engine" or whatever) and wants for example make something like "Mario Kart", he looks at samples, starts with playing with some of them or starts modifying the closest one to his goal. He reads available documentation "ah I can use Blender and the exporter to make car models", "ah that's how I can import that and attach physical wheels with physic constraints",... I don't think his main concern is getting regularly new features, unless he really needs something or something is bugged.
Also I mentioned my sample projects idea already: having small games in various genres would make an entry way easier and would hugely boost the "fame"/community. "Urho Tournament"? "Urho Commander"? "Age of Urho"? "Urho Cart"? "Super Urho Maker"? :smiley:

[quote="cadaver"]
For the "roadmap" thing, yes it could easily become outdated or too optimistic and therefore be "fake" like you say, whereas the Github issue tracker (mostly) reflects the reality of development. PBR is now listed there as a future issue that will be worked on.[/quote]
Hm, so one could say that the issue list is the roadmap. Tags like "next version" would be good to define rough milestones to be more like a real roadmap (I think Irrlicht had a nice roadmap with progress bars BTW). Also wished features / feature request which are "sane, good and doable" could be seen as "long term roadmap points".

[quote="Lunarovich"][quote]Also we could try improving the usability, that has always been one of my main concerns (thus all the wiki work) and I'm currently a bit working on that. Could someone name things that could be improved without sacrificing performance? (better a new thread if someone has ideas)[/quote]

The most difficult thing for me, that kept me for months away from Urho3D, was the fact that I did not know how to start the damn thing :slight_smile: If I was provided with a working example of c++ minimal "hello world" that I could simply compile, modify and see effects, I would certainly start using Urho3D earlier. 

I'm not talking about already existing compiled examples in the static, pre-compiled version of the engine. I'm not talking about script examples that you can modify and run with the player. I'm talking about a possible pre-provided Code::blocks c++ project, for example, that I can simply download from the internet, bundled with the needed libraries and jump straight in. 

I had to spand a day to figure out just how to compile the engine and setup a first working minimal project. I admit, I come from the world of JS development, and things are obviously much simpler there. However, if we had a simple bundled project that can be compiled and run, then even newcomers to C++ could start bashing Urho3D right away :slight_smile:  [/quote]
Ah I see. There are articles about building and setting up Urho and a simple hello world thing in the making (like [github.com/urho3d/Urho3D/wiki/First%20Project](https://github.com/urho3d/Urho3D/wiki/First%20Project)).
A pre-compiled package would require a specific tool set like "Visual Studio 2015 and DirectX11". The Urho community seems to be quite diverse (I'm usually using MinGW on Windows for example and not VS, others Linux or MacOS X or Mobile). Which tool sets should be provided? The more, the more work.
Is that really needed if there are tested and simple step by step guides with images? One of the big strengths of Urho is the (usually) good working CMake build systems. I remember that we weren't able to build Ogre ourself with MinGW for example.

[quote]
[quote]I would appreciate some kind of connectivity, "hubbing", news page or whatever you wanna call it. Not sure about what to use though as I'm not really a social media guy (I don't like Facebook but I'm >=neutral to all others).[/quote]

I don't like FB myself either and fully subscribe to this: [url]https://www.youtube.com/watch?v=BBUNNbgrXQM[/url]. However, FB is became a necessity these days, specially if you want to get visibility. Sure, we can have the same or even better functionality on other platforms. However, there are no groups like this ([facebook.com/groups/IndieGameDevs/](https://www.facebook.com/groups/IndieGameDevs/)) on other platforms that have nearly 60k members and growing. [/quote]
Hm. Facebook likes and subscribes seem to be not much worth though, for example Youtubers say that a lot. Also in our company we had Facebook campaigns which led to a lot of likes but barely anyone visited our site and looked at the product, they just click "like" and move on without looking at anything or having a real interest. Also we had videos directly on Facebook with a multitude of likes as views, how? Who presses "like" to a video that he didn't even watch? (unless the video view counter didn't count a "jumping through")

What do we even want/need? Something like news could be posted on multiple sites at once (like Facebook + Twitter + G+) and just link to the full article somewhere else. GitHub is already a kind of "social media for developer".

[quote]
P.S. I was amazed to see how mayn Urho3D mobile published games are out there.[/quote]
There are? Didn't know that. I'm not really into mobile dev and more into classical desktop dev though.

-------------------------

cadaver | 2017-01-02 01:10:54 UTC | #13

[quote="gawag"]Could you give some more examples of required stuff for "user-first" engines besides the editor? More like other external tools like material and particle editors or more as in engine behavior and API changes?
The things bothering me are not a "huge leap", maybe that's because I'm coming from Ogre and CrystalSpace and not those giant Unity/Unreal things.
[/quote]
Some examples could be:
- the concept of a project and one-click publish to various platforms (*)
- comprehensive per-API function documentation with examples
- seamless asset import workflow, for example you drag your Blender file to the project folder and it gets automatically converted
- light baking inside the editor
- various social media and provider integrations

But actually it's good to hear if your problems are smaller. Naturally any contribution to help are appreciated. Also, it occurred to me that this "user-oriented" direction is fulfilled quite well by the Atomic Game Engine based on Urho. But it isn't free.

(*) this actually flies in the face of Urho being a library which can be used in various ways. This would assume there is "one true way" to run Urho applications and so would actually hurt its flexibility, but I could see certain kinds of users expecting / appreciating it

-------------------------

gawag | 2017-01-02 01:10:54 UTC | #14

[quote="cadaver"]
- the concept of a project and one-click publish to various platforms (*)
(*) this actually flies in the face of Urho being a library which can be used in various ways. This would assume there is "one true way" to run Urho applications and so would actually hurt its flexibility, but I could see certain kinds of users expecting / appreciating it[/quote]
A "typical way" or "encouraged way" (as the CMake way already is) is not really contrary to the concept of a library that can be used in various ways. That can still be a major design point. I don't know how many ways there are to use Urho without getting too fancy but I guess there's one (the currently usual CMake way I guess) that is more recommendable as the others for the typical use case of a game engine.
This one-click publish could currently already be done with some scripting (I think). The CMake scripts can already pretty easily build on all platforms. A project could use Git hooks or Cron jobs to trigger an automatic build process (on possible different machines/platforms) that builds the application for multiple targets, builds setups or whatever and uploads that as a snapshot (or whatever) to a website. This is relative project specific, some use setups, some use Steam, some launcher tools with updaters, some multiple things.

[quote="cadaver"]
- comprehensive per-API function documentation with examples
[/quote]
Yes! There's currently some work being done in that direction. Some functions and concepts are really hard to understand when just seeing function names.

[quote="cadaver"]
- seamless asset import workflow, for example you drag your Blender file to the project folder and it gets automatically converted
[/quote]
Currently I tend to use quite different options in the exporter. There could definitely be more auto recognition (like exporting a sceleton and animation if they exist and remove the checkbox or have it on "auto" per default).
Oh it would be quite handy if the exporter would remember it's settings per model or Blender file. An external tool (like you mentioned per drag&drop) could open the file in Blender, trigger the exporter and close the project, to achieve a more seamless import workflow. Though I don't mind opening the Blender file, usually one wants to change the model anyway, why should he otherwise want to export again. "- better Blender exporter that remembers setting per .blend or model in .blend".

[quote="cadaver"]
- light baking inside the editor
[/quote]
Is light baking still used (a lot)? I like dynamic scenes and lightbaking is not really useful for that. A feature that at least I wouldn't use, I guess.

[quote="cadaver"]
- various social media and provider integrations
[/quote]
What do you mean with "provider"?
A more active community and better organization would certainly be good (also the reason of this thread).

[quote="cadaver"]
But actually it's good to hear if your problems are smaller. Naturally any contribution to help are appreciated. 
[/quote]
One of the thing bothering me the last days is for example the weird and unintuitive way of modifying the height and splatting map of a terrain. One of the things I have in mind are various drawing functions being added to the Image class to smoothen or flatten an area or raise a mountain for example. I'm working on drawing functions (like thick lines with outward gradients) currently anyway. Also getting texture arrays will super improve terrain too.
Another thing I'm fighting with is the weird mouse cursor behavior and I'm currently checking out the newest Urho version and may report a bug (or at least really weird behavior). Also more cursor shapes potentially incoming.
The things bothering me are usually either due to being not documented properly or due to a bad or weird library design. Like having to set a default style and a cursor and a font in the GUI, there have been multiple questions due to not knowing that, there should be loaded defaults. 

[quote="cadaver"]
Also, it occurred to me that this "user-oriented" direction is fulfilled quite well by the Atomic Game Engine based on Urho. But it isn't free.
[/quote]
Oh. Are they at least contributing back to Urho? It looks nice but I don't get their licenses.
I found another commercial engine yesterday which seemed to be based on Urho: [clockwork.sunwells.net/](http://clockwork.sunwells.net/) Doesn't seem to be doing well, empty forum.

-------------------------

cadaver | 2017-01-02 01:10:54 UTC | #15

[quote="gawag"]
What do you mean with "provider"?
[/quote]
Things like Apple / Android leaderboards, or various ad system integrations (mobile oriented) which to be honest I want to stay as far away as possible, but that's just me :slight_smile:

[quote="gawag"]
Oh. Are they at least contributing back to Urho? It looks nice but I don't get their licenses.
[/quote]
Josh has made some PRs / issues, but not in a major sense. It's a fork which has drifted quite far.

-------------------------

gawag | 2017-01-02 01:10:55 UTC | #16

[quote="cadaver"][quote="gawag"]
What do you mean with "provider"?
[/quote]
Things like Apple / Android leaderboards, or various ad system integrations (mobile oriented) which to be honest I want to stay as far away as possible, but that's just me :slight_smile:
[/quote]
Like those "most popular app" lists in the app stores? Why should a library be in there? (Unless in some pre-compiled form like some libraries in the Steam Store)

-------------------------

weitjong | 2017-01-02 01:10:55 UTC | #17

[quote="cadaver"]
[quote="gawag"]
Oh. Are they at least contributing back to Urho? It looks nice but I don't get their licenses.
[/quote]
Josh has made some PRs / issues, but not in a major sense. It's a fork which has drifted quite far.[/quote]
Just want to chip in on this point. Don't you think that exactly why its fork has drifted so far? I have not seen any meaningful contributions from them back to upstream Urho3D project. It is a embrace and extend strategy. Of course I understand why corporate America does this, but still ... (this is just my personal view).

-------------------------

gawag | 2017-01-02 01:10:55 UTC | #18

[quote="weitjong"][quote="cadaver"]
Josh has made some PRs / issues, but not in a major sense. It's a fork which has drifted quite far.[/quote]
Just want to chip in on this point. Don't you think that exactly why its fork has drifted so far? I have not seen any meaningful contributions from them back to upstream Urho3D project. It is a embrace and extend strategy. Of course I understand why corporate America does this, but still ... (this is just my personal view).[/quote]
That's exactly what I thought too. Just taking something free and selling it is really cheesy. They seem to have added a lot though and their price isn't that high (that's the reason I decided to not comment on it after wanting at first) but it still feels unfair. Apple and Microsoft and other did similar things: taking stuff from BSD for example and making it commercial. (These two have changed though a bit in the last years and are contributing in various big free software projects now.)

General thoughts unrelated to this case:
I thought a lot about this "moral stealing" and how to avoid such a thing via a license (which is the only thing one can do) since learning about the free software idea many years ago. The license could require commercial projects to give back a certain amount (money or code) in relation to how much work they added and money they earned.

Somewhere I also mentioned that I see it as a moral obligation to (somehow) contribute back to free software if you benefit from it (by making money from it or just using it). Such a moral obligation does not just concern software though but all parts of live. Most people don't contribute back though. (this "contributing back" doesn't have to be towards exactly the software one uses IMHO, that software may be doing fine and other good project may need the help more)

This "moral stealing" is the reason some projects make a dual license: GPL or commercial license (for a price).
The basic idea behind copyleft licenses is to require that the software stays free. It emerged from exactly this: companies taking free software, making it proprietary (and commercial) and earning money by doing that.
Demanding a fair profit share is a similar idea. Though copyleft is often seen as non-commercial so a profit-share demand would, in the eyes of some, seem contrary to the free software ideal. Though copyleft too is often seen as contrary to "real free software" (BSD-, MIT- style license).

Big philosophical topic.

Edit: added a note and slightly changed the wording in the first part to make stuff clearer. Also with "moral stealing" I tried to describe a "legal but unfair exploiting".

-------------------------

dragonCASTjosh | 2017-01-02 01:10:55 UTC | #19

Just to clear things up about Clockwork and where it sits from Urho. Clockwork is my attempt to turn Urho into a commercial style engine with everything available through 1 editor. Despite the editor not being part of the repo yet it's on the roadmap currently I want to improve the renderer to more modern standards, changes like the rendering that fit in with Urhos targets will get PR's to the master. As for the website that was linked the information there is not correct, the web developer use placeholders and never finished. I do not intend to sell any part of the engine, although I have considered selling themed starter packs to build things like a Sci-Fi game, to be clear this does not mean example and tutorial projects. Any money I gain from the project will be put into Urho3D in some form, but I believe this is a long way off.

If there comes a point where the Urho developers want to streamline the workflow I am happy to drop Clockwork In order to merge all changes to the master and then focus my effort on Urho alone. When i first started I considered doing all my chances to Urho3D but believed it was to big of a change from the current engine goals.

-------------------------

Enhex | 2017-01-02 01:10:55 UTC | #20

[quote="gawag"]This "moral stealing" is the reason some projects make a dual license: GPL or commercial license (for a price).[/quote]

There's no "moral stealing" since permission was given, not just for any specific user but to everyone including you and me.
And don't use GPL, it's such a nasty "free as in complies with our totalitarian ideology", a legal minefield with tons of restrictions.

I don't think it's possible to grow a professional game development community around Urho3D with GPL (It's kinda hard to sell a game when you must make it available for free).
Not to mention that at that point developers will just go with other engines.

If you want to force users to share changes to the licensed software, Mozilla Public License is a better option. With MPL if a user makes changes to the licenced source code he must make them available under MPL, but he can keep his own separate files closed-source. It's still a long license and requires learning it which is a big hassle. If you want try to look at "3. Responsibilities":
[mozilla.org/en-US/MPL/2.0/](https://www.mozilla.org/en-US/MPL/2.0/)

GPL 3.0 is ~31,550 characters long.
MPL 2.0 is ~14,784 characters long.
MIT is ~461 characters long.

Also a license means nothing if you're not going to enforce it. You'll needs laywers and to spy on your users, do you really want to go down that route?

To sum up, if you're doing an open source project just keep it simple and use MIT license and let the users do whatever they want.

-------------------------

weitjong | 2017-01-02 01:10:55 UTC | #21

Sorry, but just need to chip in again. That quote about the "moral stealing" thing was from gawag and not from cadaver. I believe there is no question about Urho3D license here. It will always be MIT. PERIOD. The point that I want to make earlier is about contribution from community back to Urho3D or from successful downstream project back to upstream and benefiting the community all. The rest of the points are opinions from each individual and we each entitle for one or two.

-------------------------

Enhex | 2017-01-02 01:10:55 UTC | #22

[quote="weitjong"]That quote about the "moral stealing" thing was from gawag and not from cadaver.[/quote]
Fixed that, was an error when cleaning up the quotes.

-------------------------

cadaver | 2017-01-02 01:10:55 UTC | #23

[quote="weitjong"]
Just want to chip in on this point. Don't you think that exactly why its fork has drifted so far? I have not seen any meaningful contributions from them back to upstream Urho3D project. It is a embrace and extend strategy. Of course I understand why corporate America does this, but still ... (this is just my personal view).[/quote]
Sure. I would believe that the development of added features has occupied the Atomic team to such degree that there has not been possibility or motivation to interact more closely with upstream.

In case of Atomic I'd be somewhat sympathetic as it's a small team who has banked their livelihood on being able to provide a service built on Urho, but yes, essentially it is "embrace and extend."

The MIT was chosen way back with the full understanding that such scenarios would happen. Of the alternatives, technically speaking LGPL is nasty on platforms where you can't reasonably allow the user to actually replace / update the library. Then there are other licenses such as EPL (and also MPL which was mentioned by Enhex) which have the clause to give back contributions, but don't have the static / dynamic linking hassle. But all in all I believe MIT is still the right choice for its simplicity and permissiveness, as I'd consider it a greater loss if someone could not use Urho in their scenario because of the license, compared to the risk of being commercially extended without contribution back. A person or team who decides to fork will always create more difficulty for themselves to follow the upstream development, as well as dividing the userbase in case we're talking of the same set of users.

-------------------------

gawag | 2017-01-02 01:10:56 UTC | #24

Whopsie, box of pandora. :unamused: 

[quote="dragonCASTjosh"]Just to clear things up about Clockwork and where it sits from Urho. Clockwork is my attempt to turn Urho into a commercial style engine with everything available through 1 editor. Despite the editor not being part of the repo yet it's on the roadmap currently I want to improve the renderer to more modern standards, changes like the rendering that fit in with Urhos targets will get PR's to the master. As for the website that was linked the information there is not correct, the web developer use placeholders and never finished. I do not intend to sell any part of the engine, although I have considered selling themed starter packs to build things like a Sci-Fi game, to be clear this does not mean example and tutorial projects. Any money I gain from the project will be put into Urho3D in some form, but I believe this is a long way off.

If there comes a point where the Urho developers want to streamline the workflow I am happy to drop Clockwork In order to merge all changes to the master and then focus my effort on Urho alone. When i first started I considered doing all my chances to Urho3D but believed it was to big of a change from the current engine goals.[/quote]

Ah, that makes things a lot clearer. That also explains why the licenses seemed so weird and contradictory (that I meant by "not getting the licenses").
(My post was also meant quite general.)

[quote="Enhex"][quote="gawag"]This "moral stealing" is the reason some projects make a dual license: GPL or commercial license (for a price).[/quote]

There's no "moral stealing" since permission was given, not just for any specific user but to everyone including you and me.
[/quote]
Yes, that's why I wrote "moral stealing" not "stealing" or "copyright infringement". I meant the thinking of "hey they are giving stuff away for free, lets make a profit out of it by reselling it!". Some greedy companies take free software, put a new logo and name on it and sell it as if they made the whole thing on their own. (and again I meant that quite general and not specifically this case, which I don't know that well and I already said that it doesn't seem that unreasonable)
[quote="Enhex"]
And don't use GPL, it's such a nasty "free as in complies with our totalitarian ideology", a legal minefield with tons of restrictions.

I don't think it's possible to grow a professional game development community around Urho3D with GPL (It's kinda hard to sell a game when you must make it available for free).
Not to mention that at that point developers will just go with other engines.
...
Also a license means nothing if you're not going to enforce it. You'll needs laywers and to spy on your users, do you really want to go down that route?

To sum up, if you're doing an open source project just keep it simple and use MIT license and let the users do whatever they want.[/quote]
I didn't say that I suggest putting Urho or something like it under a copyleft license, I was talking about general options regarding software. Also I agree with you, there are other engines who would "take it's place".
Saying that everyone should do MIT is pretty stupid though. There's a reason for all the licenses (more or less, some are quite similar or even stupid). Not everyone wants to get sucked up into a proprietary product.
Commercial licenses are often a "totalitarian ideology" and a "legal minefield with tons of restrictions" and if you want to enforce those you need lawyers as well. 

This is the whole copyleft debate which was discussed countless times. I mentioned that with the "Though copyleft too is often seen as contrary to "real free software" (BSD-, MIT- style license)." part.

I think I even released every software that I really released as MIT, so I'm not a "GPL fan" (nor generally against it). I see the motivation behind (L)GPL but also the problems and the difficulties ("minefield-ness").

[quote="weitjong"]I believe there is no question about Urho3D license here. It will always be MIT. PERIOD. The point that I want to make earlier is about contribution from community back to Urho3D or from successful downstream project back to upstream and benefiting the community all.[/quote]
Should have made myself clearer. I was already thinking if it was clear that I'm talking in general, but I thought mentioning Copyleft, Apple and Microsoft made that clear (as those are clearly not related to this case).
I also didn't want to suggest that Urho's license should be changed (or that it shouldn't), it was completely general talk.
My point was also about contribution from users back to the project, usual options and my "older" ideas about that.

[quote="cadaver"]
The MIT was chosen way back with the full understanding that such scenarios would happen. Of the alternatives, technically speaking LGPL is nasty on platforms where you can't reasonably allow the user to actually replace / update the library. Then there are other licenses such as EPL which to my understanding have the clause to give back contributions, but don't have the static / dynamic linking hassle. But all in all I believe MIT is still the right choice for its simplicity and permissiveness, as I'd consider it a greater loss if someone could not use Urho in their scenario because of the license, compared to the risk of being commercially extended without contribution back. A person or team who decides to fork will always create more difficulty for themselves to follow the upstream development, as well as dividing the userbase in case we're talking of the same set of users.[/quote]
Oh how well I know these thoughts.
All this stuff about dynamic and static linking and code in header files is really weird. A lot of the LGPL "minefield-ness" comes from such things. Especially with header only libraries, what is that? Licenses don't really cover that and don't explain such things in "developer terms".

I think most people don't want to be exploited by getting their work taken, barely modified, sold and others earning money with it. In regards of fairness, there should ideally be at least a more or less appropriate compensation/share. That was my point basically. Though it depends on the case, some projects are small enough that I just don't care (or the developer in general may not care) what happens to them.

-------------------------

jenge | 2017-01-02 01:10:56 UTC | #25

Just a reality check for anyone looking to be a "greedy corporate American preying on MIT projects" :slight_smile:

THUNDERBEAST GAMES LLC is 2 people and only one of us can code.  We have gone over $30,000 in debt, pretty much just in living expenses, getting Atomic to its current state.  We have put a ton of [url=http://atomicgameengine.com/blog/future-of-atomic-1/]fulltime sweat and tears[/url] in and made a point on the frontend to contact @cadaver with our plans to make sure it was "ok".  Thus we chose Urho3D as a base for technical reasons, licensing, and the fact that its project lead is a solid industry vet who understands both... and the value of hard work :slight_smile:

We do not have a "fork" of Urho3D for reasons I posted to the Atomic thread.  We also don't have the resources to make much in the way of PR's right now, though have placed the entire Atomic runtime (the bulk of our Urho3D usage) under the MIT, and anyone is free to pull whatever they want from it.  We also offer [url=http://atomicgameengine.com/blog/announcement-1/]free licenses to contributors of all technology used[/url], including Urho3D.

As my "Urho3D cred" has also been brought into some question, I was the first person to get Urho3D running in the web via Emscripten.  Some of that code is now in the Urho3D repo, however pulled from Atomic and committed by someone else, which I have no problem with and gave permission.  Atomic is also raising a significant amount of awareness in the Urho3D project, for example I personally told @migueldeicaza from Xamarin about Urho3D after he contacted us about Atomic, Urho3D was a better fit for their purposes and led to UrhoSharp... and now they were acquired by Microsoft.  I put up a [url=https://www.youtube.com/watch?v=m3ehQwfbjGg]video in 2013[/url] that now has 30,000 views, I  also got [url=https://www.youtube.com/watch?v=_eSRhcfeb_U]idTech2 running on Urho3D[/url] and shared the code, we link Urho (and other tech we use) on our [url=http://atomicgameengine.com/about/]About Us[/url] page, and so on.

What I see in Urho3D is a great Object model, scene graph and rendering model, and a nice integration with other libraries such as Bullet and Detour.  I totally get that it is a "developer driven" effort and as such a strong base for building all kinds of stuff, including fulltime, throw your entire career at it projects, like the Atomic Game Engine

Cheers!
- Josh

-------------------------

Lunarovich | 2017-01-02 01:10:56 UTC | #26

Just wanted to say that the first galery is on the FB page. You can see it here: [url]https://www.facebook.com/media/set/?set=a.1113579658672822.1073741828.1112089795488475&type=3[/url]

I've tried to put chosen pics from actual games first, and later I will add, in other galeries, images in relation to post-processing, editor etc.

Anyway, you can see pics I've gathered so far here: [pinterest.com/darkodraskovic/](https://www.pinterest.com/darkodraskovic/)

If you have pics relating to any category, please feel free to send them to me.

-------------------------

gawag | 2017-01-02 01:10:56 UTC | #27

"jenge" edited his post while I wrote mine and another post got inbetween  :unamused: 

[quote="jenge"]...[/quote]
Interesting.
My point (again) though was less against the kind of thing that you seem to be doing and more against those more stereotypical "greedy companies" who don't give back in any way, get rich, act as if they did everything and are really unfair in total. There really have been cases of people simply rebranding a free software product, making it proprietary and selling it, sometimes even by violating the license.
If there is a reasonable and fair amount of "contributing back" or some other kind of compensation I don't see any moral problem.
Other people have put a lot of effort into the code you are using too and it would be unfair to only see your part of the work and being the only one getting money for a more or less tiny part of the whole work and not contributing back in any way.

[quote="Lunarovich"]Just wanted to say that the first galery is on the FB page. You can see it here: [url]https://www.facebook.com/media/set/?set=a.1113579658672822.1073741828.1112089795488475&type=3[/url]
I've tried to put chosen pics from actual games first, and later I will add, in other galeries, images in relation to post-processing, editor etc.
Anyway, you can see pics I've gathered so far here: [pinterest.com/darkodraskovic/](https://www.pinterest.com/darkodraskovic/)
If you have pics relating to any category, please feel free to send them to me.[/quote]
Nice collection so far. Didn't knew there is a game on Steam made with Urho  :slight_smile: "mostly negative"  :frowning: 
I'm still unsure though about how that is going to be organized and managed and what the goal is? (I'm also not that familiar with the possibilities of Facebook.)
Can there be community contributions?

-------------------------

cadaver | 2017-01-02 01:10:56 UTC | #28

FB pages can have varying roles assigned to accounts (editor, admin, etc.) so I guess it's a matter of contacting Lunarovich if you want to be part of administering the page?

-------------------------

jenge | 2017-01-02 01:10:56 UTC | #29

@gawag [i]"Other people have put a lot of effort into the code you are using too and it would be unfair to only see your part of the work and being the only one getting money for a more or less tiny part of the whole work and not contributing back in any way"[/i], putting aside that we're spending money on Atomic not making any at this point, a lot of people put a lot of work into code Urho3D uses ([github.com/urho3d/Urho3D/tree/m ... ThirdParty](https://github.com/urho3d/Urho3D/tree/master/Source/ThirdParty)), not sure how to "compensate" them too, this quickly devolves into a GPL-esque conversation. 

The best I have been able to come up with is to offer free licenses to everyone who has any code into Atomic at all, including Urho3D, Chromium, Duktape, SDL, TurboBadger, TypeScript, etc: [atomicgameengine.com/blog/announcement-1/](http://atomicgameengine.com/blog/announcement-1/)

- Josh

-------------------------

cadaver | 2017-01-02 01:10:56 UTC | #30

For me personally it's compensation enough to know that I've taken part in architecting something that's useful commercially *and* being able to sleep soundly even should the engine black-screen on some Android device (pointing sarcastically to the "disclaimers" part of the MIT license) while you can't, as you're actually offering a product / service. :smiley: On the other hand you've had enough faith in Urho to risk a commercial venture based on it, so respect to you.

-------------------------

jenge | 2017-01-02 01:10:56 UTC | #31

@cadaver Thanks, Urho3D is inspiring faith in many these days, excellent work sir!  I have been crunching a long time here and still enjoy working with the code, that says a lot :smiley:  BTW, I've been to Helsinki once back when I was working with the Hybrid guys on SurRender.  If I get back, I'll have to see about visiting the [url=http://www.airguitarworldchampionships.com/]Air Guitar Capital of the World[/url]   :astonished: 

- Josh

-------------------------

dragonCASTjosh | 2017-01-02 01:10:57 UTC | #32

Just had an slightly off the off topic talk but i thought a little on what was mentioned with Clockwork and Atomic. With how i plan to merge everything from Clockwork that fits into Urho could it be worth creating a side version of Urho similar to how linux distros such as ubuntu have multiple flavors. This game to mind as i remember somewhere Cadaver mentioned something along the lines of if a user does not understand the engine it may not be the right engine for them, my idea is to provide a version of Urho that is more beginner friendly. I would be willing develop Clockwork as Urho [fill in gap] but only if this is something Cadaver is happy with. I believe that if it would allow for a version that deferrers from what the main Urho goal are by including featues that are typical of a commercial engine such as an artist focused workflow. Im mixed on what people will think of this idea especilly the core devs as it branched the community a little unless there are changes to the repo project structure, i will talk more on my idea if its something the devs are happy with :slight_smile:

-------------------------

cadaver | 2017-01-02 01:10:57 UTC | #33

Well, you don't need my approval, the license already gives you everything you need. It's more of a question whether you're able to gain a critical mass of users. If your project is attractive enough and you put in good work that shouldn't be a problem. Of course any changes that aren't in conflict with Urho's mission as a flexible library and don't negatively affect its maintainability, or for example drag in mandatory commercial / closed SDKs, would likely also be welcome to Urho itself.

-------------------------

dragonCASTjosh | 2017-01-02 01:10:57 UTC | #34

[quote="cadaver"]Of course any changes that aren't in conflict with Urho's mission as a flexible library and don't negatively affect its maintainability would likely also be welcome to Urho itself.[/quote]

Ill give you a list of features i plan going forward:

-Merge PBR when its done
-Lightmap generator for the editor
-Possibly new editor written in C++
-Further rendering improvements
-possibly experiment with realtime GI at some point (will not work on low end systems)
-Visual Scripting
-Unified shader language
-Unreal/Unity style play in editor feature
- likely more things.

i understand this may take me a year or 2 to complete this list alone but it will be fun to do. Do you feel these features are all acceptable for Urho main

-------------------------

gawag | 2017-01-02 01:10:58 UTC | #35

[quote="cadaver"]FB pages can have varying roles assigned to accounts (editor, admin, etc.) so I guess it's a matter of contacting Lunarovich if you want to be part of administering the page?[/quote]
Ah. I hoped for some more community driven approach. Like wikis have, where everyone can contribute per default but that can also be moderated if needed. 

[quote="jenge"]@gawag [i]"Other people have put a lot of effort into the code you are using too and it would be unfair to only see your part of the work and being the only one getting money for a more or less tiny part of the whole work and not contributing back in any way"[/i], putting aside that we're spending money on Atomic not making any at this point, a lot of people put a lot of work into code Urho3D uses ([github.com/urho3d/Urho3D/tree/m ... ThirdParty](https://github.com/urho3d/Urho3D/tree/master/Source/ThirdParty)), not sure how to "compensate" them too, this quickly devolves into a GPL-esque conversation. [/quote]
But Urho3D's code is free software, that's contributing back. "compensate" does sound monetary, that's why I picked "contribute" to mean any kind of giving back. With "whole work" I also meant all the stuff Urho uses, I intentionally didn't name Urho.
It just would be immoral to make code (found with a free license) proprietary, make a lot of cash, and not give back in any way.
Again everything more meant in the stereotypical "greedy taking" case which this case doesn't fit.

Also making commercial offers around free software (like support, bundling, maintenance, service, teaching, adaption or whatever) is not immoral at all. Moral wise seen (IMHO) everything as long as the "earning" or "profit" taken out of free software is in a fair ratio to the contribution back, which can be in many forms like code, money or whatever. That's kinda the same as with commercial software where you pay for using the software as well. Commercial licenses say "give us money for using our software", copyleft licenses say "give back (or "pass on") the code of the software and your changes". BSD-/MIT-Style don't require anything, but I still see it as a moral obligation to "give back a fair amount in some way if possible". General "fairness".

About the "creating a side version" idea:
That requires continuous additional work (syncing) and would split communities. It would be better to work together on the same system as far as possible. Making Urho more beginner friendly is the goal of many and is in itself not contrary to any of Urho's design decisions.
Is there anything where a split would be required due to wanting conflicting things? Could these differences be resolved with some kind of option like the LUA safe vs. performance option?

[quote]
Ill give you a list of features i plan going forward:
...
Do you feel these features are all acceptable for Urho main[/quote]
Sounds good, acceptable and not conflicting to me.

You could also do additional commercial tools like the editor(s) you mentioned. I personally wouldn't pay for that though, I would try making a free alternative if I really have a need but you could try your luck of course.

I'm thinking of your concern regarding needing a way to make money in some way:
The thing I see as the most obvious way is making games and contribute back to code used (this is not a suggestion, just "an obvious way"). Same as making any commercial software and contributing back to free stuff used like libraries or tools. Making money with libraries/engines or software developer tools is kinda hard I think as the target market is quite small and the price really sensitive and many developers try to fill the needs of developers.
There is for example the commercial "SpeedTree" library for vegetation (there is also a wrapper for Ogre for example) which is a product for developer, but I don't know how good the profit is. Also there are already way more powerful engines like Unreal or CryEngine which have quite an unbeatable offers of price vs. benefit. Trying to compete with those is pretty impossible with a small team and undercutting the price is not really possible (at least Unreal and Unity are really cheap if I remember correctly, no idea about CryEngine).
Unless you find some kind of niece or area where your engine is better or you score in other ways, I don't see a big hope as there are already many affordable commercial engines. I mean you could try but I would try finding a better looking business model. Though I may also misjudge the market completely, I'm not in the area of commercial engines or commercial game development.

I'm for example working in the area of image editing software and the photography area has a lot of really special needs and there are often not that many products available. Some areas have like 2-3 bad tools and everyone tries to find a better tool, that's where we try to come in and try to fill that gap with a better product, or making a completely new product.
Many areas in all the industries / business areas have special needs. The difficult thing is finding those as one has to know the area. And because software developer know their own area, that area is pretty over saturated. In other areas many people spend hours doing stuff that can be avoided or speed up or automated with software tools or simple devices and they would even pay thousands of dollars for a single (software) tool ("solution") as it may safe them hundreds of hours of work per year which logically pays of for them. Many people also don't even know what they want but if they see a tool they are like "oh with that my work/life gets so much easier! I can haz?!" :wink: [c1.staticflickr.com/3/2614/3880 ... 6ee91b.jpg](https://c1.staticflickr.com/3/2614/3880106888_581e6ee91b.jpg)
[s-media-cache-ak0.pinimg.com/73 ... f8e091.jpg](https://s-media-cache-ak0.pinimg.com/736x/c3/91/f0/c391f010ab9f54e2bf82389993f8e091.jpg)

TL:DR: I'm skeptical of your commercial idea and you may have already felt that lack of demand. Making software products for non-developers is generally easier / more profitable, but you can try of course.
Also not having to compete with free software or freeware makes selling even easier of course.

Basic business science of markets with demand&benefit vs. competitors.

-------------------------

