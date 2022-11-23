Modanung | 2020-10-31 12:44:11 UTC | #1

When "open source loving" Microsoft [announced to acquire](https://discourse.urho3d.io/t/microsoft-is-acquiring-github/4286) GitHub, I migrated all my projects to [GitLab](http://gitlab.com/) and have been avoiding GitHub ever since. But every I time I *do* visit GitHub, yet another feature seems broken. By now:

1. I cannot upload avatars
2. Emojis are broken
3. History within subfolders does not load
4. Authorizing outside services is broken

Am I the only one experiencing this, or may it be time to migrate before it sinks?

[poll name=decay type=regular results=always public=true chartType=bar groups=trust_level_1]
# What should we do?
* Stick to GitHub
* Abandon GitHub for something else
[/poll]

Btw, it seems somebody created Urho and Urho3D groups on GitLab without putting them to use.

**EDIT:** The poll may be too vague to reach a final decision, follow-up polls could provide more clarity.

-------------------------

Modanung | 2020-10-31 16:06:51 UTC | #2

Note that GitLab also allows for self-hosting.

https://gitlab.com/gitlab-org/gitlab-foss

-------------------------

1vanK | 2020-10-31 11:10:15 UTC | #3

Is discorce related to github?

-------------------------

Modanung | 2020-10-31 11:11:10 UTC | #4

Apart from being hosted there, I think not.

-------------------------

rku | 2020-10-31 11:19:55 UTC | #6

I do not see how any of listed arguments have any impact on the project. Suggestion seems to be purely politically motivated. In different words: doing a heavy work migrating project will yield no benefits, while come at a significant cost, both in effort to migrate and in feature loss. I do not believe gitlab offers this much CI resources for free.

-------------------------

Modanung | 2020-10-31 11:32:16 UTC | #7

I think that's what self-hosting and runners are for:
https://docs.gitlab.com/runner/

And you don't care for history? :face_with_raised_eyebrow:
All the rest just signifies a _falling apart_.

-------------------------

Modanung | 2020-10-31 11:30:22 UTC | #8



-------------------------

Modanung | 2020-10-31 11:35:45 UTC | #9

I replaced the poll in the first post with a simple yes or no.

-------------------------

Modanung | 2020-10-31 13:00:54 UTC | #10

[quote="rku, post:6, topic:6482"]
Suggestion seems to be purely politically motivated.
[/quote]

Ideologically, *partially*... but political? How?

-------------------------

rku | 2020-10-31 11:37:29 UTC | #11

[quote="Modanung, post:7, topic:6482"]
I think that’s what self-hosting and runners are for:
[/quote]

That costs. Not to mention this invalidates all the effort of migrating to gh actions, almost on the next day it was done.

-------------------------

Modanung | 2020-10-31 11:41:00 UTC | #12

[quote="rku, post:11, topic:6482"]
That costs.
[/quote]

Only if you think that way.

-------------------------

Modanung | 2020-10-31 13:04:59 UTC | #13

> :musical_note: [**I Saw the Sign** by _Ace of Base_](https://www.youtube-nocookie.com/embed/iqu132vTl5Y?autoplay=true)

-------------------------

weitjong | 2020-10-31 15:05:42 UTC | #14

[quote="Modanung, post:1, topic:6482"]
Btw, it seems somebody created Urho and Urho3D groups on GitLab without putting them to use.
[/quote]

I actually want to know who has the audacity doing that :smiley:.  But rest assured unless until one day MS drop the ball, we will be staying here on GitHub.

-------------------------

Modanung | 2020-10-31 15:09:44 UTC | #15

[quote="weitjong, post:14, topic:6482"]
But rest assured [...] we will be staying here on GitHub.
[/quote]

In my case, that's the opposite of assuring.

-------------------------

weitjong | 2020-10-31 15:25:52 UTC | #16

But why you so hate MS? I also not its fan but nowadays this company is not so bad anymore (after Steve Balmer left).

-------------------------

Modanung | 2020-10-31 15:29:01 UTC | #17


[quote="weitjong, post:16, topic:6482"]
But why you so hate MS?
[/quote]

Because I'm relatively well-informed, apparently.

-------------------------

Modanung | 2020-10-31 15:31:21 UTC | #18

I cannot believe the *ubiquity* of gullibility.

-------------------------

weitjong | 2020-10-31 15:31:19 UTC | #19

We all live in a not so perfect world.

-------------------------

Modanung | 2020-10-31 15:32:21 UTC | #20

And I was *hoping* we're trying to make it a better one. But I guess that's just me.

-------------------------

weitjong | 2020-10-31 15:33:10 UTC | #21

When you have reached my age, probably you will see the world the same as me.

-------------------------

Modanung | 2020-10-31 15:35:47 UTC | #22

You *do* realize you are a *part* of this world you speak of?

Not even the dead are powerless.

-------------------------

weitjong | 2020-10-31 15:41:21 UTC | #24

I have a few more buckets to kick and ready to see the next one.

-------------------------

Modanung | 2020-10-31 16:01:24 UTC | #25

I think it would be foolish to expect people to continue using that shaky construction much longer.

Enjoy the barrage, while I yearn for `source.urho3d.io`.

-------------------------

vmost | 2020-10-31 16:42:25 UTC | #26

For reference, open source project Monero [tried out Gitlab](https://github.com/monero-project/meta/issues/236#issuecomment-572720802) and ultimately decided not to migrate there.

-------------------------

Modanung | 2020-10-31 16:51:07 UTC | #27

The best option, in my view, would be to *self-host* [GitLab FOSS](https://gitlab.com/gitlab-org/gitlab-foss)... but in the end it's just a git server.

-------------------------

rku | 2020-10-31 16:59:20 UTC | #29

What i miss most in such discussions is cost/benefit analysis. So far i see only costs and no benefits.

-------------------------

Modanung | 2020-10-31 17:01:58 UTC | #30

Fear of the unknown is all too common, even when facing impending doom.

-------------------------

rku | 2020-10-31 17:17:19 UTC | #31

I will take it as "i have no data to back up my claim".

-------------------------

Modanung | 2020-10-31 18:17:42 UTC | #32

Empty words for an empty mind.

-------------------------

vmost | 2020-10-31 18:37:56 UTC | #33

Dude... [you are a moderator](https://discourse.urho3d.io/guidelines#agreeable)

-------------------------

Modanung | 2020-10-31 20:11:53 UTC | #34

Those are guidelines, not rails.

-------------------------

vmost | 2020-10-31 20:22:39 UTC | #35

A cheap excuse... Surely there is a higher standard for someone with the word 'Leader' next to their name.

-------------------------

Modanung | 2020-10-31 21:06:32 UTC | #36

Indeed, it is not the standard.

https://www.youtube.com/watch?v=QhJ6bE4z5vs

Happy bury y'all.
:wave:

-------------------------

weitjong | 2020-10-31 21:22:36 UTC | #37



-------------------------

weitjong | 2020-10-31 21:25:21 UTC | #38



-------------------------

