Leith | 2019-01-17 10:29:04 UTC | #1

Just wondering why the thread for Issues is on the github, but not here, or at least reproduced here.
It would be more efficient for me at least, to see everything in one place, and not dance around between hosts.
Is there a technical reason for not displaying the Issues threads here?

-------------------------

Modanung | 2019-01-17 10:55:37 UTC | #2

I think it makes sense to keep issues closer to the source and to not organize one thing in two places. Can  GitHub and Discourse be coupled in some way in order to mend the gap?

-------------------------

Leith | 2019-01-17 11:49:19 UTC | #3

I don't know, but I intend to look into it  - I expect GitHub can provide an RSS Feed, and Discourse can consume one? I know, I expect too much, but it seems reasonable and doable.

PS https://bandito.re/ we can emit RSS feeds from the git, now I need to check the other end, which I have no idea about - can our discourse read an RSS?

Apparently so : https://meta.discourse.org/t/enabling-rss-feed-on-discourse-setup/55647/2

Note this solution is all about piping stuff here from the git page, it does not necessarily work both ways, but at least we can all see and talk about things in one place

-------------------------

weitjong | 2019-01-17 16:03:40 UTC | #4

I beg to differ. I don't see any problem with current setup. IMHO, the issue log should be in the GitHub so that we can link the commits to the relevant issues. And I want to keep the relevant comments on the issue in the issue log too and not in other place. The forum should be used only for open discussions, support, etc, but not for bug reporting. See our [forum rules](https://discourse.urho3d.io/t/urho3d-forum-rules/8).

-------------------------

Leith | 2019-01-18 05:56:12 UTC | #5

I'm not suggesting that the github issues should be removed or replaced, but I am suggesting that we can set up a feed between there and here ;)
I apologize if I appear eager to change things, but a realtime feed from issues on github to here does not seem to be a bad idea, and it appears to be technically feasible at relatively little effort.
No offence intended!

-------------------------

weitjong | 2019-01-18 06:52:30 UTC | #6

None taken. But I also want to prevent comments for the issues to be posted here in the forum. And to do that, just don’t show the issues here.

-------------------------

Modanung | 2019-01-18 16:50:53 UTC | #7

Note that Discourse creates a so called onebox when placing a link to an issue or pull request on it's own line. For example:

https://github.com/urho3d/Urho3D/issues/2413

https://github.com/urho3d/Urho3D/pull/2412

So issues and pull requests can be pretty neatly linked to. Unfortunately this is not comment-specific. It will always show the first post in case of an issue.

-------------------------

