evolgames | 2021-03-16 21:34:37 UTC | #1

Anyone do self-updating for a game? I'd like to implement this. I'm pretty sure I could figure out downloading files from a server to the game directory. How would urho handle those changes? Or should I have a "launcher" that either checks for updates (and performs them) then launches the game?

-------------------------

JSandusky | 2021-03-17 01:32:26 UTC | #2

I use the HttpRequest (`Network::MakeHttpRequest(...)`) for all of the communication bits (with CryptoPP added to deal with base64 and RSA). For my needs I'm only using encryption for protecting user persistence information and player activity data going over the wire.

Almost all of the content is in the form of PAKs with manifests and two initialization scripts, one runs once (after download) and another runs every startup. PAK initialization scripts run in multiple passes so the early-initialization of one PAK may remove another PAK from the available ones before it sets stuff up.

There's obviously more to it, a local SQLite database contains records/manifests of everything (which is used by a ResourceRouter), there's a lot of round-tripping for confirmations and constant queries to server that may tell you to go piss at anytime, etc. It's all to be expected in a "*I don't trust you*" environment.

It's worth reiterating that those PAK manifests find their way into an SQLite database, there it's really easy to run all of that offline on your dev machines to confirm what many layers of PAKs will actually do in regards to who is overriding who and so on.

[quote="evolgames, post:1, topic:6759"]
How would urho handle those changes?
[/quote]

Eh who knows, depends what you need to do. At the simplest you could probably get away with transferring PAKs and calling it a day.

-------------------------

evolgames | 2021-03-22 04:41:52 UTC | #3

Thanks a lot, I appreciate the response. I'm going to look into this and start with whatever is the most simple I can get away with, first.

-------------------------

