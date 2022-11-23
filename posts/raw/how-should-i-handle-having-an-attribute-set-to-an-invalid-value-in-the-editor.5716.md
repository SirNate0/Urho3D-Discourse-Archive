throwawayerino | 2019-11-12 11:12:10 UTC | #1

In-game things are a bit easier since I'm the one who set up everything. But what if, for example, a component asks for a Node ID as an attribute and I give it a zero? Is there a built in way to error while inside the editor or should I show an error at runtime?

-------------------------

Modanung | 2019-11-12 11:11:56 UTC | #2

Could you provide some more details or rephrase the question? I fail to understand what you mean exactly. The editor does some validation; removing non-numericals from number input boxes for instance.

-------------------------

cadaver | 2019-11-13 19:43:57 UTC | #3

Some components do validation of attributes in the OnSetAttribute function, for example Light. If they see an illegal value they just correct it on the spot. Or if attribute access happens through the setter functions, you could prevent illegal values similarly as when calling the setter.

Typically a zero ID is valid for cases where a component or node connection is yet missing. If you are writing new Urho3D C++ components, it's a good habit to check that no matter what the attribute values are, your code shouldn't crash, so insert nullchecks or other checks where necessary.

There is no built-in mechanism for illegal value response. You could e.g. send an event when an illegal value is detected and show a popup as a response, but that could quickly get tedious, so I would probably advise against it. Attributes are also being set at scene load time so you could get errors at a moment you don't expect.

-------------------------

