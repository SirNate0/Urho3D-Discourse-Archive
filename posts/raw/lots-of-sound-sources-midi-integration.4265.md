enppu | 2018-05-25 19:25:07 UTC | #1

Hi there,

I'm new to this forum. I'm currently loking into a bunch of 3d engines for a potential project. I have two questions regarding the Urho sound system:

(1) how many sound sources can Urho handle? Let's say you have a scene with a city model (the size of a typical city center) with each of the buildings having their own sound source (potentially other objects having sound sources too). Would that work?

(2) has anybody ever used MIDI with Urho? For those who know the code, would it be possible to maybe subclass SoundSource and have it send out midi instead of controlling sound playback?

thanks!

-------------------------

Modanung | 2018-05-25 22:04:03 UTC | #2

If you're thinking about using MIDI, you might want to look into [OSC](https://en.wikipedia.org/wiki/Open_Sound_Control).

-------------------------

