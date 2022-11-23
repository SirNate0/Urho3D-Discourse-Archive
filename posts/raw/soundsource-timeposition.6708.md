krokodilcapa | 2021-02-13 10:39:33 UTC | #1

Hi!

I would like to ask how much accurate is SoundSource.timePosition? Is it counts the sound starting delay like Unity's dspTime? Is it capable for rhythm games in its current state?

-------------------------

Modanung | 2021-02-13 13:28:10 UTC | #2

It's tied into the number of samples processed in `SoundSource::Mix`:
```
timePosition_ += (static_cast<float>(samples) / mixRate) * frequency_ / soundStream_->GetFrequency();
```

-------------------------

