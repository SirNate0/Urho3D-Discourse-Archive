elemusic | 2017-01-02 01:10:41 UTC | #1

I'm trying to play a music from the middle of the song,and i want to loop the music from certain sample or seconds.
Say the music is 60 seconds long.i want to play with it from 30 sec to 40 sec and loop it.
how can i do that?
i search the document,found some function called SetPositionAttr(int value)

guess this is the audio offset play function,but is it not working.

i use the 14_soundeffect example

and add some code like this

[code]
musicSource->SetPositionAttr(44100 * 5);
musicSource->Play(music);
[/code]

nothing is happening
then i thought maybe it will work after the play function call.
still nothing.

not sure what's going on here.

what's correct way to use this SetPositionAttr function?

-------------------------

gawag | 2017-01-02 01:10:41 UTC | #2

No idea about that SetPositionAttr but it may generally be a better idea to copy a part of a sound to create a new sound. With your approach you would have to set the position back at a very precise time moment to not hear any kind of click-sound. There may be still a distortion due to sound buffers even if you hit the exact moment. When creating a new sound you can just use the normal hardware accelerated (is it?) sound looping.
Also you may want to fade in and out at your cut so that there is no abrupt change in the waveform, which is hearable as a click-sound. You would do that fading out by changing the sound data. The fading can be pretty short and is usually not noticeable directly (unless the music change fells weird rhythm and melody wise), but a jump due to not fading is really noticeable.
I'm note really a sound or sound buffer expert though.

-------------------------

cadaver | 2017-01-02 01:10:41 UTC | #3

SetPositionAttr() is an internal method used for serialization, but I suppose you can use it. The alternative is to call SetPlayPosition() with the pointer to the audio data, which means you must yourself calculate the address from the sound sample's start.

However the catch is that for ogg compressed samples it would require arbitrary seeking within the compressed stream which isn't presently implemented. On a wav sample it should work.

-------------------------

