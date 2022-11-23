OMID-313 | 2017-01-02 01:14:45 UTC | #1

Hi all,
I attempted several times to install Urho3D on RPi, which failed.
Finally, I reinstalled Raspbian Jessie OS.
Then reinstalled Urho3D with the following method(with RPi's experimental OpenGL disabled, and GPU=768 MB.) :

[code]sudo apt-get update
sudo apt-get install build-essential
sudo apt-get install freeglut3 freeglut3-dev
sudo apt-get install unixodbc-dev

sudo apt-get install libevdev2

sudo apt-get install libasound2-dev
sudo apt-get install libaudio-dev
sudo apt-get install libesd0-dev
sudo apt-get install libpulse-dev
sudo apt-get install libroar-dev
sudo apt-get install libreadline6-dev

sudo apt-get install git cmake make

sudo git clone https://github.com/urho3d/Urho3D
cd Urho3D
sudo ./cmake_rpi.sh /home/pi/Urho3D
sudo make[/code]

Now after installation, when I run ./Urho3DPlayer , it gives the following error:

[code][Thu Oct 13 10:56:17 2016] INFO: Opened log file /home/pi/.local/share/urho3d/logs/NinjaSnowWar.as.log
[Thu Oct 13 10:56:17 2016] INFO: Created 3 worker threads
[Thu Oct 13 10:56:17 2016] INFO: Added resource path /home/pi/Urho3D/bin/Data/
[Thu Oct 13 10:56:17 2016] INFO: Added resource path /home/pi/Urho3D/bin/CoreData/
[Thu Oct 13 10:56:17 2016] INFO: Added resource path /home/pi/Urho3D/bin/Autoload/LargeData/
[Thu Oct 13 10:56:17 2016] ERROR: Could not create window, root cause: 'Could not initialize OpenGL / GLES library'[/code]

What is the problem !!?
How can I successfully get Urho3D to work on RPi !!!?!?!?!?

-------------------------

GSpub64 | 2017-01-02 01:14:46 UTC | #2

The error is telling you that OpenGL wasn't able to initialize. I think might be because of the:

[quote]Then reinstalled Urho3D with the following method([u][i][b]with[/b][/i][/u] RPi's experimental [u][i][b]OpenGL disabled[/b][/i][/u], and GPU=768 MB.) :[/quote]

I haven't a Rasberry Pi yet so this is a stab in the dark but now that you have Urho3D installed, try enabling the RPi's experimental OpenGL feature and see if it starts.

-------------------------

weitjong | 2017-01-02 01:14:47 UTC | #3

Our RPI port has only be built and tested using GLES at the moment. Personally I haven't tried it with OpenGL yet, so I have no idea whether it will work with OpenGL.

-------------------------

OMID-313 | 2017-01-02 01:14:47 UTC | #4

[quote="weitjong"]Our RPI port has only be built and tested using GLES at the moment. Personally I haven't tried it with OpenGL yet, so I have no idea whether it will work with OpenGL.[/quote]

Thanks @weitjong for your reply.
But I don't want to use OpenGL. I just want to run Urho3D ! That's it !!
So, what is my system's problem !?
Please help me solve this.  :cry:

-------------------------

weitjong | 2017-01-02 01:14:48 UTC | #5

It is easier to verify that you have a working build environment by first test building a simple GLES project instead of using Urho3D. I did that when I first got my RPI. After you know for sure you can build a simple project then come back to retry to build Urho3D project. It has been awhile since the last time I build it natively on the board itself, to tell you the truth. I may try that later when I have time on my newer RPI 3. Usually just cross-compile on a Linux host and scp to the board for actual testing. I am not sure what went wrong with your build environment, but this is how I setup mine.

[ul][li]For cross-compiling: just follow the steps as outlined in [urho3d.github.io/documentation/ ... aspberryPi](https://urho3d.github.io/documentation/HEAD/_building.html#Building_RaspberryPi). The section of the text is contributed by me, so it exactly outlines what I did.[/li]
[li]For native build on the board: install the prerequisite software as root and then build Urho3D as normal user (I hope I won't catch you using root again, I cannot stand such mistake :wink: and may opt to not respond at all and let others to help you). After calling cmake, verify the generated build tree contains this file: <your-build-tree>/Source/ThirdParty/SDL/include/generated/SDL_config.h and verify this file contains entries that indicate SDL has detected the video driver for RPI and OpenGL ES 1 and 2. If not then install the missing prerequisite package and rinse & repeat, each time deleting the previously generated build tree first when you are reusing a same build tree path.[/li][/ul]

-------------------------

OMID-313 | 2017-01-02 01:14:48 UTC | #6

[quote="weitjong"]It is easier to verify that you have a working build environment by first test building a simple GLES project instead of using Urho3D. I did that when I first got my RPI. After you know for sure you can build a simple project then come back to retry to build Urho3D project. It has been awhile since the last time I build it natively on the board itself, to tell you the truth. I may try that later when I have time on my newer RPI 3. Usually just cross-compile on a Linux host and scp to the board for actual testing. I am not sure what went wrong with your build environment, but this is how I setup mine.

[ul][li]For cross-compiling: just follow the steps as outlined in [urho3d.github.io/documentation/ ... aspberryPi](https://urho3d.github.io/documentation/HEAD/_building.html#Building_RaspberryPi). The section of the text is contributed by me, so it exactly outlines what I did.[/li]
[li]For native build on the board: install the prerequisite software as root and then build Urho3D as normal user (I hope I won't catch you using root again, I cannot stand such mistake :wink: and may opt to not respond at all and let others to help you). After calling cmake, verify the generated build tree contains this file: <your-build-tree>/Source/ThirdParty/SDL/include/generated/SDL_config.h and verify this file contains entries that indicate SDL has detected the video driver for RPI and OpenGL ES 1 and 2. If not then install the missing prerequisite package and rinse & repeat, each time deleting the previously generated build tree first when you are reusing a same build tree path.[/li][/ul][/quote]

Thanks @weitjong for your reply.

I solved the problem !!
First I did:
[code]sudo apt-get remove mesa-common-dev[/code]
Then reinstalled Urho3D.
Now it works.

Now I have another problem(!!!) which I described here:
[topic2447.html](http://discourse.urho3d.io/t/keyboard-keys-not-working-on-rpi-platform/2335/1)

-------------------------

cnx_coder | 2017-01-02 01:14:49 UTC | #7

[quote]
I solved the problem !!
First I did:
[code]sudo apt-get remove mesa-common-dev[/code]
Then reinstalled Urho3D.
Now it works.
[/quote]

i've been following this thread over the weekend and have had the same errors. removing mesa-common-dev also worked for me.

thanks for all effort.  :smiley:

-------------------------

OMID-313 | 2017-01-02 01:14:52 UTC | #8

[quote="cnx_coder"][quote]
I solved the problem !!
First I did:
[code]sudo apt-get remove mesa-common-dev[/code]
Then reinstalled Urho3D.
Now it works.
[/quote]

i've been following this thread over the weekend and have had the same errors. removing mesa-common-dev also worked for me.

thanks for all effort.  :smiley:[/quote]

It's nice to hear that this issue is common among RPi users.
Maybe Urho3D developers can think about a workaround.

Also, I've faced another issue described here: [topic2447.html](http://discourse.urho3d.io/t/keyboard-keys-not-working-on-rpi-platform/2335/1)
Do you have the same issue !!?

-------------------------

