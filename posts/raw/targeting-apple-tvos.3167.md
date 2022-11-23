weitjong | 2017-05-27 10:28:15 UTC | #1

I am currently rebasing my local feature branch which ports Urho3D to Apple tvOS platform. With some luck I should be able to resolve all the conflicts by this weekend. I did not push the branch out last year because it depends on some upstream changes that had not made it into SDL yet (which is not the case now) and because I don't have the actual tvOS device to fully test the port myself. I am using simulator only to verify, which is not ideal.

https://github.com/urho3d/Urho3D/issues/1309

If some of you are willing to help out to test the port on the actual device then I will push the branch out to Github when it is ready. I suppose if the port is solid then there would be no problem to merge the feature branch into master before 1.7 release.

-------------------------

weitjong | 2017-05-29 16:29:46 UTC | #2

Finally I have pushed the feature branch out after I left the code idling for over one year. :slight_smile: There are quite a number of conflicts needed to be resolved because of that. Probably I might have missed out a couple of C++'s #if or CMake's if here and there, but at least now it builds cleanly on my local test environment. I haven't tried the samples out in the simulator though as it is quite late and I am a bit tired now. Anyway, I am hoping some of you are able to help to test them out in the actual device. The work won't be merged into master branch without any positive confirmation.

To help to test:

    rake cmake tvos && rake make tvos

-------------------------

weitjong | 2017-05-30 13:54:52 UTC | #3

Good news. Tested a few samples on AppleTV Simulator and they ran fine. Captured one screenshot below.
<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/a6acfeecb196986fa175ea85b2d1c66f6517cec9.jpg" width="690" height="388">

As I don't have the actual device, I could not test on the input. This is as far as I can go for now.

-------------------------

