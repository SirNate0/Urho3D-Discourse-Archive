whtemple1959 | 2018-11-04 04:04:57 UTC | #1

re-posted from  erroneously posting in "Showcase"

I got these errors when making ...
Could NOT find Readline development library (missing:  READLINE_LIBRARIES READLINE_INCLUDE_DIRS) 
Could NOT find Esound development library (missing:  ESOUND_LIBRARIES ESOUND_INCLUDE_DIRS) 
Could NOT find aRts development library (missing:  ARTS_LIBRARIES ARTS_INCLUDE_DIRS) 
Could NOT find NetworkAudioSystem development library (missing:  NAS_LIBRARIES NAS_INCLUDE_DIRS) 
Could NOT find RoarAudio development library (missing:  SNDIO_LIBRARIES SNDIO_INCLUDE_DIRS) 
Could NOT find Wayland display server (missing:  WAYLAND_CLIENT WAYLAND_SCANNER WAYLAND_CURSOR WAYLAND_EGL EGL XKB WAYLAND_INCLUDE_DIRS WAYLAND_CORE_PROTOCOL_DIR WAYLAND_PROTOCOLS_DIR) 
Configuring done
should I go ahead and complete the install or should I abort and ...
Do I need to hunt them down, install them, and re-make?

-------------------------

weitjong | 2018-11-04 04:15:12 UTC | #2

No, you are good to go. You don't need all the display and sound servers, unless you really want to. You will probably want to install libreadline6-dev, if you want to use Lua interpreter or isql host tool later. Those tools would be built without Readline too but you will not able to "edit" command line from history in the tool. Good luck.

-------------------------

whtemple1959 | 2018-11-05 15:25:14 UTC | #3

Thank you weitjong for the advice
stay tuned I am organizing a new post that you may be interested in

-------------------------

