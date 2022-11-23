OMID-313 | 2017-01-02 01:14:52 UTC | #1

Hi all,

Developers suggested me to install version 1.5 on RPi ([topic2447.html](http://discourse.urho3d.io/t/keyboard-keys-not-working-on-rpi-platform/2335/1)).
But after I installed it, I receive the following error every time I try to run an example:

[code]. . .
libEGL warning: DRI2: failed to authenticate
ERROR: Could not create window, root cause: 'Could not create GLES window surface'[/code]

So, what should I do !?

-------------------------

OMID-313 | 2017-01-02 01:14:52 UTC | #2

Ok, I found the solution from the FAQ of Pi3D here:
[pi3d.github.io/html/FAQ.html#gl ... thenticate](https://pi3d.github.io/html/FAQ.html#glx-dri2-not-supported-or-failed-to-authenticate)

--------------------------------------------------------

[b][u]GLX DRI2 not supported or failed to authenticate[/u][/b]

When I try and run the demos I just get a load of error messages such as libEGL warning: GLX/DRI2 is not supported/failed to authenticate etc

    The chances are this is because ?something? (such as gedit) has installed mesa which added its own versions of libEGL and libGLESv2. If you run:

[code]    $ sudo find / -name libEGL*
    $ sudo find / -name libGLESv2*[/code]

    on the Raspberry Pi you should just get /opt/vc/lib/libEGL.so and /opt/vc/lib/libGLESv2.so if other ones turn up i.e. /usr/lib/arm-linux-gnueabihf/libEGL.so.1 you could try creating symbolic links for them all like this:

[code]    $ sudo ln -fs /opt/vc/lib/libEGL.so /usr/lib/arm-linux-gnueabihf/libEGL.so
    $ sudo ln -fs /opt/vc/lib/libEGL.so /usr/lib/arm-linux-gnueabihf/libEGL.so.1
    $ sudo ln -fs /opt/vc/lib/libGLESv2.so /usr/lib/arm-linux-gnueabihf/libGLESv2.so
    $ sudo ln -fs /opt/vc/lib/libGLESv2.so /usr/lib/arm-linux-gnueabihf/libGLESv2.so.2[/code]

--------------------------------------------------------

-------------------------

