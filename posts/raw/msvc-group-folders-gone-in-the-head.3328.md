Lumak | 2017-07-06 22:15:37 UTC | #1

Whose bright idea was it to do this?

[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/0b6050fd1eee892e0a5fbc3ce44bb4119d17ce97.jpg[/img]

-------------------------

weitjong | 2017-07-06 22:57:24 UTC | #2

That would be me :slight_smile:, although that was not the original intention. If I recall correctly the "source_group" was changed in order to fix a long known issue in Xcode where it always complained about the resources being added into multiple groups. The "source_group" for the sources were also changed/dropped around that time because somehow I think that is simpler, i.e. one doesn't need to know where the group before opening a file. The sources are just grouped either as "Source Files" or "Header Files". It has been like that for many months already! It should not be difficult to put the script back though (anyone can do it). I believe the "source_group" thingy is only being honored by VS and Xcode, and ignored by the rest of the IDEs.

-------------------------

Lumak | 2017-07-06 23:04:50 UTC | #3

I see. Yeah, I don't update to the head often. Just looked at what I call "Urho3D-1.6-Orig" folder, where everything in that folder never gets touched and where I make copies from for different type of projects, is dated Dec. 27, 1016.

Ok, I'll make changes to add the "source group" to my msvc projects. Although, I hate the idea of having to do this every time I update to the head... but that only happens every 6-7 months, haha.

-------------------------

weitjong | 2017-07-07 01:34:36 UTC | #4

If the majority VS users think otherwise also, we could try to carefully add back the source group without causing any regression to Xcode's build tree generation.

-------------------------

Eugene | 2017-07-07 08:34:12 UTC | #5

I've just re-generated Urho and was scared by this source mess. It definetely have to be reverted for Visual Studio.

-------------------------

JimSEOW | 2017-07-07 10:09:56 UTC | #6

Hi Eugene, can u revert? Are u using VS2015 or VS2017?

-------------------------

JimSEOW | 2017-07-07 10:14:49 UTC | #7

How often this one-person decision to change something without requesting feedback from VS users? Pls let me know so I could make the appropriate recommendations.

If this happens often, we need to implements a community best practice. Otherwise months of work went down to drain

-------------------------

weitjong | 2017-07-07 10:15:19 UTC | #8

What is your point? Are you suggesting I am breaking VS build on purpose?

-------------------------

JimSEOW | 2017-07-07 10:18:25 UTC | #9

Weighing, u have the big overview that all of us depend on you. If you see something needs to be done, no one can question your decision. 

When user feedback, it is a chance for community to learn as a whole.

-------------------------

weitjong | 2017-07-07 10:19:04 UTC | #10

You didn't answer my question.

-------------------------

JimSEOW | 2017-07-07 10:22:56 UTC | #11

We are deciding if we could go ahead to do something that will have a great impact to children all over the World using Urho3d through UrhoSharp. I need to get feedback if this decision is,wise or the whole vision depends on a few here. U get my point. I only focus on big picture. What is good for the majority.

-------------------------

weitjong | 2017-07-07 11:21:42 UTC | #12

Already explained to Lumak why the change was made. And that we are all human and that mistakes do happen. Urho3D is a cross platform project, with that it means it is easy to inadvertently break other platform or build on other IDE due to limited tests. When that happened, we just own the problem and fix it. So, what is your issue. What is your point?

-------------------------

weitjong | 2017-07-07 10:33:09 UTC | #13

If you want make Urho great, by all mean do it. Don't just talk rubbish here.

-------------------------

JimSEOW | 2017-07-07 10:47:39 UTC | #14

Your guys have done good. I tried 12 months ago. No success. Now i am comparing UWP XAML interop for SharpDx, OpenGLE, and UrhoSharp. Before Trying Urho3D again, try to figure what have achieved. Great job to all have contributed.

-------------------------

weitjong | 2017-07-07 11:00:33 UTC | #15

I think we are rather off topic now. So, may I request you to create another topic to further your discussion there. Thanks.

-------------------------

JimSEOW | 2017-07-07 11:29:00 UTC | #16

Sound like a plan :-)

-------------------------

weitjong | 2017-07-07 15:51:58 UTC | #17

I am home and have some free time. Since this is a matter of great emergency, the "source mess" is being dealt with immediately :slight_smile:. Tested on both Win7 VM (for Windows 64bit platform only) and Mac VM (for macOS + iOS platforms only).

-------------------------

cadaver | 2017-07-07 20:37:20 UTC | #18

Can confirm source folders appearing in VS2015. Thanks!

-------------------------

Eugene | 2017-07-08 08:37:06 UTC | #19

Thanks! It works now.

-------------------------

Lumak | 2017-07-08 18:40:50 UTC | #20

Thx, weitjong. saved me the trouble.

-------------------------

