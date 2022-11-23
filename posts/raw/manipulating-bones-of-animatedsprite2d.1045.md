rku | 2017-01-02 01:05:02 UTC | #1

After reading source code of AnimatedSprite2D it seems there is no support for manipulating bones of a sprite. It would be great to have such functionality. Now very simple action like aiming rifle to the position of cursor is not really doable with keyframe animations. This of course should blend with executing animation so we can have running and aiming to arbitrary direction.

-------------------------

cadaver | 2017-01-02 01:05:02 UTC | #2

The AnimatedSprite2D does not have an API for bone control, but it creates internal child scene nodes with StaticSprite2D components for each bone, so in theory you should be able to get at these and manipulate their positions. However I haven't tested that in practice so I don't know if it interferes with the animation playback. At least trying to manipulate a child node with a currently playing animation track would lead to conflicts. Aster will likely know better.

-------------------------

rku | 2017-01-02 01:05:03 UTC | #3

Is Aster ([url=http://urho3d.prophpbb.com/member60.html]aster2013[/url]?) sort of responsible for 2d animation stuff? Because i have here this animated spriter character which is proprietary and i cant really post it publicly, and it has "limp leg". I was wondering whom i could send it privately to hopefully get bug fixed.

-------------------------

cadaver | 2017-01-02 01:05:04 UTC | #4

Yes.

-------------------------

rku | 2017-01-02 01:05:06 UTC | #5

Alright, thanks. By the way manipulating nodes does completely nothing when animation is playing. I guess animation just re-sets positions of sprites before screen updates. So feature request still stands.

-------------------------

stark7 | 2017-05-18 22:10:23 UTC | #6

Hello cadaver - I am trying to add new nodes to the bone nodes of my AnimatedSprite2D made with Spriter and it's not clear to me where these scene bones with StaticSprite2D components that you are mentioning are created. Can you please offer some direction?
What I want to do is basically attach particle effects and stuff to certain bones.

-------------------------

cadaver | 2017-05-19 08:04:52 UTC | #7

There's practically no use directing questions of the 2D-related classes specifically to me. I have little knowledge of them; mostly just fixed small bugs where I could.

-------------------------

cadaver | 2017-05-24 06:54:59 UTC | #8

Took a look at the code and I believe Aster changed the implementation since this thread was initially started. Originally it created child StaticSprites; now it no longer does that, it just lets the animation implementation update its internal skeleton, and generates vertex data from that. That can result in better performance (avoid extra overhead of the child nodes) but loses the flexibility to attach other objects.

-------------------------

stark7 | 2017-05-27 05:57:18 UTC | #9

Thanks for the follow-up! I can't seem to find this vertex data and attempt to attach to it. Can you please point me to the member that has it or can you suggest anything else I might be able to use to that end? - I am OK with a performance hit.

-------------------------

cadaver | 2017-05-27 15:18:27 UTC | #10

Follow the code from AnimatedSprite2D::UpdateSourceBatches() onward. It uses either Spine (closed source, not enabled by default) or Spriter animations. For Spriter, look further into AnimatedSprite2D::UpdateSourceBatchesSpriter(); I think you will find that you can not add attachments (at least using Urho nodes) easily without extensive surgery of the code.

-------------------------

