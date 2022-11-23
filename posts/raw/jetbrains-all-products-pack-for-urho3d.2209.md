weitjong | 2017-01-02 01:13:56 UTC | #1

This invitation is only open to Urho3D core team developers.

We have a couple of "All products pack" Open Source licenses from Jetbrains*. A single license can be used to activate all the products available from Jetbrains, including CLion and IntelliJ IDEA. The only catch is the registered products can only be used in conjunction with Urho3D project development as stipulated by the Open Source licenses that we obtained.

If any of you are interested then please kindly PM me your "Jetbrains account". If you don't have one, you can quickly register one at their website free of charge. If the number of interested parties is more than the number of spare licenses that we have then the priority will be given to the more active contributors first. Please register your interest by end of August.

* We are not affiliated with Jetbrains. You must agree to the license term [jetbrains.com/store/license_opensource.html](https://www.jetbrains.com/store/license_opensource.html). The license is revocable and re-assignable at our discretion.

-------------------------

Victor | 2017-01-02 01:13:56 UTC | #2

Wow, that's pretty cool! I've been using CLion for my Urho3D development and I can say it's a pretty nice cross-platform IDE. I hope you guys get a chance to enjoy it as well! :slight_smile:

-------------------------

weitjong | 2017-01-02 01:13:57 UTC | #3

We have 7 unused licenses as of now.

-------------------------

Egorbo | 2017-01-02 01:13:57 UTC | #4

I'd recommend JetBrains Resharper++ for those who uses Visual Studio and C++ :wink: really great tool!

-------------------------

bubobubo | 2017-01-02 01:14:03 UTC | #5

Is there AngelScript support in Jetbrains CLion or any other Jetbrains products?

-------------------------

weitjong | 2017-01-02 01:14:03 UTC | #6

Not that I am aware of. CLion depends on the code inspection in order to function correctly and meaningfully. When the code inspection fails to understand a piece of code, as in the case of AngelScript, the IDE does not only show a lot of red flags but also disable many of its nice features like smart code completion. I have a better luck with Eclipse with CDT plugin. Search the forums, there was a post of two sometimes back on how to trick some of the IDEs to work nicely with AngelScript.

-------------------------

bukkits | 2017-01-02 01:15:04 UTC | #7

For those using CLion, what are your opinions of it so far? 

The Git and CMake integration seem nice, but CLion seems to have trouble with sample files and marking Urho3D's types in red as if it cannot find them.

-------------------------

rku | 2017-01-02 01:15:05 UTC | #8

Works fine for me. One thing to note is that i keep my cmake directory in /tmp therefore it is gone on reboot. Next time i open project it generates new cmake dir and all urho types are in red. It takes IDE restart to make them show up. In general autocompletion works great except for Urho3D::Context type. No idea why IDE cant pick that up.

-------------------------

weitjong | 2017-01-02 01:15:06 UTC | #9

It works great for me too. The coming version,  2016.3 will be even better. Currently only available for those in Early Access Program. For the first time I managed to do a cross-compiling build with ease with this new version. The only problem I have related to this is, sometime the cache symbols in the IDE become stale due to git mass mutation operations like checking out a branch or changing target platform, and I see red markers all over the places in the editor. However, a click of a button to invalidate the caches usually fixes my problem. The worse case is to delete it's internal cache directory manuall, the symbols will be rediscovered in the next start.

-------------------------

bukkits | 2017-01-02 01:15:06 UTC | #10

I think my issue must be with the CMake cache as I was having issues building from a fresh git clone. I'm keen on switching to CLion because I use IntelliJ at work and keeping shortcuts the sane would be excellent. Also the linux compatibility is a big advantage over Visual Studio for me as well

-------------------------

weitjong | 2017-05-04 14:11:06 UTC | #11

Just renew our licenses for another year. The offer is still valid for the core team developers as we still have some unused licenses. See the first post before applying.

-------------------------

weitjong | 2018-04-26 13:14:05 UTC | #12

We have gotten the support from JetBrains to renew the OS license program for Urho3D project for another year. We have also obtained extra 2 more All Products licenses, which should make us having enough licenses for all the core devs currently in Urho3D project even when all want to take the offer. The core devs are: Alex Parlett, asterj, Lasse Öörni, Eugene Kozlov, Chris Friesen, hdunderscore, Mike3D, primitivewaste, TheComet, Yao Wei Tjong. I know some of you may not be active in this project anymore, still that is the list I have now in the GitHub team. PM me if you are interested to try out the product working on Urho3D project. See the T&C in the first post.

-------------------------

weitjong | 2019-04-12 16:47:49 UTC | #13

Got the licenses renewed again for another year, but this time we only managed to get 3 licenses.

-------------------------

Miegamicis | 2019-04-23 06:32:51 UTC | #14

Have you decided to whom to give those licenses?

-------------------------

weitjong | 2019-04-23 08:13:36 UTC | #15

We have left with one spare. You and I got one license assigned. Other core dev who needs it can PM me. T&C applies.

-------------------------

