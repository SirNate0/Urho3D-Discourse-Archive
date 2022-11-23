djmig | 2017-01-02 01:14:20 UTC | #1

Hi,
I am new to Urho3D. I have just compiled Urho3d on my OS X. The compilation of libUrho3D.a and demo through cmake went smoothly. I am wondering which SDL version was linked to the resulting library since I have both SDL and SDL2 in /usr/local? 

Regards,
Don

-------------------------

weitjong | 2017-01-02 01:14:21 UTC | #2

Neither of them. Urho3D has its own fork of 3rd-party libraries in the Urho3D project source tree. A few of them are now being managed using git subtree and SDL is one of them. See [github.com/urho3d/SDL-mirror/tr ... for-urho3d](https://github.com/urho3d/SDL-mirror/tree/release-2.0.4-modified-for-urho3d). Note the last commit in this branch may or may not be equal to the last commit we made for SDL library in Urho3D project source tree. So the answer to your question, we are using a modified version of SDL 2.0.4 at the moment.

-------------------------

djmig | 2017-01-02 01:14:22 UTC | #3

I understand; as others under ThirdParty.
Thank you

-------------------------

