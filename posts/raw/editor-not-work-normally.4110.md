att | 2018-03-20 14:57:24 UTC | #1

When I want to change node's properties, the Attribute Inspector always show "Selete editable objects".
Someone has encountered this problem?

-------------------------

johnnycable | 2018-03-20 15:53:46 UTC | #2

Are you on Os X? (20 char filler)

-------------------------

Eugene | 2018-03-20 16:09:31 UTC | #3

Ensure that Attribute Inspector isn't locked (button before close button)

-------------------------

att | 2018-03-20 16:17:59 UTC | #4

Yes, I run editor on my Macbook.

-------------------------

att | 2018-03-20 16:25:56 UTC | #5

Thank very much, It works.

-------------------------

johnnycable | 2018-03-20 16:23:23 UTC | #6

There's a long-running bug on 1.7 and Os X editor. https://github.com/urho3d/Urho3D/issues/2178
I use 1.6 version when I need it (rarely)

-------------------------

att | 2018-03-21 02:23:40 UTC | #7

As Eugene said, unlocking the Attribute Inspector make it works, but I must always check the lock state, it is annoying.

-------------------------

johnnycable | 2018-03-21 08:18:58 UTC | #8

Well well. Both me and @weitjong thought it was an editor bug. So it looks like it's a bug, but a different one: do not set this creepy thing (attribute inspector locking) on by default.
Is the feature documented somewhere?
I'll modify the issue to reflect this.

-------------------------

Eugene | 2018-03-21 08:26:24 UTC | #9

[quote="att, post:7, topic:4110"]
but I must always check the lock state, it is annoying.
[/quote]

I've never faced auto-locking Inspector (on Win 8 tho)
Actually, never used this feature.
Are you sure it's turning on automatically?

-------------------------

johnnycable | 2018-03-21 11:43:03 UTC | #10

I just run the editor after a native source build on Os X. Yes is on.

-------------------------

