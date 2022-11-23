CE184 | 2021-01-16 06:31:48 UTC | #1

I found a weird problem where all my rigid body collision layer is 0. 
```
rigid_body->SetCollisionLayer(10);
// the following two lines print 0!
spdlog::info("Get collision_layer = {}", rigid_body->GetCollisionLayer());
PrintLine("Get collision_layer native = " + String(rigid_body->GetCollisionLayer()));
```
Everything was fine earlier. Probably it was because I deleted xcode and set new compiler path. But the compiler should have no relation to this. So I cleaned up all build cache, reset cmake cache and reload project, even restarted the computer. The GetCollisionLayer() still gives all zero for all objects in the scene no matter what value I set.

I somehow messed up with cmake version in the process so I also reinstalled the latest version cmake.
I also reinstall back the xcode and remove/reinstall the xcode command line tools. Still not working.

I started to doubt if my previous git version really worked so I run ```git stash``` and build/run the program again. Now the collision layers are correct values! I rerun ```git stash apply``` and build/run the program again. **Now all the collision layers are correct too!**

**I am glad it's solved finally but I have no idea what happened. I guess it's due to some cache but I have no clue what it is.** I don't really care the reason now after long time debugging but I just want to share this in case someone knows the answer.

-------------------------

SirNate0 | 2021-01-16 14:52:29 UTC | #2

My very tentative guess is some sort of minor ABI incompatibility with the compiler change, and some leftover object files that got rebuilt when you changed the files with git stash. But you say you cleaned the build cache, so maybe an incompatibility with your build of the Urho3D library.

-------------------------

