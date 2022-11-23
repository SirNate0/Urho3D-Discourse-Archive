Lumak | 2018-03-16 04:42:24 UTC | #1

It would change the dynamics of your AI, allowing skilled enemies to get to the player much sooner.

Character colors:
* white - can traverse on white
* blue - blue + white
* green - all

https://youtu.be/OP1NM18x9pc

-------------------------

Lumak | 2018-05-04 05:16:53 UTC | #2

I'm considering creating a repo for this. But, would it be a waste of github space and waste of my time like many other repos that I've created?

edit: I actually created a repo already - https://github.com/Lumak/Urho3D-NavPolyFlag-Editor
I'm considering whether I should complete it or remove it.

-------------------------

slapin | 2018-05-04 10:49:05 UTC | #3

Your repos are not wast of space. Don't think that if I do not say anything then I ignore. I really consult your code quite often for ideas. Your offroad vehicle, effects repos are frequently consulted by me (I don't think I'm unique here). I just have fucking too little time to comment, but I will really need this later, when I will reshuffle NPC code, just as soon as I finish with NPC editor. So please create the repo, it is VERY useful and thank you so much for your work!

-------------------------

Lumak | 2018-05-04 14:52:12 UTC | #4

Ok, I'll complete the repo, but it won't be fast as I'm doing this while making a game (finally).
Here's what's completed (as seen in the video):
* edit tiles with different polyflag mask values, and you can specify any mask value to treat it as untraversable (essentially a hole). For the demo I specify MSB as disabled.
* setup crowd manager's dtQueryFilters and specify agent's (character's) query filter type to adhere to -- agent's own color for clarity.
* save and load edited polyflag navmesh to a navfile -- loading a navfile would bypass the navmesh build process.

What I'd like to accomplish is to be able to load the entire scene from an xml file that'll include crowd management and agent info and have it fully function w/o writing code to have the same sample fully functional. This will probably not get in on the 1st phase, and is TBD when it'll get added.

-------------------------

yushli1 | 2018-05-08 03:03:25 UTC | #5

Thank you for all the repos you created and open sourced. That helps a lot.

-------------------------

Lumak | 2018-05-15 16:49:26 UTC | #6

Initial check in uploaded. Let me know if I missed something.

-------------------------

