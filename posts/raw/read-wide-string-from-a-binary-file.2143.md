Pellucas | 2017-01-02 01:13:27 UTC | #1

Hi all.

Can Urho3D read directly a string of wide characters of [b]2 bytes per character[/b] from a binary file in a easy way? I want to mention that I want my project to be cross-platform, I'm working with Ubuntu right now and I think wchar_t uses 4 bytes per character on Linux.

-------------------------

cadaver | 2017-01-02 01:13:27 UTC | #2

No, there isn't a direct library function for that, and furthermore the WString class is very limited (just for conversions when it's needed for passing into the OS) so now your best bet is to read the character yourself using the Deserializer API.

-------------------------

Pellucas | 2017-01-02 01:13:27 UTC | #3

ok, thanks anyway.

-------------------------

