rogerdv | 2017-01-02 01:01:23 UTC | #1

When I compiled Urho at home I noticed something: samples were not built, in both Linux and Windows, despite passing the URHO3D_SAMPLES=1 parameter. But yesterday, I also noticed that neither lua support was compiled, no matter if I use plain lua or luajit. Here at office all options enabled are correctly compiled. What can be happening?

-------------------------

friesencr | 2017-01-02 01:01:24 UTC | #2

are you using master on both? 1.31 had different parameter names.

-------------------------

rogerdv | 2017-01-02 01:01:24 UTC | #3

Yes, I pull here and bring the code home in a flash drive, every 2-3 weeks. But even the oldest code I brought home was pulled from master after 1.31.

-------------------------

