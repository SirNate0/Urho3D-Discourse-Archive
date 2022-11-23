TikariSakari | 2017-01-02 01:04:06 UTC | #1

Hello, I installed linux mint couple of weeks ago and I have this very weird fps drop issue at times.

For example when I run the urho thing that I have, most of the times it runs at 200 fps, but after some time/some weird reasons after I run the compiled file, it starts running at 34 fps and becomes extremely choppy. 

Also the weirdest part is, that if i resize the window, at some resolutions the window runs at 200 fps, and some resolution 34 fps. Sometimes it might actually run higher fps even if the drawing area is bigger. I have a feeling like this is some kind of driver issue, since my pulseaudio keeps crashing from time to time. (I am using asus xonar dx/xd sound card.) I am using engineParameters_["WindowResizable"] = true, but even if its false and using fullscreen it still does this weird choppiness.

I have to admit that I haven't been fiddling with linux before, in other words I do not know much about linux, so the settings I have are mostly default.

I am using skeletalanimation as my base and I tried to remove update-function from it, so it should be pretty bare bones.

If my program leaks memory, could it cause something like this?

A side note, in windows I didn't notice this thing happening.

Edit: Ok it looks to be some very weird issue with my hardware. For example flash in windows somehow kills my gpu, (ati radeon 5870). I had forgotten to take off hardware acceleration from flash, and that causes some issues. Also cinnamon seems to sometimes semi-crash + pulseaudio, so once I restarted them all + disabled hardware acceleration from flash, it seems to work normally again for now.

-------------------------

