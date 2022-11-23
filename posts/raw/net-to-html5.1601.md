DragonSpark | 2017-01-02 01:08:49 UTC | #1

Hello,

I see that you support HTML5 via Enscripten:
[urho3d.github.io/HTML5-samples.html](http://urho3d.github.io/HTML5-samples.html)

And I see that you now support .NET.  Is there any way to combine these two?  That is, develop a Urho3D application in .NET, and then have it output to HTML5?

Thank you,
Michael

-------------------------

cadaver | 2017-01-02 01:08:50 UTC | #2

The .NET support is provided by a third party (Xamarin) and is not a part of the Urho core repository, we make no claims to what it supports or doesn't. You should ask them. Though my guess is that if it's based on the Mono runtime, Emscripten is out of the question.

-------------------------

DragonSpark | 2017-01-02 01:08:51 UTC | #3

Bummer, [url=http://blog.developers.win/2015/10/existing-net-client-application-models/#urho3d]the search continues[/url].  Thank you for taking the time to explain that.

-------------------------

Egorbo | 2017-01-02 01:08:54 UTC | #4

[quote="cadaver"]The .NET support is provided by a third party (Xamarin) and is not a part of the Urho core repository, we make no claims to what it supports or doesn't. You should ask them. Though my guess is that if it's based on the Mono runtime, Emscripten is out of the question.[/quote]
In theory it compiles to LLVM, but you are right - no Emscripten so far.

-------------------------

