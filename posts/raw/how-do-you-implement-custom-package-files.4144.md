S.L.C | 2018-04-02 19:10:52 UTC | #1

I need to read an existing archive/package file and I'm curious as to how do you do it in Urho. I am looking at the `PackageFile` type from the `IO` directory but I see that it enforces a custom entry format which I understand and I could get around. But I see that pretty much all other functions that have to deal with retrieving the entries or various information about the package file are not virtual.

So how do I use `AddPackageFile` from `ResourceCache` with my own implementation without having to modify any engine code?

There's absolutely no documentation about this. And while looking at the code could yield some results. I thought I should ask first.

Can anyone guide me into the right direction? Than you.

-------------------------

cadaver | 2018-04-02 19:35:04 UTC | #2

Make virtual what you need (or any other necessary engine changes), submit PR. The engine has not been planned with that usecase in mind beforehand.

-------------------------

S.L.C | 2018-04-02 20:53:25 UTC | #3

Thank you for the quick reply. One more question. Is the `checksum_` member critical for entries? I'd like to avoid calculating it each time I load the package file or keeping a separate file since I can't alter the existing package format.

From a quick code search it doesn't seem critical. So can I set that to 0?

-------------------------

cadaver | 2018-04-02 20:58:55 UTC | #4

As far as I remember, it was used only for network sending of packages, so if you don't use that feature, it can be kept zero.

-------------------------

Eugene | 2018-04-02 21:00:32 UTC | #5

I have strong deja vu feeling. This topic was asked, and even PR was submitted. However, it required massive nasty renames or hacks, so it wasn’t merged.

-------------------------

S.L.C | 2018-04-02 22:22:57 UTC | #6

It should actually be quite simple to add. And with minimal changes I might add. What gets in the way is the scripting part. That'll get nasty very quickly. Which is why I'll keep the changes to myself for now because Lua is not something I want to touch right now.

You guys really need to get rid of Lua. The language is ugly to work with and even uglier to maintain.

-------------------------

SirNate0 | 2018-04-03 20:14:41 UTC | #7

The PR mentioned is probably mine [here](https://github.com/urho3d/Urho3D/pull/2210), if you want a possible starting point for your work. I think I created an example integrating gzipped package files, though I don't remember if it was in that branch it a separate repo...

-------------------------

S.L.C | 2018-04-04 18:39:01 UTC | #8

I've done a basic implementation of of custom package files in my fork but unfortunately I don't use Lua enough to learn the toLua syntax right now. If anyone knows it already and is willing to perform that task then I'll gladly make a pull request.

Of course, if the implementation I've done is considered worthy of a pull-request. I've tried to keep engine changes as minimal I could. Scripting components required the use of the factory approach. And to allow future implementation of custom package files over network.

https://github.com/iSLC/Urho3D/tree/custom-package-files

-------------------------

