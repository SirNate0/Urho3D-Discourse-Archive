hdunderscore | 2017-01-02 01:15:44 UTC | #1

We've been looking at migrating from these forums to discourse, generously hosted for free without ads by discourse ([github.com/urho3d/Urho3D/issues/1505](https://github.com/urho3d/Urho3D/issues/1505)). The migration should be complete soon, however just giving some warning ahead of time so everyone knows what to expect.

You can view the forums here with some old data migrated: [discourse.urho3d.io/](http://discourse.urho3d.io/)

You will need to reset your password to log in. Some users may be too new to have an account there.

If you experience any problems or have some objection, feel free to voice it. Wouldn't want to repeat the Unity forum 'upgrade' debacle :wink:

-------------------------

cadaver | 2017-01-02 01:15:44 UTC | #2

Please email me (fastest response that way) when you want me to request the final SQL dump from this forum.

For me, Discourse will take some getting used to, but it's great to be rid of the ads and random downtimes :slight_smile:

-------------------------

Enhex | 2017-01-02 01:15:45 UTC | #3

A welcome change!

I'm not familiar with Discourse, but shouldn't the subforums be mapped into a category for each one so users can filter topics according to them?

-------------------------

hdunderscore | 2017-01-02 01:15:45 UTC | #4

Looks like in mobile view the filters don't show maybe?

Currently on desktop you do get the filter options, but since it was a direct import of these forums there are categories and sub-categories, eg: [discourse.urho3d.io/c/urho3d-user-forum/showcase](http://discourse.urho3d.io/c/urho3d-user-forum/showcase) . It probably makes sense to reduce it to just categories in the final move.

Edit: Alternatively you can look at the categories view: [discourse.urho3d.io/categories](http://discourse.urho3d.io/categories)

-------------------------

weitjong | 2017-01-02 01:15:46 UTC | #5

Let me know when it is time to change the forum URL on our website.

-------------------------

rasteron | 2017-01-02 01:15:47 UTC | #6

This is just right, a modern forum for a modern game engine. Perfect fit.

-------------------------

Modanung | 2017-01-02 01:15:49 UTC | #7

I would really like to see an optional [url=https://github.com/B-iggy/discourse-dark-theme]dark theme[/url] on the new forums.
But seems like a good move. Could links to posts and threads be converted too, after the migration?

-------------------------

hdunderscore | 2017-01-02 01:15:50 UTC | #8

@Modanung, good news is looks like we can put in themes, but a quick test of that theme seems to be a little off, maybe it was intended for a different version.

I will look into the links, I believe it should be something that is handled during migration.
edit: The links will be updated in the final migration.

-------------------------

Modanung | 2017-01-02 01:15:50 UTC | #9

[quote="hd_"]@Modanung, good news is looks like we can put in themes, but a quick test of that theme seems to be a little off, maybe it was intended for a different version.[/quote]
Ok, it was just an example, not a theme-specific suggestion.

[quote="hd_"]The links will be updated in the final migration.[/quote]
Awesome :slight_smile:

-------------------------

hdunderscore | 2017-01-02 05:20:29 UTC | #10

The new forums are ready with new data. The old forum will be put into read-only soon, and any posts there won't make it across. I encourage the use of the new discourse, unless there happens to be some unexpected error.

You will need to reset passwords again-- alternatively you can log in with your github accounts and it should be linked with your forum account if they use the same email address. 

If you use a different email address and you want to log in via github, reset your old password, log in and request an email change to your githubs email then you will be able to log in through your github account.

-------------------------

weitjong | 2017-01-02 03:25:46 UTC | #11

I think we need the inverse logo to be used on dark background, like the one in the top nav here.

-------------------------

hdunderscore | 2017-01-02 03:31:22 UTC | #12

Feel free to make the change, upload the image to the assets post and make change in admin panel :D

-------------------------

boberfly | 2017-01-02 18:29:34 UTC | #13

Yeah new forum! Just testing to see if this works, do old account messages get auto-linked to your name or email with the new account? By the looks of things, "Suggested Topics" are all the ones I've started in the past, despite using my Github account to log-in this time which was never linked to the old forum. Cool!

-------------------------

jmiller | 2017-01-02 19:05:02 UTC | #15

Excellent work! :slight_smile:

The only issue I have seen is minor: [gist] and [video] bbcode tags may need a little something.

-------------------------

Modanung | 2017-01-02 22:18:34 UTC | #16

For videos (and other links) Discourse apparently creates a so-called onebox when you put the link on a separate line. So simply removing the tags should fix most of those.

https://github.com/discourse/onebox

-------------------------

jmiller | 2017-01-02 21:49:07 UTC | #17

I'm thinking of the tags in the already existing posts. The URLs are intact, but the links are left nonfunctional.  Maybe those can be automatically converted with a bit of PHP or editor work, or...?

-------------------------

hdunderscore | 2017-01-02 21:59:54 UTC | #18

I updated the logos, I think they look a bit better.

It should be possible to fix the tags if it bothers a lot of people.

-------------------------

jmiller | 2017-01-02 22:26:05 UTC | #19

Looking really nice.  I can easily fix my own tags. Others can decide what to do about the others, if anything. :)

-------------------------

artgolf1000 | 2017-01-03 07:41:58 UTC | #20

Dark background please.:eyes:

-------------------------

hdunderscore | 2017-01-03 08:16:30 UTC | #21

Certainly don't want to play around with things too much to confuse or upset anyone, but since it's all still new maybe we can get a feel for things. I've put up a darker colour scheme for testing.

On one hand I like light because it feels more open and maybe feels more connected to our github, on the other I do like the benefits of not blasting my eyes with white.

-------------------------

1vanK | 2017-01-03 09:14:54 UTC | #22

It is really hard for me to read gray text on gray background

-------------------------

hdunderscore | 2017-01-03 10:05:42 UTC | #23

That's bad so I reverted it to defaults. It seems like it's possible to create a custom css and share the preview link for evaluation, although that will take a little more effort to set up.

-------------------------

hdunderscore | 2017-01-03 20:22:44 UTC | #24

One of the cool new features on this forum is being able to mark posts as solutions, I have now enabled it on the Discussions sub-categories and encourage future posts to make use of them.

https://meta.discourse.org/t/discourse-solved-accepted-answer-plugin/30155

-------------------------

