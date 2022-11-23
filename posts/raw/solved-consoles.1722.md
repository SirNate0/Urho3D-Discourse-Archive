sovereign313 | 2017-01-02 01:09:41 UTC | #1

Just out of curiosity (looking the cmake scripts) Can Urho3D run on an Xbox One or Playstation 4?

Thanks for the responses.

-------------------------

cadaver | 2017-01-02 01:09:41 UTC | #2

Certainly not out of the box. If you were a licensed developer then you could add the support yourself, but the agreements you would have signed to get to that point would prevent you sharing the code.

See how Unreal4 handles it, basically their Github doesn't include console code, and by verifying as a licensed console developer you get access to the respective console platform code.
[unrealengine.com/blog/plays ... -supported](https://www.unrealengine.com/blog/playstation-4-and-xbox-one-now-supported)

-------------------------

valera_rozuvan | 2017-01-02 01:09:42 UTC | #3

I believe that this is possible!

[ul]
[li]First you have to get a *nix system running on the PS4. Take a look at the detailed instructions of how to jailbreak that console: [link removed by moderator] .[/li]
[li]Then you have to get the Urho3D source tree on to the console, and compile it.[/li]
[li]Figure out how to run shaders on PS4. For the PlayStation 4, Sony introduced GNM and GNMX and also their custom shading language, PlayStation Shader Language (PSSL).[/li][/ul]

Obviously, you may get mixed results!

-------------------------

rogerdv | 2017-01-02 01:09:44 UTC | #4

[quote="valera_rozuvan"]I believe that this is possible!

[list]
[*]First you have to get a *nix system running on the PS4. Take a look at the detailed instructions of how to jailbreak that console: [link removed by moderator] .
[/quote]

And then force your game players to do the same? I think it is not the same as having Urho3d ported for the native console system. Which, as mentioned, requires keeping the console specific code closed.

-------------------------

valera_rozuvan | 2017-01-02 01:09:44 UTC | #5

[quote="rogerdv"]And then force your game players to do the same? I think it is not the same as having Urho3d ported for the native console system.[/quote]
+1

-------------------------

weitjong | 2017-01-02 01:09:44 UTC | #6

I am sure reader can find the link elsewhere. We don't want it to be included here in any of our posts. Better safe than sorry.

-------------------------

valera_rozuvan | 2017-01-02 01:09:45 UTC | #7

[quote="weitjong"]I am sure reader can find the link elsewhere. We don't want it to be included here in any of our posts. Better safe than sorry.[/quote]
+1

-------------------------

