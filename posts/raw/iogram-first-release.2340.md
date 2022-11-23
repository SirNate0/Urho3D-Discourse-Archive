godan | 2017-01-02 01:14:50 UTC | #1

Hi all,

I'm very pleased to announce the first public WIP release of Iogram! There are still a ton of things we need to do, and plenty of bugs, but we wanted share our progress so far. There is a website and everything  :smiley: [url=http://iogram.ca/]iogram.ca[/url].

Here are some screenshots, and [url=https://dl.dropboxusercontent.com/u/69779082/IogramDemos/Hex/IogramPlayer.html]here is live demo[/url] of a little configurator that you might build with Iogram:

[img]http://iogram.ca/wp-content/uploads/2016/10/demo_rpath.gif[/img]

[img]http://iogram.ca/wp-content/uploads/2016/10/demo_3.gif[/img]

[img]http://iogram.ca/wp-content/uploads/2016/10/mesh_ops_test.jpg[/img]

[img]http://iogram.ca/wp-content/uploads/2016/10/Pasted-image-at-2016_10_11-04_57-PM.png[/img]

[img]http://iogram.ca/wp-content/uploads/2016/10/demo_2.gif[/img]

-------------------------

Egorbo | 2017-01-02 01:14:50 UTC | #2

Amazing, I can't wait to try it!!

-------------------------

ghidra | 2017-01-02 01:14:50 UTC | #3

whoa

-------------------------

weitjong | 2017-01-02 01:14:51 UTC | #4

Congrats! Any plan for a WIP release for Linux platform as well?

I have tried on the online demo using Chrome + FF on Linux. After finishing loading I could not manipulate any of the sliders.

-------------------------

godan | 2017-01-02 01:14:51 UTC | #5

@weitjoing Yep definitely plans for Linux!

As for the online demo - could you try dragging in the top half of the slider handle (I know, I know...:slight_smile:) I think I messed up the Clip Border on those things...

-------------------------

weitjong | 2017-01-02 01:14:51 UTC | #6

Thanks for that. Yes, grabbing the top half works. Other than that, nicely done!

-------------------------

sabotage3d | 2017-01-02 01:14:51 UTC | #7

Congrats! Any chance we can some of these operations back in Urho3D? Would there be open source release or it will be completely closed source?

-------------------------

godan | 2017-01-02 01:14:53 UTC | #8

[quote]Congrats! Any chance we can some of these operations back in Urho3D? Would there be open source release or it will be completely closed source?[/quote]

Yes, that is certainly the plan. However, the code base is not quite ready for public eyes yet :slight_smile: Also, I need to think a bit more about what bits should be open/closed source. Certainly the geometry library will become open. Keep an eye out on [url]https://github.com/meshgeometry[/url]

-------------------------

sabotage3d | 2017-01-02 01:15:10 UTC | #9

Thanks. What are you using for the UI?

-------------------------

godan | 2017-01-02 01:15:10 UTC | #10

[quote]Thanks. What are you using for the UI?[/quote]

Everything is pure Urho (including the Geometry lib, although there is a dependency on Eigen and LibIGL). Once I got my head around the whole XML Style file thing, the UI was actually pretty straightforward. Time consuming (i.e. we had to design 100+ icons!), but straightforward. I actually tested a bunch of 3rd party UI libs, but in the end, Urho was the best way forward.

-------------------------

yushli | 2017-01-02 01:15:10 UTC | #11

[quote="godan"][quote]Thanks. What are you using for the UI?[/quote]

Everything is pure Urho (including the Geometry lib, although there is a dependency on Eigen and LibIGL). Once I got my head around the whole XML Style file thing, the UI was actually pretty straightforward. Time consuming (i.e. we had to design 100+ icons!), but straightforward. I actually tested a bunch of 3rd party UI libs, but in the end, Urho was the best way forward.[/quote]

That sounds really exciting. I always look forward to using Urho3D's builtin UI system instead of adding dependencies. Any chance that you can share some code, and better yet, write some tutorial on how to do that?

-------------------------

rasteron | 2017-01-02 01:15:11 UTC | #12

Hey, congrats on your release! Very interesting tool. :slight_smile:

-------------------------

