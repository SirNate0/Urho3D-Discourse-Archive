1vanK | 2022-01-28 09:14:50 UTC | #1

Hooray! 

![This is an image](https://povareshkino.ru/files/userarticles/19527_1cdbe1bd.jpg)

Now for the bad. Something has changed in a images of MacOs environments. Looking for users of this operating system. Yo need in file <https://github.com/urho3d/Urho3D/blob/master/.github/workflows/main.yml> replace `run: sudo xcode-select -s '/Applications/Xcode_12.app'` to something from this <https://github.com/actions/virtual-environments/tree/main/images/macos> and force the engine to compile. Otherwise, we will not be able to guarantee support for MacOS.

-------------------------

GodMan | 2022-01-29 00:02:14 UTC | #2

So is 1.8 out now? If so can I build on VS2013?

-------------------------

1vanK | 2022-01-29 00:06:03 UTC | #3

Try it. If it doesn't work out for you, then send a PR

-------------------------

GodMan | 2022-01-29 00:06:32 UTC | #4

Okay awesome. I will try this later.
Thanks

-------------------------

1vanK | 2022-08-03 12:48:01 UTC | #5

<https://github.com/urho3d/Urho3D/issues/3046>

-------------------------

