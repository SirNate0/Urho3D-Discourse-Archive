indie.dev | 2017-01-02 00:58:39 UTC | #1

Personally, I like angel script, it looks quite suitable as a static typed (means less error prone), C++ friendly script just like [b]C#[/b] in Unity or [b]Unreal Script[/b] in Unreal Engine.
However, I found it's hard to code with it if there is no IDE or debugger.
To some extent, I guess it would be easy for the engine author to write the Urho3d Editor with it...  or there is some secret which would be uncovered later... :wink:   
But for me while I'm certainly not familiar with every engine objects and their methods the global variables in the editor code can be quite confusing.
"Visual studio + visual assist" would be a little helpful but still not enough. 
For the script itself, it could be as welcomed as Mono in Unity, but apparently we need our [b]MonoDevelop[/b] [url]http://monodevelop.com/[/url] to make it happen.

Any suggestion?

-------------------------

Azalrion | 2017-01-02 00:58:39 UTC | #2

You can get some level of autocomplete for angelscript: [topic45.html](http://discourse.urho3d.io/t/configuring-codelite-for-editing-as-scripts/68/1). Personally I just use word autocompletion and custom syntax highlighting in notepad++ but I've been using angelscript for a long time and have ripped out most of the as binding and have only my own set as I don't want users to be able to access engine level features.

As for a debugger, we've discussed it before and angelscript does provide debugging utilities beyond angelscript errors and log/print but no one has ever got round to implementing it and as this is a hobby project for most of the developers someone will need to be the driver behind it. Same goes for creating an angelscript ide as well, people have talked about it before on the angelcode forums at gamedev but nothing has ever come about thats been kept up to date with the library.

-------------------------

