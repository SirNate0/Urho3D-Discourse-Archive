Alex | 2017-01-02 00:59:48 UTC | #1

Hi,

Is there a way to start Urho3D without X Window System on raspberry pi ?  

[code]
pi@raspberrypi ~/alex/Urho3D/Bin $ ./23_Water
[Wed Jul 16 09:41:38 2014] INFO: Opened log file /home/pi/.local/share/urho3d/logs/Water.log
[Wed Jul 16 09:41:38 2014] INFO: Added resource path /home/pi/alex/Urho3D/Bin/CoreData/
[Wed Jul 16 09:41:38 2014] INFO: Added resource path /home/pi/alex/Urho3D/Bin/Data/
libEGL warning: DRI2: xcb_connect failed
libEGL warning: DRI2: xcb_connect failed
libEGL warning: GLX: XOpenDisplay failed
[Wed Jul 16 09:41:38 2014] ERROR: Could not open window
[/code]

Thanks,
Alex

-------------------------

weitjong | 2017-01-02 00:59:48 UTC | #2

Welcome to our forum.

Our Urho3D port on Raspberry Pi platform does not require X11 since day one. There could be other reasons why you see that error in the log. It has been awhile since I last tried Urho3D samples on Raspberry Pi and not all the samples work accordingly on Raspberry Pi platform then due to its GPU hardware and/or OpenGL ES implementation limitation, but it should not produce "Could not open window" error in the log if I recall correctly. Need to investigate later when I have time.

-------------------------

Alex | 2017-01-02 00:59:48 UTC | #3

Thanks, can it be related to how much RAM is dedicated to the GPU ?

-------------------------

weitjong | 2017-01-02 00:59:48 UTC | #4

I think it is unlikely that is the cause, however, it is recommended to allocate at least 128MB RAM to GPU as per our documentation, if you have not done so.

-------------------------

Alex | 2017-01-02 00:59:49 UTC | #5

This fixed my problem, apparently package conflict. Someone more knowledgeable may propose more elegant solution.

[code]
sudo ln -fs /opt/vc/lib/libEGL.so /usr/lib/libEGL.so
sudo ln -fs /opt/vc/lib/libEGL.so /usr/lib/arm-linux-gnueabihf/libEGL.so
sudo ln -fs /opt/vc/lib/libEGL.so /usr/lib/arm-linux-gnueabihf/libEGL.so.1
sudo ln -fs /opt/vc/lib/libGLESv2.so /usr/lib/libGLESv2.so
sudo ln -fs /opt/vc/lib/libGLESv2.so /usr/lib/arm-linux-gnueabihf/libGLESv2.so
sudo ln -fs /opt/vc/lib/libGLESv2.so /usr/lib/arm-linux-gnueabihf/libGLESv2.so.2
sudo ln -fs /opt/vc/lib/libbcm_host.so /usr/lib/libbcm_host.so
sudo ln -fs /opt/vc/lib/libbcm_host.so /usr/lib/arm-linux-gnueabihf/libbcm_host.so
sudo ln -fs /opt/vc/lib/libvchiq_arm.so /usr/lib/libvchiq_arm.so
sudo ln -fs /opt/vc/lib/libvchiq_arm.so /usr/lib/arm-linux-gnueabihf/libvchiq_arm.so
sudo ln -fs /opt/vc/lib/libvcos.so /usr/lib/libvcos.so
sudo ln -fs /opt/vc/lib/libvcos.so /usr/lib/arm-linux-gnueabihf/libvcos.so
[/code]

-------------------------

weitjong | 2017-01-02 00:59:49 UTC | #6

I am the maintainer of the Urho3D port for Raspberry Pi. I have tested both Raspbian and Pidora in the past and they both work. I don't recall setting up any symlinks manually in order to get Raspbian to work. Our FindBCM_VC.cmake module should be able to find the VideoCore "driver" for both Raspbian in /opt/vc and Pidora in /usr/lib; and use the found paths as appropriately when building the software. Not sure why you need those symbolic links in /usr/lib pointing back to /opt/vc/lib in your Raspbian, but your problem could be just a runtime issue. Can you post the result of "ldd 23_Water". Pay attention to the location of the shared library dependencies in the output. If the location is not proper then a wrong shared library (not from VideoCore) may get invoked instead (probably like in your case) or you get a missing lib error. To prevent such issues, ensure that your system has an up-to-date /etc/ld.so.cache to the most recent shared library list. Use "ldconfig" command to check the list or to create a new one. Make sure you have a file called 00-vmcs.conf in the /etc/ld.so.conf.d directory before doing the latter. I think this is the configuration file to make shared libs from VC to be listed on top in the cache. Hope this help. BTW, glad to hear you get it working regardless.

-------------------------

