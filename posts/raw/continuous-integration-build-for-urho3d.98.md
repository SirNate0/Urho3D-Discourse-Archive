weitjong | 2017-01-02 00:57:58 UTC | #1

As you may already know that we have setup Travis-CI to perform the CI build for Linux platform which will be triggered on every commits or pull requests made into our main repository. Currently the build matrix for Linux platform are:

[ul]
[li]64-bit native build[/li]
[li]32-bit native build[/li]
[li]32-bit Android cross-compile build[/li][/ul]
Each build has two variants: static or shared library types.

Through a lot of trial and error, I have also managed today to setup CI build for OSX and IOS platforms with the following build matrix:

[ul]
[li]64-bit OSX build using Makefile[/li]
[li]32-bit OSX build using Makefile[/li]
[li]64-bit OSX build using Xcode[/li]
[li]32-bit OSX build using Xcode[/li]
[li]64-bit IOS build using Xcode[/li]
[li]32-bit IOS build using Xcode[/li][/ul]
Most comes with two variants except for IOS build which only has static variant, so a total of 10 combinations. The first successful build details can be seen here [travis-ci.org/weitjong/Urho3D/builds/18870915](https://travis-ci.org/weitjong/Urho3D/builds/18870915). Now I can test all the builds on these platforms with a click of a button. Hopefully any faulty commit that breaks thing could be detected timely and automatically. I even found a couple of errors with our build script while trying to get this setup running.

At the moment, this new setup is only done in my Urho3D fork and not in main Urho3D repository because I am not quite sure of its implication to have it there. Therefore I am posting here to get your opinion. In order to achieve this feat, I have to create a new branch called "master.OSX-CI" which is a mirror of master branch with just one commit ahead, among others is to change .travis.yml's language setting from 'gcc' to 'objective-c'. As such, it requires a constant "git rebase" to reapply that one commit on top of master branch. It is the rebase part that I am a little worry about. It is easy to automate the git rebase for this new branch. But would this cause any confusion or have any negative implication to user tracking the main repository? For sure we have to inform everyone not to check out the mirror branch locally or make changes on it.

I am also perfectly fine to let this setup just available in my fork. Still I prefer it to be in main repo.

-------------------------

Azalrion | 2017-01-02 00:57:58 UTC | #2

I'd say go for it, our CI uses a rebase to make our private changes which dont fit on the main urho branch and as long as people are aware that's what its for there shouldn't be a problem.

-------------------------

friesencr | 2017-01-02 00:57:58 UTC | #3

wow.  what are your thoughts on collecting build artifacts?  we can also use a webhook to sync a fork if we want to keep it clean.

-------------------------

weitjong | 2017-01-02 00:57:58 UTC | #4

[quote="friesencr"]wow.  what are your thoughts on collecting build artifacts?  we can also use a webhook to sync a fork if we want to keep it clean.[/quote]

I haven't thought of collecting the build artifacts. Travis CI build environments are so cheap anyway, they are all setup on the fly and scrapped away at the end (including those build artifacts). I reckon we could tarball/zip and transfer them to somewhere else if we really want to. The question is, to where?

Which webhook service are you referring to? I have been searching for one and could not find the one I need.

-------------------------

cadaver | 2017-01-02 00:57:59 UTC | #5

Having this branch setup is fine by me. Maybe not have "master" in the branch name at all (so for example, just "osx-ci") so that no-one mistakes it for the actual master branch?

Btw. awesome work!

-------------------------

weitjong | 2017-01-02 00:57:59 UTC | #6

[quote="cadaver"]Having this branch setup is fine by me. Maybe not have "master" in the branch name at all (so for example, just "osx-ci") so that no-one mistakes it for the actual master branch?[/quote]

I think that is a good idea to avoid the confusion. I will set it up in the main repo later. A quick update on our current CI setup in Linux build environment, the CI build for the Windows platform using MinGW cross-compiling toolchain is also almost working. Which means, by the end of the day, all our CI build matrix combined together will have covered all the platforms that Urho3D supported (except Raspberry Pi).

-------------------------

weitjong | 2017-01-02 00:58:04 UTC | #7

[quote="weitjong"][quote="friesencr"]wow.  what are your thoughts on collecting build artifacts?  we can also use a webhook to sync a fork if we want to keep it clean.[/quote]

I haven't thought of collecting the build artifacts. Travis CI build environments are so cheap anyway, they are all setup on the fly and scrapped away at the end (including those build artifacts). I reckon we could tarball/zip and transfer them to somewhere else if we really want to. The question is, to where?[/quote]

The question has been answered. Lasse and I have agreed to upload those build artifacts to [sourceforge.net/projects/urho3d/](https://sourceforge.net/projects/urho3d/).

Those packages are labeled as 'snapshot' to indicate that they are auto generated by CI build without human QA, so users who download them should manage their expectation on the quality or stability of the binaries in the package. If you have any issues with downloading those packages or with their content, please let us know.

-------------------------

friesencr | 2017-01-02 00:58:05 UTC | #8

nice.  did you explore the github file api as an option?

[developer.github.com/v3/repos/contents/](http://developer.github.com/v3/repos/contents/)

EDIT:
nm they really gimped this service.  1mb file limit psshhh.

-------------------------

weitjong | 2017-01-02 00:58:29 UTC | #9

[quote]Which means, by the end of the day, all our CI build matrix combined together will have covered all the platforms that Urho3D supported (except Raspberry Pi).[/quote]

If my last commit for Travis CI works as intended then we should have CI builds for ALL the platforms supported by Urho3D, including Raspberry Pi.

-------------------------

