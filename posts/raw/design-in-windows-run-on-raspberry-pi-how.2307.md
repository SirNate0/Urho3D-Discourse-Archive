OMID-313 | 2017-01-02 01:14:37 UTC | #1

Hi everyone,

I'm trying to design a very simple project on Raspberry Pi, which is rotating a 3D object by USB mouse or joystick.
But I don't want to design and compile the project in RPi because of its limited resources.
I want to design the project in Windows platform, and compile it for armv7 (right?) so that I can run it in RPi.

Now, here are my questions:

1. What do I have to install in Windows so as to be able to design/compile the project?
2. What libraries, packages, and dependencies have to be installed in RPi, so as to be able to run the game?
3. Are there simple examples of similar projects? So that I can learn the basics?

Thanks a lot.
Your time and help are highly appreciated.

-------------------------

weitjong | 2017-01-02 01:14:37 UTC | #2

Welcome to our forum. 

Although in theory it is possible, our build system currently does not support cross-compiling targeting Raspberry Pi platform on a Windows build/host system.

-------------------------

OMID-313 | 2017-01-02 01:14:37 UTC | #3

[quote="weitjong"]Welcome to our forum. 

Although in theory it is possible, our build system currently does not support cross-compiling targeting Raspberry Pi platform on a Windows build/host system.[/quote]

Thanks @weitjong for your reply.

I can run Ubuntu on VMware on windows.
Is it possible to cross-compile in Ubuntu targeting Raspberry Pi ?

-------------------------

weitjong | 2017-01-02 01:14:37 UTC | #4

Yes, that is definitely possible. See [urho3d.github.io/documentation/ ... aspberryPi](https://urho3d.github.io/documentation/HEAD/_building.html#Building_RaspberryPi) for more detail.

-------------------------

OMID-313 | 2017-01-02 01:14:37 UTC | #5

[quote="weitjong"]Yes, that is definitely possible. See [urho3d.github.io/documentation/ ... aspberryPi](https://urho3d.github.io/documentation/HEAD/_building.html#Building_RaspberryPi) for more detail.[/quote]

Thanks again @weitjong for your reply.

Just one more question:
Is there a clean and easy way to install Urho3D on Ubuntu? Something like [i]apt-get install urho3d[/i] and that's done!
What is the easiest way to install and run Urho3D on Ubuntu !?

-------------------------

weitjong | 2017-01-02 01:14:37 UTC | #6

There is prebuilt Urho3D binary in the deb format so you can use "dpkg -i /path/to/deb/file" to install it. Having said that, that is usually not you want especially when you are just getting started in learning 3D game programming or any software programming in general. You are better off compiling it from source. Additionally Urho3D is not an end product, it is just a library. One way or another you still need to get over the hurdle to set up a build environment  where you can start developing/designing your game. The link I gave you earlier only contains information specific to Urho3D library building. There are a few essential development packages that you need to install that are not listed there, especially when you just got yourself a stock Ubuntu installation. Something like "build-essential" and package providing an OpenGL API implementation. Good luck.

-------------------------

OMID-313 | 2017-01-02 01:14:37 UTC | #7

[quote="weitjong"]There is prebuilt Urho3D binary in the deb format so you can use "dpkg -i /path/to/deb/file" to install it. Having said that, that is usually not you want especially when you are just getting started in learning 3D game programming or any software programming in general. You are better off compiling it from source. Additionally Urho3D is not an end product, it is just a library. One way or another you still need to get over the hurdle to set up a build environment  where you can start developing/designing your game. The link I gave you earlier only contains information specific to Urho3D library building. There are a few essential development packages that you need to install that are not listed there, especially when you just got yourself a stock Ubuntu installation. Something like "build-essential" and package providing an OpenGL API implementation. Good luck.[/quote]

Thanks @weitjong for your advice.

I followed the instructions from here ([github.com/urho3d/Urho3D/wiki/G ... d-in-Linux](https://github.com/urho3d/Urho3D/wiki/Getting-started-in-Linux)) to install Urho3D on Ubuntu (on VMware on Windows!).

Everything went fine, until this error:
/usr/bin/ld: cannot find -lGL

I searched a lot, and tried to install libgl by apt-get install libgl but it cannot locate it.
I tried libgl1, libgl1-mesa-glx but none worked.

What is the correct way of installing libgl?

(My GPU is NVidia GeForce 9400 GT)

-------------------------

OMID-313 | 2017-01-02 01:14:37 UTC | #8

The following solved the problem:

sudo apt-get install libgl1-mesa-dev

-------------------------

OMID-313 | 2017-01-02 01:14:38 UTC | #9

[quote="weitjong"]There is prebuilt Urho3D binary in the deb format so you can use "dpkg -i /path/to/deb/file" to install it. Having said that, that is usually not you want especially when you are just getting started in learning 3D game programming or any software programming in general. You are better off compiling it from source. Additionally Urho3D is not an end product, it is just a library. One way or another you still need to get over the hurdle to set up a build environment  where you can start developing/designing your game. The link I gave you earlier only contains information specific to Urho3D library building. There are a few essential development packages that you need to install that are not listed there, especially when you just got yourself a stock Ubuntu installation. Something like "build-essential" and package providing an OpenGL API implementation. Good luck.[/quote]

Dear @weitjong, I encountered a new problem.

Please see my new post on it:

[topic2420.html](http://discourse.urho3d.io/t/error-no-opengl-support-in-video-driver/2308/1)

Thanks for your time and support.

-------------------------

Alexander | 2017-01-02 01:15:24 UTC | #10

Hi,

We do exactly that, program and debug i Visual studio (2012 i think...), and cross compile on our windows machines, but actually run the code on the Raspberry Pi.

The compiled files are sent to the Pi, and i can have breakpoints and step in the code like normally.
This is done with the help of VisualGDB, a plugin(?) to visual studio.

I cant tell you how its done, because its wery complicated and beond my understanding. My companies tech guy sat it up.
It works mostly fine, but there are issues with intellisense simetimes, and cashed versions of source code can give you surprises sometimes.

If this sounds intresting I could ask our expert to give a short explenation of the components and how they are sat up.

Sincerely

-------------------------

Sir_Nate | 2017-01-02 01:15:25 UTC | #11

You can try the tool chain from [url]http://gnutoolchains.com/raspberry/tutorial/[/url] if you want to compile directly from Windows - I've used it for other things, though I'm not certain I ever tried Urho with it. Now I use Ubuntu, and I find it's much easier...

-------------------------

