bvanevery | 2020-04-14 16:24:16 UTC | #1

TL;DR: weitjong doesn't like me, doesn't get along with me, and generally takes offense at things I say.  I do not feel the same way in return, but this is not a viable working relationship.

How has this developed?  I've been monitoring Urho3D for maybe 5 years now.  I've contributed some very minor bugfix stuff in the build system at some point.  I've certainly made no major contribution, but to be frank, 5 years ago Urho3D was not solving any of my problems.  I had old laptops and the performance on those was bad.  So if I wanted rendering on low performance hardware, I was going to have to implement it myself.  I found other things to do.

Time passes.  The project leader steps down, and eventually makes it clear he's not coming back.  weitjong persists in a sort of interim capacity, but eventually makes it clear that he doesn't want to be around and probably wants out someday as well.  The project forks because people can't agree on some basic strategic directions, like whether C# is good or bad for instance.  Pull requests become bottlenecked.  Development is pretty noticeably on a downslide.

Meanwhile, I pretty much complete a 2 year modding project, and turn my attention to do something that can actually make me money.  I need a 3D engine, either of my own design or contributing to someone else's effort.  Can Urho3D do it?

At first, I think my core need is a good scripting language.  I imagine myself creating 3D art assets using scripts.  When I look into Urho3D's Lua support, I find out it's on a creaky foundation that needs to be redone.  It may also not be getting much battle tested.  I also learn that Lua itself is a fractious ecology, where half the world actually went with LuaJIT, which is stagnant back on Lua 5.1 for the most part.  Lua 5.4 is imminent, and I find several viable solutions for C++ bindings.  But I balk at trying to think of everything in 3D graphics as a table.  The Lua programming model is a bit weird and it's not clear to me how it best expresses my original problem.  Rather, it seems like the world fell in love with LuaJIT's performance.

I also investigate Python, and become fully conversant in its Global Interpreter Lock problem.  Turns out there's a reason why it gets used for 3D modeling and animation UI stuff, but not for game stuff.

I decide that AngelScript is something I'll never use, has no audience, and can't grow Urho3D to any kind of success.  I leave it to those who are passionate about AngelScript to carry on their rearguard action.  Best of luck to them.

I go up a learning curve about C++ modernization and versioning issues.  They're sticky, and can lead to religious wars.

In the course of all of this, I learn a lot about the development energies of various people "in orbit" around Urho3D.  A good number of them excel as individual programmers, and I respect them on that basis.  But their *team dynamics*, their ability to cooperate to accomplish major things, is rather poor.  Lots of things go into that.  One's ability to have important strategic technical insight, is part of the mix.  But a lot of it is just whether they're capable of getting along with the other people in the room.  Whether they share values, and in cases of conflict, whether they are "big enough" to resolve problems and find solutions that move things forwards.

The dirty little secret of Open Source is it's not about the code.  It's about the people.  I learned that quite awhile ago, the hard way.  The kind of way that makes you say "Never Again".  There's a reason I've watched, waited, and evaluated for so long.  I know the price of jumping in, doing a man year's worth of work, and having some project lead torpedo your effort because you're not getting along with them.

So as I tromped through Urho3D's entire public history recently, and found out various things about the code, I managed to rub weitjong the wrong way.  Since broken is broken, I'm unapologetic about that, even if nicer words can always be used to state a case.

I have the attitude of an engineer, I *fix things*.  If I'm going to, that is.  Something that's broken, I say it's *broken*, and I don't care whose implementation or "baby" it was.  Could be my own stuff.  I've been modding for 2 years, I've found plenty of things that were broken and fixed them.  I've had other people tell me about broken stuff, and I've fixed that too.  I've had long arguments about stuff that others thought was broken, but ultimately I decided it wasn't, and I kept my own counsel.  I know how to say "no".  I don't resent the argument though.

So, what just happened?  With all of this interaction lately, Discord decided that I'm a "Regular".  There are tiers of trust in this forum, I found out.  A few days ago, Discord promoted me to Tier 3.  I got some new limited powers, one of which was access to a secret chamber called the Lounge.  Well it was a quiet place, hardly anyone talking, and certainly not about anything that matters.  But hey, trouble ensued, weitjong took a *lot* of offense that I'd stepped into "his tree fort", and kicked me out.  I don't have Lounge access anymore, and I'm clearly not Tier 3, I've been demoted.  I got signed off, which never happens, and when I came back some goofy "noob autotutorial" instructed me on things I mostly already knew how to do.

This just shows me that what leadership there is here, has no "human touch" to it, that would ever handle the likes of me.  And I think I know something about running forums, since I have one on Reddit called r/GamedesignLounge, with rules about how to keep people playing nice with each other and not getting too upset.  weitjong don't get it.

Meanwhile, Urho3D has *still* not solved any actual technical problem for me.  My current thinking is I might need to look at glTF, and graft / possibly invent a scripting language to manipulate it.  If not glTF, then some other format.  Anyways, stuff that Urho3D doesn't do.  It's all "from scratch" yet again.

There are other codebases out there, offering more stuff off-the-shelf for my purposes, if I think such code is even valuable.  They don't have communities attached to them, i.e. DiligentEngine.  Evaluating a community is a lot of work.  But, it is a necessary part of the process.

Sadly, this one has been found wanting, and IMO it's down to 1 person.  Great CMake engineer, best of the breed, and I say that as someone who's had that job for money.  But *not good* with the people skills, getting unpaid volunteers to actually contribute positively.

I won't delete my account, because I've said technical things that are worth keeping around, for the next people trying to figure out what Urho3D's worth, or could be worth.  But I'm done worrying about its future, and I *did care* enough to take that very seriously for awhile.  To me, this is just more proof that the ideologies of Open Source, don't actually work.  Because, *people*.

Soon as I figure out how to end all notifications, you won't be hearing from me anymore.  If anyone has some reason they wish to continue to interact, I'm easy to find on Reddit.

-------------------------

Modanung | 2020-04-14 18:56:03 UTC | #2

Sometimes it seems to me like @weitjong's definition of a troll is "any person that won't shut up" (although I cannot exclude the possibility of him - instead - having keen senses), and you *have* proven yourself lately to be a wordy one. :slightly_smiling_face:

[quote="bvanevery, post:1, topic:6088"]
To me, this is just more proof that the ideologies of Open Source, don’t actually work. Because, *people* .
[/quote]

In a proprietary world you'd have lost a job or gone bankrupt in a similar situation... *or* otherwise continued collaborating in culturally calcified colonial cannibalism, colloquially referred to as "success". Nothing works all of the time and no one shoe fits all; forks are a part of the open source dynamic. It might come with uneasy feelings at times, but unfortunately that's what makes us budge.

[quote="bvanevery, post:1, topic:6088"]
If anyone has some reason they wish to continue to interact, I’m easy to find on Reddit.
[/quote]

Reddit is on my boycott list, but I trust our paths will cross again if they have to.
[details=March 31, 2016]
> **[Reddit deletes surveillance 'warrant canary' in transparency report](https://www.reuters.com/article/us-usa-cyber-reddit-idUSKCN0WX2YF)**
> Social networking forum reddit on Thursday removed a section from its site used to tacitly inform users it had never received a certain type of U.S. government surveillance request, suggesting the platform is now being asked to hand over customer data under a secretive law enforcement authority. 
[/details]

May you be well and enjoy freedom, @bvanevery. :pray:

-------------------------

bvanevery | 2020-04-14 19:24:51 UTC | #3

Money-wise, I actually only believe in self-employment, and haven't bent from that belief in 22 years.  Excepting this one ridiculous game testing gig I did briefly for $10/hour when I was *really* desperate.  I made it what, a month?

It remains to be seen whether I'll ever employ others someday.  As far as life goals go, I'd rather not.  I work on technologies to enable a one man band.

If I were a manager, AFAIAC, Management 101 is "remember everything a manager did, that you didn't like.  *Don't do that*.  Remember everything you did like.  Do *that*."

Now business partners, that's a sticky wicket.  So far, all candidates have proven useless, for various reasons.  Actually I crossed a finish line with a small Wesnoth campaign team once.  They said thanks for your heroic contribution! and then booted me, as they felt threatened by the degree to which I was taking over.  No money possible from what I had from that exercise either, so that was that.

The point is, I choose people to work with *very carefully*.  The answer to date has been "nobody".  Sometimes it's lack of agreement on technical or business focus.  Sometimes it's personality clash, as with weitjong.  Sometimes people don't know how to do any real work.  It ends up being, if you want it done right....

I'm actually pretty easy to find on the entire internet.  Last I checked.  Awhile ago.  So!

Happy trails to you
Until we meet again
Happy trails to you!
Until we meet again

-------------------------

Modanung | 2020-04-14 19:38:43 UTC | #4

I believe in UBI: *Humanity* is not worthy of its title while it lives as a sophisticated pack of blind jackals.

-------------------------

bvanevery | 2020-04-14 22:05:33 UTC | #5

[quote="Modanung, post:4, topic:6088"]
I believe in UBI
[/quote]

heh, c.f. **const** in C++.  Or is that wrong, and I should just think of constants in math?

I've cobbled together a *cheap substitution*: food stamps and seasonal gifts.  I get an extremely tiny, but sustainable, amount of money per year.  Which allows me to live in austerity and further my goals of indie game developer liberation.

Are jackals really that bad?  Even blind ones?

-------------------------

Modanung | 2020-04-14 20:39:47 UTC | #6

Things can always be worse. :slightly_smiling_face:

-------------------------

bvanevery | 2020-04-14 22:04:53 UTC | #7

I now know more about jackals, hyenas, civets, aardwolves, aardvarks, anteaters, donkeys, mules, and hinnies than I ever did.  Ain't Wikipedia great?  I still haven't learned much about jackal pack behavior.  But it seems, they only get together to hunt in a pack.  Most of the time they just stay in their family groups.

-------------------------

1vanK | 2020-04-15 00:15:13 UTC | #8



-------------------------

1vanK | 2020-04-15 00:15:50 UTC | #9

Non-technical discussion

-------------------------

Modanung | 2020-04-15 00:54:14 UTC | #10

[quote="Modanung, post:6, topic:6088, full:true"]
Things can always be worse. :slightly_smiling_face:
[/quote]

Hate to say I told you so. :wink:

-------------------------

