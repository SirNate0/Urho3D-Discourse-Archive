matalink | 2019-08-01 08:09:49 UTC | #1

Does a urhosharp community forum exist? Because so far I havent found any and I desperately need help since we are nearing our deadline for our project.

-------------------------

Modanung | 2019-08-01 08:27:43 UTC | #2

https://forums.xamarin.com/categories/xamarin-forms

-------------------------

Modanung | 2019-08-01 08:27:46 UTC | #3



-------------------------

Lumak | 2019-08-11 13:51:35 UTC | #4



-------------------------

Lumak | 2019-08-11 13:52:46 UTC | #5

Apparently, Urhosharp project is no longer maintained.
https://forums.xamarin.com/discussion/141631/urhosharp-is-dead-should-we-fork-it

-------------------------

Modanung | 2019-08-11 14:13:52 UTC | #6

Support has always been meager. But hey, at least some people got paid, right?

-------------------------

throwawayerino | 2019-08-11 15:40:15 UTC | #7

Isn't this just a C# wrapper? It shouldn't be difficult to build it but with the new code base so official support isn't a big issue here.
And anyways their syntax is similar but with more dots instead of arrows. We shouldn't try to chase them all away

-------------------------

Modanung | 2019-08-11 15:46:39 UTC | #8

You're right, they should be converted, not hunted down.

-------------------------

throwawayerino | 2019-08-11 15:42:55 UTC | #9

This man is savage
>Of course, that is a total fantasy considering that Satya Nadella would rather focus on what flavor of incense to burn in the meditation sessions than actually manage a company. You have to be high as a kite to blow $7.5 billion on GitHub, a site that could be cloned in 2 days. It's like he had a conversation with Ballmer that went like this:
>>Ballmer: We've got too much money just sitting in the bank. I'm going to blow $7 billion on a dying phone manufacturer.
Nadella: Hold my beer.

-------------------------

Modanung | 2019-08-11 15:46:43 UTC | #10

http://luckeyproductions.nl/images/PRISMslide.jpg

-------------------------

throwawayerino | 2019-08-11 15:52:43 UTC | #11

[offtopic incoming]
I have that thing memorized. Did you know they even embedded telemetry with every msvc program in 2016?
https://old.reddit.com/r/cpp/comments/4ibauu/visual_studio_adding_telemetry_function_calls_to/d30dmvu/
https://windowsreport.com/visual-studio-2015-function-telemetry-call/
https://yro.slashdot.org/story/16/06/10/1350245/visual-studio-2015-c-compiler-secretly-inserts-telemetry-code-into-binaries

-------------------------

Modanung | 2019-08-11 15:53:51 UTC | #12

https://discourse.urho3d.io/t/visual-studio-2015-secretly-inserts-telemetry-code-into-c/2073
;)

-------------------------

Modanung | 2019-08-11 16:26:24 UTC | #13

[Unity does too](https://spyware.neocities.org/articles/unity.html). This can be disabled (for the editor) if you pay up.
Which makes me think that an [article on Spyware Watchdog](https://spyware.neocities.org/articles/) might be a nice thing for Urho to have.

That *is* what convinced me to switch to [IceCat](https://spyware.neocities.org/articles/icecat.html).

-------------------------

throwawayerino | 2019-08-11 16:27:28 UTC | #14

Overall advertisement is always a nice thing. Urho3D is very underrated.
But the fsf has a wiki page about it
https://directory.fsf.org/wiki/Urho3D

-------------------------

Modanung | 2019-08-11 16:29:00 UTC | #15

And [LibreGameWiki](https://libregamewiki.org/Urho3D). :slight_smile:

-------------------------

throwawayerino | 2019-08-11 16:37:24 UTC | #16

What riles me up is that people think Godot is the only good open source engine, which is absolutely insulting since Urho3D is a very capable and feature complete engine, where godot doesn't have proper 3d support

-------------------------

rku | 2019-08-14 08:15:42 UTC | #18

Back on topic.. I dont think forking UrhoSharp is an option to anyone. It is a terrible wrapper. Bindings generator runs only on MacOS. Bindings require patching engine in several places so you can override virtuals. Many more useful virtuals you cant even override. Bindings depend on mono explicitly too.

If you want Urho3D with C# - https://github.com/rokups/rbfx. As far as C# is concerned - engine changes are minimal (mostly cosmetic stuff to make wrapper compile, missing `URHO3D_API` added here, missing constructor or few added there). Someone determined enough could rip it out and make a standalone addon to Urho3D.

-------------------------

suppagam | 2019-08-12 13:32:29 UTC | #19

What are, mostly, the differences between Urho and rbfx, other than C#?

-------------------------

rku | 2019-08-12 17:31:07 UTC | #20

Editor, eastl, profiler.. download zip and compare dirs ;)

-------------------------

1vanK | 2019-08-16 09:52:53 UTC | #21

I have not tried it, but it looks interesting https://xenko.com/ if you like C#

-------------------------

