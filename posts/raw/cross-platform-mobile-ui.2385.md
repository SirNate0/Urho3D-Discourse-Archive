sabotage3d | 2017-01-02 01:15:06 UTC | #1

Hi guys,
Does anyone know any good cross platform mobile UI? Something that looks and feel native. There are all kind of different frameworks like xamarin and haxe, but they are self-contained. Is there anything that could run inside Urho3D but has the benefits of using HTML5, Java and Flash for the UI with C++ bindings for callbacks.

-------------------------

johnnycable | 2017-05-17 14:42:53 UTC | #2

You "could" try React Native.
The good of it is the code generators for mobile envs are full native, that is you get objc on apple and java on android. So you are free to add on them.
From there, you could integrate urho... but beware none of these are easy ports... 
De facto there's no easy solution for a plug'n'play UI for mobile, moreover it depends on requirements... except for a thing like Noesis engine, but comes at a cost...
Best fw are QT and Xamarin, afaik.
Given urho is c++ I'd say qt.

-------------------------

sabotage3d | 2017-05-17 15:35:46 UTC | #3

Thank you for now I am using highly modified nanogui it is quite bad experience in general as there are tons of things really hard to implement in non-mobile UI. I am looking at xamarin forms as well.

-------------------------

johnnycable | 2017-05-17 16:52:23 UTC | #4

[Paintcode3](https://www.paintcodeapp.com/new)

-------------------------

