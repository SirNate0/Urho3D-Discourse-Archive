Kinth | 2017-01-02 01:13:51 UTC | #1

Hi, 

I have made a build for the Raspberry Pi cross compiling from Ubuntu. The builds complete with no errors and run on the R Pi (and surprisingly well, though I have only tried the first few samples) , the problem is they don't seem to detect input. The input is still interacting with the desktop behind the sample. Has anyone come across this before and know how to fix it?

P.S I am fairly new to builds, toolchains and linux in general. So I am a bit out of my depth (it took me nearly a day to get the cross compile working to begin with :stuck_out_tongue:). So any starter guides on this stuff would be welcome!

-------------------------

codingmonkey | 2017-01-02 01:13:52 UTC | #2

Yes, I have same problem (have tested a month+ ago). Input on rpi3 not working and I don't known why )

-------------------------

Kinth | 2017-01-02 01:13:52 UTC | #3

Probably worth mentioning that I have a Raspberry pi 2B

-------------------------

weitjong | 2017-01-02 01:13:52 UTC | #4

I have not tested RPI build on my actual RPI board for quite some time. My old RPI is now being used as a poor man's server at home and I don't have another spare. There are two reasons I can think of why you have this problem.
[ol][li]General case. The build could probably be broken since SDL 2.0.4 upgrade. After the upgrade our build system now auto detects and configures the SDL configuration file. So, it may have wrongly configured it. If that is the case then I think you can test to recover it by using the SDL_config for linux platform (SDL_config_linux.h) that we used to have in older release tag.[/li]
[li]Specific case. It can also be just specific problem to your OS configuration. Our RPI port does not require X11, so you need to configure your OS to boot into text mode instead of graphic mode.[/li][/ol]
Hope this help.

-------------------------

weitjong | 2017-01-02 01:13:53 UTC | #5

I just got my hand on a brand new RPI 3 model B. I am eager to test it in the next few days when I have time.

-------------------------

