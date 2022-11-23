Eugene | 2017-01-02 01:15:05 UTC | #1

Currently 'Play' just starts scene updating and related stuff.
I want to really _play_ in Editor as character, not as flying spirit.
I understood that I will need to write all my game logic in logic components, it's okay. I'll manage to do it.
I am unsure about disabling Editor stuff. How to properly override controls and main View?

Actually, this is just a face of single question: Urho definetly needs more tight integration between editor and game.
I've seen some threads about in-game Editor. I am unsure what way is better:
1) Have easy integration of editor logic in any script (flexible way)
2) Have playable scenes and Editor that is able to play them (Unity-way)

-------------------------

rasteron | 2017-01-02 01:15:07 UTC | #2

I think it will be not that hard but will take some time to get this to work. The editor code itself is well organized and grouped by file. Maybe you can examine how the current animation test feature works with the editor since everything is done through subscription and events and that would be a good start.

As an alternative, you could probably do a reverse implementation but that is building your own editor from scratch or use the NinjaSnowWar as a template since it has already a Pause event.

-------------------------

