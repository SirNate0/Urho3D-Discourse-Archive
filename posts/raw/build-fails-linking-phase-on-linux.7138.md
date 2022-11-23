jasperry | 2022-01-20 03:08:29 UTC | #1

Hi, build on 64-bit Arch fails for me in the linking phase with these errors:

```
/usr/bin/ld: ../../../lib/libUrho3D.a(SDL_waylandvideo.c.o): in function `Wayland_VideoInit':
SDL_waylandvideo.c:(.text+0x674): undefined reference to `wl_proxy_get_version'
/usr/bin/ld: SDL_waylandvideo.c:(.text+0x693): undefined reference to `wl_proxy_marshal_flags'
```
I have Wayland 1.20 installed and I'm pretty sure its include files are being found, or else the error would be earlier. My best guess is that the makefiles are missing a libwayland-client.so reference, but I don't understand CMake enough to fix it. Thanks for any ideas.

-------------------------

dertom | 2022-01-20 09:33:49 UTC | #2

Hi and welcome,
I had the same problem on my arch based linux distro. And afaik I deactivated 'VIDEO_WAYLAND' in cmake(gui) and afterwards it worked....
greets
![image|627x104, 50%](upload://7HWPq5aHr5w8ZFFxKG4IeW7Smfr.png)

-------------------------

jasperry | 2022-01-20 21:02:27 UTC | #3

Yes, that worked, thanks very much! And now I know there's a GUI for CMake :slight_smile:

-------------------------

lebrewer | 2022-01-21 15:27:41 UTC | #4

That seems to be related to SDL. If you replace the SDL within Urho with the latest version (2.0.20), the error should go away. But only if you really want Wayland. Fuck wayland.

-------------------------

