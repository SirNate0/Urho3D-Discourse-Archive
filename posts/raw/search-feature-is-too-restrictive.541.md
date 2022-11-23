setzer22 | 2017-01-02 01:01:15 UTC | #1

Hello everyone!

I remember many times when trying to learn something new in urho that I had a hard time fighting the forum's search engine. For example.

When I wanted to write a custom shader and didn't really understand the documentation I thought: "Time to search the forum". To my surprise, the word "shader" is too common and the search engine chooses to exclude it from the search, so my searches were not restricted to shader-related topics.

I had more than a fight with this "too common" feature, and I think everyone would benefit from a more powerful search engine, specially newbies like me, because it's difficult not to replicate posts when the search ignores most of the keywords. Any ideas on that?

Also, any thoughts on joining the stackexchange network? I find that a way more powerful (and already implemented) Q&A site than the support subforum.

I'm sorry I can only apport ideas for now, my coding skills are not still at the level Urho needs and I can't really contribute with code, although I think I'm speaking in behalf of many newcomers who find difficult to adopt Urho3D for their projects.

-------------------------

gwald | 2017-01-02 01:01:16 UTC | #2

Hi,
Google crawls this forum.
You can use it to search like this:
[quote]site:urho3d.prophpbb.com shaders[/quote]
[url]https://www.google.com/search?q=site%3Aurho3d.prophpbb.com+shaders[/url]

-------------------------

thebluefish | 2017-01-02 01:01:16 UTC | #3

It won't be possible as long as the forum is being hosted through prophpbb as they manage all of the software used to run the forum, though it may be possible to change the settings depending on what's available in the admin panel. It's been years since I've admin'd a phpbb-based board (Mine switched to vBulletin a while ago), so I don't quite remember what is available.

If we switched to a self-hosted forum, we would need someone who is knowledgeable in such hosting solutions since there are security concerns, spam issues, and other problems that a non-experienced admin might not know how to resolve. So there's pros and cons to either way we approach it.

As previously mentioned, Google is your best bet in this case.

-------------------------

setzer22 | 2017-01-02 01:01:17 UTC | #4

Well I guess Google's search function is ok given the forum's size. Thanks for the tip!  :smiley:  prophpbb's search can be awful sometimes...

-------------------------

OvermindDL1 | 2017-01-02 01:01:19 UTC | #5

[quote="thebluefish"]It won't be possible as long as the forum is being hosted through prophpbb as they manage all of the software used to run the forum, though it may be possible to change the settings depending on what's available in the admin panel. It's been years since I've admin'd a phpbb-based board (Mine switched to vBulletin a while ago), so I don't quite remember what is available.

If we switched to a self-hosted forum, we would need someone who is knowledgeable in such hosting solutions since there are security concerns, spam issues, and other problems that a non-experienced admin might not know how to resolve. So there's pros and cons to either way we approach it.

As previously mentioned, Google is your best bet in this case.[/quote]
If there was a demand for it then I could always host it on my servers, they are remaining up for the foreseeable future (and I can give full system backups to who-ever as well at regular intervals).  I host the MinecraftForge sites, build server, forums, file hosting, everything, and can host it on the same server.  The new forum system that we have been setting up and experimenting with for the site design overall is Discourse,  you can see our in-progress tests of it (and feel free to mess with it to see how it works if you want in the meta category) at [url]http://discuss.minecraftforge.net/[/url].  It is a forum system made by the creator of Stack Overflow designed to be a Stack Overflow style Forum.  I can set you up a new instance if you wish and the instances are portable so if you wanted to move it to a new server of your own sometime then you just install discourse and copy the data directory, that contains *everything* for the site.  Only thing I would need is just some DNS pointed to it (discuss.urho3d.org or so?) or I can set up a temporary one (urho3d.overminddl1.com or urho3d.minecraftforge.net or whatever).

Discourse has amazing functionality built in and it is amazingly simple to integrate with external services.  it even has Github integration since it was designed to co-exist with Stack Overflow (see example of github integration at:  [url]http://discuss.minecraftforge.net/t/testing-a-new-topic/14/7?u=overminddl1[/url]).  I can walk anyone through how to set it up and manage it as well.

For note, this prophpbb website was down (SQL server was not responding error) for about a half hour last night, unsure if that is common, but eh...  Only time I take down Forge's is to install an update, usually down for about 5 minutes as I do.

-------------------------

weitjong | 2017-01-02 01:01:19 UTC | #6

It was not the first time our forum gone down and up again. We have had longer outage before. But considering we are not paying for anything, we do not complain much about it. Having said that, among Urho3D team members we have discussed about moving our forum server during the last outage. We have an action plan already. The plan is, to host the forum using the same server hosting our website currently and it will be powered by Disqus. It is still too early to say whether this plan could be implemented smoothly. So, I think we should keep it open minded for other hosting solution. Thanks for your offer. Chris also has offered similar setup using Discourse by the way.

-------------------------

OvermindDL1 | 2017-01-02 01:01:19 UTC | #7

[quote="weitjong"]It was not the first time our forum gone down and up again. We have had longer outage before. But considering we are not paying for anything, we do not complain much about it. Having said that, among Urho3D team members we have discussed about moving our forum server during the last outage. We have an action plan already. The plan is, to host the forum using the same server hosting our website currently and it will be powered by Disqus. It is still too early to say whether this plan could be implemented smoothly. So, I think we should keep it open minded for other hosting solution. Thanks for your offer. Chris also has offered similar setup using Discourse by the way.[/quote]
Discourse is an utterly fantastic forum system, however you get it hosted I do highly recommend it.

I always thought Disqus was more of a commenting system (which Discourse also has the functionality of, you can embed it in webpages like Disques to be a commenting system as well, I use it for that on the Forge site), so it would be interesting to see how it would work as a forum.

-------------------------

