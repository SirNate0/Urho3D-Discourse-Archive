TheComet | 2017-08-08 19:13:43 UTC | #1

I was thinking: It seems like lately people have been writing custom reusable Urho3D components or otherwise wanting Urho3D to have more useful components.

Would it make sense to start a separate community repository that consists of a collection of small, useful components that can easily be added to your project next to Urho?

-------------------------

slapin | 2017-08-08 19:44:51 UTC | #2

My opinion is that small useful components should go to core.
Also a carefully selected set of bigger high level components
should go to core to set as basis, as these will be well tested and
work well after upgrades. The alternate repository might not work with latest versions of Urho,
which is hard problem as we can't expect individual developers to be up to date - many
prefer not to update at all.

-------------------------

Modanung | 2017-08-08 19:48:20 UTC | #3

[quote="TheComet, post:1, topic:3433"]
Would it make sense to start a separate community repository that consists of a collection of small, useful components that can easily be added to your project next to Urho?
[/quote]
I like the idea. Alternatively a page on the [wiki](https://github.com/urho3d/Urho3D/wiki) could simply index these community components without moving/copying repositories around while still keeping them close to Urho's source.

-------------------------

TheComet | 2017-08-08 19:47:59 UTC | #4

[quote="slapin, post:2, topic:3433"]
My opinion is that small useful components should go to core.
[/quote]
I don't think high level utility stuff should necessarily go to core.

Maybe it might be possible to add a new folder for these components under ```Urho3D/Source/Community``` or something along those lines?

-------------------------

slapin | 2017-08-08 19:48:15 UTC | #5

That would either increase maintenance costs or will not be up to quality. So I really doubt there are resources (in time and hands) to do that in foreseable future. I think adding components to core is way to go

-------------------------

Modanung | 2017-08-08 20:16:41 UTC | #6

@slapin You're not making any sense.

-------------------------

slapin | 2017-08-08 19:53:37 UTC | #7

Well, for something specialized there could be something like "contrib" stuff in main repository, which is maintained like
"experimental" code.
But that doesn't mean  Urho should avoid hight-level components in core - there is basic set which is expected to have,
like IK, Ragdolls, AI components like Behavior Tree, etc. with carefully created editors and easy to use by people.
Otherwise these will have to be constantly reinvented. There is no enough high-level components in Urho.

-------------------------

slapin | 2017-08-08 19:56:12 UTC | #8

Somehow I wonder if i should feel offended or not. Please explain.

-------------------------

slapin | 2017-08-08 20:03:30 UTC | #10

Please read my message again and don't feel this way.

-------------------------

slapin | 2017-08-08 20:08:10 UTC | #12

I don't understand why you feel it this way. I suggested a way to handle this so ti be still able to do it with limited efforts.
I'm really sorry if I broke your dream.

-------------------------

Eugene | 2017-08-08 21:04:21 UTC | #13

On the one hand, putting things into Urho core helps community reuse them.
On the other hand, it will bloat Urho core.

Urho core is simple and lightweight for now. I am not about actual code size, I am mostly about generic achitecture. It has few basic blocks that could be reused in the million of differect tasks.

One we start adding things to Urho code, it will lose its elegance. It will be getting bloated... E.g. I dislike `RibbonTrail`. It is nice feature, but I doubt that it is as generic and reusable as e.g. `StaticModel`. For me it's something that should lay as 3rdparty asset like Skybox or smth else.

Possible soluion is to put all these things into Urho3D.lib but separate them from Urho core file and class tree.

-------------------------

slapin | 2017-08-08 21:12:00 UTC | #14

As currently things are, not including stuff with core means that the stuff is basically unusable - it will not be updated,
it will not be built. Also making people start easier with their project is much more preferred than keeping things lightweight. If you don't use things you don't need they are not included with your software and do not consume resources.

-------------------------

weitjong | 2017-08-09 03:38:00 UTC | #15

I like the idea too.  To prevent the code rot, we could setup nightly CI (or something like that) on those components and subsystem against the current master branch of Urho3D repo. Granted that it will not verify the correctness nor the functionality provided by them, but at the very least we know immediately enough which one break and does not build cleanly. And in order not to burden the core developers, we could setup the CI build notification to be sent to the maintainer(s) of each component/subsystems directly. Maintainer that fails to perform the maintainer role can be replaced or in the event no one else could replace him/her then the component/subsystem itself could be ejected from the community repository (or being marked as DEPRECATED / ONLY WORK WITH specific old version of Urho3D).

If we really decide to do this, IMHO, the community repo should be resided in the [urho3d](https://github.com/urho3d) org  in GitHub. It does not only have a maximum visibility there but also technically it is easier to setup all the above when they are centralised. Note that I do not mean to say you can't have your own components/subsystems outside if/when we have this setup in place.

-------------------------

slapin | 2017-08-09 03:54:34 UTC | #16

I agree that it would be best if it will work. Thanks!

-------------------------

slapin | 2017-08-09 03:58:43 UTC | #17

However, before doing that there should be established skeleton build system to build entire repository of modules against current Urho tree and guidelines to a tree structure and naming convections.

-------------------------

weitjong | 2017-08-09 05:00:05 UTC | #18

Yes, of course when it has been decided. But we are only brainstorming the idea now, so let's not derail the discussion with the implementation detail yet.

-------------------------

slapin | 2017-08-09 05:36:22 UTC | #19

I need to stress an idea that if this repository will have any chance do doverge from main Urho or have any difficulties
building it (in relation to main tree) it is not worth it. It should not become class 2 citizen in infrastructure,
so it is "still part of Urho" and separation is "for maintenance needs". Otherwise it will become nightmare to maintain and support so it eventually die out (probably engraving some good things). So it should not be a case for "lets remove features" direction of some community members (who apparently need some kind of OSG/Ogre3D/Irrlicht to just play their shader games and do not care for much else). So that means it is a subject to bugs in issue tracker and release management.

-------------------------

Alex-Doc | 2017-08-09 06:19:43 UTC | #20

I like the idea too, but I'm not really enthusiastic about having them in the core:
I've chosen Urho3D because it's not bloated with things I don't need or I will never use.

In my opinion, just a wiki page which lists them would work.
On the other way it would be cool to have a separate repository where can be optionally downloaded and built by using CMake options.
I'm not sure about the maintainability of the last one  though.

-------------------------

weitjong | 2017-08-09 08:04:20 UTC | #21

Just want to clarify. We can have many repositories in the same "urho3d" org. So the new community repo(s), should we agree to put them there, won't bloat the existing "urho3d/Urho3D" repo.

Perhaps it is too early to talk about having a  convenience way/tool to auto download/configure the optional components/subsystems, but the idea is certainly intriguing. In my day work I use https://start.spring.io/ to quickly generate a new Java/Kotlin project. I agree with you that it will be cool if we are heading to that direction.

-------------------------

TheComet | 2017-08-09 12:56:23 UTC | #22

[quote="Alex-Doc, post:20, topic:3433"]
I like the idea too, but I’m not really enthusiastic about having them in the core:

I’ve chosen Urho3D because it’s not bloated with things I don’t need or I will never use.
[/quote]

I strongly agree with this sentiment.

@weitjong I quite like the idea of adding a repository under Urho3D/Community (or maybe we'll be able to come up with a snazzier name, something epic, like *THUNDERDOME*). What can I do to help get this in motion?

-------------------------

Eugene | 2017-08-09 13:03:48 UTC | #23

Another question is how to provide simple configuration and linking this repo into Urho library.

-------------------------

weitjong | 2017-08-09 13:39:36 UTC | #24

I like your enthusiasm. May be wait until we hear the opinion from @cadaver. If Lasse is also supportive in this idea and with his permission, I can help to create the initial repo(s) and also a new "team" in the org for maintaining this new repo(s). You and others who want to help will be added as the team member.

-------------------------

johnnycable | 2017-08-09 16:32:42 UTC | #25

Against core bloating, of course. Sleek and slender, please.
Favorable to CI. Tried to compile Head yesterday, got errors.
About integration, I think it is sufficient to keep the same dir structure. It takes to decide how to number/name additional examples (not core components) so they don't clash.
For core components, please head to the urho3d steering committee... :wink: 
Consider many people has their own git repo already... maybe best thing would be to link to those external repos (for those who agrees) directly from urho3d. org...
Short of creating an "awesome urho3d" website with all possible links...

-------------------------

slapin | 2017-08-09 14:13:16 UTC | #26

It ie easy to discuss things you won't ever use.

List of crappy unmaintained repos is last thing Urho community needs.

-------------------------

johnnycable | 2017-08-09 14:14:29 UTC | #27

Yes, so it's better they're kept external...

-------------------------

Eugene | 2017-08-09 14:20:05 UTC | #28

[quote="slapin, post:26, topic:3433"]
List of crappy unmaintained repos is last thing Urho community needs.
[/quote]

Actually, we already have such list: tons of links are stored in wiki, docs and showcase. Usability is about zero.

-------------------------

weitjong | 2017-08-09 14:30:39 UTC | #29

Seriously I don't have all the answers but this is how I see it. Don't treat the community components/subsystems as a CMake target where they need to be built separately and linked against the canonical Urho3D lib. There is no canonical version anyway. Instead, treat them as optional source codes to be built into the each person customized Urho3D lib. So, we can just set aside a subdir in the Source/ and tell our build system to recurse into it to find the source codes, if any. I think that would work.

-------------------------

slapin | 2017-08-09 15:19:32 UTC | #30

Have you cinsidered the following scenario:
1. We have all initially OK
2. API change happens in Urho (probably by a person who knows nothing of side effects of change)
3. CI step in main Urho3D repository passes OK. PR is accepted.
4. Repository with modules break.

I think there should be CI for both repos so if change occurs in Urho3D, both should be checked, as
API consistency is on the one who changes it, not on otheres.

In addition - putting stuff manually in main Urho repo leads to huge can of worms and usability problems.
The repository should be created, maintained, usage should be standard, the doc should be written on how to add
own modul to the repo. Otherwise it will be huge crap pile and Urho usability and popularity will decrese below zero.

You know, products are used not because they are thin, they are used because they do what you want.
The ones who don't want stuff can just remove everything they don't need.

I do understand that maintaining more code is harder than maintaining less code, but I think if
the tossed code gets no attention it is the same as dead. Nobidy will happily search all Internet for modules,
then try to match versions with Urho, find which oes work, etc. There are much more established platforms
which tried this approach for ages, they at least found some solutions to this problem. I think Urho should not repeat these errors.

-------------------------

weitjong | 2017-08-09 16:35:56 UTC | #31

May I ask you to spell check your post before sending. And to answer your question: no, it is not the concern of the core developers. If the maintainers could not keep up then the components will be dropped. The rule is as simple as that. Just which part of the "community repo" you don't understand? 😄

-------------------------

slapin | 2017-08-09 19:01:58 UTC | #32

Yeah, I understand, the usuall kicking of dead horse. Lets see what happens.

-------------------------

cadaver | 2017-08-09 19:49:46 UTC | #33

Community repo which leverages Urho's CI sounds like an excellent idea.

-------------------------

hdunderscore | 2017-08-10 01:24:59 UTC | #34

I'd also like to see this set up :D

-------------------------

weitjong | 2017-08-10 01:55:57 UTC | #35

Right. I think that settled it. Will do the initial setup at the soonest.

-------------------------

George1 | 2017-08-10 02:32:42 UTC | #36

It's a bad idea to go into core.
It's better to have its own repo with targeted Urho version.
This way we will know which component is abandon by the author and lagged behind the Urho Trunk.

-------------------------

weitjong | 2017-08-10 16:44:19 UTC | #37

I have created a new team called "Community repository maintainers" and invited @TheComet to join. Once he has accepted that, I will set him as the maintainer of the new team. Anyone else that would like to help may request to join the team, subjected to team maintainers approval. Below is how I think we could set this up. Open for discussion.

This new team will be the parent team of all the other subteams. Each substeam is associated with one repository. The member of the subteam is the maintainer of the repository. Each repository only contains the source code for one component or subsystem. An individual can be a member of multiple subteams, of course. The repository may be originated from "urho3d" org or just a forked from external repository originated from other personal account or organization account in GitHub with compatible permissive license as Urho3D project. That is, the developer of a new component/subsystem or the would-be-maintainer (in case it is not the same person as the original developer) has to approach the "Community repository maintainers" to request for joining the community, although at the initial stage I expect we are the one that would be more proactive to invite them in (or just fork them anyway :-).

The CI setup will be daily cron-based. Each repo maintainer can decide what is the best time to run. I hope travis-ci and appveyor are able to sync up with the team structure setup above and allow the maintainer to configure the cron jobs independently. To be verified.

The build system will be revised slightly to allow library builder (or CI) to "download" additional source code from one or more community repositories before configuring/generating the initial build tree. Any one who has a better idea than this or objecting this approach, please shout now. The CI for each repo simply uses this new enhancement to test build each component/subsystem against master branch of Urho3D repo. Maintainers will be notified of any build failures as discussed before.

-------------------------

slapin | 2017-08-10 17:11:13 UTC | #38

I'm fine with it as long as it will be easy to use for both developers and users.
Automatic approach is the best I think.

How it will defined what goes to community repo and what goes to core?
Also - how AS/Lua bindings will be handled for community modules?

I think some guidleines are to be written.

Feel free to add me too if @TheComet is not against it.

-------------------------

Eugene | 2017-08-10 18:33:41 UTC | #39

I am ready to maintain community repos as core repo.

[quote="weitjong, post:37, topic:3433"]
Each repository only contains the source code for one component or subsystem
[/quote]
This sounds a bit too huge. Won't it end up in hundreds of repos hard to deal with?

-------------------------

slapin | 2017-08-10 18:55:24 UTC | #40

Look at how Android is :)

-------------------------

TheComet | 2017-08-10 20:39:10 UTC | #41

I think we should just start with collecting and maintaining these community components in a single repo. I wouldn't even know what to call each repository at this point.

If everything is pooled into a single repository then it will also be easier to adapt all of the community components to potential API changes in Urho3D.

With that said, the changes you propose to the build system can still be made to potentially support multiple future community repositories.

@weitjong I didn't receive any invite on github. My name on github is ```TheComet93```, unfortunately there is an imposter who stole my name and [we're working on it](https://github.com/TheComet/EasyRanking/issues/1) :P

-------------------------

Eugene | 2017-08-10 22:18:20 UTC | #42

[quote="TheComet, post:41, topic:3433"]
My name on github is TheComet93, unfortunately there is an imposter who stole my name and we’re working on it
[/quote]
Have you asked GitHub support for renaming inactive user?

-------------------------

1vanK | 2017-08-10 22:22:57 UTC | #43

I do not think that the rules of github have a clause obliging to be active xD

-------------------------

Eugene | 2017-08-10 22:27:40 UTC | #44

[quote="1vanK, post:43, topic:3433, full:true"]
I do not think that the rules of github have a clause obliging to be active xD
[/quote]

You should have read rules of github before laughing, rly.

-------------------------

1vanK | 2017-08-10 22:29:30 UTC | #45

It's hard for me xD
But I'm sure you'll be able to read the rules and find this clause !

-------------------------

Mike | 2017-08-11 06:10:18 UTC | #46

From the [terms of service](https://help.github.com/articles/github-terms-of-service/#3-github-may-terminate):

> GitHub has the right to suspend or terminate your access to all or any part of the Website at any time, with or without cause, with or without notice, effective immediately. GitHub reserves the right to refuse service to anyone for any reason at any time.

-------------------------

Eugene | 2019-05-23 13:20:02 UTC | #47

![image|662x337](upload://w6SjTJlFgXmBazkRYX1HM35HLCc.png)

-------------------------

Gentle22 | 2017-08-11 13:02:54 UTC | #48

I like the idea of having a separate repository for each component. It makes it simpler to manage responsibilities, also for the maintainers it is easier to find issues with their components. For the users it makes it easier to choose the components they want to use. But that is only my opinion.

-------------------------

slapin | 2017-08-11 13:46:05 UTC | #49

Separate repository might be going too far, look at how Android is organized - I think some better granularity is needed.
Liks topic rpositories  or subdirectory-based model.

-------------------------

weitjong | 2019-05-23 13:20:02 UTC | #50

[quote="Eugene, post:39, topic:3433"]
I am ready to maintain community repos as core repo.
[/quote]

I have added you as team member with maintainer role. Your membership is added explicitly as there is "no connection" between the `Core developers` and the new team. Also note that after all the setup is done and when things are running smoothly, I may leave `Community repository maintainers` team, however, I can always re-add myself in anytime.

[quote="Eugene, post:39, topic:3433"]
This sounds a bit too huge. Won’t it end up in hundreds of repos hard to deal with?
[/quote]

Why having hundreds of repos is a problem? On the contrary I think we should be happy if that is true :slight_smile:.  We can easily create a page to catalog all the components and subsystems with their past build history. The active repos will float to the top and the inactive ones sink to the bottom organically. The key point is, each repository is maintained by each subteam; and you and TheComet are the maintainers of the team structure only (unless of course when you guys also happen to have your own components/subystems in the community repo).

[quote="TheComet, post:41, topic:3433"]
I think we should just start with collecting and maintaining these community components in a single repo. I wouldn’t even know what to call each repository at this point.

If everything is pooled into a single repository then it will also be easier to adapt all of the community components to potential API changes in Urho3D.
[/quote]

I have considered both carefully. I believe in the long run the multiple repos approach is in fact has more benefits than drawbacks. Being able to fork or clone individually is already a big win to me. An original developer of the component who happens to be also an expert in Git/Github, may choose to host it in his/her own personal Github account and still be able to participate in the community repo via a fork (changes could be pushed/pulled in both directions). The source code is self-contained and can be self-documented with single page `README.md`. Having separate build status per repo. Selfishly, it is also easier for me when modifying the build script as it is easier to say, hey, take *all* the source codes and build scripts from the chosen community repos and not have to worry about the directory structure of each repo, which would have been the case if a single repo can contain multiple components/subsystems. I can keep going :slight_smile:.

As for the drawbacks of "potentially" having too many of them, it can be easily mitigated as I mentioned above.
[quote="TheComet, post:41, topic:3433"]
@weitjong I didn’t receive any invite on github. My name on github is TheComet93, unfortunately there is an imposter who stole my name and we’re working on it :stuck_out_tongue:
[/quote]

I have sent the invite to TheComet93.

![Screenshot from 2017-08-11 22-57-43|452x347](upload://e9435ZHyNKQbvB8xwekF731qu8p.png)

-------------------------

johnnycable | 2017-08-11 18:11:39 UTC | #51

Having multiple repos means a release, for instance, needs to compile correctly against all contributions as a whole? That is, if a contributed repo doesn't work, all the release is halted?
If it's like that, imho it takes a failsafe mechanism so as the urho core goes on and can compile, while all the rest can come along the way when they're ready, in order of importance...
sort of master/plugins subdivision...

-------------------------

weitjong | 2017-08-12 02:54:16 UTC | #52

I think we have already answered that. The separation to put them in the community repos is really a separation of concerns. The Urho core will do its business as usual unaffected by community. The release could be automated though. As it is now our release/deploy process is already automated using a rake task triggered by CI jobs when it sees a release-tag has been made, so it is relatively easy I think to enhance that rake task to make a synchronous release-tag to all the community repos (native or fork) under our Github organization that have made it, i.e. build cleanly in the past 24 hours against the master branch (I know Travis provides an API client to query for such information, I bet Appveyor does too). If you haven't noticed, our copyright license year is bumped up automatically and synchronously to all our repos using similar automation.

-------------------------

weitjong | 2017-08-12 05:20:23 UTC | #53

There is one drawback of having many repos with many more CI build jobs that could choke the build queue of our free Travis CI/Appveyor account one day as the number of repo really grows. But I suppose we could worry about that later than now. And also someone said if a problem can be solved with money then it is not a problem at all.

-------------------------

johnnycable | 2017-08-12 13:30:24 UTC | #54

Ok. got it, thank you.

-------------------------

hdunderscore | 2017-08-18 10:08:17 UTC | #55

What's the word on this ? I think a simple 'follow object' type component would be a good first/example component to get the ball rolling.

I may submit some procedural terrain components.

-------------------------

Eugene | 2017-08-18 11:08:33 UTC | #56

[quote="hdunderscore, post:55, topic:3433"]
I think a simple ‘follow object’ type component would be a good first/example component to get the ball rolling.
[/quote]

I thought about Procedural Sky component from the forums. Its pretty useful, not too big and not too small.

-------------------------

weitjong | 2017-08-18 12:31:56 UTC | #57

[quote="hdunderscore, post:55, topic:3433"]
What’s the word on this ?
[/quote]

Not sure we have reached any consensus yet. But so far I believe it is leaning toward having multiple repos containing source code module. I have an idea build on top of that which I would like to share as soon as we have reached the agreement.

-------------------------

TheComet | 2017-08-19 16:53:34 UTC | #58

I'd say we can agree that supporting multiple repositories is a good idea.

@weitjong Since you are the one who's going to modify the build system, I think it would make the most sense if you could set up a "hello world" example repository to show how this works, so everyone sees how exactly the components are supposed to be tied in to their Urho3D projects.

That will at least get the ball rolling.

-------------------------

weitjong | 2017-08-21 14:17:00 UTC | #59

Ok. I will take that as though we have reached a consensus since there are no more objection for the multiple repositories approach. As promised, I would like to share more how I see it implemented before actually doing any work on it. In other words, as of this writing I don't know whether they could be fully implemented or not.

Each individual repository is a "module" which contains a collection of C++ source code, CMake build scripts, and assets if any. It may just contain things for a single component but It may as well be a group of related components. It may even be a complete new subsystem containing many components working together. The "module" may use other modules as its dependencies (like Russian doll). Library user has the freedom to mix and match the modules in their own project.

There will be a new user defined metadata file in JSON format describing this dependencies. Similar to the `dependencies` key in `package.json` for those who familiar with node.js development. Then there will be a cross-platform CLI tool to automatically read this metadata file and do all the necessary (like git cloning the source modules recursively) to bootstrap the project. Analogy to `npm install` for node.js. One way to implement such cross-platform CLI tool is by leveraging on the `cmake -P` feature. For instance, we could use the `execute_process()` to spawn other subprocesses. We can wrap this inside a batch file/shell script called `csm.bat` or `csm.sh` or something like that. CSM stands for "CMake Source Module". Well, unless you guys have better name for it. So, the complete command to install all the source codes will be as simple as: `csm install`.

-------------------------

TheComet | 2017-08-23 08:09:20 UTC | #60

I have no major objections to this approach, but will note two things.

Using bat/sh initially seems like a bad idea to me, because it requires you to effectively maintain two implementations of the same tool.

CMake has facilities to clone repositories and parse JSON (look at the ExternalProject submodule for example). Would it make more sense to write "csm" in cmake instead?

As to the name, I feel like "USM" might be a better name (Urho3D source module).

-------------------------

weitjong | 2017-08-23 10:55:27 UTC | #61

[quote="TheComet, post:60, topic:3433"]
CMake has facilities to clone repositories and parse JSON (look at the ExternalProject submodule for example). Would it make more sense to write “csm” in cmake instead?
[/quote]

That's exactly what I originally had in mind! Writing a cross-platform script using CMake script in itself and call the script using `cmake -P csm.cmake -Dinstall=1`, which is a mouthful however. Thus the proposed convenience batch file or shell script is just a thin wrapper for invoking the CMake script, but contains no business logic. 

But considering this tool could support other options, the wrapper script itself may require logic to parse arguments properly, and worse, we have to do it for batch file too, I am thinking may be the tool might be developed using C++ as well. Solve the portability and other issue in one go. 

[quote="TheComet, post:60, topic:3433"]
As to the name, I feel like “USM” might be a better name (Urho3D source module).
[/quote]

I call it CSM because the new tool needed to be made available to the library builder before it downloaded/clone Urho3D project itself. I also want it to be more generic, i.e. It can be used for other projects as well. In other words, the "urho3d/Urho3D" is a value in one of the key in this `modules.json` file. But its value can be anything else.

The use case would be:

- library builder acquires the tool (clone and build from source)
- library builder prepares the `modules.json` in the root of source tree by using the tool
- library builder install the source codes from all the modules by using the tool
- library builder uses cmake and make as of today to build the library with the optional modules built-in.

-------------------------

weitjong | 2017-08-23 12:48:50 UTC | #62

However, I am fine to scale it back too if you all think it is too ambitious. Regardless of the scope of this new tool, its end result will be the same. Under the original source tree of Urho3D there will be a new subdir called "Source/Modules" containing yet more subdirs from each repo. So this weekend when I have time at least I could start to work on that to modify our build system to automatically discover CMake build scripts from each module and then invoke them to give them a chance to configure what is needed for each module.

-------------------------

hdunderscore | 2017-08-23 12:23:53 UTC | #63

I like the idea as you have proposed it.

We can work towards it step-by-step with the goal of adding repo's now while the automated process is being developed, eg

- we need a template repo/cmake script so contributions can start going in, and hopefully the changes to get them working with the automated system will be small
- we can use basic git commandline to clone in the short term

I have some old not-good-enough PRs that I can re-purpose to share.

-------------------------

slapin | 2017-08-24 00:37:24 UTC | #64

I also think that there could be some "contrib" repo which could contain components of lower quality,
like "staging" in Linux kernel, for small components which might go to core or elsewhere but not yet
ready by quality standards. like some very wip but useful stuff people still can use if they want,
also very small things.

-------------------------

weitjong | 2017-08-24 06:25:19 UTC | #65

Anyone can keep their own pet component in their own github account. If they decide to join and host in the community repos then they have to commit themselves to maintain the component against the Urho core, which is a moving target. As discussed, unmaintainted module will naturally break (CI notified the maintainers every day as long as it still break). Also user will not use such components and eventually I foresee we will have some kind of steering committee to decide when to prune the unmaintained modules.

So, do or do not, there is no try. If it is not ready and break the CI since day one then don't bother as it will just waste our CI computing resource.

-------------------------

slapin | 2017-08-24 06:24:15 UTC | #66

I don't say about unmaintained - I say about "not yet up to quality, developed and improving" and CI is a way to improve.
I think that opens a way for some ad-hoc small components to grow into something good and have visibility in central place, get advices from experienced people, etc.

-------------------------

slapin | 2017-08-24 06:36:53 UTC | #67

So I'd set the following limitations for "contrib" components:

i) the component file structure:
1. 2 files - Component.h and Component.cpp (replace Component with a name).
2. tests directory with unit tests which run sequentally for the component, each test should return 0
as process (and not crash). Tests run noninteractively and headless (?)/
3. examples directory with usage.
4. doc directory with component.dox file which describes component and all the documents are added to the documentation.

ii. Should compile,all (including examples and tests) against current Urho tree,
unit-test should succeed.

This way this tree will have enough quality standards so this will not too much burden on CI.

-------------------------

weitjong | 2017-08-24 10:00:51 UTC | #68

Nope. We already agreed that our build system doesn't need any knowledge of the internal structure of each repo.

I will leave to the community repo maintainers to decide the entry criteria. I suppose the usefulness of a module is more important than whether, says, it has complete documentation or none at all; or that it has a dozens of unit tests or none at all. I would not set those as guidelines if I have a say for it.

-------------------------

slapin | 2017-08-24 13:53:02 UTC | #69

Well, you really make no sense.
You're not even sure if you have a voice and say there is something decided.
I don't really understand why no plans are shared and no activity on the subject.
All you do is reject suggestions. If you decide something in shadows, would you better please
display it? All I see is sparse drafty document which explains nothing and does nothing
to have feature implemented as there is no motion towards contributors.

-------------------------

weitjong | 2017-08-24 14:43:36 UTC | #70

Consider this as your final warning. You are not welcome here. You can continue to derail or troll someone else in the other topics, I don't care.

-------------------------

slapin | 2017-08-24 14:48:49 UTC | #71

Well, I see that voice of reason will not work here.
You constantly attack me, troll and spread bullshit.

I think I'm done here. This utter bullshit of last months overwhelms all
reason. I don't to happy to see you either, so I think I just leave.
I hope your karma will eventually hit you really hard. Too bad I can't want it.

-------------------------

TheComet | 2017-08-24 14:56:08 UTC | #72

Guys, chill.

I do agree with slapin's proposal to have at least some minimal guidelines as to how things should be structured. While you can make the build system so generic to the point where this structure can be completely user-defined, the argument is more about ensuring quality and consistency.

I think a reasonable enforcement is to require the directory structure to be similar to how Urho3D already structures stuff. I also believe it's reasonable to enforce inclusion of docstrings, and obviously, the code should actually compile and run correctly (maybe not go as far as unit tests, but a sample would be nice).

-------------------------

Eugene | 2017-08-24 15:09:28 UTC | #73

Damn, please, _stop_. Such arguing about anything except codestyle is a kind of unprofessional.

-------------------------

weitjong | 2017-08-25 02:18:38 UTC | #74

I could be wrong but my idea of community repos is that they should have minimal guidelines as possible so that more people are encouraged to participate. I don't need the modules to be standardized. They could be developed by each of their maintainers/developers with their own code style and coding convention. It's just like how it is with our 3rd-party libs are and yet there is not much of a big problem to integrate them. There should be some guideline to be adhered to, that I agree. But I don't definitely agree on those being listed by Slapin.

Now what come next from him is uncalled for. I know exactly what I just saw and that's the only name I have for their kind.

-------------------------

George1 | 2017-08-24 17:32:11 UTC | #75

I agree with weitjong on this, I think build system should be independent of these components.

The user can choose to use or don't use these components. It's just an include file in their project. There is no point for them to be existed or affecting the build.

-------------------------

weitjong | 2017-09-14 01:52:32 UTC | #76

Sorry for the delay. Will get back to this after I completed the Clang-tidy thingy.

-------------------------

TheComet | 2017-09-17 21:10:14 UTC | #77

No rush, I'm under a pretty heavy workload myself right now.

-------------------------

Eugene | 2018-05-23 12:53:32 UTC | #78

It's time to up this topic, maybe?
Lack of good structurized asset and code storage makes things harder to search and reuse.

-------------------------

TheComet | 2018-05-25 16:47:22 UTC | #79

I'm pretty much back and want to get this project going. @weitjong how are we doing on cmake integration? :stuck_out_tongue:

-------------------------

weitjong | 2018-05-25 17:09:47 UTC | #80

I am taking a short break, spending my free time with ML at the moment.  :slight_smile:

-------------------------

Eugene | 2018-05-29 14:36:32 UTC | #81

I find it funny to be "Community repository maintainer" when there's no community repositories.
Like a lone barkeeper in his pub in the post-apocalypse world where's no more living ones.

-------------------------

TheComet | 2018-05-29 14:52:28 UTC | #82

That's about to change! I believe the decision was made for @weitjong to adapt Urho's build system to facilitate the inclusion of external repositories containing components and to create a "hello world" sample repository demonstrating how the system should be used. When he has time and implements this, I have a few of my own components ready to contribute and hopefully from there we can get this project rolling.

Also sorry for being away for this long. I had a lot of student related things to do.

-------------------------

slapin | 2018-05-30 23:09:40 UTC | #83

Well, I think in this community nothing will happen until someone does it. And if you really want it done, just do it yourself...

-------------------------

rku | 2018-06-01 08:26:47 UTC | #84

@Lumak's repositories are closest thing to this. Although dropping bunch of files to your own repo is rather suboptimal.

-------------------------

Eugene | 2018-06-01 08:51:19 UTC | #85

I recalled about this topic exactly because of yet another @Lumak's thread.
I thought that it would be so nice if all these repos could be used w/o manual file stuff, as if they are part of the engine.

-------------------------

rku | 2018-06-01 08:52:57 UTC | #86

Or part of parent project. Engine assumes it is the main project here while user projects should be main ones. And we are circling back to build system debate.

-------------------------

weitjong | 2018-06-01 10:46:06 UTC | #87

No one say you have to reuse Urho3D build system for your own project. But yes, Urho build system always assumes Urho project as the main project at the moment.

-------------------------

TheComet | 2018-06-02 17:54:13 UTC | #89

This is off topic to this thread, but my thoughts on Urho3D are this: The only thing going for it is its clean design. In every other aspect it has become inferior to other engines (I'm looking at Godot). I really wish someone would implement some new rendering features, such as dynamic GI, because everyone I ever talk to about Urho3D turn it down becase its graphics look bad.

With that said, I will be staying with Urho3D for a while as I write my game using it, and I want to believe it can grow in the future. I happen to believe graphics not maketh the game, **gameplay** maketh the game.

Having a collection of community components will definitely help spark some interest in moving the engine forwards.

-------------------------

Eugene | 2018-06-02 21:52:18 UTC | #90

[quote="TheComet, post:89, topic:3433"]
I really wish someone would implement some new rendering features, such as dynamic GI, because everyone I ever talk to about Urho3D turn it down becase its graphics look bad.
[/quote]
Yep. Light mapping, light probes, real-time GI...
PhysX with clothes and fluids.

I’m revisiting Urho renderer during last month. It’s not that bad, but definitely has some weak points.
GI and all these lighting things would be quite complicated from algorithmic point of view. I’m quite familiar with graphics, but still. Maybe @dragonCASTjosh have tried something like this?

-------------------------

Lumak | 2018-06-02 23:24:20 UTC | #91

This just confirmed I have been wasting my time. Thank you very much for letting me know.

-------------------------

weitjong | 2018-06-03 02:44:41 UTC | #92

[quote="TheComet, post:89, topic:3433"]
Having a collection of community components will definitely help spark some interest in moving the engine forwards.
[/quote]

When you started off this thread, I was (still am) very supportive because I like to see that happens too. However, it was before the project has lost Lasse. I too don't want to waste my time. The Urho3D project is what its users want it to be. If you want something, make your hand dirty and if the result is good, share it by contributing it back to the project. That is what Lasse always said when someone just expects advanced features to be made available.

-------------------------

Eugene | 2018-06-03 08:41:35 UTC | #93

[quote="weitjong, post:92, topic:3433"]
If you want something, make your hand dirty and if the result is good, share it by contributing it back to the project.
[/quote]

I like this thought. Heartbeat of the open-source shall be in its users, not authors.

I find it quite sad that we have a lot of half-done features that weren't merged in master.

-------------------------

TheComet | 2018-06-04 14:30:01 UTC | #94

[quote="weitjong, post:92, topic:3433"]
When you started off this thread, I was (still am) very supportive because I like to see that happens too. However, it was before the project has lost Lasse. I too don’t want to waste my time. The Urho3D project is what its users want it to be. If you want something, make your hand dirty and if the result is good, share it by contributing it back to the project. That is what Lasse always said when someone just expects advanced features to be made available.
[/quote]

Perhaps if we introduced some structure, management wise, the Urho3D project could be more successful. What if we had "developer meetings" every week, where we discuss what's being worked on and had a roadmap and timeplan in place to track progress of new features? If you look at blender or Ogre3D for example, if you want to contribute a new feature or fix an existing feature in those projects, you first have to put in a well structured proposal document and get it approved by the core developer team. In this proposal you state how long it will take you, what parts of the code you're affecting, etc. and this allows the core developer team to create a timeplan for you and track what you're doing.

A system like this would also prevent what happened to @Lumak, where multiple people are working on conflicting ideas.

 Just some thoughts. Maybe the Urho3D project is too inactive to warrant such a system. Over the last week I've only seen about 2-3 people writing code.

While I did like the lay back style of Lasse, I think if we are serious about advancing Urho3D we should also be more serious about managing the advancements.

-------------------------

Modanung | 2019-01-23 23:37:54 UTC | #95

I think staying alive and functional should be our prime directive, instead of going fast (possibly straight into the spaghetti realm of mung). There's pros and cons to every situation. It's good to take breaks, to be outside, to have real social contact.
Fear not! And please ignore heretical suggestions like these:
[quote="cadaver, post:9, topic:3825"]
Urho (the fish) was killed with a kitchen knife on the draining board when it was found too sick to thrive &amp; fight in the fish tank any more. Then the halves were flushed down the toilet. If you someday decide to do the same for the project, you also have my blessing.
[/quote]
;)

-------------------------

dragonCASTjosh | 2018-06-04 21:56:36 UTC | #96

I have already done some rendering changes, but i ended up getting tied down with work. i hope to one day find the time to finish up what i started

-------------------------

cadaver | 2018-06-05 09:35:49 UTC | #97

Ahem.. I could revise that to be a bit more positive. Work on Urho3D if it brings you joy. If it doesn't, don't.

On the topic of Ogre .. it's basically a group of guys maintaining the 1.x line, and Dark_Sylinc working on his own on 2.x. He makes proposals for himself, and no-one is really in a position to contest them, though they get discussed a bit.

-------------------------

slapin | 2018-06-05 12:27:39 UTC | #98

Well, you did not waste your time, this thread did. Just avoid the thread and everything will be ok.

-------------------------

TheComet | 2019-08-05 09:02:34 UTC | #99

I want to try and revive this. I've created a central repository for community components and subsystems here:[https://github.com/urho3d/Urho3D-Components](https://github.com/urho3d/Urho3D-Components)

I've added the first subsystem to it. I think we need to work out the best way to include these into Urho3D's build system. @weitjong did you end up doing any work on this when we last talked about it? What's your status?

-------------------------

weitjong | 2019-08-05 11:15:06 UTC | #100

I have other priority in my mind right now. Don’t let me stop you though.

-------------------------

Bluemoon | 2019-09-21 08:51:37 UTC | #101

Quite a long thread and I don't know if what I'm searching for lies in it :sweat_smile:

However, I feel community components/subsystem will be a great boost to this engine, at least keep it sustained and , kind of, active for a while. It will help pool together a good number of interesting and quality component/subsystem implementations and even experiments that have been done in isolation.

In the long run it might server as a "plugin" store for users of this engine if their desired feature is not in the core.

Now back to what I was looking for :upside_down_face:

What are our plans of dealing with third party licenses that might creep in through external libraries used in these components/subsystem?
What restrictions are to be placed?

-------------------------

Modanung | 2019-09-21 09:34:32 UTC | #102

I think it would make sense to only "officially accept" extensions with a license  compatible with Urho3D's.

-------------------------

TheComet | 2019-09-24 09:12:50 UTC | #103

Pretty much what @Modanung said. The community components that end up in the official repository should be compatible with Urho3D.

There may be 3rd party components with a different license but those would have to be hosted elsewhere.

-------------------------

