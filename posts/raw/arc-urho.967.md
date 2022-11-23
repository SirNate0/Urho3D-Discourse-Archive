TikariSakari | 2017-01-02 01:04:30 UTC | #1

I noticed an interesting project by chrome: ARC. [url]https://developer.chrome.com/apps/getstarted_arc[/url]

I was curious if APK made with Urho would work with ARC, and it does seem to. I didn't try out examples, mostly just my own test thingie. The performance does take quite a hit tho at least on my computer with my test like ~140 linux -> ~25 with ARC. Also this could be that the "openglES" drivers it says I have, aren't the best.

I couldnt figure out how to do multitouch tho, so I couldn't change the camera angle with chrome, but it did indeed read all the keypresses from keyboard. Sadly it counted my mouse as a touchdevice, so right clicking (could be faulty programming), was considered just another mouse press. I think touchEnabled_ is true when using this, so I guess it is more of a logic problem on my program than any real problem with urho and arc.

Linux with ARC:
[url]http://i.imgur.com/FlosYz0.png[/url]

Linux:
[url]http://i.imgur.com/ZpwBe72.png[/url]

I guess this is bit redundant since there are now all the emscripten support, but nevertheless it seems kinda cool.

-------------------------

thebluefish | 2017-01-02 01:04:35 UTC | #2

It sounds interesting, but I don't know how useful this would be. It looks to me like this is for android developers to get their apps on the desktop where they otherwise couldn't. While the idea of android emulation in Chrome sounds nice, I don't think any sort of emulation is going to beat a native port. I'd personally wait for the emscripten port to be fleshed out and fully functional, but good work either way!

-------------------------

