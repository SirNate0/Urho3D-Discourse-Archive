godan | 2017-01-02 01:13:47 UTC | #1

I'm working on getting OpenHMD integrated with Urho. Progress so far:

- CMake build system for linking OpenHMD and hidapi into a Urho app.
- Ported the Oculus Manager from the OpenHMD Ogre demo
- Ported the Oculus shader
- Created a renderpath for Oculus rendering.

Baby steps... :slight_smile: Here's a screen shot of a totally boring test scene...

[img]https://dl.dropboxusercontent.com/u/69779082/UrhoVR_1.png[/img]

Also, a quick question: does anyone know how OpenHMD transfers the frame buffers to the device? Does it just "know" about the window it's being called from? There doesn't seem to be anything in the update loop about pushing textures....I'm sure it works, I'd just like to understand how this works.

-------------------------

TheOnlyJoey | 2017-01-02 01:15:18 UTC | #2

Hey, just saw this forum post on my radar, I am one of the OpenHMD developers.
Don't know if you are still working on this, but I could give you some insights.

OpenHMD has drivers which decipher the usb packets from the devices and turn them into usable data.
We construct GL Matrices (Projection and Modelview) and provide quaternion data among others.
openhmd.net/doxygen/0.1.0/openhmd_8h.html has most of the calls and information about what you can get from the devices.
More will be added in the future.

You set information FROM the device TO your application, there is no communication back to the device currently.
Since we do not handle things like 'direct mode' yet, you just have to open the render window on the HMD or drag it manually.

If you have any additional questions feel free to respond, join our irc (freenode #openhmd) or hang on our subreddit! /r/openhmd.

-------------------------

sabotage3d | 2017-01-02 01:15:18 UTC | #3

Would there be full support for HTC Vive soon? I saw it was added recently but only for rotations.

-------------------------

godan | 2017-01-02 01:15:19 UTC | #4

Hey thanks! As it happens, I'm just getting back in to this code, so your response was well timed :slight_smile:

So, Direct Mode would be amazing! Is that a big job?

-------------------------

TheOnlyJoey | 2017-01-02 01:15:23 UTC | #5

[quote="sabotage3d"]Would there be full support for HTC Vive soon? I saw it was added recently but only for rotations.[/quote]
As currently everything is reverse engineering work, and we do this in our free time (not enough donations and support yet for part/full time development) this will take a while.

[quote="godan"]Hey thanks! As it happens, I'm just getting back in to this code, so your response was well timed :slight_smile:

So, Direct Mode would be amazing! Is that a big job?[/quote]

Great to hear!
Things like 'Direct Mode' are still locked by GPU vendors to a select group of people, we are working with 'a vendor' for support in the future but we have yet to acquire support from the others. On FreeBSD, Linux and Mac OSX there is no implementation yet for direct mode, so on these platforms it does not matter.
For Windows, extended works well enough as well.

-------------------------

godan | 2017-06-21 13:20:45 UTC | #6

Progress! 
https://youtu.be/rhEHVI7NGQ4

-------------------------

madscientist42 | 2017-12-17 18:27:04 UTC | #7

As an observation, it's my understanding that Direct Mode is stock, exposed on Vulkan- and if you're doing SteamVR stuff on Linux with the Vive, you only HAVE Vulkan as an option...

https://vulkan.lunarg.com/doc/view/1.0.30.0/linux/vkspec.chunked/ch29s03.html

-------------------------

