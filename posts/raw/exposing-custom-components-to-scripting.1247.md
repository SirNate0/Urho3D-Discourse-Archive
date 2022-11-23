Enhex | 2017-01-02 01:06:22 UTC | #1

Are classes deriving from Component are automatically exposed to scripting?
If not what is required to expose them?

-------------------------

rasteron | 2017-01-02 01:06:22 UTC | #2

[quote="Enhex"]Are classes deriving from Component are automatically exposed to scripting?
If not what is required to expose them?[/quote]

Check out the sources in Urho3D/Script directory. You can also check the smaller classes like Audio API or CivetWeb to get started and how it was exposed as a script.

-------------------------

Enhex | 2017-01-02 01:06:23 UTC | #3

Ok, thanks.

Right now what I have in mind for making an app(game) level API is to derive Script and add a RegisterGameAPI(), like the other global functions with the .cpp files that got static functions for each class type.

-------------------------

