Bananaft | 2018-03-20 22:55:36 UTC | #1

I hacked together Urho3d and SoLoud audio library: http://soloud-audio.com
I decided to try it after investigating on this issue: https://discourse.urho3d.io/t/audio-artifacts-on-low-frequency-sounds/3946

Here is a comparison video, enable CC:
https://www.youtube.com/watch?v=OSPhJRYwBOM&cc_load_policy=1

-------------------------

johnnycable | 2018-03-21 15:38:00 UTC | #2

Great! This is definitely welcome! Always find the sound to be hacky. Do you plan to contribute it?

-------------------------

Bananaft | 2018-03-21 20:51:06 UTC | #3

Well, um... yeah, about that...

1) I'm just learning C++, and I code like no one is watching. I can share my code but it is terrible. And I broke a lot of stuff.
2) It seems like a big feature, will require setting up build system (I broke it in my repo). Checking if it will work on all platforms Urho supports.
3) It is better to change interface of audio system to better support SoLoud features (like filters, mixing busses), and that's a decision for someone smart from core team.

-------------------------

johnnycable | 2018-03-22 08:47:51 UTC | #4

I see. Don't worry about integrating it, it's complicated anyway. These days I'm trying to fit turbobadger into Urho, just for the sake of improving...
Anyway, if you don't mind, you could share some spare code, or simply describe your workflow...
I'd like to try to make this thing work with Android. Android it's notoriously problematic on sounds, and that would be a real test...

-------------------------

Bananaft | 2018-03-22 20:25:27 UTC | #5

Ok, but you've been warned:
https://github.com/Bananaft/urh_sld

I basically took Urho's audio classes, removed their guts and made them use SoLoud instead. There should be a name for this? Glue code? (edit: wrapper) There are also some dead code, especially in audio.cpp.

I also wrote my own attenuation model.

So I used Urho 1.7 source. I added the library, threw out some exotic file formats that cause build errors, defined backend: #define WITH_SDL2_STATIC

One little problem I ran into is that SoLoud uses #define M_PI for Pi value, and Urho uses static const float M_PI, and they conflict.

-------------------------

Sinoid | 2018-03-22 20:08:42 UTC | #6

> One little problem I ran into is that SoLoud uses #define M_PI for Pi value, and Urho uses static const float M_PI, and they conflict.

That's because you put SoLoud headers into your headers instead of just your sources and forward declaring the SoLoud types. Headers only in the source files after all Urho3D headers, and #undef M_PI if necessary.

-------------------------

