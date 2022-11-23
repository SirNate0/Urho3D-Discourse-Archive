yushli | 2017-01-02 01:02:36 UTC | #1

How difficult is it to port gameplay3d's samples to Urho3D? For example, gameplay3d/samples/racer is a car racing game. Can we port it to run in Urho3D?

-------------------------

cadaver | 2017-01-02 01:02:36 UTC | #2

Welcome to the forums!

You'd be looking at a complete rewrite of the application source code to the Urho API + re-exporting of assets. Can't speak of the assets, but the code conversion shouldn't be difficult if you know both engines well. Note that Urho doesn't have Bullet's raycast vehicles yet, but we have a feature request issue written in GitHub.

If your question is actually asking if someone of Urho team is going to convert the examples, that's probably a no.

-------------------------

yushli | 2017-01-02 01:02:36 UTC | #3

Thanks for the quick reply. Actually I am evaluating these two engines, both on feature rich and performance. Urho3D seems really fast and responsive when running its own samples. But these samples seem quite simple, comparing to gameplay3d's samples such as racer and spaceship. If we can have similar samples (which look like mature games), that will be much more convincing for people to adopt this amazing engine.

-------------------------

gwald | 2017-01-02 01:02:38 UTC | #4

Funny really.
I posted on the GP3D's forum after Sean's post:
[gameplay3d.org/forums/viewto ... 7503#p7503](http://www.gameplay3d.org/forums/viewtopic.php?p=7503#p7503)
[quote]
There is indeed too many other priorities and we want to focus on with our attention on the features and supporting the major volume groups.
On Windows 90%+ develop use Visual Studio. In fact, I worked for 2 years meeting game developers to know these numbers to be accurate.
I am not trying to discourage others either from doing this yourselves in your own forks and branch. 
[/quote]
I said that GP3D isn't indie like it's slogan, but more for independent establish gamedev's and that there are two obvious types of users of GP3D.
The haves (maya,VS, MS, 64bit, etc) and the have nots (blender, cmake, linux, 32bit, etc).
I guess he didn't like it, because it was removed quickly.
I tinkered with GP3D since 2013 and switch to urho3d after they dropped 32bit and moved to VS2011(vista+) dropping previous VS and winXP support!
Anyway, my point about GP3D is
#1 if you don't have the latest OS/HW, you'll be on 'your own'.
#2 if you don't have maya or a solid FBX tool, you'll be debugging your assets and on 'your own'.
#3 if you want to support anything that's not on their agenda... (backward compatibility) yip you're on 'your own'.
If these are issues for you then drop GP3D ASAP!

If you want a good flexible, (real) indie, C++ game engine, then urho3d is better.
But, If you're learning gamedev or C++, then I would recommend GP3D, it's a lot less complicated ( simpler C++ ).

Re, migrating the demo's.. I think the hardest part would be the assets (from maya FBX).
From the little I've looked at urho3d (unfortunately), the GP3D code is much higher level then urho3d and wouldn't be hard to do.

Don't be fooled by the racer demo lol
it's not much smarter then urho3d's car physic demo but with fancy assets!
For a better demo, look at the urho3d's ninja snow demo!

-------------------------

