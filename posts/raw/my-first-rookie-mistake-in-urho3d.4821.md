Leith | 2019-01-15 05:04:22 UTC | #1

Today I made my first rookie mistake.
It involved UI, and please note, I am completely new to Urho3D and its workflow.

I had some code that called UI::SetDefaultStyle for UI elements:
        ui_->GetRoot()->SetDefaultStyle(cache->GetResource<XMLFile>("UI/DefaultStyle.xml"));

Later, I had some code to set up a splash screen, and based on public examples, I brainlessly had this:

            UI* ui = GetSubsystem<UI>();
            BorderImage* splashUI = new BorderImage(context_);
            splashUI->SetName("Splash");
            texture = cache->GetResource<Texture2D>("Textures/LogoLarge.png");
            splashUI->SetTexture(texture); // Set texture
            splashUI->SetSize(texture->GetWidth(), texture->GetHeight());
            splashUI->SetAlignment(HA_CENTER, VA_CENTER);
            ui->GetRoot()->AddChild(splashUI);
 
            splashUI->SetStyleAuto(); // <-- here's the culprit

What this does?
It sets the Texture of my UI Element to be the one used by the built-in UI elements.
Even though I could check my loaded texture name, size, etc was the one I thought I loaded, I would see the UI atlas texture instead.
It overrides the texture you thought you set, for that element.

I've learned my first lesson - don't brainlessly attempt to string together code from different places, have a look at what it actually does!

-------------------------

Modanung | 2019-01-15 08:24:00 UTC | #2

But calling `SetStyleAuto` earlier would solve it, right?

-------------------------

Leith | 2019-01-15 08:52:10 UTC | #3

I'll find out! But setting it later definitely didnt - my texture setting was ignored.

-------------------------

Modanung | 2019-01-15 08:55:44 UTC | #4

Which makes sense to me, since it is a style property which would be overridden by `SetStyleAuto`.

-------------------------

Leith | 2019-01-15 08:57:06 UTC | #5

I'm glad it makes sense to you, but its not well documented. In fact, the documentation needs a dust-off in general, and is entirely missing in parts, such as physics, which I might consider adopting.

-------------------------

Modanung | 2019-01-15 09:03:03 UTC | #6

Often the samples provided with Urho's source, or the engine's code itself are most informative. Since Bullet is used for (3D) physics its documentation may be useful at times as well.

-------------------------

Leith | 2019-01-15 09:01:51 UTC | #7

I am well familiar with both box2d and bullet engines, I should be fine to advise on both, once I check the bindings

-------------------------

Leith | 2019-01-15 09:03:44 UTC | #8

this also opens the possibility of filling in some gaps in the docs for urho

-------------------------

Leith | 2019-01-15 09:05:10 UTC | #9

I'm also pretty handy with networking, and though I am not a friend of the latest network lib, I am sure I can grok it and advise on it very soon

-------------------------

Modanung | 2019-01-15 09:09:43 UTC | #10

Note that there is also a [wiki](https://github.com/urho3d/urho3d/wiki), which is more suitable for things like tutorials. Honestly _I_ kind of like the bare essentials documentation approach.

-------------------------

Leith | 2019-01-15 09:08:12 UTC | #11

The wiki has missing holes for networking, and physics

-------------------------

Leith | 2019-01-15 09:09:09 UTC | #12

I offer to assist, in all humility, and try to fill some missing gaps

-------------------------

Leith | 2019-01-15 09:13:15 UTC | #13

what is the point of the engine being capable, if there is no public point of presence to learn it, or at least associate it with what you may already know? we should (hell I am already using the queens language) make it accessible. The more accessible it is, the more people will use it.

-------------------------

Leith | 2019-01-15 09:14:41 UTC | #14

its ok for us who already know bullet or box2d or any number of other core systems but if we cant explain our bindings, we're just talking to ourselves

-------------------------

Leith | 2019-01-15 09:17:06 UTC | #15

Lets say I DID know bullet, or box2d, and wanted to code in angelscript, which is I assume the preferred scripting language we support. Where can I learn about the bindings?

-------------------------

Leith | 2019-01-15 09:17:33 UTC | #16

More to the point, where can I learn the engine api?

-------------------------

Leith | 2019-01-15 09:19:06 UTC | #17

It all exists, just not on wiki, am I wrong? Have we got NO DOCS for the physics or networking?

-------------------------

Leith | 2019-01-15 09:20:26 UTC | #18

Please correct me, and the wiki if I am wrong

-------------------------

Modanung | 2019-01-15 09:21:26 UTC | #19

I think the code samples are quite complete, up-to-date and well commented. They are available in C++ _and_ AS.

-------------------------

Leith | 2019-01-15 09:21:25 UTC | #20

Code samples are not useful for a starting point, they rely on a base class for sample apps, which hides most useful information for new users

-------------------------

Leith | 2019-01-15 09:23:33 UTC | #21

the only use for sample apps, is proving things work, they fall short of telling how the engine works

-------------------------

Leith | 2019-01-15 09:24:58 UTC | #22

disemboweling demo sourcecode is not a good place to start
docs are good

-------------------------

Modanung | 2019-01-15 09:35:40 UTC | #23

It worked for me, with no degree. Yet to some extent, I agree.

Note that it has also been proposed to switch to Newton Dynamics for physics.

-------------------------

Leith | 2019-01-15 09:37:43 UTC | #24

doxygen is not a good enough guide for novices, we have some small holes in the public docs that need filling, I may find time to help there, as well as general problem solves
I don't like Newton, it's slower than Bullet, and though more accurate, it is less suited to realtime gamedev

-------------------------

Modanung | 2019-01-15 09:40:23 UTC | #25

Indeed Doxygen doesn't add much on top of the - already open - source. Sometimes it's convenient to link to, though.

-------------------------

Leith | 2019-01-15 09:42:43 UTC | #26

I'm simply stating that there are some [missing] links on the home page of the engine, which are outright not referenced, in any way, by web spiders like google, or anyone else - the info simply is not available, and would only take me a few days each to fill those holes, with all this free time on my hands as it were

-------------------------

Leith | 2019-01-15 09:51:22 UTC | #27

Linking back to bullet and box2D specs would likely be a breeze, assuming we didn't corrupt the api with our wrapper

But assume I was a new user who DID NOT KNOW Bullet or Box2D - do you still think the samples are sufficient to teach me how to use these systems?

-------------------------

Dave82 | 2019-01-15 15:16:56 UTC | #28

I get into urho in one week 100% only by reading the example codes.

-------------------------

Modanung | 2019-01-24 14:51:06 UTC | #29

The samples demonstrate creation of physics worlds, bodies and colliders as well as how to apply forces. Beyond that point the header files of the involved classes show many of the possibilities. Often the accompanying comments are enough to understand their use.
Then of course there's the forums, with search function.

That said, I agree expansion of the documentation and wiki would be nice, just not very important given the grips that are available. Personally I think many users will benefit from wizards like [these](https://discourse.urho3d.io/t/wrench-class-and-project-wizards-for-qtcreator/2076) (for QtCreator) to get them started. Even when knowing your way it can save a ton of work. Instead of building this into the editor - like Unity (sort of) does for instance - Urho could support a whole bunch of IDEs through wizards.

EDIT: @Bluemoon made a [project wizard for **CodeBlocks**](https://discourse.urho3d.io/t/urho3d-codeblocks-wizard/1379).

-------------------------

I3DB | 2019-01-25 16:50:27 UTC | #30

[quote="Modanung, post:29, topic:4821"]
Beyond that point the header files of the involved classes show many of the possibilities. Often the accompanying comments are enough to understand their use.
[/quote]

Could you show an example or two of this? Just not sure what you're referring to, or where these comments are. 

In the examples there are a lot of comments sprinkled about and throughout the code that explain what's happening, if that's what you're referring to.

-------------------------

Modanung | 2019-01-25 16:57:28 UTC | #31

I was referring to - for instance - `RigidBody.h`

-------------------------

I3DB | 2019-01-25 19:49:49 UTC | #32

[This](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Physics/RigidBody.h)?  

The file on urho3d repository?

-------------------------

Modanung | 2019-01-25 20:43:21 UTC | #33

[quote="I3DB, post:32, topic:4821"]
The file on urho3d repository?
[/quote]

Yes, that file... only that the way I work this file is opened when pressing **F2** as my text cursor in QtCreator is over an occurrence of `RigidBody`. Meaning this reference is always nearby for any class you may use.

-------------------------

Miegamicis | 2019-01-25 20:43:27 UTC | #34

I would agree with @Modanung. Plain documentation is nice and all, but all the small important bits are present in the headers as comments, which helps a lot more, except if you are using notepad or gedit to generate code.

-------------------------

