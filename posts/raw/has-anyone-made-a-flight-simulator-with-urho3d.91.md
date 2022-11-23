GIMB4L | 2017-01-02 00:57:55 UTC | #1

I'm trying to make a jet fighter game using Urho3D for the main game engine, and a third-party library called JSBSim the flight dynamics.

After a few days trying to get the thing to work, I'm pulling my hair out with how overly complicated the library is, and I have no idea how to do what I want. Their forums and reference manuals are no help either.

Is there by any chance anyone here who has used JSBSim or YASim in the past? Not just with Urho3D, but with anything that got the library to work.

Thanks!

-------------------------

JTippetts | 2017-01-02 00:57:55 UTC | #2

I just took a quick skim of the docs for JSBSim. That looks like a fairly complex piece of software. (I wouldn't say it is overly complicated, though, given the inherent complexity of the problem domain it is trying to simulate. Flight itself is complex.) The thing with complex and specialized software like that is that technical proficiency usually can not be transmitted via forum post, short article or anything less than an in-depth and extremely involved tutorial/discussion/lecture. Such a thing probably doesn't exist. You might be able to gather bits and pieces here and there, but I'm afraid that there really is no 'easy' way. You're going to have to get your hands dirty, and wade through some hours of frustration to figure things out. It will probably take you awhile.

Setting aside the complexity of using the library, the first place you'll probably need to look is the section on integrating the software into your project. It starts on page 88 of [jsbsim.sourceforge.net/JSBSim/](http://jsbsim.sourceforge.net/JSBSim/) as you are going to need them.

 If you are having trouble getting it to build and/or run, then you might need to brush up on the basics of building and running complex projects. On the bright side, once you've fought the good fight, you could probably win yourself some fame and recognition by writing an interface layer for Urho3D.

-------------------------

