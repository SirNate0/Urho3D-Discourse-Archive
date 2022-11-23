scorvi | 2017-01-02 01:01:12 UTC | #1

hey 

Two Game Jams, [url=http://7dfps.com]7DFPS[/url] and [url=http://itch.io/jam/procjam]Procedural Generation Jam 2014[/url], are starting tomorrow. 
I want to participate in one of these two. The last few weeks i had no time to do some programming but next week i have some free time to do so. :slight_smile:

Are there others, who have some interest to work together or just meet in an irc chat or so ?

-------------------------

hdunderscore | 2017-01-02 01:01:13 UTC | #2

Hm, they both sound like good jams -- 7DFPS, a chance to try make something unique about FPS's, ProcGen also includes tools as entries.

Does 7DFPS have a theme ?

If I do enter I might go solo, but it would be cool to bounce ideas around. I am in the #urho3d irc channel on freenode if you want to talk !

-------------------------

hdunderscore | 2017-01-02 01:01:21 UTC | #3

In the end I wasn't able to finish to a quality I wanted, although since I like the idea I was working on I'll definitely continue it at some point (it's something I was bouncing around in my head for a while).

I posted screenshots and blab here: [url=http://hdsanctum.com/post/102640015676/i-didnt-get-my-7dfps-entry-to-a-standard-that-i]Blog[/url]

-------------------------

Azalrion | 2017-01-02 01:01:21 UTC | #4

[quote]- Inheritance in scripts can trip you up. Node::GetScriptObject only grabs explicitly named script objects, so if "Bot" inherits from "Player" you're not going to find bot by looking for player. However, it was a natural enough choice to split the "Bot" away from the "Player" with the bot using the "Player" to make decisions. I think there's still some remnants of the "OR OR OR" nightmares.
[/quote]

Thats a good point, script instance was never improved even though script file lets you create objects via their interfaces now. I'll add it to the todo list.

-------------------------

