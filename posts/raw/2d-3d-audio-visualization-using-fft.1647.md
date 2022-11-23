shlomok | 2017-01-02 01:09:12 UTC | #1

Dear All, 
What is the best way to:
[ul]
Capture the mixed audio played like in the SoundEffects example
Run an FFT on the data (possibly using [fftw.org/](http://www.fftw.org/))
Visualize the data either in 3d like so: [youtube.com/watch?v=IRpm9Qcnp-k](https://www.youtube.com/watch?v=IRpm9Qcnp-k) or like so:[img]http://gracefulspoon.com/blog/wp-content/uploads/2009/03/processingapp.jpg[/img]
[/ul]

Thanks,

-------------------------

weitjong | 2017-01-02 01:09:12 UTC | #2

This reminds me of another OSS project called projectM. There are two approaches that comes to mind immediately. Feed the FFT data to a custom geometry modeller. Or render a texture using the FFT data and let the shader samples the texture and uses the data there to affect the visualization of the audio.

-------------------------

