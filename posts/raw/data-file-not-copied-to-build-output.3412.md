behindcurtain3 | 2017-08-02 18:16:54 UTC | #1

Hello, I seem to be having a recurring problem with files in the bin/Data folder not always being updated/copied to the build output bin/Data folder.

I'm using Visual Studio 2017. When I add a new file to the bin/Data folder, the first time I run a build it copies it to the output. However, if I edit the file further the changes aren't copied. If I manually copy the file the ResourceCache can't find it, even though it is in the same place as the previous file it could find. I also tried creating a symlink but then the ResourceCache couldn't find any of the files.

Help, what am I doing wrong?

-------------------------

weitjong | 2017-08-03 02:03:18 UTC | #2

On Windows host system the symlink (MKLINK) privilege is not granted by default to normal user. Thus, the build system cannot just assume it and perform a detection first, and using it automatically when available, or falling back to use hard-copying. As a "fallback" it may not be entirely bulletproof, at least personally I do not test it in a long period of time or in a day to day development context. So, if you are in the latter situation then I am afraid to say you have to be careful and take care of yourself. Instead of worrying about files being out of sync, I would be worrying more about (good) modified files being erroneously (but dutifully) overwritten by the fallback copying during build.

Having said that, it does not explain your second observation. If the ResourceCache cannot "see" your resources then most probably it is due to something else in your engine init code, like the resource prefix path engine parameter.

-------------------------

