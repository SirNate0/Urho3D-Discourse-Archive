devrich | 2017-01-02 01:02:36 UTC | #1

Hi,

I have been doing a lot of reading through the forums and documations but so far i don't see a way of connecting to a web server using TCP.  Does this exist or is there another way to connect to a webserver using UDP?

-------------------------

cadaver | 2017-01-02 01:02:37 UTC | #2

Check the HttpRequest class in the Network subdirectory. It implements simple HTTP requests using the Civetweb library. Personally haven't tested much after the initial implementation and there's no actual example for it, so your mileage in using it may vary. Naturally you always have the option of doing raw socket IO yourself, or integrating another network library.

-------------------------

devrich | 2017-01-02 01:02:37 UTC | #3

Thanks cadaver!

I had been very heavily considering using  cURL  but since my primary target platform is Android devices ( 4.2.2+ ), Android TV, and Rasberry Pi then i wasn't sure if trying to modify the engine to add a library would be as cross-platform compatable as i would need.


BTW; Sony announced a few weeks ago at CES that "all" of their 2015 TV's will have Android TV lolipop.  How would I go about getting a Urho3D game on Android TV ( is there anything special I would need to do ) ?

-------------------------

boberfly | 2017-01-02 01:02:38 UTC | #4

Hi devrich,

I think if you just make an android build it should 'just work' on the play store, pending any sony-specific needs eg. [en.wikipedia.org/wiki/PlayStation_Mobile](http://en.wikipedia.org/wiki/PlayStation_Mobile)

It's interesting to see all the TV manufacturers have all chosen their own linux-specific OSes (Tizen, Android, WebOS, etc.) which complicates things a little, but I'm sure if you target SDL2.0+Linux (which Urho3D already does) it's in a very good place for porting. Plus it works with WebGL/Emscripten so there's that also.

Do we need game consoles now with these TVs? Especially if they will adopt something like Nvidia's Tegra X1.

-------------------------

devrich | 2017-01-02 01:02:38 UTC | #5

[quote="boberfly"]Hi devrich,

I think if you just make an android build it should 'just work' on the play store, pending any sony-specific needs eg. [en.wikipedia.org/wiki/PlayStation_Mobile](http://en.wikipedia.org/wiki/PlayStation_Mobile)

It's interesting to see all the TV manufacturers have all chosen their own linux-specific OSes (Tizen, Android, WebOS, etc.) which complicates things a little, but I'm sure if you target SDL2.0+Linux (which Urho3D already does) it's in a very good place for porting. Plus it works with WebGL/Emscripten so there's that also. [/quote]

Awesome!!  :smiley: 

[quote="boberfly"]Do we need game consoles now with these TVs? Especially if they will adopt something like Nvidia's Tegra X1.[/quote]

Yeah I hear ya on that one.  It seems that console gaming is taking a turn for either:  tablet/smartphones -or- pc/mac/linux -or- TV's with built-in gaming systems.  I think Sony may be ahead of the curve on that one but i wonder where samsung is on that.

-------------------------

