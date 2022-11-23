NinjaPangolin | 2017-10-27 13:15:12 UTC | #1

I decided to try out Urho3d engine, so the first thing I did was downloading git repository, compiling it and then checking out provided samples. Then I saw that 19_VehicleDemo doesn't have any textures and looks like that:

![dsadfsfdsfdsfds|646x500](upload://aHojsTnmRJhCDMbVtAjoZzZe8fk.png)

What am I doing wrong? I use Lubuntu.

    ~/Urho3D/build/bin $ ./19_VehicleDemo 
    [Fri Oct 27 15:11:05 2017] INFO: Opened log file /home/mariusz/.local/share/urho3d/logs/VehicleDemo.log
    [Fri Oct 27 15:11:05 2017] INFO: Created 1 worker thread
    [Fri Oct 27 15:11:05 2017] INFO: Added resource path /home/mariusz/Pobrane/Urho3D/build/bin/Data/
    [Fri Oct 27 15:11:05 2017] INFO: Added resource path /home/mariusz/Pobrane/Urho3D/build/bin/CoreData/
    [Fri Oct 27 15:11:05 2017] INFO: Added resource path /home/mariusz/Pobrane/Urho3D/build/bin/Autoload/LargeData/
    [Fri Oct 27 15:11:05 2017] INFO: Set screen mode 1024x768 windowed monitor 0
    [Fri Oct 27 15:11:05 2017] INFO: Initialized input
    [Fri Oct 27 15:11:05 2017] INFO: Initialized user interface
    [Fri Oct 27 15:11:05 2017] INFO: Initialized renderer
    [Fri Oct 27 15:11:05 2017] INFO: Initialized engine
    Used resources:
    Textures/Ramp.png
    Textures/Spot.png
    Textures/FishBoneLogo.png
    Textures/UI.png
    Textures/TerrainWeights.dds
    Textures/TerrainDetail1.dds
    Textures/TerrainDetail2.dds
    Textures/TerrainDetail3.dds
    Textures/Mushroom.dds
    Textures/StoneDiffuse.dds
    Textures/StoneNormal.dds
    Techniques/NoTexture.xml
    Techniques/TerrainBlend.xml
    Techniques/Diff.xml
    Techniques/DiffNormal.xml
    RenderPaths/Forward.xml
    UI/DefaultStyle.xml
    Textures/UrhoIcon.png
    Textures/HeightMap.png
    Fonts/Anonymous Pro.ttf
    Materials/Terrain.xml
    Materials/Mushroom.xml
    Materials/Stone.xml
    Models/Mushroom.mdl
    Models/Box.mdl
    Models/Cylinder.mdl
    Shaders/GLSL/Shadow.glsl
    Shaders/GLSL/LitSolid.glsl
    Shaders/GLSL/TerrainBlend.glsl
    Shaders/GLSL/Basic.glsl

-------------------------

Eugene | 2017-10-27 13:22:39 UTC | #2

What about other demos?
Hardware? OS?

-------------------------

NinjaPangolin | 2017-10-27 13:37:49 UTC | #3

Some demos seems to be rendered correctly and some not. 23_Water looks very bad. In 18_CharacterDemo only character is rendered correctly:

![dsadfsfdsfdsfds|649x500](upload://9QYcX3NK2SzVNrnRC7gNPq30l9w.png)

GUI and particle effects seems to work.

OS is Lubuntu Linux, as previously mentioned. PC is quite old, Radeon HD 4850 graphic card.

    $ sudo lshw -short
    H/W path                   Device      Class       Description
    ==============================================================
                                           system      MS-7395 (To Be Filled By O.E.M.)
    /0                                     bus         MS-7395
    /0/0                                   memory      64KiB BIOS
    /0/4                                   processor   Intel(R) Core(TM)2 Duo CPU     E7200  @ 2.53GHz
    /0/4/5                                 memory      64KiB L1 cache
    /0/4/6                                 memory      3MiB L2 cache
    /0/f                                   memory      2GiB System Memory
    /0/f/0                                 memory      DIMM [empty]
    /0/f/1                                 memory      1GiB DIMM SDRAM Synchronous
    /0/f/2                                 memory      1GiB DIMM SDRAM Synchronous
    /0/f/3                                 memory      DIMM [empty]
    /0/100                                 bridge      82G33/G31/P35/P31 Express DRAM Controller
    /0/100/1                               bridge      82G33/G31/P35/P31 Express PCI Express Root Port
    /0/100/1/0                             display     RV770 [Radeon HD 4850]
    /0/100/1/0.1                           multimedia  RV770 HDMI Audio [Radeon HD 4850/4870]
    /0/100/1a                              bus         82801I (ICH9 Family) USB UHCI Controller #4
    /0/100/1a/1                usb3        bus         UHCI Host Controller
    /0/100/1a/1/2                          input       G203 Prodigy Gaming Mouse
    /0/100/1a.1                            bus         82801I (ICH9 Family) USB UHCI Controller #5
    /0/100/1a.1/1              usb4        bus         UHCI Host Controller
    /0/100/1a.7                            bus         82801I (ICH9 Family) USB2 EHCI Controller #2
    /0/100/1a.7/1              usb1        bus         EHCI Host Controller
    /0/100/1a.7/1/3            scsi8       storage     ADATA USB Flash Drive
    /0/100/1a.7/1/3/0.0.0      /dev/sdb    disk        7775MB USB Flash Drive
    /0/100/1a.7/1/3/0.0.0/0    /dev/sdb    disk        7775MB 
    /0/100/1a.7/1/3/0.0.0/0/1  /dev/sdb1   volume      7414MiB Windows FAT volume
    /0/100/1a.7/1/4            scsi9       storage     DataTraveler 3.0
    /0/100/1a.7/1/4/0.0.0      /dev/sdc    disk        7803MB DataTraveler 3.0
    /0/100/1a.7/1/4/0.0.0/0    /dev/sdc    disk        7803MB 
    /0/100/1a.7/1/4/0.0.0/0/1  /dev/sdc1   volume      7437MiB Windows FAT volume
    /0/100/1b                              multimedia  82801I (ICH9 Family) HD Audio Controller
    /0/100/1c                              bridge      82801I (ICH9 Family) PCI Express Port 1
    /0/100/1c/0                enp2s0      network     RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
    /0/100/1c.4                            bridge      82801I (ICH9 Family) PCI Express Port 5
    /0/100/1c.4/0                          storage     JMB363 SATA/IDE Controller
    /0/100/1c.4/0.1                        storage     JMB363 SATA/IDE Controller
    /0/100/1c.5                            bridge      82801I (ICH9 Family) PCI Express Port 6
    /0/100/1c.5/0              eth0        network     RTL8111/8168/8411 PCI Express Gigabit Ethernet Controller
    /0/100/1d                              bus         82801I (ICH9 Family) USB UHCI Controller #1
    /0/100/1d/1                usb5        bus         UHCI Host Controller
    /0/100/1d.1                            bus         82801I (ICH9 Family) USB UHCI Controller #2
    /0/100/1d.1/1              usb6        bus         UHCI Host Controller
    /0/100/1d.2                            bus         82801I (ICH9 Family) USB UHCI Controller #3
    /0/100/1d.2/1              usb7        bus         UHCI Host Controller
    /0/100/1d.3                            bus         82801I (ICH9 Family) USB UHCI Controller #6
    /0/100/1d.3/1              usb8        bus         UHCI Host Controller
    /0/100/1d.7                            bus         82801I (ICH9 Family) USB2 EHCI Controller #1
    /0/100/1d.7/1              usb2        bus         EHCI Host Controller
    /0/100/1e                              bridge      82801 PCI Bridge
    /0/100/1e/0                            network     RTL8169 PCI Gigabit Ethernet Controller
    /0/100/1f                              bridge      82801IB (ICH9) LPC Interface Controller
    /0/100/1f.2                            storage     82801IB (ICH9) 2 port SATA Controller [IDE mode]
    /0/100/1f.3                            bus         82801I (ICH9 Family) SMBus Controller
    /0/100/1f.5                            storage     82801I (ICH9 Family) 2 port SATA Controller [IDE mode]
    /0/1                       scsi2       storage     
    /0/1/0.0.0                 /dev/cdrom  disk        DVD-RW  DVR-215D
    /0/2                       scsi3       storage     
    /0/2/0.0.0                 /dev/sda    disk        320GB ST3320613AS
    /0/2/0.0.0/1               /dev/sda1   volume      294GiB EXT4 volume
    /0/2/0.0.0/2               /dev/sda2   volume      4073MiB Extended partition
    /0/2/0.0.0/2/5             /dev/sda5   volume      4073MiB Linux swap / Solaris partition

-------------------------

JTippetts | 2017-10-27 14:24:28 UTC | #4

What does glxinfo tell you about your OpenGL version?

-------------------------

NinjaPangolin | 2017-10-27 14:29:25 UTC | #5

    $ glxinfo | grep 'version'
    server glx version string: 1.4
    client glx version string: 1.4
    GLX version: 1.4
        Max core profile version: 3.3
        Max compat profile version: 3.0
        Max GLES1 profile version: 1.1
        Max GLES[23] profile version: 3.0
    OpenGL core profile version string: 3.3 (Core Profile) Mesa 17.0.7
    OpenGL core profile shading language version string: 3.30
    OpenGL version string: 3.0 Mesa 17.0.7
    OpenGL shading language version string: 1.30
    OpenGL ES profile version string: OpenGL ES 3.0 Mesa 17.0.7
    OpenGL ES profile shading language version string: OpenGL ES GLSL ES 3.00

-------------------------

NinjaPangolin | 2017-10-27 20:11:00 UTC | #6

If I force using OpenGL 2 with -gl2 flag as described [here](https://discourse.urho3d.io/t/opengl-type-to-be-used/1656), textures are rendered correctly.

![dsadfsfdsfdsfds|646x500](upload://7ooZZINVIfbClXlsK3OyrJrHwkS.jpg)

So it looks like handling OpenGL version 3 is the source of the problem.

-------------------------

Eugene | 2017-10-27 20:15:05 UTC | #7

I'm afraid that if these issues are caused by GL drivers, it's unlikely to have them solved inside Urho.
However, I suggest you to check the program in any GL debugger. Urho may have some non-standard constructions that get broken.

-------------------------

NinjaPangolin | 2017-10-27 21:37:42 UTC | #8

Problem solved.

I used GL debugger, as advised above ([this one](https://www.opengl.org/sdk/tools/BuGLe/)) and I found out that engine, among other things, requires `GL_EXT_texture_compression_s3tc` extension, which I didn't have. I installed using `sudo apt-get install libtxc-dxtn-s2tc0` as described [here](https://askubuntu.com/questions/909004/dota-2-error-in-ubuntu-17-04-required-opengl-extension-gl-ext-texture-compress) and managed to run examples correctly.

Perhaps some sort of a warning when an OpenGL extension is not found could be implemented?

Thank you for help and suggestions!

-------------------------

weitjong | 2017-10-28 03:47:31 UTC | #9

I would usually not recommend to use Mesa driver, if your GPU vendor provides a better one.

-------------------------

