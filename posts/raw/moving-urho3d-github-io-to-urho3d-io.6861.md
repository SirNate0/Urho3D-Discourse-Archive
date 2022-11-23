weitjong | 2021-05-28 09:02:58 UTC | #1

This is the thing that we should have done it a few years ago, but we did not because the person who maintaining the gh-pages and the person who owning the domain name was not the same person. While investigating this unrelated [issue](https://discourse.urho3d.io/t/dnssec-issue-with-forum/6810) recently, I find that it is just a few clicks away to link the two together. At this juncture of the Urho3D project life, this does not really matter much, but at the very least it saves you a few key strokes to access the main site :slight_smile: 

urho3d.io

-------------------------

weitjong | 2021-06-05 14:02:13 UTC | #2

The DNS updates propagate faster than I thought. I still have to do a search and replace everywhere in our docs to use “`urho3d.io`” consistently. While I am at it, I may “refresh” the gh-pages with a newer static site generator technology. Don’t hold your breath for it though.

EDIT: completed the migration setup on "Google Search Console" and "Google Analytics" too. Let's hope we keep the SEO ranking.

-------------------------

weitjong | 2021-05-29 11:50:04 UTC | #3

So, I have started working on a new website using ReactJS and Docusarus 2. In order to speed up the work, I will reuse the existing content from the old website as much as possible and will use some of the screenshots from the Showcase category in the forums as new assets. For the screenshots as new assets, I assume I am allowed and has permission to do that. However, if this is not the case then the copyright owner of the screenshot can just inform me and I will substitute it immediately. Obviously I will only choose those that are relevant to Urho3D :slight_smile:, but I haven't started choosing any yet. On the other hand, if you want the screenshots from your new game to be featured/showcase in the website, you can also PM me with the relevant material.

My plan is to release the new website progressively over the next few weeks, migrating the content from the old Jekyll site to the new one bit by bit, instead of one big bang like the one I did many years ago. It was the Jekyll site that we use till today.

-------------------------

johnnycable | 2021-05-29 16:02:30 UTC | #4

You have my bypersonal, nonconfident, outproprietary, subjugated, preposterous,  irrevocable permit and/or agreement to 

http://www.wtfpl.net/


with my content. Hopefully the others will do the same.
HTH

-------------------------

weitjong | 2021-06-06 02:11:21 UTC | #5

The "News" (aka blog) section is now in. Temporarily there are two "News" in the navbar. The left hand side is the new one, while the right hand side is the old one. I have migrated the last 4 news entries only. I won't be wasting my time bringing every entry over. The news content is now hosted on the main repo under https://github.com/urho3d/Urho3D/tree/master/website/news. So, anyone could submit PR to add new entry and/or edit the existing entry. Urho3D maintainers (with push privilege) should be able to directly modify the entry using the Github web interface. Check out the link on the lower left corner on rendered page for each entry.

-------------------------

SirNate0 | 2021-06-07 11:10:58 UTC | #6

Is the documentation available anywhere while the new website is under construction?

-------------------------

throwawayerino | 2021-06-07 11:28:44 UTC | #7

It's still there, there's a legacy dropdown
https://urho3d.io/documentation/HEAD/index.html

---
Also, please tell me you're not keeping that red font on the front page.

-------------------------

weitjong | 2021-06-07 11:49:33 UTC | #8

[quote="SirNate0, post:6, topic:6861, full:true"]
Is the documentation available anywhere while the new website is under construction?
[/quote]

I have been very careful about that. In fact all the old links that people have around the internet will still be able to get served correctly. I will minimize the number of broken links. In fact the whole legacy website is still there, what really got changed so far is the "index.html" page with all the magic of React hydration in the background. In short, currently the website is in the hybrid mode.

[quote="throwawayerino, post:7, topic:6861"]
Also, please tell me you’re not keeping that red font on the front page.
[/quote]

It is in my believe that by displaying the pale bones of the dead fish and drawing some new blood, we could summon cadaver back in action. Or may be not :slight_smile:

-------------------------

throwawayerino | 2021-06-07 11:57:37 UTC | #9

Well I'm convinced .

-------------------------

johnnycable | 2021-06-07 15:05:28 UTC | #10

Well, seems to come up nicely...

-------------------------

Eugene | 2021-06-08 08:07:47 UTC | #11

Is there any practical reason why *news* and docs should be stored in the same repository with code? It obstructs the work of tools like git bisect and maybe wastes CI time (not sure how it’s configured)
https://github.com/urho3d/Urho3D/tree/master/website/news

I know that existing Urho docs are in main code repo as well, but is it really the only way it can be?

-------------------------

weitjong | 2021-06-08 08:17:23 UTC | #12

Why not? And why do you care?

The CI/CD will not be triggered if it only contains changes for the website content. When I make changes in the code, I may want to update the docs at the same time. Only in this case both the CI/CD and the website build event will be dispatched at the same time.

-------------------------

Eugene | 2021-06-08 08:32:27 UTC | #13

[quote="weitjong, post:12, topic:6861"]
And why do you care?
[/quote]
Because I’m working with git and doing git bisects regularly.
Unfortunately, git doesn’t know that these are “just doc” commits.

It’s not a big deal since I can always skip commits I don’t want to test, but it’s just one more point for not doing docs and code in the same repo.

I wonder how good “GitHub wiki” is... I don’t like the lack of control tho.

-------------------------

weitjong | 2021-06-08 08:56:03 UTC | #14

I don't care with how good you are with git. But have a look around with other projects. There are many projects with docs and codes at the same repo.

-------------------------

rku | 2021-06-08 15:09:23 UTC | #15

[quote="weitjong, post:12, topic:6861"]
Only in this case both the CI/CD and the website build event will be dispatched at the same time.
[/quote]

There is nothing that prevents us from creating a build job that builds docs/web/whatever using another repo.

-------------------------

weitjong | 2021-06-08 15:28:16 UTC | #16

[quote="rku, post:15, topic:6861"]
There is nothing that prevents us from creating a build job that builds docs/web/whatever using another repo.
[/quote]
You can do whatever you like in your fork. Please leave us die alone. We don't care what you do over there, so please stop giving us instructions what we can or cannot do in our own project.

BTW. The whole github actions for the new Urho3D website project is in place now. Any pushes to the website content will trigger the website build on my private repo, which in turn will  deploy the built result back to `urho3d.github.io`. There are still teething problem but nothing major. I will fix that when I am in the mood again.

The builder is in my private repo, so no copycat can steal my work.

-------------------------

weitjong | 2021-06-08 15:59:16 UTC | #17

Just to be clear, our MDX files will contain custom React components that only my/our builder can understand. The custom components will make the website unique. Unfortunately, it will also mean that our MDX files will only be useful specifically for Urho3D project.

-------------------------

1vanK | 2021-06-08 19:02:59 UTC | #18

If I understand correctly, then users will not be able to generate documentation locally on their computer? I'm not sure how much this is in the spirit of open source.

-------------------------

amerkoleci | 2021-06-08 21:19:19 UTC | #19

Calm down dude and don't act like 10 years old kiddo, as I can read he was just suggesting and wasn't any kind of personal attack.

I mean, what does this mean:

You can do whatever you like in your fork. Please leave us die alone. We don’t care what you do over there

-------------------------

weitjong | 2021-06-08 22:35:04 UTC | #20

Users will still be able to generate the API doc using Doxygen locally. However, they can’t generate the “website” locally, that looks like the final one on `urho3d.io`. That’s the drawback with my decision to make the builder a private repo, which I am willing to take. However, the online website will be PWA when I am done with my work, so it can be “installed” locally and read offline. So, I hope that addresses your concern.

Getting the website code (builder) closed source is to protect us from having multiple website clones later on. The code is also my own copyright. It is totally up to me whether to license it for others or not. If you hire a dedicated website designer to develop the website, you will probably get the same deal. You got the result deployed somewhere but not the code.

-------------------------

weitjong | 2021-06-08 22:44:14 UTC | #21

For those that do not follow the forum very closely for the past one year or two, my reaction to some people may seem rude. My apology if you are one of those readers. However, I have had enough with them. Every time when I/we doing something that may get the project into the right track, here they are to throw the curve ball at us. I have had personal attack from them in the past and I don’t feel bad to return some back. Again, my apology if that offend you.

-------------------------

rku | 2021-06-09 06:20:30 UTC | #22

Curve balls are thrown at particular decisions. If you can not handle criticism and you think your decisions are always perfect.. That explains state of things i guess. I am rather disappointed how your recent decisions never include users in equation. Dumping website on your users is not exactly nice. Or kotlin android cruft for that matter. This leaves urho in a weird state. It sort of is a public project that other people are supposed to use, but at the same time it is a personal playground for various (experimental) ideas, which does not play well into a public project description. This is where this confusion and irritation stems from.

P.S. seems to me you are the one swinging personal attacks at me the moment i start discussing technical points of some decisions. this sounds awfully a lot like @Modanung in gitter, which was lots of "no u troll" while continuously trolling.

-------------------------

weitjong | 2021-06-09 07:24:31 UTC | #23

Yeah, right. Why didn’t you start to give your bright idea on how to start to make thing better instead of just picking bones. For what I see, all you guys are protecting your own selfish interest. Less change on the main repo means less work on your fork. I got it.

-------------------------

rku | 2021-06-09 07:25:43 UTC | #24

[quote="weitjong, post:23, topic:6861"]
For what I see, all you guys are protecting your own selfish interest.
[/quote]
Of course. This is what everyone does. Your decisions impact me as urho3d user therefore i speak out. Thing is, i believe things i push for are beneficial for other users as well.

[quote="weitjong, post:23, topic:6861"]
Less change on the main repo means less work on your fork.
[/quote]
This claim has no basis in reality. Urho3D recently got a ton of commits regarding automated AS bindings. This benefits me in no way. Whats worse - all headers got littered with extra comments aiding auto-binding process, creating me a ton of extra work when doing merges. I have no complaints about that, as this is a very reasonable feature to have if project supports AS. So if i am so selfish, why do i speak out about something that takes me three clicks to solve and remain silent about something that wasted considerably more of my time? Answer is: because website on the repo benefits nobody and is very out of place, while AS bindings are a valid feature benefit upstream users. I can see you hate my guts, but it would be nice if you at least criticized me based on my actions, not based on what you think of me personally.

-------------------------

weitjong | 2021-06-09 07:31:09 UTC | #25

Again, I have absolutely zero interest on what happening on your fork. So, just leave us alone. Cut the umbilical cord with the upstream Urho3D repo if you are so afraid of the changes. This will be the last time I will respond to you. Next time you post anything here that tries to derail this thread again, I will ban you from my forum.

Just for the record, I have not heard anyone else complaining about the migration to Kotlin or the website move. Just you alone.

-------------------------

rku | 2021-06-09 08:20:46 UTC | #26

[quote="weitjong, post:25, topic:6861"]
Just for the record, I have not heard anyone else complaining about the migration to Kotlin or the website move. Just you alone.
[/quote]

We found more strange bugs that nobody ever complained about. Probably because nobody used those features. Same is true for android build system. I had enough problems with old gradle build system. Huge ecosystem behind it was enormously helpful troubleshooting all all kinds of stuff from weird gradle quirks to simple "how do i do xyz". Now imagine going through the same ordeal, except using a new fresh-from-the-oven system which even was alpha at the time of integration to urho. The fact that nobody complains does not mean everything is good. Nobody complains about rbfx either. Because nobody uses it :smiley:

-------------------------

weitjong | 2021-06-09 08:57:43 UTC | #27



-------------------------

weitjong | 2021-06-09 09:02:21 UTC | #28

This thread is closed as it has been derailed.

-------------------------

weitjong | 2021-06-10 16:59:24 UTC | #29

Just want to update that the initial teething issues that I mentioned before should be now all fixed. The CI/CD workflow should be now smart enough to bail out cleanly when it detects non-code change. The website event dispatcher workflow on the other hand should only dispatch the build event when it detects there are changes to the website content. Both workflows will run to their full course when the change is a mix of code and content.

Now with this behind me, I could focus on writing the content. English is not my primary language, so I need all the help.

-------------------------

weitjong | 2021-06-28 02:14:34 UTC | #30

It is progressing slower than I expected. Aside from moving the old content over, I also need to “refresh” a few section to reflect the current state in the master branch especially on the build system side. The doc update did not take place at the time I completed the rewrite of the rakefile and the new CI using GH Actions.

I was also slow down by the fact that I need to develop the custom React components for our website as I go. It is fun, however. Don’t be surprised to see better integration with WASM samples, including the Urho3DPlayer, later.

-------------------------

