empirer64 | 2017-01-02 01:02:43 UTC | #1

Hello Urho friends,
I would like to ask if there aren't any plans on creating a wiki page. I think that a wiki page would be great so new users aren't so lost in here and dont have to ask "stupid" questions. I already got a few tips I can share with others.

-------------------------

setzer22 | 2017-01-02 01:02:43 UTC | #2

+1 for that.

I think a wiki would attract more newcomers, it's a bit intimidating when you start with Urho. I'd be glad to contribute with examples and tutorials. I already have some material written waiting to be posted somewhere.

-------------------------

devrich | 2017-01-02 01:02:43 UTC | #3

+1 for if we can add our own "User Contributions" section _but_ have regular wiki sections for admin/moderator _only_

 :smiley:

-------------------------

codingmonkey | 2017-01-02 01:02:43 UTC | #4

wiki +1: with many smallest examples and of course code tips and optimization tips

-------------------------

friesencr | 2017-01-02 01:02:44 UTC | #5

We had a wiki before on the urho3d repo.  It wasn't well maintained.   It would be good to distance the wiki from what the urho team officially supports to allow for more varied, wierd, poorer quality, broken contributions, without burdening the urho main contributers.  It is pretty nuts that the urho team is running near 40 examples in 3 languages, 5 (6 if you count the pi) platforms, and fixes bugs at god like speed.

I personally like githubs wiki / pull request model.  It has no cost, statically generated, and free from databases and applications servers!  I can open a urho3d-contrib organization and throw a wiki on there and give liberal access to anyone that wants it.  Anyone have any thoughts on this?

-------------------------

setzer22 | 2017-01-02 01:02:44 UTC | #6

[quote="friesencr"]It would be good to distance the wiki from what the urho team officially supports to allow for more varied, wierd, poorer quality, broken contributions, without burdening the urho main contributers. It is pretty nuts that the urho team is running near 40 examples in 3 languages, 5 (6 if you count the pi) platforms, and fixes bugs at god like speed.[/quote]

That's exactly the point, at least the way I see it: Allowing users who are willing to contribute with examples and tutorials to have a place to post in. The examples provided with Urho are great, but sometimes I miss examples on how to use the classes while reading the documentation, a wiki would help with that. Of course that would be a hell to maintain if it were to be done by the main Urho team!

Your pull request idea seems fine to me!

-------------------------

codingmonkey | 2017-01-02 01:02:44 UTC | #7

>Anyone have any thoughts on this?
About what ? wiki based on git ? ok, i do not mind )
I think that we need examples of how this might work

-------------------------

weitjong | 2017-01-02 01:02:44 UTC | #8

Our old wiki (hosted on Urho3D repo) was being disabled mainly due to lack of content instead of lack of maintenance. Wiki, by nature, is supposed to be maintained by the project community and I think back then we had opened our wiki for everyone to edit. We promise to bring the wiki feature back again when there are requests to bring it back and it looks like we have built up enough momentum this time.

IMHO, we should not create another GitHub org or even repo for this purpose. It will just be a few button clicks to get the old wiki feature back on Urho3D repo. I want to drive all the web traffic as much as possible to the same web domain.

-------------------------

friesencr | 2017-01-02 01:02:44 UTC | #9

[quote="weitjong"]IMHO, we should not create another GitHub org or even repo for this purpose. It will just be a few button clicks to get the old wiki feature back on Urho3D repo. I want to drive all the web traffic as much as possible to the same web domain.[/quote]

I am always glad to defer. If you want it on the github pages site i can help merging the wiki into the github pages site on the build process.  Mating Jekyll and Gollum is always... interesting :slight_smile:  Subtrees / offline process are the basic options I think.

-------------------------

devrich | 2017-01-02 01:02:44 UTC | #10

[quote="weitjong"]Our old wiki (hosted on Urho3D repo) was being disabled mainly due to lack of content instead of lack of maintenance. Wiki, by nature, is supposed to be maintained by the project community and I think back then we had opened our wiki for everyone to edit. [/quote]

I seriously believe that the momentum of the Urho3D development team should always remain chiefly focused on developeent of Urho3D as to ensure that Urho3D development does _not_ stall which I noted has happened many times to many game engines over the years ( including another engine I became an expert at many years ago ).  The horrible problem with changing development focus away from engine developement and towards "documentation maintenance" is the leading cause of engine downfalls, IMHO. 

[quote="weitjong"]We promise to bring the wiki feature back again when there are requests to bring it back and it looks like we have built up enough momentum this time.

IMHO, we should not create another GitHub org or even repo for this purpose. It will just be a few button clicks to get the old wiki feature back on Urho3D repo. I want to drive all the web traffic as much as possible to the same web domain.[/quote]

I believe that the best thing that we can all do here is to keep in mind my previous statements in this post and try to help by way of:

1:  Make sure that everybody who contributes examples to the wiki should put the date of their last update and the tested Urho3D version.

2:  Every so often ( perhaps every other minor-release of Urho3D ) have some of the community verterans go through and re-test the examples in the wiki in order to maintain that the examples still work with newer Urho3D versions.

I am still very new to Urho3D and trying to get as up to speed as possible and with the other engine i mentioned earlier; me and many of our community had spent many many many hours doing what I am suggesting here.  Our wiki was ( in general ) extremely up to date and us community vertrans would spend a great deal of our own personal time going on the forums to help keep both new comers and regular users supported.

^-- This allowed the engine developers to spend the bulk of their time on active engine development and only a couple days a week ( with the occasional full week usually after a release ) to come on the forums to help everyone.

Urho3D's developers and community members have been [i][u]extremely supportive in all areas[/u][/i] and this is why I choose this engine over others out there, because I feel at home here and look forward to the day when I am good enough at Urho3D to help the community like so many of you have been helping me  :smiley: hey many thanks for that everyone! :smiley:

p.s. sorry for the long post, I'm really loving Urho3D  :smiley:

-------------------------

gawag | 2017-01-02 01:03:21 UTC | #11

Has there been any progress regarding a wiki?
I would love one too (and think Urho really needs one). I could write a setup&build guide since I just build Urho yesterday and wrote everything down what I did.
I don't know these Git Wikis. We could also use [url]http://www.wikia.com/Wikia[/url] (though I never worked with that).

The old wiki seems to be at [code.google.com/p/urho3d/source ... n219&r=219](https://code.google.com/p/urho3d/source/browse/wiki/Urho3D.wiki?spec=svn219&r=219)

The Ogre Wiki could be used to get ideas: [ogre3d.org/tikiwiki/tiki-index.php?page=Home](http://www.ogre3d.org/tikiwiki/tiki-index.php?page=Home)

I like the ideas from devrich:
[quote]1: Make sure that everybody who contributes examples to the wiki should put the date of their last update and the tested Urho3D version.
2: Every so often ( perhaps every other minor-release of Urho3D ) have some of the community veterans go through and re-test the examples in the wiki in order to maintain that the examples still work with newer Urho3D versions.[/quote]
Number 2 would be nice but someone needs to do that...
Though it's also possible to add a line like "Last tested with Urho3D 1.32", to get a last working version. Also if it didn't work for whatever reason. This may be in irregular intervals/versions.

-------------------------

weitjong | 2017-01-02 01:03:22 UTC | #12

I am mainly in charge of the infra setup. I have commented before in this thread that it is only a simple flip to reenable the Wiki in our GitHub repo, with the approval from the project author of course. However, I have yet to seek his permission for this because I am (or was) experimenting with prose.io to create wiki pages directly in our main website (which is a GitHub Pages basically) using pull-request workflow. The idea is to concentrate all the readership traffic to our main website. Without promising anything, I believe it is achievable. Having said that, a few of the Urho core teams including myself are working on Emscripten port right now. So, it will probably take a while before our wiki is back again. But, please don't wait for it. You and other would be wiki writers can start writing about Urho3D now.

-------------------------

gawag | 2017-01-02 01:03:23 UTC | #13

Having a Wiki more connected to the main site would be great.
What does this pull-request workflow mean for that? Are there some administrators/moderators who need to approve every change before it gets visible?
What about including images and maybe other material? Or embedding videos from like youtube or something?
The old wiki seems to have had only text.

-------------------------

weitjong | 2017-01-02 01:03:24 UTC | #14

The pull-request workflow for the wiki will be similar to how now the dev contributors submit their code changes. The changes can / will be reviewed / commented by anyone, but only the core team members who has the push privilege will be able to merge the changes into master branch. Those that contribute frequently sooner or later would be offered to have the push privilege so he/she can push directly without submitting a pull-request first. If everything goes as plan then yes, there will be a way to upload rich media content to the server. But don't hold me to that.

-------------------------

setzer22 | 2017-01-02 01:03:24 UTC | #15

While the pull-request-based approach seems better to me in order to maintain a wiki I think it would be beneficial to start off with an unofficial wiki anyone can edit (or maybe just requesting for write-access here in the forum).

I think that's a good alternative mainly because as weitjong just mentioned, the main devs are busy working on the core engine right now and the wiki would start slowly. That or they would need to spend time reviewing changes instead of working on the engine, anyway both things are a problem.

So I'm talking about staring off with a user-based wiki and then when there's something tangible switching to the pull-request model. This can make the wiki's start a bit smoother. I'm basically suggesting quantity over quality for a start, so we can get a lot of content in there.

And by unofficial I don't mean it can't be hosted on the Urho site itself, but as long as the Wiki is user-based and not "officially" reviewed it should be labeled as such.

What do you think?

-------------------------

gawag | 2017-01-02 01:03:24 UTC | #16

I'm not sure if it would be really necessary to check every change before it gets public. Many wikis allow edits by any (registered) user and changes can be undone easily. A more open model could lead to more people contributing.
Though it should be possible to restrict this (generally), if there are too many trolls.

[quote]I think that's a good alternative mainly because as weitjong just mentioned, the main devs are busy working on the core engine right now and the wiki would start slowly. That or they would need to spend time reviewing changes instead of working on the engine, anyway both things are a problem.[/quote]
Yeah. Though having tutorials and other material is important, too. If there are enough contributors they should do most of the work and not the core developers. Though the developers or experienced users may need to look for errors in generated documents (regarding Urho3D details/usage).


...I accidentally the whole...
As already mentioned above: I knew about this Wikia thing but never used that. So yesterday I took a look to see what it can do. The "create a wiki"-assistant had four step and I wanted to see what can be adjusted/set. At step three I got like three emails with "Welcome! Your new Wiki has been created!" ... :unamused:
So now we have a Wiki! :laughing: 

I already inserted many links to interesting forum posts, sites that may be useful for game developers and already started two tutorials. The one about Blender is mostly finished and I'm currently working on the Urho Build one to finish it ASAP.

Wiki: [urho3d.wikia.com/](http://urho3d.wikia.com/)
I mostly added content and didn't really configure it.
This Wikia system has some minor quirks (like image positioning being a bit primitive) but it seems ok for a start.

Can one of the core developers create an account so I can make him an administrator?

Edit: Finished the Urho3D Build Tutorial and started another one. That build tutorial took super long, i had to do every step like a dozen times until I had every screenshot correct and everything was working smoothly... Didn't expect that much work. (Though not every tutorial is such a step by step guide for the absolute beginner.)

-------------------------

hdunderscore | 2017-01-02 01:03:24 UTC | #17

Thanks for taking the initiative ! I agree the best thing is for users to start contributing freely, when we can see the interest in the wiki then we can all get more excited for it.

I see there is an export option if we decide to move in another direction later.

The pull-request model is definitely valuable from a quality-ensured perspective (with added bonus of simply being cleaner/github style without ads etc), but it can also be useful to have less official resources available for quick content generation.

-------------------------

gawag | 2017-01-02 01:03:24 UTC | #18

[quote]without ads etc[/quote]
There are ads? I don't see any, got an adblocker :mrgreen: (Adblock Plus for Firefox).

The wiki should be already editable by registered users. You could already contribute ideas or other material.
A gallery of nice screenshots would also be nice.

-------------------------

GoogleBot42 | 2017-01-02 01:03:25 UTC | #19

Awesome! I will make contributions over time!

Unfortunately, the username "GoogleBot" was taken so I had to use "GoogleBot42" could an admin change my name on these forums to GoogleBot42?  Thanks!

-------------------------

devrich | 2017-01-02 01:03:25 UTC | #20

[quote="GoogleBot"]Awesome! I will make contributions over time!

Unfortunately, the username "GoogleBot" was taken so I had to use "GoogleBot42" could an admin change my name on these forums to GoogleBot42?  Thanks![/quote]

* curious * Why GoogleBot for your username ?

-------------------------

GoogleBot42 | 2017-01-02 01:03:25 UTC | #21

[quote="devrich"][quote="GoogleBot"]Awesome! I will make contributions over time!

Unfortunately, the username "GoogleBot" was taken so I had to use "GoogleBot42" could an admin change my name on these forums to GoogleBot42?  Thanks![/quote]

* curious * Why GoogleBot for your username ?[/quote]

At first I used it as my username when gaming because I thought it was funny.  (Googlebots, Bingbots, Yahoobots, etc.  are begining to crawl so much of the web now they crawl the in-game chat.)  Afterwards it kind of stuck and so I use it elsewhere too.  :slight_smile:

-------------------------

devrich | 2017-01-02 01:03:25 UTC | #22

lmao!  Good show!  :exclamation:   :smiley:

-------------------------

weitjong | 2017-01-02 01:03:25 UTC | #23

As usual I think I need to clarify my point a little bit (sorry for my bad English). I didn't mean to say that in this proposed PR-workflow all the wiki pages contribution will be vetted by core team members ONLY. Well, in the beginning this could be the case but we can certainly create another "team" in the urho3d organization just for persons who document. We can create, say, a new "documenter" team who only has push privilege to the "urho3d.github.io" repo but not other code-based repos. It should lower the barrier for one to request or being offered to be a member of this new team. The worry that this workflow will slow down the core team members is unfounded. Having said that, until this plan actually materializes or even after it has been materialized, I think there should be no issue with other wikis about Urho3D to exist in parallel.

-------------------------

Bluemoon | 2017-01-02 01:03:26 UTC | #24

I believe this wiki will go a long way in helping new comers get to terms with the nuts and bolts of Urho3d... I don't mind devoting my time contributing :slight_smile:

-------------------------

gawag | 2017-01-02 01:03:26 UTC | #25

@weitjong:
I already knew what you meant. But also with a normal moderation team: "we will check every change before it is made public" sounds more serious and like needing to double check everything or needing a higher skill before contributing, and may make it less likely for someone to contribute. I have no real experience with moderating wikis or similiar, but I would try to keep it open at first and restrict when its getting out of hand. Though I also had experience with spammers and likelihood of reverting bad changes vs. likelihood of someone not contributing due to being less open may be higher as I'm currently guessing.
I Ogre wiki was open for every change. Which really surprised me at that time. I could change things and that was directly visible for everyone.
Both models require moderation, either checking for bad changes or checking every incoming material.
Ah! It may be a good idea to give someone the right to contribute directly (without having to wait for clearance) after making a few good changes (like 3-5 good changes maybe). That would make working efficiently possible and keep spammers out. Though new stuff needs still to be at least a bit checked, not only for trolls/spammers, but also for accidental errors.

There seems to be quite some interest in the wiki, though most has been done by me until now. I just fixed an error / wrong assumption about Urho3D. The wiki needs more experienced users. I just started with Urho a few days ago (though knowing other engines like Ogre quite a bit).
The wiki contains already quite some good ideas about helpful content. Those could be implemented, commented or expanded.
It may also be a good idea to know if someone is already working on something, like working on a sample project, before another one does the same at the same time. Though I don't know how to do that... Maybe just commit often so there is visible working in progress.

-------------------------

setzer22 | 2017-01-02 01:03:26 UTC | #26

I'll start writting a guide on how to build everything in Linux and set up a basic project. And I also wanted to make one about making your own C++ components and use them in scripts. It took a while to figure those out when I got here.

-------------------------

empirer64 | 2017-01-02 01:03:26 UTC | #27

Thank you gawag for creating the wikia page :smiley: . I also like the idea about the open wiki where every registered user can contribute, that was the main idea of wiki.

-------------------------

Bluemoon | 2017-01-02 01:03:26 UTC | #28

I already have a completed project that is very basic that I'm using to write an introductory tutorials to Urho3d

I plan on explaining the basic parts and features of Urho3d and then demonstrate how they were used in bringing the project to life

-------------------------

devrich | 2017-01-02 01:03:26 UTC | #29

Many thanks to everyone who is kickstarting contributions to the wiki.  I promise; I will use them well! :smiley:

-------------------------

gawag | 2017-01-02 01:03:26 UTC | #30

That plans sound great!

[quote]Thank you gawag for creating the wikia page :smiley: .[/quote]
That was just an accident  :laughing:
And when I was like: "Oh I should fill this thing up to have something to show. I need to hurry!"

Just started an article/gallery/list about the techniques shipped with Urho.

-------------------------

GoogleBot42 | 2017-01-02 01:03:27 UTC | #31

Could we add an extension to add code syntax highlighting?  One is available on this page: [url]http://community.wikia.com/wiki/Help:Extensions[/url]

-------------------------

setzer22 | 2017-01-02 01:03:27 UTC | #32

[quote="GoogleBot"]Could we add an extension to add code syntax highlighting?  One is available on this page: [url]http://community.wikia.com/wiki/Help:Extensions[/url][/quote]

That seems like a must-have.

Also, is it me that I don't know how to do it, or is there currently no way to put a multiline box of monospaced code snippets? I haven't managed to do it...

I'll keep editing in my free time! I want this to keep going :smiley:. Also please don't hesitate correcting any mistakes I might have made both in style and the explanation itself.

-------------------------

gawag | 2017-01-02 01:03:27 UTC | #33

[quote]Also, is it me that I don't know how to do it, or is there currently no way to put a multiline box of monospaced code snippets?[/quote]
I prefer the editor that comes when clicking the Edit buttons on the page and not that one from the top right Contribute->"Edit this Page" button. But in both editors you change the text style from "Paragraph" to different Headings and also to "Preformatted", which is a multiline greyish monospace text box.

I just looked into this syntax highlight module (great find!) and can't find it anywhere in the admin settings. They are mentioning the need to request some features by contacting the Wikia staff. I just did that:
[quote]
Contact Wikia Support Staff
Thank you for contacting Wikia. We receive and review all messages submitted here. We will do our best to get back to you in the next 2-3 business days, but please be patient as we work through all of the messages.
Remember, you can also find help in our Community Forum and Help pages. You can keep up to date with the latest Wikia news on our Staff Blog. Happy editing!
Return to Unofficial Urho3D Wiki.[/quote]
So let's wait.

The wiki is making good progress and has more and more active editors! Great!
Still could need more hands. Doing raw stuff like article drafts with big content holes does help too.

I'm so to say learning Urho by writing Wiki articles on how to use it :laughing:

-------------------------

gawag | 2017-01-02 01:03:33 UTC | #34

They answered: 
[quote]Hello,
Thanks for contacting us. This extension should already be available on your wikia (it's globally available by default) - have you tried it out? It seems to be working properly on [urho3d.wikia.com/wiki/User:Kirkburn/Dev](http://urho3d.wikia.com/wiki/User:Kirkburn/Dev), in a quick test.
Best regards,
George Marbulcanti (Kirkburn)
Wikia Community Support[/quote]

But it doesn't seem to work for C++: [urho3d.wikia.com/wiki/First_Project](http://urho3d.wikia.com/wiki/First_Project)
I just wrote them back about that. So let's wait again...

-------------------------

GoogleBot42 | 2017-01-02 01:03:33 UTC | #35

Syntax highlighting on that page seems to work for me...  :slight_smile:  although I don't think the highlighting is very good... it is better than nothing though.

-------------------------

gawag | 2017-01-02 01:03:34 UTC | #36

Ah, now it's working for me too. Interesting...

The Wikia support wrote back, that it was working for them to.

Just tested highlighting for C, but that only changes some colors. Also saw that I need to fully reload the page (Ctrl+F5) to see the highlighting.

-------------------------

setzer22 | 2017-01-02 01:03:34 UTC | #37

How did you make the syntax highlighting work? I'm totally dumb with this editor. Just discovered how to make multiline Preformatted blocks ._.

-------------------------

gawag | 2017-01-02 01:03:35 UTC | #38

Yeah that's a bit complicated:
You need to use the Source Editor and use tags like:
[code]
<syntaxhighlight lang="cpp">
#include <iosteam>

int main()  // "void main" is, and was always, wrong
{
    std::cout<<"C++ code!"<<std::endl;
    return 0;
}
</syntaxhighlight>
[/code]
See [urho3d.wikia.com/wiki/Wiki_Playground](http://urho3d.wikia.com/wiki/Wiki_Playground) for an example.
You can use the Source Editor with one of the buttons at the top right. Or, if you use the other editor, by switching to the "Source" tab.

-------------------------

hdunderscore | 2017-01-02 01:03:43 UTC | #39

Nice to see activity is still occurring on the wiki, keep it up :smiley:

-------------------------

devrich | 2017-01-02 01:03:44 UTC | #40

[quote="hd_"]Nice to see activity is still occurring on the wiki, keep it up :smiley:[/quote]

+1

It's really helpful for me too guys, many thanks!   :smiley:

-------------------------

Faizol | 2017-01-02 01:04:14 UTC | #41

Hi all,

 Is it possible to have this thread pinned at the top of the discussion subforum (or perhaps support subforum?) so that new users can easily find the link to the wiki page?

 About wiki, aside from actual source code, can I suggest for the contributors to have contributions using pseudo code on the best practice in developing games using Urho3D? And for each component of the pseudo code, to suggest which classes that the readers should look for if the readers want to implement the tutorial? I think that would be much more informative to the users who are already familiar with other game engines but wanted to get familiarized with Urho3D. Plus discussions on why certain Urho3D's classes would be more suited to the tasks would be invaluable as that directly involves Urho3D's architecture. In short, that would be best practices that users should apply when using Urho3D engine.

-------------------------

gawag | 2017-01-02 01:04:16 UTC | #42

I'm not a fan of pseudo code. I always found it harder to read and write as real code. But some "plans" or "structure overviews" could be useful. To show how the different classes interact or how the game/program works.
Though I'm no fan of UML either...they are so time intensive to create and hard to modify, especially in a wiki. Maybe such an overview could be in text form or simplified/shortened code that just show how the things are connected, like:
[code]
class level_npc                  // NPC stored in levels for loading and saving
{
public:
    int id;
    Vector3 position;
    std::map<item,int> inventory;    // <item,amount>
};

class level                         // used to store all things associated with one level of the game, like all object, level geometry, NPCs...
{
public:
    std::vector<npc> npcs;  // all NPCs/monster contained in this level     (Urho has its own version of std::vector which may be better in some cases)
};
[/code]
As already mentioned in my Urho "Blog": I'm currently working on a simple flight simulation, a weather system (with sun/moon and day/night) and a vegetation system (like switching 3D trees with billboards and also grass). I know there are many working on such systems but none seems to be public. Such things are really essential for many games and should be publicly accessible and well maintained (aka working). Ogre has such systems available (though mixed maintained).
The flight sim could be a simple example game and put into the wiki. It currently contains sound effects (with modulations), particle effects (with changed intensity), manually controlled bones for the rotor and flaps, physics, the weather system with particle clouds and a moving sun...

Haven't contributed to the wiki in quite some time but did a lot of stuff that could be written down.
Also we really could need more contributors and general more activity in the wiki. There are comment sections everywhere and also a forum. I don't really now if the current style is good, if there are things badly explained and what kind of things are missed the most.

-------------------------

Faizol | 2017-01-02 01:04:17 UTC | #43

Hi gawag,

[quote="gawag"]I'm not a fan of pseudo code. I always found it harder to read and write as real code. But some "plans" or "structure overviews" could be useful. To show how the different classes interact or how the game/program works.[/quote]
That would be awesome and definitely a much better choice.

[quote="gawag"]Haven't contributed to the wiki in quite some time but did a lot of stuff that could be written down.
Also we really could need more contributors and general more activity in the wiki. There are comment sections everywhere and also a forum. I don't really now if the current style is good, if there are things badly explained and what kind of things are missed the most.[/quote]
I would like to join in and contribute but I'm not yet at the level where I can say that I know Urho3D enough to make coding tutorials using it and definitely need to brush my skill in using UrHo3D. I am currently experimenting with small scale projects using Urho3D. I can contribute in other areas if needed, just let me know what could possibly be helpful for the wiki.

Cheers.

-------------------------

gawag | 2017-01-02 01:04:17 UTC | #44

[quote]I would like to join in and contribute but I'm not yet at the level where I can say that I know Urho3D enough to make coding tutorials using it and definitely need to brush my skill in using UrHo3D. I am currently experimenting with small scale projects using Urho3D.[/quote]
 :laughing: That's exactly my status as well. I just spent several hours on getting a Vector3 (sun direction) into my atmosphere shader. After finally getting it to work, I wrote it down into a new HowTo-Section (the second): [urho3d.wikia.com/wiki/HowTos](http://urho3d.wikia.com/wiki/HowTos)
The small scale project I'm working on is my already mentioned flight sim. I just found out that Urho can use transparent textures to make shadows (via masking)! My tree leaves have shadows now! Some time ago as I first loaded the trees the leaves shadow ignored the transparent parts and the shadow was much to big and blocky and I thought Urho can't do those things out of the box.

[quote]I can contribute in other areas if needed, just let me know what could possibly be helpful for the wiki.[/quote]
As already mentioned you can also write what kind of articles you could need and what things you don't understand (there is a page about wiki ideas). Or comment the existing articles if there are things badly explained or could be improved otherwise (or correct typos, just found one...).

Whenever I'm figuring something new out, I try to add it to the wiki so others don't need to search that long. Often my knowledge about the topic I'm writing about is still quite rough and I already removed or rewrote parts of older articles because I said something completely wrong there (so embarrassing  :blush:, but it fills the wiki  :wink: ).
As with the shader parameters: they were a bit explained in the documentation, but "hidden" in a bigger document.
I'm also sometimes writing on my message wall in the wiki about the things I'm currently doing and planing to do (just added a new entry: [urho3d.wikia.com/wiki/Thread:2345](http://urho3d.wikia.com/wiki/Thread:2345)). You could do the same and tell us about your small scale projects. Maybe others are spending days trying to figure things out which you already managed to do and ask for an explanation. We could make an FAQ section for such small questions and questions can also lead to new or extended articles.

BTW I still need to ask things here on the forum because I just don't understand them. Like: How to paint on a texture? I want to modify my terrain weight map and just can't get it to work. These are [b]SO[/b] things for the HowTo section.

-------------------------

Faizol | 2017-01-02 01:04:18 UTC | #45

Wholeheartedly agree. I sent you a PM regarding some ideas about tutorials.

-------------------------

jmiller | 2017-01-02 01:09:27 UTC | #46

Very nice ongoing work on the wiki.  :slight_smile: 

For increased visibility, maybe a link in the documentation and/or pinned topic?

-------------------------

gawag | 2017-01-02 01:09:35 UTC | #47

(just saw that new post here)
I've actually planned a lot for the wiki. Wikia has been criticized multiple times and I've done some research and I think I've found better offers.
I'm currently working on a GUI which should be also usable with Urho (it has currently only a wrapper for Qt, using it elsewhere (OpenGL, SDL,...) is super simple (~100 lines for Qt currently)), that currently takes my "Urho time" away. It's making good progress. (My last Urho project (the second wiki sample project) got stuck by not having a good GUI and there was another thread here about wanting a better GUI, I'm working on it. A first version may be ready soon.) In my job we are using Qt and some of it's issues are also addressed with my GUI project. It's based on a lot of experience with Qt and a lot of new ideas how to make stuff far better and simpler (C++11 is required though).

There's currently some work being done on getting Urho on Android (and iOS) and document that: [urho3d.wikia.com/wiki/Using_Urho_on_Android](http://urho3d.wikia.com/wiki/Using_Urho_on_Android)
I've no experience with that, maybe someone can help there?

A Urho Wiki restart is incoming. I guess I at least start working on that these days. I'll make a new thread when ready and having copied/moved the content.
One of the main goals is to get more people involved, most of the current wiki has been done by me. Editing Wikia is kinda meh, I hope to find a better alternative. Also the new wiki will be better structured and organized.

-------------------------

rasteron | 2017-01-02 01:09:35 UTC | #48

[quote="gawag"](just saw that new post here)
I've actually planned a lot for the wiki. Wikia has been criticized multiple times and I've done some research and I think I've found better offers.
I'm currently working on a GUI which should be also usable with Urho (it has currently only a wrapper for Qt, using it elsewhere (OpenGL, SDL,...) is super simple (~100 lines for Qt currently)), that currently takes my "Urho time" away. It's making good progress. (My last Urho project (the second wiki sample project) got stuck by not having a good GUI and there was another thread here about wanting a better GUI, I'm working on it. A first version may be ready soon.) In my job we are using Qt and some of it's issues are also addressed with my GUI project. It's based on a lot of experience with Qt and a lot of new ideas how to make stuff far better and simpler (C++11 is required though).

There's currently some work being done on getting Urho on Android (and iOS) and document that: [urho3d.wikia.com/wiki/Using_Urho_on_Android](http://urho3d.wikia.com/wiki/Using_Urho_on_Android)
I've no experience with that, maybe someone can help there?

A Urho Wiki restart is incoming. I guess I at least start working on that these days. I'll make a new thread when ready and having copied/moved the content.
One of the main goals is to get more people involved, most of the current wiki has been done by me. Editing Wikia is kinda meh, I hope to find a better alternative. Also the new wiki will be better structured and organized.[/quote]

This is awesome gawag! :slight_smile: It's really great that you got this Wikia thing started. I think this Urho Wikia is already looking great for added content besides the main Urho wiki, but if this really needs an redo then we'll be looking forward to this new stuff. :slight_smile:

Keep it up!

-------------------------

gawag | 2017-01-02 01:09:35 UTC | #49

Yay!  :mrgreen: 

[quote="rasteron"]
I think this Urho Wikia is already looking great for added content besides the main Urho wiki, but if this really needs an redo then we'll be looking forward to this new stuff. :slight_smile:
Keep it up![/quote]
"main Urho wiki"? Do you mean the documentation? [urho3d.github.io/documentation/1.5/index.html](http://urho3d.github.io/documentation/1.5/index.html)

I wanted to restructure the wiki for a really long time. This super long list on the main page has been bugging me since the beginning. I just did that as I created the first content and just kept expanding and resorting it.
I want to have a "Todo-Page" with ideas and stuff being requested and or being currently being worked on. Lists of Urho projects in general. More and better structured links to other ressources (like a big (game) development hub). "Copy" and adapt tutorials from other engines, ...

There seems to be a general wish here for something like a wiki and Wikia seems to be a reason for some people to not help with that. Also the editing is complicated and sometimes the editor just kills your work.

Also I just requested a wiki at the hosting offer that looked the best.
Oh it just got accepted, new wiki created! It's a mediawiki (like Wikipedia) and without ads and free.
Addition features have been requested. So let's see when I manage to bring the new wiki into a "ready" status.  :wink: 
I also read that Wikia doesn't like moving the wiki elsewhere, I try to move the content away slowly, maybe they don't see that (flying under the radar). Or maybe they don't care because it's not big enough or whatever.
The old wiki can still be used until the new one is ready, if someone wants to do something.

-------------------------

rasteron | 2017-01-02 01:09:35 UTC | #50

[quote="gawag"]
"main Urho wiki"? Do you mean the documentation? [urho3d.github.io/documentation/1.5/index.html](http://urho3d.github.io/documentation/1.5/index.html)

Also I just requested a wiki at the hosting offer that looked the best.
Oh it just got accepted, new wiki created! It's a mediawiki (like Wikipedia) and without ads and free.
Addition features have been requested. So let's see when I manage to bring the new wiki into a "ready" status.  :wink: 
I also read that Wikia doesn't like moving the wiki elsewhere, I try to move the content away slowly, maybe they don't see that (flying under the radar). Or maybe they don't care because it's not big enough or whatever.
The old wiki can still be used until the new one is ready, if someone wants to do something.[/quote]

Yes, I did remember there's a section labelled wiki before on the repo, but I'm not entirely sure. Hey, MediaWiki is a great choice!

-------------------------

weitjong | 2017-01-02 01:09:35 UTC | #51

I have taken liberty of reactivating our wiki on Github. I believe Lasse would agree to it.

-------------------------

gawag | 2017-01-02 01:09:35 UTC | #52

[quote="rasteron"]
Yes, I did remember there's a section labelled wiki before on the repo, but I'm not entirely sure. Hey, MediaWiki is a great choice![/quote]

There was previously a wiki using the Github wiki feature but it was disabled due to inactivity.
Edit: Oh it was on Google Code: [code.google.com/p/urho3d/source ... iki/?r=219](https://code.google.com/p/urho3d/source/browse/wiki/?r=219) Seems to be no longer accessible.

[quote="weitjong"]I have taken liberty of reactivating our wiki on Github. I believe Lasse would agree to it.[/quote]

And there it seems to be again.  :question: 
Why has it been enabled again? What now? What's that supposed to mean?

There it is: [github.com/urho3d/Urho3D/wiki](https://github.com/urho3d/Urho3D/wiki)

-------------------------

weitjong | 2017-01-02 01:09:36 UTC | #53

[quote="gawag"][quote="weitjong"]I have taken liberty of reactivating our wiki on Github. I believe Lasse would agree to it.[/quote]

And there it seems to be again.  :question: 
Why has it been enabled again? What now? What's that supposed to mean?

There it is: [github.com/urho3d/Urho3D/wiki](https://github.com/urho3d/Urho3D/wiki)[/quote]

We understand the value of wiki. Our wiki on GitHub was disabled due to lack of community content at the time. Since now you are going to move out from Wikia anyway and you have already some good content, it is a no-brainer to re-enable it so that you can park your content there. As for our old wiki on Google Code, it was not wiki content at all. We didn't have main website (GitHub pages) at that time, so what were there was in fact just the early incarnation of our online documentation today.

You can of course choose not to move your content to our wiki on GitHub. And if so and after a while if no one else contributing to it then we can easily disable it again. I hope it clarifies.

In case if you are wondering with my original plan to use prose.io for wiki content push request management, I didn't have enough time and enough commitment to see it through unfortunately. Although on paper it should work.

-------------------------

gawag | 2017-01-02 01:09:36 UTC | #54

(whoops that text got long :unamused:)

[quote="weitjong"]
We understand the value of wiki. Our wiki on GitHub was disabled due to lack of community content at the time. Since now you are going to move out from Wikia anyway and you have already some good content, it is a no-brainer to re-enable it so that you can park your content there. As for our old wiki on Google Code, it was not wiki content at all. We didn't have main website (GitHub pages) at that time, so what were there was in fact just the early incarnation of our online documentation today.

You can of course choose not to move your content to our wiki on GitHub. And if so and after a while if no one else contributing to it then we can easily disable it again. I hope it clarifies.

In case if you are wondering with my original plan to use prose.io for wiki content push request management, I didn't have enough time and enough commitment to see it through unfortunately. Although on paper it should work.[/quote]

I don't know how powerful such a GitHub wiki would be and how easy or complicated to use. Wikia had various issues that made it more complicated as it should have been, like having two different editors with both having various issues. I think that's one of the things that slower/hindered more people in participating.
The new wiki is a mediawiki and uses the VisualEditor which makes editing pretty easy and straightforward. The only thing really bugging me is the more difficult integration of images, one has to upload images in one place and insert the filename manually somewhere completely different, even Wikia made that better. I've asked about that in their support but no answer yet. Also the VisualEditor could be better with handling tables and other "more advanced" stuff, some things have to be done in markup.
The new wiki is at [urho3d.miraheze.org/](https://urho3d.miraheze.org/). It's not yet configured as I want it to be (like the "Main Page" title still being there), most content has not been moved as I just started yesterday and not every new idea has been (fully) implemented. There's one completely new article and some new links I found.
I could also give you (the main "Urho3D-Guys") admin access (I guess) and we could turn that (or something else) to the "official wiki". There are not that many settings but one can request specific settings or additional extensions at their request page. You could play around at [urho3d.miraheze.org/wiki/Sandbox](https://urho3d.miraheze.org/wiki/Sandbox), there's a neat syntax highlighting (accessible also directly from the VisualEditor) and video embedding possibility. Mediawiki (or others) is far more powerful as Github Wiki, which would have advantages obviously.
I compared various offers and Miraheze seemed the best, but also not without flaws as I found out later. Like the Media Manager displaying images from all of their wikis and not just this Urho3D wiki. I also tried selfhosting mediawiki, which worked, but I couldn't get a good (visual) editor running without modifying that server too heavily (ridiculous dependencies and wrong Linux distribution).

How would that GitHub "content push request management" work?
What about policy? The "Unofficial Wiki" was/is not just about Urho but about more general (game) development topics as well, to act as one entry point/hub into the whole game dev area.
Ogre's wiki for example contains also various extensions to Ogre like weather/water/terrain/grass/GUI systems with Ogre wrapper but that wiki is also often ridiculously outdated (but even those old articles are idea-wise still useful to an extend).
What ideas&plans are there?
One of my main points is ease of participation to get more community work going. I also would like to help organize the community a bit better like having lists of current projects going on regarding Urho and games/stuff using Urho, projects needing certain thing, other projects having various things (like a weather system that could be shared, under certain non-free conditions perhaps[b]**[/b] too). A forum is good for discussions, GitHub good for hosting projects, a wiki could help document and connect stuff.

Ogre, Crystalspace and other engines do have project galleries on their sites (often with terrible and old stuff there though). I still see Urho3D as being more capable and easier as Crystalspace and Ogre (yeah Ogre is just 3D but still). The usage of Urho does not reflect that at all and it's pretty unknown. That's also one of the reasons I'm working on those "Sample Projects". Having simple but still neat example (and free software) games in various genres would be great to show of and to also start own projects (user perspective) in similar directions.

I don't have a real overview of the Urho community. There seem to be 3-4+ core developers putting seemingly like all of their time into the free engine. I read there was a shooter game in development but abandoned and Urho emerged from that. Are the core (or other more active) developer working on games as their jobs? Besides those core developers there seem to be a heavily fluctuating amount of hobbyists (often still in school/university) playing around a bit with Urho but often dropping it again quite soon due to lack of time.
As already mentioned somewhere here, I'm working as a (mainly) C++ software developer on image editing software made with Qt and deployed to Windows and Mac (media industry is like half Windows half Mac...). I started playing around with (game) development when I was like 14 and still have a lot of ideas regarding games. There's nearly no game where I'm not like "Oh I could make that thing better, that's a bad idea there, this would be better different...". There are now a lot of indie games made by often just a handful or just one guy with great new ideas, these games are often selling for 5$-15$ on steam with high ratings (no idea how much they sell of those though). I could also imagine going (partly or fully) into such a indie-ish game scene, currently I'm doing all that Urho stuff just as a "hobby". Though that wiki work I accidentally stumbled into often feels more like work, one kinda has the obligation to keep ones articles up to date and ones projects going. I also see it as a moral obligation to give-back to the free software community when earning money by using the work of so many volunteers, so this is kinda currently my part of doing that.

[b]**[/b] Whoops: wrote "eventually" there instead "perhaps". That gave that part a totally different meaning. The german word "eventuell" is written similiar but the english word for it is not "eventually" but "possible/maybe". That just came to my mind as I used "eventuelly" wrong again somewhere else...

-------------------------

rasteron | 2017-01-02 01:09:36 UTC | #55

[quote="weitjong"]I have taken liberty of reactivating our wiki on Github. I believe Lasse would agree to it.[/quote]

This sounds great and I wouldn't mind having to check multiple Wiki resources or sites!

[quote="gawag"]The new wiki is at [urho3d.miraheze.org/](https://urho3d.miraheze.org/).[/quote]

Looking good  :exclamation:

-------------------------

gawag | 2017-01-02 01:09:39 UTC | #56

Whoops: just fixed one wrong word in my last post here (marked with [b]**[/b]). Classical case of "false friend", german word "eventuell" and english "eventually", surprisingly totally different meaning... Gave that part a totally different meaning...

About the wiki: just saw there's now a link on the Urho main page [urho3d.github.io/](http://urho3d.github.io/) "Wiki Guides and Tutorials" leading to the empty Github wiki... Would be good to remove that link if possible until there's something useful in the wiki.
What about the "wiki case"? My questions haven't been answered. What are the plans and ideas regarding that?
Using the relatively limited GitHub wiki features? Using some other wiki system? Mediawiki? Something else? That one currently on Miraheze or somewhere else?

Not much new on the Urho Miraheze wiki besides a few new links. Just requested two new extensions.

-------------------------

weitjong | 2017-01-02 01:09:40 UTC | #57

I take that you won't park your wiki content under GitHub and I respect that. Since we have already enabled our GitHub wiki, let's see it gets any traction this time. I will give it a few months before reassessing the situation. BTW, the link and GitHub wiki were initially enabled when we first move in to GitHub, so it is not something new. They just being commented out/disabled for the past one year or so. The content is empty now because I have erased the old content, they were just links to some old posts. Hoping for a fresh good start. Finger cross.

-------------------------

gawag | 2017-01-02 01:09:41 UTC | #58

(Oh it got long again :unamused:)
[quote="weitjong"]I take that you won't park your wiki content under GitHub and I respect that. [/quote]
Haven't said that. Just that we may want more features as the Github wiki offers. I'm trying to find a good solution and one that makes community additions/work easy.
I just tested the features it has:
[ul][li]Inserting images is done by entering an URL and Github seems to copy that image then onto it's own servers. So one has to upload an image somewhere else first. Mediawiki is weird with images too. Wikia was nice.[/li]
[li]Headlines are ok.[/li]
[li]One can't do tables. On the new wiki on Miraheze for example I used tables to structure the main page a bit into side by side content (think I got that idea from the Ogre wiki).[/li]
[li]There are codeblocks but no syntax highlighting.[/li]
[li]Lists are ok though would be nice to have a more intelligent editor that continues the list automatically when pressing enter.[/li][/ul]

[quote="weitjong"] Since we have already enabled our GitHub wiki, let's see it gets any traction this time. I will give it a few months before reassessing the situation. BTW, the link and GitHub wiki were initially enabled when we first move in to GitHub, so it is not something new. They just being commented out/disabled for the past one year or so. The content is empty now because I have erased the old content, they were just links to some old posts. Hoping for a fresh good start. Finger cross.[/quote]

... What kinds of content should be there? Strictly Urho3D oriented? Also more general Game Dev articles? Other ideas regarding the wiki?
Like the Wikia wiki has articles about creating textures with Blender, like using a 4 dimensional generator I worked on for like a week to get seamless generic textures. Other articles may be about shaders with just a bit of Urho or purely theoretical articles about game dev (topics). I also have stuff and ideas lying around about general C++ articles (may be also interesting for game dev), though I don't even know If that would fit onto the "Unofficial Wiki".
Github is usually quite project focused, hm.
What about assets like models made for Urho and sharing those? There could be a sharing area like Unity has. There are special sites for models, textures and stuff but there's also Urho's scene format and models could be pre converted for Urho and shaders written or adapted for Urho. Something like that would have greatly helped me with my test/sample projects. One has to crawl other pages for hours to find suitable models for a game engine with a proper license and more hours to "fix them" and to get them into Urho (blender files (or similar) could be packed with the assets too).

Having a wiki on Github may look more like official documentation or an internal wiki and not that inviting to the community. There are already many people saying "oh I don't know enough to write about Urho/something".
I'm still surprised that there were several people saying "oh a wiki would be so cool and I would totally participate" and then not that much was done by others than me. Though the last time I checked Ogre the wiki seemed also relatively inactive.
I started writing articles about stuff I was just figuring out and still have often no idea if that's the proper way of using Urho. Others didn't even fix my typos, so much for "community work"... Would be good if more experienced or even core developers could at least give a bit of input here and there or fix bad practices or something.

Hm... What about the state of the community in general? What could they want from an Urho wiki or something in that direction?
What is already around? What is needed? On what are various people working? It's hard doing anything with an engine when one has to do so much by themself. In Ogre I could combine various extensions that already offered a lot (though they collided with each other in my case and everything was usually outdated).
I still don't know if there are any usable extensions to Urho. Like Ogre had extensions for water (Hydrax, ...), for time & weather effects (Sky- something), for grass, plants and similar (PagedGeometry), alternative terrain engines (ETM: Editable Terrain Manager, ...), for GUIs (CeGUI, MyGUI, ...), ...
I started working on a simple weather thing in my first test project to get a day-night-cycle and clouds, it kinda worked but not that good.
I also tried getting grass and trees on terrain, didn't manage to get something good and fast.
Currently I'm quite focused on my GUI project, though it's not just for Urho and there's no Urho wrapper yet, but it should be easy to make one. (yeah Urho has already something like a GUI but I don't like that and don't like Qt so I'm trying to make a better alternative for at least some basic and custom stuff.)

What about updating the Urho samples (the ones shipped with it)? They are the first things the user sees. As already written in my first post ever here: the textures are super low res, there's a [b]ninja[/b] with a [b]sword[/b] throwing [b]snowballs[/b], ... The samples could be made nicer with using the features the engine already has, like better textures with normal and specular maps, more fitting and nicer models, maybe a proper car in the car sample and with rocks and/or trees instead of giant shrooms...
Urho is wasting potential.

-------------------------

valera_rozuvan | 2017-01-02 01:09:41 UTC | #59

Just thought about being the first to add something to the [b]Urho3D GitHub wiki[/b]... decided to go the path of creating pages that will explain how to install Urho3D on Linux and on Windows. Also decided to add pages about seting up a stand-alone project using Urho3D.

Well, then I really started to think about what to put on those pages = ) Looking at [urho3d.github.io/documentation/H ... lding.html](http://urho3d.github.io/documentation/HEAD/_building.html) ... now, what can I possibly add to the wiki that is not already covered in that doc? Also, even if someone does have a problem with the [b]_building.html[/b] doc, he can come over to the forums and ask for help with his specific problem.

I came to the conclusion that I should not duplicate what's in the [b]_building.html [/b] doc.

So, this begs the question: Should the wiki be used as a place to put forward unique HOWTOs and tutorials with information that can't be found anywhere else? Or should it be used for reiterating things already discussed in the forums or in the documentation [urho3d.github.io/documentation/1.5/index.html](http://urho3d.github.io/documentation/1.5/index.html) ?

-------------------------

gawag | 2017-01-02 01:09:41 UTC | #60

[quote="valera_rozuvan"]Just thought about being the first to add something to the [b]Urho3D GitHub wiki[/b]... decided to go the path of creating pages that will explain how to install Urho3D on Linux and on Windows. Also decided to add pages about seting up a stand-alone project using Urho3D.
Well, then I really started to think about what to put on those pages = ) Looking at [urho3d.github.io/documentation/H ... lding.html](http://urho3d.github.io/documentation/HEAD/_building.html) ... now, what can I possibly add to the wiki that is not already covered in that doc? Also, even if someone does have a problem with the [b]_building.html[/b] doc, he can come over to the forums and ask for help with his specific problem.
I came to the conclusion that I should not duplicate what's in the [b]_building.html [/b] doc.[/quote]
In my tutorials I tried to make the build process easier by making a step by step guide and by adding images where to find certain things. Like a quick starting guide. I always tested the steps on a fresh system (virtual machine) to be sure that that method actually works. Also there are alternate methods of using CMake like using the in-build CMake functionality of QtCreator ([urho3d.miraheze.org/wiki/Buildi ... Creator%29](https://urho3d.miraheze.org/wiki/Building_Urho_1.5_from_source_%28Windows_10,_QtCreator%29)). Sometimes steps differ between Urho versions, like in older versions the Data/ and CoreData/ folders for the samples had to be copied manually.

[quote="valera_rozuvan"]So, this begs the question: Should the wiki be used as a place to put forward unique HOWTOs and tutorials with information that can't be found anywhere else?[/quote]
Yes that for sure. Or to improve existing things, update them, make them clearer, adapt stuff to Urho, ... Or just link to it to make it easier to find.

[quote="valera_rozuvan"]Or should it be used for reiterating things already discussed in the forums or in the documentation [urho3d.github.io/documentation/1.5/index.html](http://urho3d.github.io/documentation/1.5/index.html) ?[/quote]
Exactly repeating the documentation would not make much sense, though one could link to specific parts, like an alternative index.
The "Unofficial Wikis" link to several interesting forum threads. Searching the forum manually can be quite cumbersome and it's often unclear if the stuff their (still) works and it is often unfinished. There are several discussions about materials/shaders but often without providing a really working sample, just a discussion. Something like a material library would be great. For example shaders for triplanar texture mapping, I found that method somewhere and managed to write own shaders, I think I wrote articles about that on the "Wikia wiki". There's also an article about parallax occlusion mapping. All those articles and more could be bundled and a gallery with working materials and shaders be made. Would be super helpful. It's weirdly hard to get into shader programming, also Urho makes it a bit different.

-------------------------

Bluemoon | 2017-01-02 01:09:54 UTC | #61

About repetition or duplication, from my experience with Urho3D doc, it sometimes, can be difficult to avoid. The doc is so comprehensive and great but I figured out it has a kind of flaw. That doc is more like a reference guide for people like you and I, people that have dabbled with one or two Game Engines before and have a sketchy idea of how it all runs , people that don't mind delving into the code of Urho3D to better understand what goes on under the hood. You see, the doc more or less puts us in the part to help us satisfy our curiosity about Urho3D, we investigate more by ourselves.
But for newbies, I really don't think they catch up that fast. You might need to explain the doc over again for them but further simplified for easier understanding, coupled with the fact that everyone don't have the same assimilation rate. 
When I was writing the very short tutorial at [url]http://darkdove.proboards.com/thread/30/urho-flow-1[/url] I referenced the doc more than a thousand times  :smiley: . In-fact almost every section from it had a content from the doc, some even word for word (quoted of course). I realized this right at the first section and contemplated for a while about it. Fortunately enough I ended up seeing the doc as a very good foundation to build the tutorial and it really helped.
I know that subsequent tutorials will still gratefully leverage the contents of the doc (  :exclamation:  Yeah, its almost a year since that tutorial was put up but there is plan to reignite the project)

We might not be able to completely avoid duplication, but we can make it less severe and even well detailed :stuck_out_tongue:

-------------------------

gawag | 2017-01-02 01:09:56 UTC | #62

[quote="Bluemoon"]About repetition or duplication, from my experience with Urho3D doc, it sometimes, can be difficult to avoid. The doc is so comprehensive and great but I figured out it has a kind of flaw. That doc is more like a reference guide for people like you and I, people that have dabbled with one or two Game Engines before and have a sketchy idea of how it all runs , people that don't mind delving into the code of Urho3D to better understand what goes on under the hood. You see, the doc more or less puts us in the part to help us satisfy our curiosity about Urho3D, we investigate more by ourselves.
But for newbies, I really don't think they catch up that fast. You might need to explain the doc over again for them but further simplified for easier understanding, coupled with the fact that everyone don't have the same assimilation rate. 
When I was writing the very short tutorial at [url]http://darkdove.proboards.com/thread/30/urho-flow-1[/url] I referenced the doc more than a thousand times  :smiley: . In-fact almost every section from it had a content from the doc, some even word for word (quoted of course). I realized this right at the first section and contemplated for a while about it. Fortunately enough I ended up seeing the doc as a very good foundation to build the tutorial and it really helped.
I know that subsequent tutorials will still gratefully leverage the contents of the doc (  :exclamation:  Yeah, its almost a year since that tutorial was put up but there is plan to reignite the project)

We might not be able to completely avoid duplication, but we can make it less severe and even well detailed :stuck_out_tongue:[/quote]

Oh Bluemoon! I remember reading your tutorials quite a while ago, they are also linked from both "Unofficial Urho3D Wikis". I just quickly jumped through that link of yours: explaining the basic stuff like view frustum is really great for beginners.
Urho does also have an orthographic mode: [urho3d.github.io/documentation/1 ... amera.html](http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_camera.html), that could be added to such an article as well.
I found a big video series where someone makes a game in C with a bit of C++ and makes everything himself (like the engine with a software renderer) and explains everything in detail: [hero.handmadedev.org/jace/guide/](https://hero.handmadedev.org/jace/guide/)
In a similar fashion something like a "game dev with Urho" article series would be great. Like shader development with Urho (as Urho is a bit different) or modifying the rendering pipeline (if that's realistically needed for "normal" games). The old Unofficial Urho Wiki does have a Blender to Urho Tutorial to bind Blender Tutorials together with Urho such stuff could be expanded.
Something like "Let's make a (simple) game XY with Urho"-Series would be great as well (can be written or video, video would have the disadvantage of not being searchable and fast readable, could be written and with small embedded videos). 

Do we have someone who could participate to some kind of wiki article stuff or something? I'm not really a professional nor experienced game developer, "just" a software developer (mainly C++) who does and did game dev stuff as a hobby, so help would be really welcome. Someone with more game dev experience willing to help? Or someone in general?
@Bluemoon: Having new ideas? Wanting to participate in some way? What kind's of plans do you have?

I paused my wiki work to see what happens with the official Urho wiki at [github.com/urho3d/Urho3D/wiki](https://github.com/urho3d/Urho3D/wiki)
*cough* looks like it's making great progress *cough*  :unamused: 
BTW: Both the Unofficial Urho3D Wiki's content is under free licenses as per their defaults and therefore free to be copied.

My questions regarding the official wiki are still unanswered: Ideas regarding that? How Urho focused does it have to be? (GitHub sounds already quite project focused, AKA no (more) general (game) dev articles) Maybe splitting ideas regarding the wiki to multiple websites?
I'm also making a new thread with a (more or less) different topic and hope for some community response.

-------------------------

weitjong | 2017-01-02 01:09:57 UTC | #63

[quote="gawag"]I paused my wiki work to see what happens with the official Urho wiki at [github.com/urho3d/Urho3D/wiki](https://github.com/urho3d/Urho3D/wiki)
*cough* looks like it's making great progress *cough*  :unamused: 
BTW: Both the Unofficial Urho3D Wiki's content is under free licenses as per their defaults and therefore free to be copied.[/quote]

Sigh... It's not an competition. Please continue to do your good work in your own wiki page. The fact that we have our wiki on GitHub reenabled should not have impacted your work, unless you are seriously considering to participate to use it. However, since this is not the case, it is totally a BS. I am sorry about the language here. Both wiki or even more can coexist. When there are no other wiki writers to participate in our wiki on GitHub, we could switch it off again easily and waiting for someone else to knock at our door. The truth is, I thought I have heard someone knocked, but apparently I was wrong.

-------------------------

gawag | 2017-01-02 01:09:58 UTC | #64

[quote="weitjong"][quote="gawag"]I paused my wiki work to see what happens with the official Urho wiki at [github.com/urho3d/Urho3D/wiki](https://github.com/urho3d/Urho3D/wiki)
*cough* looks like it's making great progress *cough*  :unamused: 
BTW: Both the Unofficial Urho3D Wiki's content is under free licenses as per their defaults and therefore free to be copied.[/quote]
Sigh... It's not an competition. Please continue to do your good work in your own wiki page. The fact that we have our wiki on GitHub reenabled should not have impacted your work, unless you are seriously considering to participate to use it. However, since this is not the case, it is totally a BS. I am sorry about the language here. 
[/quote]
You got me totally wrong there! :unamused: 
I didn't want to say that it's a competition and it's also not the case that I don't want to participate in "an official wiki" / that GitHub wiki.
I just wanted to say that I want some clarity on what that "official Github wiki" is supposed to be. What kind of content should be on the official one? That effects if there is still material or a reason for a separate "unofficial wiki" or some other external site. It may merge or cover different topics or cover the same stuff in a chaotic way. What ideas do you or other core devs have? Is there some consensus? What are the general plans and goals regarding Urho? Is there a page or some implicit plan/goal? Is it just planned as a kind if user generated documentation strictly Urho focused? The Unofficial Wiki is/was more about "Game Development, with Urho3D as an engine and other stuff".
Like I just wrote an article about optimizing code, it's about copying data to an Urho3D::Image but it's still more a general C++ article so it would be kinda misplaced in any Urho wiki (I have no idea where to publish that article). I also figured out how to draw on an Urho3D::Image and creature a texture out of it ([post10670.html](http://discourse.urho3d.io/t/faster-manual-image-texture-painting/1764/5)), that's definitive something for an Urho Wiki article/HowTo (took me a while to figure out (the documentation could be improved) and I still don't know if I'm doing the proper thing or if there is a better Urho way).

[quote="weitjong"]
Both wiki or even more can coexist. When there are no other wiki writers to participate in our wiki on GitHub, we could switch it off again easily and waiting for someone else to knock at our door. The truth is, I thought I have heard someone knocked, but apparently I was wrong.[/quote]
That's also my wiki life :laughing:
> Someone: "Yeah I totally wanna participate!"
> does nothing or just a bit and disappears a few days later
:unamused:

-------------------------

dvan | 2017-01-02 01:09:59 UTC | #65

As a "newbie" to Uhro3d, I want and need beginner stuff. Currently, I'd be lost if not for the "unofficial" wiki. I think it would be good to think of this as 2 levels of information (if not more).

1. Beginner Wiki:  Think the Wiki gawag has produced is the best I've found. It covers a lot of beginner stuff that those who have no exposure to Urho3D need. I've referenced it many times over the past weeks+.

2. Best Way Wiki:  There is a big difference between the basic way to get things done, and the best way to do something for a given situation. Think the "official" Wiki could focus on the "Best Practice" way with efficiency and performance focus. 

That said, I would rather the core Urho3D developers spend their time on improving the API and working on the next version incorporating updates to existing code and fixing / enhancing things as they come up.

There are a lot of "hint's" and notes scattered throughout the forum. Would be nice we could find the "best practice" or solution for a given problem, but currently it's digging through pages of stuff to just find hint's of notes that may or not relate / solve the current issue I'm looking at. Just a list of "solved" problems people have reported or struggled through would be a huge ++.

Keep in mind... people are inherently lazy (my self included). Don't expect many to get involved with either of these Wiki. But, the best chance of any involvement is when the focus of the Wiki is defined, and easy to contribute to.

gawag:  Just decide what you would want to spend time with, and do that. Others who many contribute or reference would want the easy/quickest access. Seems like it would remain an "Unofficial" Wiki. Think the "official" Wiki could just link to it.

bluemoon:  Really found your tutorials helpful. Wish you would do more!

weitjong:  Think you should keep the "official" Wiki, and just link to other helpful sites if nothing else. Think I only found some of these other sites by random searches. Would be good if Urho3D had a "helpful sites" reference that would not be too busy to maintain.

Just my thoughts today when reading some of this thread.

-------------------------

gawag | 2017-01-02 01:09:59 UTC | #66

[quote="dvan"]As a "newbie" to Uhro3d, I want and need beginner stuff. Currently, I'd be lost if not for the "unofficial" wiki. I think it would be good to think of this as 2 levels of information (if not more).

1. Beginner Wiki:  Think the Wiki gawag has produced is the best I've found. It covers a lot of beginner stuff that those who have no exposure to Urho3D need. [/quote]
Oh my  :blush:  :laughing: #Flattered
How did you find that wiki? My signature here? Google?

[quote="dvan"]
I've referenced it many times over the past weeks+.
[/quote]
Do you mean as in "visited" or as in "mentioned it to other people"? Are you in some kind of team? What are you doing with Urho? What skills do you have? We can need every helping hand and I can't do everything alone especially in areas where I'm not good at, like modelling (for sample projects or to improve the samples shipped with Urho).

[quote="dvan"]
2. Best Way Wiki:  There is a big difference between the basic way to get things done, and the best way to do something for a given situation. Think the "official" Wiki could focus on the "Best Practice" way with efficiency and performance focus. 
[/quote]
There doesn't have to be two wikis to do "Best Way" and "Beginner". There could be short and simple overview/introduction articles and articles that go into more details on the same wiki. Like I did with the "Building Urho" tutorials, they are like those quick assembly instructions with many pictures that accompany some products in contrast to their much more detailed manuals. That's why I'm referencing the official documentation ("the manual") for more details in the tutorials.

[quote="dvan"]
That said, I would rather the core Urho3D developers spend their time on improving the API and working on the next version incorporating updates to existing code and fixing / enhancing things as they come up.
[/quote]
Yeah that's also one of my main concerns and the reason I want a community wiki as apposed to one where core devs have to read and accept every change (someone mentioned a push-pull system that sounded like this). But we also need people who know Urho quite well, I'm usually not sure if I'm doing something in a good way and the API documentation is rather thin. Something like short notes would be great (from core devs or experienced users) that can get turned into full articles by others. Like a "oh this article describes a bad way of doing it, would be better to use that and that"-note or a "We could need an article about ... this can be achieved by ... can someone describe that in more detail and test that."

[quote="dvan"]
There are a lot of "hint's" and notes scattered throughout the forum. Would be nice we could find the "best practice" or solution for a given problem, but currently it's digging through pages of stuff to just find hint's of notes that may or not relate / solve the current issue I'm looking at. Just a list of "solved" problems people have reported or struggled through would be a huge ++.

Keep in mind... people are inherently lazy (my self included). Don't expect many to get involved with either of these Wiki. But, the best chance of any involvement is when the focus of the Wiki is defined, and easy to contribute to.
[/quote]
Exactly. "easy to contribute to" is also one of my main points already pointed out in this thread and defining the focus is what I'm currently trying to get out of this thread but nothing so far. I already wrote several ideas but I'm still waiting on some comments from core developers or others. Maybe that should be asked in a GitHub issue to be more visible, "improving the examples graphically" and doing sample projects is also a point of this whole "improving Urho" topic. 

[quote="dvan"]
gawag:  Just decide what you would want to spend time with, and do that. Others who many contribute or reference would want the easy/quickest access. Seems like it would remain an "Unofficial" Wiki. Think the "official" Wiki could just link to it.
[/quote]
It's not that I'm against the official wiki. Image uploading is the biggest thing bugging me about GitHub Wikis but that's also bugging me on the new Unofficial WIki (both are unhandy). Also embedding videos like from YouTube seems to be not possible. That's why I asked about maybe doing an official wiki elsewhere but that didn't seemed to have been considered.

@dvan and other: What do you need the most? What are you working on? Are you stuck somewhere? What is difficult (Urho wise or general programming or game development wise)? What is missing (the most) in the official documentation or the Unofficial Wiki? We really need more comments about such things.
The stuff others and I did seemed helpful to some people but we could need more comments like "this area didn't have to be so long", "focus should be more on X", "I didn't get that part", "I don't know how to do X and an article would be great", "I got an idea for an article", "this forum thread X could be made an article", "would have been helpful if X would be explained somewhere, took me days to figure out", "I did X and an article would be great for others but I need help" and so on. That's why one of the thing I had planned for the new Unofficial Wiki is a todo-, wish- and stuff-being-worked-on-list.

-------------------------

dvan | 2017-01-02 01:09:59 UTC | #67

gawag, Just me, doing this for "fun"!

Working on simple 2D stuff to explore the API. Urho3D seems less supportive of 2D than some other environments, but I really don't know how true that is (just too new at game dev.). 2D is not really where I'll stay. Don't want to hijack this tread, but here are a couple of examples from past week or 2.

1. Screen Re-sizing: Spent some time getting scaling under control, then noticed that when I resized the screen, the mouse would go crazy. Dug around this forum and saw it had been reported and quickly fixed in a nightly release. I haven?t verified it (staying with the 1.5 release for now), but assume it was fixed and allowed me to move on. This is very good, but took a few hours to find that info. Would be good if a user (dummy) friendly ongoing bug list was kept, organized into various categories or easily searchable, etc.. Just takes too much digging now.

One of the things I did want to do was limit the screen size a user can adjust to. There does not appear to be in the API anyway for the code to adjust or set the screen size. We can read it, but not set it. Gave up on that for now. I'm a long way from digging into anything deeper that what the API provides (becomes an ongoing support issue too).

2. Sound Delay:  There appears to be a delay in the sound system. I have setup a simple "hit" ping when collisions occur, and there is a real concerning delay. I'm just using simple collision messaging to detect that, so was thinking I needed to get more sophisticated about it anyway to avoid double hits, etc. (you mentioned that on your wiki), checking frames or using ray tracing, etc., but not sure what the best approach to tracking collisions really is (in general or my specifics). There seems to be quite a few ways. Thought I'd change that and see if it helps my sound delay, but not convinced it will. Not sure where the issue really is. Urho3D has a few ways to approach sound also (at least when 3D is involved) and I've only tried the simplest one I've found (again, notes from your wiki).  Maybe there is a way to prioritize this over that?

I still am spending quite a bit of time changing my development environment around. Think that comes with the flexibility Urho3D offers. One thing related is the dependencies for release. Depending upon your environment and the target (just different versions of Windows for example), it seems that various .dll's are needed (VCxxy, or D3Dxx, etc.). No clear list of "this for that" that I've found. Lots of scattered notes, and some of them are probably dated by now.

-------------------------

weitjong | 2017-01-02 01:10:00 UTC | #68

[quote="gawag"]You got me totally wrong there! :unamused: 
I didn't want to say that it's a competition and it's also not the case that I don't want to participate in "an official wiki" / that GitHub wiki.
I just wanted to say that I want some clarity on what that "official Github wiki" is supposed to be. What kind of content should be on the official one? That effects if there is still material or a reason for a separate "unofficial wiki" or some other external site. It may merge or cover different topics or cover the same stuff in a chaotic way. What ideas do you or other core devs have? Is there some consensus? What are the general plans and goals regarding Urho? Is there a page or some implicit plan/goal? Is it just planned as a kind if user generated documentation strictly Urho focused? The Unofficial Wiki is/was more about "Game Development, with Urho3D as an engine and other stuff".
Like I just wrote an article about optimizing code, it's about copying data to an Urho3D::Image but it's still more a general C++ article so it would be kinda misplaced in any Urho wiki (I have no idea where to publish that article). I also figured out how to draw on an Urho3D::Image and creature a texture out of it ([post10670.html](http://discourse.urho3d.io/t/faster-manual-image-texture-painting/1764/5)), that's definitive something for an Urho Wiki article/HowTo (took me a while to figure out (the documentation could be improved) and I still don't know if I'm doing the proper thing or if there is a better Urho way).[/quote]

I am glad to hear that you are at least considering to participate in the wiki on GitHub. Note that we/I have never pronounced it as "official wiki".  As for all the other questions you asked, if I may sum them all up in one sentence then you are asking about our "wiki roadmap"[?] If so, then I don't have the answer also. The fact is, if you even ask what is the Urho3D development roadmap then none of us will be able to give you any definitely answer, let alone the roadmap for the wiki itself. The wiki pages should be read and written by any of us, so I would like to think that the answers are already available in each of us. It should grow organically by itself without much governing control.

Enough talking. Our wiki did not get any traction in the past, I think, because it did not have a good start and none of the core developers got involved. So this time round, I promise to spend some time to seed the wiki with some "Getting Started" articles for each target platform: Linux, Android, Rasperry-Pi, Windows, OSX, iOS, and tvOS (yes Apple tvOS is coming real soon). After that, we will see from there.

-------------------------

gawag | 2017-01-02 01:10:00 UTC | #69

... me and my famous long posts  :unamused: ...

[quote="dvan"]gawag, Just me, doing this for "fun"!

Working on simple 2D stuff to explore the API. Urho3D seems less supportive of 2D than some other environments, but I really don't know how true that is (just too new at game dev.). 2D is not really where I'll stay. Don't want to hijack this tread, but here are a couple of examples from past week or 2.
[/quote]

Oh could we do some kind of simple 2D sample game out of your experience in that area? Like an animated character jumping around platfomer style or fighting stuff Zelda style or some Pacman thingy. What is your project about? I think there are three Urho 2D samples: one with 2D physics, one with 2D sprites and one with an animation being playing. Or could you write a bit about how to do 2D stuff in the wiki?

[quote="dvan"]
1. Screen Re-sizing: Spent some time getting scaling under control, then noticed that when I resized the screen, the mouse would go crazy. Dug around this forum and saw it had been reported and quickly fixed in a nightly release. I haven?t verified it (staying with the 1.5 release for now), but assume it was fixed and allowed me to move on. This is very good, but took a few hours to find that info. Would be good if a user (dummy) friendly ongoing bug list was kept, organized into various categories or easily searchable, etc.. Just takes too much digging now.

One of the things I did want to do was limit the screen size a user can adjust to. There does not appear to be in the API anyway for the code to adjust or set the screen size. We can read it, but not set it. Gave up on that for now. I'm a long way from digging into anything deeper that what the API provides (becomes an ongoing support issue too).
[/quote]
Hm can't find anything regarding setting the screen size either. The engine has these startup parameters where one can set the size [urho3d.github.io/documentation/1 ... ngine.html](http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_engine.html). Not sure if that can be only done at startup:
[code]engineParameters_["FullScreen"]=false;
engineParameters_["WindowWidth"]=1280;
engineParameters_["WindowHeight"]=720;
engineParameters_["WindowResizable"]=true;[/code]
BTW there's an event for changes in the screen mode, like the user resizing the window:
[code]
    SubscribeToEvent(Urho3D::E_SCREENMODE,URHO3D_HANDLER(gui,e_resize));
...
    void e_resize(Urho3D::StringHash eventType,Urho3D::VariantMap& eventData)
    {
        int w=eventData[Urho3D::ScreenMode::P_WIDTH].GetInt();
        int h=eventData[Urho3D::ScreenMode:].GetInt();
        lfgui::widget::resize(w,h);
    }
[/code]
Maybe the Engine::ParseParameters (const Vector< String > &arguments) can be called again during runtime to change stuff like the resolution? The Application class is feeding the parameters to the engine in the constructor I guess.

[quote="dvan"]
2. Sound Delay:  There appears to be a delay in the sound system. I have setup a simple "hit" ping when collisions occur, and there is a real concerning delay. I'm just using simple collision messaging to detect that, so was thinking I needed to get more sophisticated about it anyway to avoid double hits, etc. (you mentioned that on your wiki), checking frames or using ray tracing, etc., but not sure what the best approach to tracking collisions really is (in general or my specifics). There seems to be quite a few ways. Thought I'd change that and see if it helps my sound delay, but not convinced it will. Not sure where the issue really is. Urho3D has a few ways to approach sound also (at least when 3D is involved) and I've only tried the simplest one I've found (again, notes from your wiki).  Maybe there is a way to prioritize this over that?[/quote]
I haven't noticed any sound delay in my projects. At least not when the sound is properly edited (starting immediately at the start and not like 0.1 seconds in, which is not really noticeable by hearing when playing the sound outside of a realtime application like a game). Maybe it's a collision (notification) delay? I haven't done any 2D stuff.
I mentioned avoiding double hits in the wiki?
Oh maybe there are multiple collisions detected before your objects have pushed away each other and you start your sound multiple times and it only starts properly after the last noticed collision. Like playing the first silent 0.01 seconds multiple times before it gets to a hearable part at like 0.1s or something. You could have a bool that saves if there already was a collision in the last frame and you only start the sound if there was no collision previously (they just collided).

[quote="dvan"]
I still am spending quite a bit of time changing my development environment around. Think that comes with the flexibility Urho3D offers. One thing related is the dependencies for release. Depending upon your environment and the target (just different versions of Windows for example), it seems that various .dll's are needed (VCxxy, or D3Dxx, etc.). No clear list of "this for that" that I've found. Lots of scattered notes, and some of them are probably dated by now.[/quote]
Yes that also confuses me. On windows 10 (not sure about 7) one seems to have to install the June 2010 DirectX Runtime Thing to run Urho applications build with DirectX9, but nothing (at least not with MinGW) seems to be required to build that. DirectX11 could also require (only) this 2010 DirectX Runtime, not sure currently.

[quote="weitjong"]
I am glad to hear that you are at least considering to participate in the wiki on GitHub. Note that we/I have never pronounced it as "official wiki". As for all the other questions you asked, if I may sum them all up in one sentence then you are asking about our "wiki roadmap"[?] If so, then I don't have the answer also. The fact is, if you even ask what is the Urho3D development roadmap then none of us will be able to give you any definitely answer, let alone the roadmap for the wiki itself. The wiki pages should be read and written by any of us, so I would like to think that the answers are already available in each of us. It should grow organically by itself without much governing control.

Enough talking. Our wiki did not get any traction in the past, I think, because it did not have a good start and none of the core developers got involved. So this time round, I promise to spend some time to seed the wiki with some "Getting Started" articles for each target platform: Linux, Android, Rasperry-Pi, Windows, OSX, iOS, and tvOS (yes Apple tvOS is coming real soon). After that, we will see from there.[/quote]
Oh that sounds way better as I expected.  :smiley: I somehow expected you being mad again about something...
I just started a Wishlist which I had planed anyway: [github.com/urho3d/Urho3D/wiki/Wishlist](https://github.com/urho3d/Urho3D/wiki/Wishlist)
I could make articles about the first two entries as I did both things before. No idea if that will be the best way though. And no real idea about the other things, I just wrote things down that would be nice to know.

That GitHub Wiki is practically build into the Urho3D website that's why we called it the Official Wiki. It's practically saying "this is our wiki" which makes it the "main wiki" like the Ogre Wiki which is linked directly to from the main Ogre site.
Yes I was asking about if there is some kind of "wiki roadmap" or some ideas regarding it. I thought there would be some ideas in you or other core devs.
There's no Urho roadmap either? Nothing like "oh we wanted to do X and that wasn't possible with existing engines" or "In contrast to Ogre (or whatever) we want to do Y differently".
It it just playing around without a goal? I just discovered gamedev.net and Lasse ??rni / cadaver / AgentC being active there (the Urho3D project starter? no idea about the history and motivations behind the main devs). He seems to play around with various engines and performance stuff here and there: [gamedev.net/user/82042-agentc/](http://www.gamedev.net/user/82042-agentc/)

About me and my "goals".
I found Urho3D as I was searching for a free software and free engine, coming from mixed experience with Irrlicht, CrystalSpace and Ogre (I already got into more detail about that in for example my first post in this forum). Basically the engines I tried before Urho3D didn't work at all (Irrlicht) or not with MinGW on Windows (Ogre stopped supporting that years ago in their stable version) or had broken physics and graphics (Crystalspace) or got too inactive (Irrlicht, Crystalspace and Ogre). Ogre seems to be kinda active under the hood and to have switched to CMake which may make MinGW available again but it's still just a 3D engine and integrating sound and physic was possible but made using it unnecessary complicated. Ogre was the best of those three but had also so much outdated stuff like their libraries which are often still listed but no longer working (already years ago and still today).
So I came to Urho3D. I could built and use it with MinGW! Shadows were working (Crystalspace had broken ones back than)! It has physics integrated (I had ODE and/or Bullet combined with Ogre before but that was a mess)! And there were some "advanced" materials already available like bump/normal mapping (I had to manually write a weird normal mapping shader for Ogre)!

I read there's some activity towards this Physics Based Rendering that some modern games have. Would be good to have some kind of list of features that are being actively worked on. The GitHub Issues contain a bit but with unknown status.
There is some community activity in various field like integrating a better GUI and making more materials but I'm not sure if anything usable came out of any of that. The thread that I started in that direction is still empty  :frowning:  :confused: : [post10657.html](http://discourse.urho3d.io/t/urho3d-ressources/1763/1)

I have various game ideas and started playing with Urho which yielded these one and a half public sample projects [github.com/LFGUI/LFGUI](https://github.com/LFGUI/LFGUI). So much for my stuff. I think I wrote most of that already multiple times here... Would be nice to see what others are working on or towards. I guess no one would answer If I ask somewhere.
What I want is practically a free and usable engine. Usable with C++ and MinGW. Doesn't have to be the fastest one but performance should be "good enough". It should also be not complicated to use. It should be also recommendable to non-experts in game development (or C++).

"My Roadmap for Urho3D" (which I may also work on) / what I would like to see is a bit like this:
[ul]
[li]some samples are ugly and weird (they are representing what Urho can do but could do that way better!):
  - the car sample could be nicer with trees and grass instead of scaled up mushrooms
  - the physics sample with the boxes is ugly and before moving the camera the ball one can shoot missed the boxes by far, maybe use a more detailed box model and better materials for the boxes and floor
  - a Ninja with a sword throwing snowballs? ... The other character model in the samples is naked and has no texture
  - textures have usually a really low resolution and could use normal and/or specular mapping[/li]
[li]more materials available for Urho (maybe a material gallery sample?)[/li]
[li]have easily usable stuff like for a day-night-cycle, clouds, grass and other plants on terrain, nicer water with waves and underwater effects, ...[/li]
[li]projects with available source code that show how games can be done with Urho (full games or smaller sample projects)[/li][/ul]

-------------------------

gawag | 2017-01-02 01:10:01 UTC | #70

Oh regarding the screen mode change: [urho3d.github.io/documentation/1 ... ering.html](http://urho3d.github.io/documentation/1.5/_rendering.html)
There's a Graphics class with a SetMode function for that. [urho3d.github.io/documentation/1 ... 9e3d21d6eb](http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_graphics.html#adc16c8a19af1584c902fe29e3d21d6eb)
I was reading through the documentation and found that. Seems like I never really looked at it :open_mouth: Or maybe that part is new.

Oh, wow. I had no idea how to get that Graphics thing and just tried it with GetSubsystem:
[code]
virtual void Start()
{
  GetSubsystem<Graphics>()->SetMode(800,600);
[/code]
It works! Yay!

-------------------------

dvan | 2017-01-02 01:10:02 UTC | #71

Wow!  I probably spent a day's worth of hours looking for a way to control the screen size with code, And there it was!

I had found E_SCREENMODE and am using it to adjust my item scaling (didn't like the simpler ways I'd found in examples), so this is a quick fix!

Thanks gawag!!

Does bring up the need for better or different documentation, how-to, or ways to search for subjects and not just classes. Seems like things are heading in the right directions. Think I had to search through header files to create a mental list of existing event message capability, and probably still missed some. Maybe there is a real list somewhere that I also missed?

Going to work on collision detection for a while since I need to do that anyway. See if it effects that sound issue.

My "training" app is where I took sample # 27, and am just playing with pong or pinball functionality. Idea is to try a few levels in 2D and then add a few levels in 3D. It's really so I can learn the API and try/test various things from window sizing, physics, animation, controller stuff, and environmental stuff like dx9 vs. OGL, windows, linux, android, web, VM's, (Apple-TV, I like it), distribution requirements, size and performance limitations / trade-offs, etc.. All this capability is why I'm spending time with Urho3D.

As we saw in this window sizing issue, I hit something I want to do, spend hours looking for the way (not all bad... exposes me to a lot of other sidetracks, but gets old after a while), and then find out it was there all along, and simple!

-------------------------

gawag | 2017-01-02 01:10:02 UTC | #72

[quote="dvan"]Wow!  I probably spent a day's worth of hours looking for a way to control the screen size with code, And there it was!
I had found E_SCREENMODE and am using it to adjust my item scaling (didn't like the simpler ways I'd found in examples), so this is a quick fix!
Thanks gawag!!
[/quote]
 :smiley: Found that by random. I didn't knew that either. I was reading the documentation to see what is in there and how good it is explained. I'm pretty sure I looked into the documentation before, but I didn't see that part. Maybe it was new or I didn't look far enough.

[quote="dvan"]
Does bring up the need for better or different documentation, how-to, or ways to search for subjects and not just classes. Seems like things are heading in the right directions. Think I had to search through header files to create a mental list of existing event message capability, and probably still missed some. Maybe there is a real list somewhere that I also missed?
[/quote]
Oh yes that was also bugging me a few days ago. I wanted various input events like the mouse wheel and had to dig through header files to get vague informations about that. It worked after guessing and experimenting a bit. There could be an article listing all events with the data they have and their values/ranges (like the mouse wheel is -1 or 1 in Urho, Qt for example has -120 or 120 in my case).
The thing with different documentation structure came also to my mind. The thing with the settings is in there but a bit hidden. One has to go into the "Subsystems" section and there he finds "Graphics: Manages the application window, the rendering context and resources." which sounds right and is. Not sure what to do about that. Maybe like an FAQ that gives directions about all things someone may be searching for and/or contains small snippets, should link to the documentation for details (if available).

[quote="dvan"]
Going to work on collision detection for a while since I need to do that anyway. See if it effects that sound issue.

My "training" app is where I took sample # 27, and am just playing with pong or pinball functionality. Idea is to try a few levels in 2D and then add a few levels in 3D. It's really so I can learn the API and try/test various things from window sizing, physics, animation, controller stuff, and environmental stuff like dx9 vs. OGL, windows, linux, android, web, VM's, (Apple-TV, I like it), distribution requirements, size and performance limitations / trade-offs, etc.. All this capability is why I'm spending time with Urho3D.[/quote]
Sounds cool. That stuff is also really useful for others. For example I haven't looked at controller stuff (you mean gamepad/joystick right?). Are there special pitfalls somewhere in the stuff you tested? Could be worth writing down  :wink: . Like in my first sample project I had this issue with "fast" 3D objects clipping into solid objects and getting stuck inside. The object wasn't even that fast (a bit over running speed), I fixed that by doing physical ray traces between the last and the current position to reset the object if it passed through a collider. I made an idea entry on the wiki wishlist for that and plan to write about it. Add any ideas you have there too: [github.com/urho3d/Urho3D/wiki/Wishlist](https://github.com/urho3d/Urho3D/wiki/Wishlist)

Also I just encountered again this mouse movement bug with weirdly high speeds for a few frames after entering the Urho window again or switching between mouse modes. Could be related to this old bug: [github.com/urho3d/Urho3D/issues/433](https://github.com/urho3d/Urho3D/issues/433) (Maybe I'll report that bug after having it pinned down more).


Oh about the Urho Wiki:
Should less Urho focused stuff be also on there? Like articles about texture creation with Blender or more general shader stuff. A wiki would be good for that (so that others can edit it too). Would be good to have some place for that. If it's not on the Urho Wiki it would be good to link to it (and other ressource sites). Though what about stuff with a bit of Urho? Like shader stuff with the shader being in the "Urho format" (no seperate file for the different parts)? I think I have linked to to game development wikis from the new or both Unofficial Urho Wikis but I'm not sure if they would be suited. Any opinions/ideas?

-------------------------

