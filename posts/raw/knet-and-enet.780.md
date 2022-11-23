rogerdv | 2017-01-02 01:02:50 UTC | #1

Is it possible to write the server side using enet and the client using Urho3d's knet based networking?

-------------------------

cadaver | 2017-01-02 01:02:50 UTC | #2

Not really, because the low-level UDP packet protocol is incompatible. Just replace the network library from both sides if you really need to do that.

Note that Urho's current networking model is pretty much an exact match with knet (for example latest-data reliable messages, which discard the old data) and moving it to enet will be difficult.

-------------------------

rogerdv | 2017-01-02 01:02:50 UTC | #3

Well, it is not a problem learning knet, but I was thinking that perhaps enet was more up to date (last update in knet repo is from 2012).

-------------------------

cadaver | 2017-01-02 01:02:50 UTC | #4

Where do you get 2012 from? Check [github.com/juj/kNet](https://github.com/juj/kNet) master branch for most recent activity. Though it must be noted that Urho doesn't follow knet's master version directly, as we have a custom UDP flow control mechanism that doesn't exist in knet master and it isn't pleasant to merge. That said important knet fixes do end up in Urho sooner or later (or in some cases are developed in Urho first)

-------------------------

rogerdv | 2017-01-02 01:02:50 UTC | #5

What seems to be the official website directs me to bitbucket, there the repo is quite old, though it compiles under Mint 17.1.

-------------------------

cadaver | 2017-01-02 01:02:51 UTC | #6

Yeah the official site has not been updated that much, and the bitbucket repo is outdated and superseded by the git repo.

-------------------------

