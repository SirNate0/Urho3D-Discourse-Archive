Bananaft | 2017-01-02 01:08:21 UTC | #1

It seems to me that directional light's frustum near and far planes are set to some very high numbers and does no change no matter what (am I right?). The only way to fix bad depth precision (like this: [i.imgur.com/B6MLGHz.png](http://i.imgur.com/B6MLGHz.png)) is to set renderer.shadowQuality from 16 to 24 bit. It helps a bit, but wouldn't be better to set near and far planes automatically ([url=https://msdn.microsoft.com/en-us/library/windows/desktop/ee416324(v=vs.85).aspx]like described here[/url]), so the range between them will be minimal, thus will provide higher precision even with 16 bit?

-------------------------

cadaver | 2017-01-02 01:08:21 UTC | #2

The logic to set the dir light shadow camera's near & far plane could be better, I agree. Right now it's derived from the amount of main view frustum it's covering. One thing to keep in mind is that changing the near / far planes radically (in a scene or view angle dependent way) also dynamically changes the significance of depth bias, making it harder to adjust.

-------------------------

Bananaft | 2017-01-02 01:08:22 UTC | #3

[quote="cadaver"] Right now it's derived from the amount of main view frustum it's covering.[/quote]

Ah, ok, thanks for clarifying. I have camera's far clip set to 12000, and last shadow split fading at 5000.

I see, it makes sense to cover all main camera depth for cases like dawn with very long shadows, even if shadow distance is much smaller. But one thing I've noted in my case, is that, when the sun is low you don't need as much precision as when it high.

Here is pretty ugly leaks i have with high sun (16 bits) [imgur.com/Bt3ULqH](http://imgur.com/Bt3ULqH)
And with low: [imgur.com/51XXetb](http://imgur.com/51XXetb)

[quote="cadaver"]One thing to keep in mind is that changing the near / far planes radically (in a scene or view angle dependent way) also dynamically changes the significance of depth bias, making it harder to adjust.[/quote]

The choice is to always have worst precision, or only sometimes. It may as well adjust bias automatically with some extra parameter. Setting up perfect bias is a pain anyway, I'm okay to have a bit more pain for better results.

-------------------------

