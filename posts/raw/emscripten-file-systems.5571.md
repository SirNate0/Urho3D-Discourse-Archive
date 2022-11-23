SirNate0 | 2019-09-13 01:28:39 UTC | #1

I haven't actually dealt with saving anything with emscripten yet, but it seems that this (or something providing similar functionality) could make the experience more painless, particularly if web is only one of the target platforms. I could be wrong though, maybe saving persistent files isn't actually that bad with emscripten. I'm not sure whether it would be appropriate to actually integrate this into the engine or just leave it to the developer (as it seems very easy to do), but here it is for anyone who's interested. Basically, it handles a wide variety of different filesystems in the browser, and from what I can tell can be used to make one type appear as another, and to provide a synchronous interface to the async filesystem that emscripten provides.

https://github.com/jvilk/BrowserFS/blob/master/README.md

-------------------------

