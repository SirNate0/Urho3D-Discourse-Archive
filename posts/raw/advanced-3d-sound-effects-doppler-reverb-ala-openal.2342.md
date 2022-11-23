TheSHEEEP | 2017-01-02 01:14:51 UTC | #1

Hey again,

today I was looking into the audio sources and it seems SDL is used for audio playback, too.
However, what I couldn't find out is if/how advanced audio effects like underwater, cave echo, etc. would be done.

A while ago, I built my own sound integration using OpenAL Soft in a different project, and the effects that come with it to achieve environmental effects in 3D did wonders.
I consider them a must-have for immersion purposes for some projects (the alternative would be recording each sound X times in some audio software, blowing up the asset sizes, and that wouldn't even have the same effect).

So, can such an effect be done with the Urho sound integration or would I have to roll my own?
If I'd have to roll my own, what method would you suggest? A custom component?

-------------------------

cadaver | 2017-01-02 01:14:51 UTC | #2

You would have to add your own implementation into the sound subsystem. You would have to expand it quite substantially, as presently there's no effects at all. Note that contributing such work as a PR would be very welcome, if you're up to it.

Ideally Urho should be using OpenAL. However there doesn't exist a nice permissive software implementation (OpenAL-Soft exists, but is LGPL which we can't include without getting into potential grey areas with linking) and using the implementation tied into the OS would require repeating the linking work per platform, and would miss features on some platforms, such as Web. So using SDL audio we get problem-free linking and feature parity, with the downside that there isn't any features to speak of :frowning:

-------------------------

TheSHEEEP | 2017-01-02 01:14:54 UTC | #3

I'm not sure I get the LGPL problem.
The usual way to handle that is to link dynamically, put the license in your project and you're done.
You're not hiding the fact you are using it, you provided the license and you didn't change the code.

Of course, what I'm not sure about is how this works with Urho3D's way of coming with its own "custom" dependencies... Maybe you mean that could be an issue?

I remember from having implemented OpenAL soft that it is indeed quite some work and you indeed have to kind of base your sound approach on the idea of "environments".
You don't set audio effects on a single audio source, but more on the audio "world".
It wasn't a nice thing to implement, and I'm afraid as long as my project doesn't need it (and at least the first won't), its more logical for me to not attempt this.

Too bad SDL is limited that way :frowning:

-------------------------

cadaver | 2017-01-02 01:14:54 UTC | #4

Replacing a LGPL library on Android / iOS packaged application would be troublesome. So an example of an acceptable solution would be to use the OS's inbuilt version of OpenAL on those, and dynamic linked OpenAL-soft on desktop.

-------------------------

boberfly | 2017-01-02 01:14:55 UTC | #5

Yeah I made a port long ago for OpenAL for my Pugsy app, it worked out better for the iOS platform at the time which comes with its own OpenAL implementation (for performance reasons and less stutters), especially since I needed capture support for a certain feature. Android just used the normal Urho3D audio.

There's also this library:
[url]http://sol.gfxile.net/soloud/[/url]

Which looks promising and implements a lot of OpenAL features but with a more permissive license. The backend can use SDL2 exactly like the current sound implementation uses as well.

-------------------------

yushli | 2017-01-02 01:14:55 UTC | #6

SoLoud looks like quite interesting. Do you have workable sample code to show how to integrate it into Urho3D?

-------------------------

cadaver | 2017-01-02 01:14:55 UTC | #7

That looks rather cool, thanks!

-------------------------

boberfly | 2017-01-02 01:14:55 UTC | #8

[quote="yushli"]SoLoud looks like quite interesting. Do you have workable sample code to show how to integrate it into Urho3D?[/quote]
Sadly not, but the API looks quite simple to map to the current audio backend of Urho3D and component if you were to use it instead. The component would just need more setters/getters to apply the audio effects and 3D spacial stuff, pretty trivial.

Edit: SoLoud already uses STB Vorbis, no need to do anything custom there either for streaming, you could even load in Vorbis without streaming if it's a short sample.
[sol.gfxile.net/soloud/wavstream.html](http://sol.gfxile.net/soloud/wavstream.html)

-------------------------

TheSHEEEP | 2017-01-02 01:14:56 UTC | #9

That looks interesting indeed.
So far I only came up with libCricket or irrKlang for an easier (though not permittive license) alternative to OpenAL for my own project.

-------------------------

Bananaft | 2018-01-13 20:26:53 UTC | #11

Hello. No Idea why this thread popped on surface, I can't see any new replies. So, why don't I just write one.

Recently I was trying to do ambient sound in Urho and found that sound system works really poorly. Changing gain or panning any low frequency sounds cause cracks and clicks.

Audio effects are great, but I just want to use low droning sounds without artifacts.

SoLoud looks neat, I may try using it. My C++ skills are very poor, so I want to repeat @yushli's  question, is there any samples of using SoLoud (or any other sound library) in Urho?

And how is your experience using it, @boberfly ? What did you end up using @TheSHEEEP , and what do you think of it?

-------------------------

