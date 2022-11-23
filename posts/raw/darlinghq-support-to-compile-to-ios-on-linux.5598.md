kapsloki | 2019-09-19 10:48:44 UTC | #1

DarlingHQ is a WineHQ clone for MacOSX and it can run XCode without GUI

https://wiki.darlinghq.org/build_instructions

https://github.com/darlinghq/darling

-------------------------

weitjong | 2019-09-19 14:54:19 UTC | #2

This is a great find. Thanks for the link.

-------------------------

kapsloki | 2019-09-19 20:08:20 UTC | #3

You're welcome. :slight_smile:
I hope this discovery help the engine.

-------------------------

weitjong | 2019-09-22 05:23:33 UTC | #4

I am able to build everything in the first try on a Docker container. It took quite some time on my old rig. However, I cannot get it to work on a container yet due to its requirement to have a custom kernel module built too. If I understood it correctly this kernel module needs to be built on the host. My intention is to integrate this into my "dockerized" project so that I can build Urho3D project (and any of its downstream projects) to target the Apple platforms as well using Docker container. Currently using DBE (Dockerized Build Environment) I can pretty much target all the platforms officially supported by Urho3D, except Apple ones. I am hoping this will fill the gap.

There is other people who try to use Darling in a container as well. I found this project after a quick internet search.

https://github.com/utensils/docker-darling

It is a MIT license project. I hope it will jump start my own experiment with Darling. It will be a perfect test for my new rig (Ryzen 7) arriving next week too.

-------------------------

kapsloki | 2019-09-22 12:12:48 UTC | #5

Any links for your .Dockerfile? Or not yet? Or never?

-------------------------

weitjong | 2019-09-22 16:02:10 UTC | #6

Not sure what you are asking. If it is the Dockerfile for the new docker Darling image then you will have to wait. I have just barely started the experiment. But when/if it is ready then I will share it in the "dockerized" project which I mentioned earlier. This project is also MIT license and it is currently being used by Urho3D CI. Check out the ".travis.yml" if you haven't done so.

-------------------------

