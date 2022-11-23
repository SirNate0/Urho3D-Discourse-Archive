rasteron | 2017-01-02 01:07:11 UTC | #1

Hey guys,

I'm trying to do some shadow masking experiment. I would like to have an object cast to selected objects only, say I have 3 objects:

Ground object
Object 1
Object 2

Object #1 to cast only to Object #2
Object #2 to cast both on Object #1 and Ground (or Ground Only)

Is this possible with shadow masking? I tried toggling the shadow mask bits/switch in the editor but I can't seem to produce these results.

-------------------------

cadaver | 2017-01-02 01:07:11 UTC | #2

Maybe if you have two lights using different light mask & shadow mask bits and setup them to affect the objects so that there's no double-lighting. But it's hack territory, so your success may vary.

-------------------------

rasteron | 2017-01-02 01:07:11 UTC | #3

Thanks Lasse. Yes, it looks like adding lights with different bits, masks and setup seems to be a decent workaround.  :slight_smile:

-------------------------

