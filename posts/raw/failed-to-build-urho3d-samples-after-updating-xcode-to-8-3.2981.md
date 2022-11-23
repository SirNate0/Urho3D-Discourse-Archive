projector | 2017-04-05 21:14:17 UTC | #1

I tried to build Urho3D samples in Release Mode, the build stuck at "Building Urho3D Universal : Running 1 of 1 custom shell script" forever.  This happens only if I build in release mode, no issue if I stick with debug mode. 

Earlier I was using Xcode 8.2 and had no issue with building both release and debug mode. I have tested with Urho3d 1.6 and latest snapshot, both have the same issue with Xcode 8.3. 

Does anybody have any idea what is causing it?

-------------------------

weitjong | 2017-04-05 03:39:47 UTC | #2

The universal binary build employs a hack to keep both CMake and Xcode happy to do what we want them to do. As it is a hack, things could easily break when CMake and/or Xcode decide to change their internal working. I haven't upgraded my Mac to use Xcode 8.3 yet, so I have no other comments at this point besides this. Probably it worth your time to check whether there is newer CMake version for Mac and retry after you have upgraded to the latest CMake version.

-------------------------

projector | 2017-04-05 04:40:17 UTC | #3

Thanks for your response. I've just updated CMake to latest version(version 3.7.2), unfortunately using latest CMake does not resolve it, looks like Apple has changed the internal working of Xcode.

-------------------------

weitjong | 2017-04-05 07:08:33 UTC | #4

I have upgraded one of development branch to use Xcode 8.3 on Travis CI build. We will see what kind of errors we get and plan our course of actions from there.

-------------------------

weitjong | 2017-04-05 07:51:50 UTC | #5

Both the iOS and macOS universal binary CI builds went successfully. Both use Release build configuration. However, for iOS CI build we could only use the iPhoneSimulator SDK instead of iPhoneOS (Urho as an org doesn't have a valid certificate to sign the binaries yet). As such, I will leave this issue as it is.

There is not much differences between current master branch and the development branch that I used to test this, in case you wonder.

-------------------------

projector | 2017-04-05 21:14:06 UTC | #6

My bad, I gave it another try, this time I decided to wait longer time, surprisingly it built successfully after spending about 30 minutes stopping at "Building Urho3D Universal : Running 1 of 1 custom shell script". Earlier, the significant longer time to process "Urho3D Universal" in Xcode 8.3 release mode made me to think the building process was stuck. 

Thanks a lot for your helpful information!

-------------------------

