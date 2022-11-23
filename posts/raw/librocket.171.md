OvermindDL1 | 2017-01-02 00:58:36 UTC | #1

I did a quick search and the forum search says that [url=http://librocket.com/]libRocket[/url] has never been mentioned here.  Did a quick google search and found a library that someone made to integrate it into Urho3D already at [url]https://github.com/realrunner/urho3d-librocket[/url] although it is fairly outdated compared to the Urho3D codebase (unsure if it still works in other words).  As libRockets license is MIT, it is highly themable, very fast, based on html/css so it is well known, and it is very easy to extend, have you thought about including it in Urho3D as the de-facto (or at least an alternative) UI library.  In addition it would also make it a lot easier to render UI's to texture among many other features.

Would it be accepted into Urho3D if it was included in a pull request with basic and to be increased lua/angelscript wrapping code?

I have had good experiences with it in the past, but has anyone had an experiences with it here, good or bad?

EDIT:  Yes it is Windows, Mac, Linux, iOS, and Android supported, no clue about the pi but I see no reason why it could not.

-------------------------

Canardian | 2017-01-02 00:58:36 UTC | #2

I tried libRocket with another engine some years ago, and it was quite horrible, because it was bloated and sluggish, and it wanted to use its own rendering engine, which conflicted with the real rendering engine.

Urho3D's XML GUI is much cleaner and more powerful than some combination of unstructured HTML+CSS spaghetti.

I would rather focus on improving Urho3D's GUI editor, than messing around with some random HTML+CSS editors.

-------------------------

cadaver | 2017-01-02 00:58:37 UTC | #3

It could be accepted as a pull request for an alternate GUI with the following conditions:

- To build & include LibRocket would be switchable on/off from CMake
- The original UI subsystem stays functional
- LibRocket resource loading ties properly into the Urho3D resource system
- LibRocket element events are tied/wrapped into Urho3D events (if this is impossible, can be skipped, but there nevertheless needs to be a mechanism to access the events from C++ and scripting)
- There is a solid base for exposing the LibRocket elements to both scripting languages, with correct memory management. Not every subclass needs to be exposed yet, but there should be indication that with the basics done, it's just mechanical / trivial work to do the rest
- You would become the maintainer for LibRocket integration from that point on and improve the bindings even after the initial pull request

-------------------------

OvermindDL1 | 2017-01-02 00:58:37 UTC | #4

[quote="Canardian"]I tried libRocket with another engine some years ago, and it was quite horrible, because it was bloated and sluggish, and it wanted to use its own rendering engine, which conflicted with the real rendering engine.

Urho3D's XML GUI is much cleaner and more powerful than some combination of unstructured HTML+CSS spaghetti.

I would rather focus on improving Urho3D's GUI editor, than messing around with some random HTML+CSS editors.[/quote]

What do you mean by its rendering engine, it has no rendering engine when I have used it, you fulfill its callback interfaces to make meshes for it when it needs them or to give it empty textures to draw on, you have to do all of that for it.  As well as I found it to be decently fast (certainly faster than CEGUI, though it might be slower Urho3D's current system by some amount but I am not sure and have not tested).  And the HTML/CSS is certainly not unstructured, you make parts as 'templates' and link them together, it very much is very structured.  Can you elaborate on any of that?  Do you have examples showing the issues?


[quote="cadaver"]It could be accepted as a pull request for an alternate GUI with the following conditions:

- To build & include LibRocket would be switchable on/off from CMake
- The original UI subsystem stays functional
- LibRocket resource loading ties properly into the Urho3D resource system
- LibRocket element events are tied/wrapped into Urho3D events (if this is impossible, can be skipped, but there nevertheless needs to be a mechanism to access the events from C++ and scripting)
- There is a solid base for exposing the LibRocket elements to both scripting languages, with correct memory management. Not every subclass needs to be exposed yet, but there should be indication that with the basics done, it's just mechanical / trivial work to do the rest
- You would become the maintainer for LibRocket integration from that point on and improve the bindings even after the initial pull request[/quote]

libRocket abstracts out about everything, including its file access, it would be pretty trivial to link in the resource system.  libRocket is also event based, would be easy to wrap it to pass on to Urho3D events.


Mostly I am curious about Canardian's issues, I did not experience any of that, sounds like something else than what I have used so do you have examples or anything that demonstrates any of that?

-------------------------

Canardian | 2017-01-02 00:58:38 UTC | #5

[quote="OvermindDL1"]What do you mean by its rendering engine, it has no rendering engine when I have used it, you fulfill its callback interfaces to make meshes for it when it needs them or to give it empty textures to draw on, you have to do all of that for it.  As well as I found it to be decently fast (certainly faster than CEGUI, though it might be slower Urho3D's current system by some amount but I am not sure and have not tested).  And the HTML/CSS is certainly not unstructured, you make parts as 'templates' and link them together, it very much is very structured.  Can you elaborate on any of that?  Do you have examples showing the issues?[/quote]

By its rendering engine I mean that it takes control over the whole rendering function, so I can't insert some custom OpenGL commands at places I want inside the GUI. It would be better if it had no callbacks, but just simple functions you can call when you need to draw something or when you want to populate the rendering node tree.

With Urho3D's GUI I have no problems, because I can put each GUI element at the exact node I want, and can add before and after some other custom elements or even raw OpenGL commands.

-------------------------

cadaver | 2017-01-02 00:58:38 UTC | #6

The Urho GUI also constructs a render queue of UI batches which it loops through, so I'm surprised you're able to customize it that way, but if it works, cool :slight_smile: The ideal IMO would be to have UI elements as scene objects so that the exact same shaders, materials and even lighting could be used for them, but currently that's impossible without a major refactor.

It's true that the libRocket rendering interface is very basic (I've also tested integrating it in an Ogre-based framework) so if we want more customizability we need to modify/fork libRocket. However I don't think that's necessarily an issue for starters.

-------------------------

friesencr | 2017-01-02 00:58:38 UTC | #7

My beef with librocket is that I do know html css too well, and librocket doesn't really do css that well.  If it had full css3 it could be tempting but last i checked it sits at poor acid2 css 1.1 with some css2 sprinkled in.  I don't think i want to relive ie 5.5 - 6.0 days.  I would rather embed webkit.  EDIT: I would rather embed webkit then use librocket.

EDIT:  Urho does have some fancy draw texture stuff we can use to procedurally generate some textures.  It may not be as good as shaders but we can make a ui to get some easier editing without having to mess around with pngs.

-------------------------

