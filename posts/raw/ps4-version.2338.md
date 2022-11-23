EricDeflandres | 2017-01-02 01:14:49 UTC | #1

Has anybody on this forum already worked with the PS4 SDK ?

As Urho3D's HAL code is designed to be portable on desktop and mobile devices, I'm wondering how difficult it would be to port a Urho3D game to run on PS4 by modifying Urho3D's graphic/audio/input/storage/networking code to use the PS4 SDK.

-------------------------

dragonCASTjosh | 2017-01-02 01:14:49 UTC | #2

I don't see the engine being a limitation for Console development as long as you have you SDK and the right understanding of the engine. For the most part all the systems in the engine can be swapped out without causing issues, especially graphics. As for windowing you may have to dig into the lower levels of SDL to get that to work correctly although there is likely something online about how to set that up.

-------------------------

cadaver | 2017-01-02 01:14:49 UTC | #3

If you want to retain the platform abstraction, you'd have to create new platform-specific subsystems in SDL2. At least audio, controllers, video/window initialization (+ a PS4-specific Graphics class implementation in Urho) It's quite a safe bet someone on the planet has already done the SDL2 work but since the SDK is proprietary the work can't be shared, except among licensees.

-------------------------

Eugene | 2017-01-02 01:14:50 UTC | #4

I am afraid that porting Urho to consoles may face performance penalty due to different hardware architecture and lack of some console-specific optimizations.

-------------------------

cadaver | 2017-01-02 01:14:51 UTC | #5

Certainly. PS4 should be "friendlier" than PS3 but if one is serious of console work one should choose an engine where the console platform is a first-class citizen. Unfortunately this pretty much rules out open source engines.

-------------------------

