justanotherdev | 2020-04-30 16:40:42 UTC | #1

What is the suggested version of Urho for production work? 

The last official release of 1.7.1 is quite a few (to put it mildly) commits behind master. Do people generally use 1.7.1 or just develop off of master? If using master is recommended for production work is there any way (even informally) to know if a given version is more or less likely to be stable or have breaking changes?

Also, what about rbfx? I saw that there's a decent amount of development activity going on there. Is that considered ready-for-production or more just experimental?

Thanks!

-------------------------

JTippetts | 2020-05-03 12:57:19 UTC | #2

I highly recommend pulling the latest master. 1.7 has some serious issues that are fixed in the master. Master stays pretty stable these days.

rbfx is a fork. I'd consider it still very experimental, especially if you're in favor of an editor-centric development approach, as the editor isn't ready yet. From a programming standpoint, it operates much like vanilla Urho, with some changes (removed Lua and AngelScript, switched EASTL containers for custom Urho containers, optional C# support, etc) and if none of those changes bothers you than it should be good.

-------------------------

