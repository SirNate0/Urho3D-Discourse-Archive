evolgames | 2021-06-21 15:21:48 UTC | #1

Not sure what happened here. Does Urho3DPlayer get locale from somewhere? I've basically taken the exact same files I was using for years and brought them to a fresh manjaro linux install (all vanilla english). Not a big deal but weird.
![Screenshot_2021-06-21_10-57-58|690x371](upload://fdCnRVAsb8UMpLyNGYAJGRO3Gh8.png)

-------------------------

Modanung | 2021-06-21 15:45:53 UTC | #2

Irrelevant to the issue, but I don't think that's Arabic. It looks more like something [Brahmic](https://en.wikipedia.org/wiki/Brahmic_scripts) to me.

![](https://www.indianetzone.com/photos_gallery/62/Tamil_Script.jpg)

-------------------------

Modanung | 2021-06-21 15:55:54 UTC | #3

Definitely Tamil, I'd say.

-------------------------

rbnpontes | 2021-06-21 16:46:06 UTC | #4

Take fire on your PC and throw in your window! :grinning:

-------------------------

weitjong | 2021-06-21 16:57:04 UTC | #5

I have never used Manjaro Linux before, but most probably its installer did not setup the locale properly or that it expects you (the user) to configure it yourself after installation. I would try the following commands as root to fix the issue:

```
lang=en_US.UTF-8
locale-gen $lang
update-locale LANG=$lang
```

HTH

-------------------------

throwawayerino | 2021-06-21 17:17:59 UTC | #6

I don't know but working in a completely different language would be a big deal to me : /

-------------------------

evolgames | 2021-06-21 18:39:44 UTC | #7

Well it's only that error popup for urho player. I dont use the editor. An IDE and the scripting api webpage is all I use really. I definitely don't speak Tamil or whatever this is lol.
@weitjong will try this, thanks. That makes sense.

-------------------------

Joshua-PotatoMan | 2022-05-07 11:32:58 UTC | #8

yep am an Arab and that's definitely not arabic ;)

-------------------------

