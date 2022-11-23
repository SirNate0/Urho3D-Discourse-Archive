pilesofspam | 2020-10-16 17:11:12 UTC | #1

Ubuntu 18.04 LTS, this is the image that Nvidia puts up on the website.

Basically, I followed the build instructions, and used cmake_arm.sh ./build to set up build as my build directory.  When I attempted to make, I received a lot of errors that broke down to this file:
~/Urho3D-1.7.1/build/include/Urho3D/ThirdParty/AngelScript/wrap16.h

The errors resulted from this line:
#define WRAP_OBJ_LAST(name)       (::gw::id(name).TMPL ol< name >())

Right above that there's a note about using the template keyword.  Here's your hint!  It should ultimately be:
#define TMPL template

My GCC is:
gcc (Ubuntu/Linaro 7.5.0-3ubuntu1~18.04) 7.5.0

Now everything is working great.  I didn't find any reference to this while searching for an answer, so I hope this helps someone.

-------------------------

vmost | 2020-10-17 00:24:07 UTC | #2

What did you do exactly? Did you edit the wrap16.h file?

-------------------------

pilesofspam | 2020-10-17 12:32:18 UTC | #3

Yes, I edited wrap16.h.   You'll see some conditional compiles near the end that define TMPL based on your GCC version.  I just commented out all of that and just made it:

#define TMPL template

^ that is one of the options, but it only decides up to GCC 5 or so.  If you're inclined you could probably just fix the conditional compile to include this for > 5.

-------------------------

weitjong | 2020-10-17 12:39:34 UTC | #4

In the master branch we have it corrected already. 

https://github.com/urho3d/Urho3D/commit/c6ea0d61cacbda5a25a5ec82601a87240e69fb0e

-------------------------

