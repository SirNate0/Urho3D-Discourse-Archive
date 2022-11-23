Modanung | 2020-03-02 09:47:46 UTC | #1

Do you primarily write Urho3D games and applications in C++ or a scripting language?
[poll type=regular results=always chartType=pie]
* C++
* Scripting language
[/poll]

What is (or would be) your preferred scripting language?
[poll name=poll2 type=regular results=on_vote chartType=bar]
* AngelScript
* Lua
* Other
[/poll]

-------------------------

SirNate0 | 2020-02-14 03:58:30 UTC | #2

Is the second question preferred if it was an option, or is it preferred in actual practice? I.e. is it my ideal scripting language (if it was supported) or is it what I actually use for my projects?

-------------------------

Miegamicis | 2020-02-14 07:31:28 UTC | #3

2nd question is misleading since it doesn't actually specify if it's the scripting language that the engine supports or is it any scripting language that is out there thus making the 2nd poll results invalid. If it's the scripting language in general, then the answers should include all the popular scripting languages that are out there, not just the "other" option as it doesn't add any value to the poll.

-------------------------

Eugene | 2020-02-14 07:55:52 UTC | #4

Yeah, second poll is invalid and should be nuked. It doesn’t specify if it is general question or about Urho specifically. Therefore it contains mixed results and already contaminated. 

If first, why only two options?
If second, why “other”?
Why there is no fallback option for ones who doesn’t use scripting?
Polls shouldn’t have any ambiguity is question.

-------------------------

1vanK | 2020-02-14 08:10:00 UTC | #5

If for example I prefer to write in C ++, but in my game there is a console in AS and user modifications in any scripting language? Each language has its own task and they do not mutually exclusive.

-------------------------

lezak | 2020-02-14 11:37:20 UTC | #6

First poll definitely should have option 'both' - for example about 80% or more of my code is written in c++, so I can vote for c++, but there is a reason why the rest is scripted, so this vote can be harmful for me in context of recent and ongoing discussions about AS removal.

-------------------------

Modanung | 2020-02-14 12:09:26 UTC | #7

The first poll is to determine how many people write (basically) their entire application in script as opposed to using script only for specific purposes. The second is to find out if the available language options are what the community is looking for. If the _other_ option were to surge, a follow-up poll could tell us more. If it does not, the available options suffice.

My apologies if this was unclear.

-------------------------

Eugene | 2020-02-14 12:37:09 UTC | #8

[quote="Modanung, post:7, topic:5925"]
The first poll is to determine how many people write their entire application in script as opposed to using script only for specific purposes
[/quote]
One person may use only C++
Another person may use C++ and some scripting, not caring about specific scripting language.
Third person may use scripting a lot and require specific language (e.g. AS), but still write most parts in C++.
Forth person may use scripting only.

-------------------------

Modanung | 2020-02-14 12:43:45 UTC | #9

We could divide these groups even further. For instance people writing only in C++ may still like the availability of script. In order to curtail complexity I decided to limit the options to **%C++ > %Script** and **%Script > %C++**.

-------------------------

Eugene | 2020-02-14 12:56:14 UTC | #10

[quote="Modanung, post:9, topic:5925"]
In order to curtail complexity I decided to limit the options to **%C++ > %Script** and **%Script > %C++** .
[/quote]
When you made a poll, what information did you want to gather?

For me, important information is how important scripting is for different people.
And there are three very separate cases. Ones who don't need scripting at all, ones who need at least some scripting in any form, and ones who need specific scripting API and language (e.g. they need AS in its current form and nothing else, or Lua in its current form). The last case is actually split into two sub-cases.

These polls gave me too little information about said groups.

-------------------------

Modanung | 2020-02-14 13:06:56 UTC | #11

As @1vanK implied, some people might also use multiple scripting languages. Also the _scripting only_ segment might still write *some* C++ at times.

Feel free to create an extra poll to your liking in this thread, I will link to it in the first post.

-------------------------

Eugene | 2020-02-14 13:18:40 UTC | #12

I think we already have overdose of polls, in last two weeks /laughing/. I think I will start one when/if it will be important.

-------------------------

Modanung | 2020-02-14 13:26:02 UTC | #13

[quote="Eugene, post:10, topic:5925"]
When you made a poll, what information did you want to gather?
[/quote]
My main goal was to answer @brokensoul's question without relying on assumptions.
[quote="brokensoul, post:37, topic:5921"]
...is AngelScript really worth it ?
[/quote]

Looking at the current results, I conclude the answer to be _yes_.

-------------------------

orefkov | 2020-02-14 13:51:59 UTC | #14

In my understanding, a good game engine should combine both options. Separate high-quality components are written in C++ that work with high performance and in isolation from other code. And in the script part, game logic is set that glues independent components together. It is like bricks and cement — you need both to build a good home. In combination with the serialization mechanism, which allows you to save the state of the scene, nodes, components, and especially the excellent built-in serialization of AngelScript's ScriptObjects, this allows you to achieve a truly editor-created and data-driven game. In which the various aspects of the gameplay are then simply set by setting the property fields in the editor, without modifying the C++ code.
I used this approach when developing games for Android. It generally used Urho3DPlayer and scripts. The main script just loaded the scene file and set up the viewport. And all the logic of the game was tied in the form of script objects to the nodes of the scene. Using scripts allowed me to achieve tremendous development speed - I just syncing the Data folder between the Android device and the development folder through rsync, and used new versions of assets and scripts without even leaving the game - no other engine provided such speed of verification on the Android device.
In this sense, scripts are good for rapid prototyping. And since AngelScript api repeats C++ api almost one to one - I could quickly rewrite already well-established and well-functioning parts of the game logic in C++.
Also, thanks to some dirty engine hacks - I have full support from the ide when writing code :slight_smile:
https://discourse.urho3d.io/t/vscode-angelscript-intellisense/5669

-------------------------

Modanung | 2020-02-14 19:15:56 UTC | #15

I added [a poll](https://discourse.urho3d.io/t/polling-language-popularity/5925/1) for those preferring an **other** scripting language.

-------------------------

throwawayerino | 2020-02-15 12:46:37 UTC | #18

Bring back UnrealScript! ChaiScript seems really easy to bind, just add one line per function and is similar to C++.

-------------------------

Modanung | 2020-02-16 18:23:48 UTC | #19

I wonder what's behind the "Other still". :slightly_smiling_face:

-------------------------

QBkGames | 2020-02-16 23:42:38 UTC | #20

BASIC :grin:  (this are padding chars so I can make this post at least 20 chars).

-------------------------

Pencheff | 2020-02-22 17:30:29 UTC | #21

Everyone bumping Lua and Python...how about JavaScript ? 
[code]
Rotate.prototype.update = function(elapsed) {
    this.entity.rotate(0, this.speed * elapsed, 0);
};
[/code]

-------------------------

SirNate0 | 2020-02-22 19:02:05 UTC | #22

I like JS over Lua (as a language, ignoring performance concerns), but still significantly prefer Python over JS.
Do you know of any nice way to bind c++ to JavaScript, though?

-------------------------

Pencheff | 2020-02-22 19:30:03 UTC | #23

I did some tests with V8 in my apps and performance-wise it was solid. SWIG didn't have support for V8 back then, now it seems to support it - http://www.swig.org/Doc3.0/Javascript.html . Atomic was using duktape - https://duktape.org/, it seems solid as well but I can't find any bindings generator.

-------------------------

pldeschamps | 2020-03-01 21:06:01 UTC | #24

Is C# a scripting language?
I would have asked "Do you primarily write Urho3D games and applications in C++ or another language?"

-------------------------

SirNate0 | 2020-03-01 21:31:47 UTC | #25

In the sense that it is "not C++" you could call it a scripting language, but technically no it's not (ignoring things like CS-Script). The third poll was added later, presumably the earlier polls weren't really written with C# in mind (and given RBFX and UrhoSharp it could be assumed people do use C#, so it's definitely appropriate to include in the 3rd poll).

[quote="Modanung, post:15, topic:5925"]
I added [a poll](https://discourse.urho3d.io/t/polling-language-popularity/5925/1) for those preferring an **other** scripting language.
[/quote]

-------------------------

Modanung | 2020-03-01 21:37:52 UTC | #26

[quote="SirNate0, post:25, topic:5925"]
...but technically no it’s not (ignoring things like CS-Script).
[/quote]

I removed the option.

-------------------------

jayrulez | 2020-03-02 06:43:45 UTC | #27

Then why keep swift? Rust? Go?

-------------------------

Modanung | 2020-03-02 09:48:04 UTC | #28

Third poll has been removed.

-------------------------

