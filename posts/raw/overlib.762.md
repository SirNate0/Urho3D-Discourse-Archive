OvermindDL1 | 2017-01-02 01:02:44 UTC | #1

I have been pulling out a lot of code that I have been sharing between my projects in to a library that they all use and have been using it for a few months now, it is not big yet as I still need to pull out more in to it (especially the Input Mapper), but it is still useful even as small as it is.  It currently contains a few helpers for the primary Application, an AttributeEditor UI creator for many of the attribute types, and an Urho3D style event driven state manager with loading screen support.  Check the project on GitHub for a fairly sizable README.md for detailed information:  [github.com/OvermindDL1/Urho3D-OverLib](https://github.com/OvermindDL1/Urho3D-OverLib)

-------------------------

thebluefish | 2017-01-02 01:02:47 UTC | #2

An example project would be nice to see, but I think I have an idea. That state manager seems perfect for what I'm trying to do, though I will probably need to extend it to include a state stack of some sort.

-------------------------

OvermindDL1 | 2017-01-02 01:02:51 UTC | #3

The StateManager in the project is for high level switching, like main menu, different games, etc..., which is what I am using it for.  I have another state manager inside each main state for the stacks, like the main menu has a main menu state, an options menu state, a choose new game state, etc...  Those ones do not use the StateManager.  Could integrate it in to the StateManager though, I would probably do it myself in time, but if you have a pull request...  :wink:

-------------------------

sabotage3d | 2017-01-02 01:03:06 UTC | #4

Looks really good. Do you have any working samples ?

-------------------------

OvermindDL1 | 2017-01-02 01:03:15 UTC | #5

[quote="sabotage3d"]Looks really good. Do you have any working samples ?[/quote]
Not samples, just in use by the mini-games I am making as I get a few minutes free here and there.  If you have questions about anything then feel free to ask and I can document.  Feel free to converse on the github repo as I will see those more readily then here, but I can check here more often than I have been if you want since this is a visible place for Urho3D.  If anything feel free to message me on github to look at this thread as a bump.

-------------------------

sabotage3d | 2017-01-02 01:03:16 UTC | #6

Thanks a lot OvermindDL1.

-------------------------

OvermindDL1 | 2017-01-02 01:03:17 UTC | #7

[quote="sabotage3d"]Thanks a lot OvermindDL1.[/quote]
No problem, I like to document well but time is definitely short so the occasional prodding is good.   :slight_smile:

-------------------------

