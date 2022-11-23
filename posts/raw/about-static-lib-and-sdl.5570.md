brojonisbro | 2019-09-13 02:20:14 UTC | #1

hey guys, im here just for 3 questions

simple question:
SDL here is SDL or SDL2?

important question:
i'm planning create a game just with data.pak and a binary
static libraries on urho3d normally need others libraries? urho3d is dependent?

for example: when using a SDL2 static library (libSDL2.a | libSDL2main.a) compiled by source code, when compiling, we need link libraries and headers (include?), no just for OpenGL (-lGL) but for... -lm -llibsnd(sdl standard audio) and it make too much work cause if we wanna make just a complete binary, is needed compile other libraries statically by source code too

its possible just compile "one time" urho3d? just linking libs and headers of the static folder?

third:
its possible unit all platform static libraries to make a easy cross-platform game like gradlew of java? using gcc (gnulinux), mingw64(windows), osxcross(macosx) and android-gcc-toolchain(android)

muchas gracias

@edited to 3 questions more detailed question

-------------------------

Leith | 2019-09-13 02:20:21 UTC | #2

1: it's SDL2 - but typically we'll never need to touch SDL directly when working with Urho.
2: Urho's static lib embeds a copy of the third-party libs, except for a small handful (GL, GLU, GLEW, and threading support) so you don't need to mess around linking all the third party stuff. Yes, you just compile it "one time", typically speaking
3: I've only used Urho on Windows and Linux so far, so I can only speak for those two - in this case, we simply run CMAKE on the target platform, and rebuild the Urho lib (and build folder) for each target. I have not attempted to automate the process for multiplatform batched compile, though I have some ideas about how that might be done too.

In regard to .pak files, don't forget to enable that option when configuring CMAKE - Urho does support file packaging, but it's disabled by default.

-------------------------

Modanung | 2019-09-13 09:27:15 UTC | #3

@brojonisbro Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

brojonisbro | 2019-09-15 22:39:11 UTC | #4

Thanks @Modanung! :slight_smile:

-------------------------

kapsloki | 2019-09-19 10:15:41 UTC | #5

@Leith "3": And what would your ideas of how to do that?

-------------------------

Leith | 2019-09-20 07:01:52 UTC | #6

One concept would be to use scripting to drive VirtualBox, and within each virtual machine, execute a suitable batch file. Another would be to farm the work out to LAN machines of various platform, using a common local SQL server to provide the platform specifics, although that would require a simple crossplatform build tool to be written.

https://www.praim.com/en/virtualbox-scripting-tutorial-2/ seems a more likely route.

-------------------------

