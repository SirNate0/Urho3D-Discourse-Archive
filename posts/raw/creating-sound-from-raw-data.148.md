GIMB4L | 2017-01-02 00:58:23 UTC | #1

This is somewhat of a crosspost from my other topic, but it necessitates a new post because I switched to Theora, and now I have a new issue.

How exactly does SetData work when dealing with sound?

-------------------------

GIMB4L | 2017-01-02 00:58:23 UTC | #2

Okay, I've gotten something going using SetData.Turns out I was using a sound source that wasn't part of a node.

However, I only get static, followed by a gap, followed by more static. I should note that Theora uses Vorbis for it's ogg decoding, so I'm assuming SetData works fine in terms of formatting.

Now, Theora will give me new audio information as soon as it gets it, and once I get the new data, I tell the sound source to play again. I feel like this may be incorrect, as maybe it's starting another sound before the current one has finished. Am I doing things correctly?

-------------------------

GIMB4L | 2017-01-02 00:58:23 UTC | #3

Alright, some further digging discovered that the data being used is in PCM format, or pulse-code-modulation. I'm guessing Urho doesn't support this type.

-------------------------

cadaver | 2017-01-02 00:58:23 UTC | #4

The SoundSource does not support (yet) outside sources feeding streaming data into it. You can try to "fake" it with SetData(), but to get it to play a gapless stream is hard.

The mechanism used by the streaming ogg decoding internally needs to be expanded and exposed so that you can feed audio data into it.

And yes, the data needs to be raw, signed 16-bit sample values, SoundSource doesn't decode it.

-------------------------

GIMB4L | 2017-01-02 00:58:24 UTC | #5

So would you recommend I feed the entire audio track into a Sound and play that back, pausing and replaying to keep pace with the video?

EDIT: I should say the playback library does the thinking for me. Since it gives me 32bit float data, could I not convert it to how Urho likes it and it should play just fine?

-------------------------

cadaver | 2017-01-02 00:58:24 UTC | #6

I suggest that you wait for the proper implementation of streaming audio in the SoundSource class.

Converting float sample data to 16-bit integer (short) sample data should be easy. If it's floats between -1 and 1, just multiply with 32767 and convert to short.

-------------------------

GIMB4L | 2017-01-02 00:58:24 UTC | #7

I tried that and I still got the same static. The engine does play back 16-bit PCM data, correct?

-------------------------

cadaver | 2017-01-02 00:58:24 UTC | #8

Yes. Though it can also play 8-bit, and stereo/mono, so check that your Sound object has the correct format set.

-------------------------

GIMB4L | 2017-01-02 00:58:24 UTC | #9

Do you mean the sample rate, etc? I'm also running out of memory when I use the SetData with the short buffer and its size.

-------------------------

cadaver | 2017-01-02 00:58:24 UTC | #10

Wrong sample rate should not cause static, only the sound playing at wrong pitch, but check that the sixteenbit and stereo flags are set right.

-------------------------

GIMB4L | 2017-01-02 00:58:24 UTC | #11

Yeah I changed them, i forgot to reset them back after messing around with the params to test. However, I have a heap allocation error when trying to set the buffer.

-------------------------

cadaver | 2017-01-02 00:58:24 UTC | #12

If you set a new buffer while the sound is being played, I wouldn't be surprised of bad things happening. The mixer thread still has an internal pointer to the old buffer, which now has been freed.

-------------------------

GIMB4L | 2017-01-02 00:58:24 UTC | #13

It's a memory allocation error for the new buffer during the resize. Also, I noticed the engine uses 'new' as opposed to 'malloc' for PODs. Why is this the case?

-------------------------

cadaver | 2017-01-02 00:58:25 UTC | #14

It's possible the heap has been corrupted earlier.

There is a convention that new[] is used for POD arrays that are pointed to with SharedArrayPtr, because it will call delete[] when the array expires.

-------------------------

GIMB4L | 2017-01-02 00:58:25 UTC | #15

Turns out it was my allocation of the short buffer for conversion. I got it to not crash, but it's still silent. I'll keep trying.

-------------------------

GIMB4L | 2017-01-02 00:58:25 UTC | #16

Okay i got it to work, but it's quite choppy (like you said :stuck_out_tongue:). Maybe I can add the audio I've received to some sort of queue the sound source will play?

I could also take last frame's audio position and data, add in the current frame, and resume playback. I think it comes down to why the delay exists -- is the system not fast enough, or too fast that the clip cannot finish playing?

-------------------------

cadaver | 2017-01-02 00:58:25 UTC | #17

I'll have to see what the API ends up like, but queueing sound data buffers should be one of the operation modes. There's an issue for it here:

[github.com/urho3d/Urho3D/issues/257](https://github.com/urho3d/Urho3D/issues/257)

-------------------------

GIMB4L | 2017-01-02 00:58:25 UTC | #18

So you're saying right before the data is taken to play the sound, it should grab the data it's going to play? I also presume that 'Play' will reset wherever the sound is, which may be contributing to my problem. I think what you could do is request some sort of pointer that the sound will use this frame. Another class would be responsible for the stream, the SoundSource will just play it.

-------------------------

GIMB4L | 2017-01-02 00:58:25 UTC | #19

The array concatenation code wouldn't be that bad. I think this would work:

[code]
Given an array of new data called void *newData and the size of the data with uint newDataSize

//Reallocate array
unsigned int newSize = curArraySize - curPlaybackPosition + newDataSize; //This assumes bytes

void *newArr;

newArr= new signed char[newSize];

//Copy old
memcpy(newArr, arr+ curPlaybackPosition, curArraySize - curPlaybackPosition);
mempcy(newArr, curArraySize - curPlaybackPosition, newDataSize);
[/code]

-------------------------

