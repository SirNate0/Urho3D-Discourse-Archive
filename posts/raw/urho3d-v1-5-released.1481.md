cadaver | 2017-01-02 01:08:04 UTC | #1

V1.5 is out now. Thanks to all contributors! Highlights this time include the new Database & Localization subsystems, and extensive SSE math optimizations contributed by clb.

Release post: [urho3d.github.io/releases/2015/1 ... lease.html](http://urho3d.github.io/releases/2015/11/11/urho3d-1.5-release.html)
Source code: [github.com/urho3d/Urho3D/archive/1.5.zip](https://github.com/urho3d/Urho3D/archive/1.5.zip)
SourceForge file archives: [sourceforge.net/projects/urho3d/ ... rho3D/1.5/](http://sourceforge.net/projects/urho3d/files/Urho3D/1.5/)

-------------------------

weitjong | 2017-01-02 01:08:04 UTC | #2

Congrats!

-------------------------

alexrass | 2017-01-02 01:08:04 UTC | #3

Congratulations! Urho3D the best!

-------------------------

Sasha7b9o | 2017-01-02 01:08:04 UTC | #4

[quote="alexrass"]Urho3D the best![/quote]
I agree!
The best engine of that met.

-------------------------

codingmonkey | 2017-01-02 01:08:05 UTC | #5

Very well) But there is still so many things what are needed to implement in future. Keep it up!

-------------------------

sabotage3d | 2017-01-02 01:08:05 UTC | #6

Awesome !

-------------------------

rasteron | 2017-01-02 01:08:08 UTC | #7

This is awesome! Congrats :slight_smile:

Side Note: Not sure of this, but currently I'm seeing a blank page on github.io or at least on Urho3D's pages

[img]http://i.imgur.com/Rr1AeQx.jpg[/img]

-------------------------

bvanevery | 2017-01-02 01:08:19 UTC | #8

[quote="rasteron"]
Side Note: Not sure of this, but currently I'm seeing a blank page on github.io or at least on Urho3D's pages
[/quote]

I can't duplicate that.  Your URL in the photo you provided doesn't look anything like how I'd obtain an Urho3D release either.  I go to [sourceforge.net/projects/urho3d/files/Urho3D/](http://sourceforge.net/projects/urho3d/files/Urho3D/) .  So, how do you get to the URL in your photo?

-------------------------

rasteron | 2017-01-02 01:08:26 UTC | #9

[quote="bvanevery"][quote="rasteron"]
Side Note: Not sure of this, but currently I'm seeing a blank page on github.io or at least on Urho3D's pages
[/quote]

I can't duplicate that.  Your URL in the photo you provided doesn't look anything like how I'd obtain an Urho3D release either.  I go to [sourceforge.net/projects/urho3d/files/Urho3D/](http://sourceforge.net/projects/urho3d/files/Urho3D/) .  So, how do you get to the URL in your photo?[/quote]

Yes sorry, old post and probably some down time on github's io pages last week.  :slight_smile:

-------------------------

zzz654321 | 2017-01-02 01:13:21 UTC | #10

I'm try 12_PhysicsStressTest.lua, in line 77, scene_.Update function
for _, spriteNode in ipairs(spriteNodes) do is dieloop in spriteNodes[1]
change to for i= 1, NUM_SPRITES do local spriteNode= spriteNodes[i ]
the sample is work ok!!!
in the all samples, pairs ipairs ALL ERR!
please change, thanks to you!
compile luajit2.1 + mingw32 VERSION, that very thank!!!


and in 12_PhysicsStressTest.lua, 
coroutine is dieloop! this is a ERROR!

-------------------------

