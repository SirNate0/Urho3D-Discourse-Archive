atai | 2017-01-02 01:09:47 UTC | #1

Hi, looking at the class Thread it uses a static variable to point to the Main Thread.

I am just curious can multiple instances of Urho3D Engines exist in the same process?  Using analogy in programming languages, Lua allows multiple interpreters to exist concurrently, while Python suffers from a "global lock" and cannot have more than one instance of its interpreter in a process. Looking at the Urho3D sources at a high level it seems there is no obvious restrictions that only one instance (of a Context or Engine) can exist.

(Use case: multiple OS level (X11) windows on GNU/Linux, each window rendering with its own Urho3D context/engine in its own thread, running concurrently, all in the same process)

If multiple instances can exist, then should the main thread be tracked at the basis of contexts; that is, the main thread pointer should exist inside the Context class and different threads can serve as the main threads of different contexts, one per context or engine and each independent of the other.
And the thread class needs to take a context as an explicit or implicit parameter for its main thread setting and checking functions.

I hope the above description is true:-)

-------------------------

thebluefish | 2017-01-02 01:09:48 UTC | #2

Yes, it is definitely possible.

You will run into issues with OpenGL with multiple GL contexts. [url=https://github.com/urho3d/Urho3D/commit/c3d5df1ea41d98f55a6fe1c70a5517d35777acd6]I submitted a PR a while back[/url] exposing a public property to allow you to properly use SDL_GL_MakeCurrent to handle this case. Used in the right spots, there should be no issues.

Subsystems, events, etc... are "global" to the Context only. Each Context can therefore have an Engine, Renderer, etc... without running into conflicts.

You should be able to create the Urho3D Context on its own thread, but I haven't tested this.

-------------------------

atai | 2017-01-02 01:09:48 UTC | #3

[quote="thebluefish"]
Subsystems, events, etc... are "global" to the Context only. Each Context can therefore have an Engine, Renderer, etc... without running into conflicts.

You should be able to create the Urho3D Context on its own thread, but I haven't tested this.[/quote]

Yes, I created a new thread and set it to be the main thread for a context, and it works fine.  Previously I was tryng to do things to a context/engine from different threads, and I gave up on that.  Now I use C++11 lamdas to "dispatch" C blocks to execute on this main thread from other threads so everything touching this engine is done in this single thread, and I don't have issues.   

Now with the workaround for switching GL contexts between Urho3D instances, and hopefully multiple Urho3D engines run concurrently and happily together :slight_smile:

-------------------------

TheComet | 2017-01-02 01:10:11 UTC | #4

What's the use-case for this if you don't mind me asking?

The only thing I can imagine is a client + server combination, the server running in headless mode.

-------------------------

atai | 2017-01-02 01:10:12 UTC | #5

[quote="TheComet"]What's the use-case for this if you don't mind me asking?

The only thing I can imagine is a client + server combination, the server running in headless mode.[/quote]


OK  for OS platform restrictions where the real main thread has to do something else, I can have a different thread being the main thread for a renderer which draws into an OS level window (X11 window, for example), and I may have several renderers in several windows doing different things

-------------------------

thebluefish | 2017-01-02 01:10:12 UTC | #6

[quote="TheComet"]What's the use-case for this if you don't mind me asking?[/quote]

I probably have different use-cases for this:

Native windowing support (X11, Windows, etc...). A rendering context can target a single window, not multiple. If you wanted to target multiple windows, you would need support for multiple rendering contexts. In cases where you want to manage multiple windows from the same project, you'd need to create multiple rendering contexts within the same Urho3D Context. However sometimes you might want to wall certain things from each other. For example, if you were editing a map and wanted to "launch" the map in an instance of the game. You wouldn't want events and subsystems from the editor affecting your game, but instead launching it in its own Context as if it was a standalone process. It helps to keep multiple Contexts in the same process in order to obtain better control over the life of each.

-------------------------

