NessEngine | 2019-03-21 20:07:05 UTC | #1

I created a very simple material with the default DiffAlpha technique: 

    <material>
        <technique name="Techniques/DiffAlpha.xml" />
    </material>

And unfortunately, shadows are not seen on it. If I replace it with 'Diff.xml' I get shadows to work, but ofc I don't get the transparent background that I want.

Is this intentional? How can I get a technique like Diff Alpha but have shadows on it? (note: I'm talking about receiving shadows not casting them).

Thanks! :)

-------------------------

Dave82 | 2019-03-23 00:26:13 UTC | #2

Which OS you are using ? i'm on Win7 Urho 1.5 and it works without any problem.

-------------------------

Modanung | 2019-03-23 07:53:27 UTC | #4

[quote="Dave82, post:2, topic:5046"]
...Urho 1.5...
[/quote]

May I ask why? :face_with_raised_eyebrow:

@NessEngine You should be able to weave the *passes* of the two techniques to get the result you seem to be looking for.

-------------------------

Dave82 | 2019-03-23 17:04:51 UTC | #5

[quote="Modanung, post:4, topic:5046"]
May I ask why? :face_with_raised_eyebrow:
[/quote]
I have a heavily modified version of Urho3d which isn't remotely compatible with the master version. Unfortunately i don't have time for rewrite the 1.7 to fit my needs so i just stick with my custom 1.5 for now :)

-------------------------

NessEngine | 2019-03-23 17:22:40 UTC | #6

[quote="Modanung, post:4, topic:5046"]
@NessEngine You should be able to weave the *passes* of the two techniques to get the result you seem to be looking for.
[/quote]

Any chance you post an example or tutorial on that subject? Tried to play around with it but it didn't work (I'm just learning Urho now, kinda new to its material system :) )

Thanks!

-------------------------

Modanung | 2019-04-16 10:20:35 UTC | #7

@NessEngine Even though I got out of it what I was looking for once or twice I still feel like a whale on Arrakis flapping my fins in hopes to be magically zapped to Waconda Lake.

Try duplicating the Diff technique and (partially?) replacing the following lines:
```
    <pass name="base" />
    <pass name="litbase" psdefines="AMBIENT" />
```
...with these one from the DiffAlpha technique...
```
    <pass name="alpha" depthwrite="false" blend="alpha" />
    <pass name="litalpha" depthwrite="false" blend="addalpha" />
```
...without any hopes of instant rehydration. :whale2:

-------------------------

