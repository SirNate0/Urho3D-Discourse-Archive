umen | 2017-01-02 00:59:25 UTC | #1

[i][b]Split from "Urho3D V1.31 released"[/b][/i]

great job all , any planes or roadmap to next version ?

-------------------------

cadaver | 2017-01-02 00:59:26 UTC | #2

Wei Tjong Yao is making an extensive animation refactor (not in a public branch yet), it'd be good to get that in before making the next release.

-------------------------

weitjong | 2017-01-02 00:59:27 UTC | #3

I had to take a long break for a personal reason. I also think it would be good to have that branch merged first before the next release. Give me some more time to clean up the branch before I make it available for public review.

-------------------------

friesencr | 2017-01-02 01:00:47 UTC | #4

I was helping someone on the internet get out engine built.

Problem A:
The readme build instructions did not respect documentation versions and they didn't know that all the cool kids were drinking the master coolaid and they built stable.  The prefixes had changed but the documentation does not indicate that.

Problem B:
The travis ci sticker said mac failed due to a branch failure which caused them to download stable

This represents a perfect storm and one of the only posible attack vectors of our build setup.  I don't think we can solve the indication of builds failing on branches.

I am thinking we should release soon.  It has been a very long time.  I am so proud of all the work that is on master.  The 2d api refactor is important.  I don't know what work it entails but am willing to help in whatever manner I can.

-------------------------

cadaver | 2017-01-02 01:00:47 UTC | #5

Yes, it has been a long time, a ton of things have been fixed, and we don't have any pending feature branch work now. When I wrote about merging the animation refactor first, the discussion had been more active on it, but now things have quieted down, so now I rather agree that we should release soon. From my point of view there are no urgent features that need to be addressed. There is coming contributions like detourcrowd by scorvi, but there's always a next release anyway :wink:

-------------------------

friesencr | 2017-01-02 01:00:48 UTC | #6

[quote="cadaver"]Yes, it has been a long time, a ton of things have been fixed, and we don't have any pending feature branch work now. When I wrote about merging the animation refactor first, the discussion had been more active on it, but now things have quieted down, so now I rather agree that we should release soon. From my point of view there are no urgent features that need to be addressed. There is coming contributions like detourcrowd by scorvi, but there's always a next release anyway :wink:[/quote]

I would like to use the release cadence as an opportunity to 'market' urho3d.  "Every couple of months' seems about right.  I am hoping the responsibility inverts soon where by people will post stuff when we release rather then me telling them, but the ball needs to get rolling.

-------------------------

weitjong | 2017-01-02 01:00:48 UTC | #7

I have split some of the posts from "Urho3D V1.31 released" topic into this new topic. It should prevent others from thinking that the new pending release has actually been released  :wink: .

-------------------------

alexrass | 2017-01-02 01:00:48 UTC | #8

Too many changes in the API, should be 1.4  :slight_smile:

-------------------------

silverkorn | 2017-01-02 01:00:48 UTC | #9

[quote="cadaver"]Wei Tjong Yao is making an extensive animation refactor (not in a public branch yet), it'd be good to get that in before making the next release.[/quote]

But would it need public testing and stability before being ready to be in an official release?

It think it would be a good idea to follow the famous Vincent Driessen's [url=http://nvie.com/posts/a-successful-git-branching-model/]Git workflow[/url] so we could make this available in the [b]development[/b] branch (or [b]feature[/b]/[i]type[/i] branch) and the [b]master[/b] branch would be judged stable thought it might need public testing before being sent to a [b]tag [/b] release.

Using this standard, you could also create specific branch namespace such as CI ("[b]ci[/b]/[i]target[/i]") too and maybe a test namespace ("[b]test[/b]/[i]feature[/i]") to invite people to test a specific feature.

This is just a suggestion and it might not fit your habits and/or structure but I've seen some projects on Github following this standard such as libtomcrypt.

BTW, I also agree that a new release would be good to have soon.  :wink:

-------------------------

cadaver | 2017-01-02 01:00:48 UTC | #10

Sure, no sudden major changes can go in without living in the master branch for a while. Note the age of the message! (June)

weitjong, I'd like to confirm from you regarding the animation refactor: as there's no feature branch for it at the moment, do you oppose if we just close the few remaining small issues / PRs we have now, then release, instead of waiting for it?

-------------------------

weitjong | 2017-01-02 01:00:48 UTC | #11

I can confirm that that animation refactoring branch will definitely not make it into this coming release.

-------------------------

primitivewaste | 2017-01-02 01:01:24 UTC | #12

Are we in a feature freeze for 1.32 now?

-------------------------

weitjong | 2017-01-02 01:01:24 UTC | #13

I have some more commits in the Android-CI branch that I hope they can be made into V1.32. One of the commit contains a simple fix to allow AngelScript library to work correctly on Android ABI x86_64 (tested using Intel Atom x86_64 system image in emulator).

-------------------------

cadaver | 2017-01-02 01:01:24 UTC | #14

I like to think that we are never in feature freeze, but at the same time I advocate being "responsible" with the commits, ie. with the idea that master branch will be in a working state :slight_smile: I don't think this has been a problem so far.

There are a couple of issues now (tagged with the 1.32 milestone) that need to be addressed before release, so the Android-CI work can well get in too.

-------------------------

weitjong | 2017-01-02 01:01:25 UTC | #15

I will merge the Android CI branch changes into master branch any time now. Here are my last test result for Android 64-bit ABIs:

[ul][li] ABI x86_64: C++ ok, AngelScript OK NOW, LuaJIT still NOT OK (this is reason why I need to get the ndk-gdb working =)[/li]
[li] ABI arm64-v8a: failed to build due to LuaJIT detected unsupported arch, fallback to Lua library instead and build is OK now. However, not able to test further in emulator as no sysimg is available but I suspect C++ and AngelScript (using AS_MAX_PORTABILITY mode) should work just fine.[/li][/ul]
Surprisingly, C++, AngelScript, and LuaJIT work on ABI x86 out of the box.

-------------------------

cadaver | 2017-01-02 01:01:27 UTC | #16

I believe a release should now be doable (today possibly if things go well). Please voice objections if you have something urgent yet.

-------------------------

ucupumar | 2017-01-02 01:01:28 UTC | #17

I had no objection!
[img]http://i.imgur.com/ZB2cEQt.jpg[/img]

-------------------------

