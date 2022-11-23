JKGiih | 2018-02-03 12:03:33 UTC | #1

I built both the engine and [this example project](https://github.com/urho3d/Urho3D/wiki/First-Project) by running the cmake_generic.sh script and then running make, assuming that the resulting executable would work on any 64-bit system, but when I try to run it on another machine with a different CPU I get the "Illegal instruction" error. I also tried, instead of running the script, just running cmake with the URHO3D_DEPLOYMENT_TARGET option set to generic, but I still got the same error. Is there something I'm doing wrong?

Also, when I run cmake_generic.sh in the project directory, I get the error "post_cmake: command not found", which I don't get when running the same script to build the engine itself. Are there some other scripts I'm supposed to copy to the project directory?

-------------------------

weitjong | 2018-02-03 13:15:46 UTC | #2

Since you are using *.sh, I assume you are using Linux host system. And if so, instead of following the wiki page which may or may not be up-to-date anymore, you can use our scaffolding task via Rake. You need to have Ruby/Rake installed though, which is usually just a command away to get it installed. Once that prerequisite is fulfilled then in the project root directory of Urho3D, type in this command:

`rake scaffolding dir=/path/to/your/new/project/source/tree`

Cd to your new project source tree and replace the placeholder cpp and h files with your own code then you are all set. Your new project is now setup with all the build scripts borrowed from Urho3D project. That should solve your "post_cmake: command not found" problem.

As for the deployment target, make sure that build option is being used when you are building Urho3D library and when using the library in your own project.

```
cd /path/to/Urho3D/project/source/tree && rake cmake URHO3D_DEPLOYMENT_TARGET=generic && rake make
cd /path/to/your/new/project/source/tree && rake cmake URHO3D_DEPLOYMENT_TARGET=generic URHO3D_HOME=/path/to/Urho3D/project/build/tree && rake make
```

Note the URHO3D_HOME is pointing to Urho3D project build tree, not source tree.

HTH.

-------------------------

JKGiih | 2018-02-03 15:00:20 UTC | #3

Thanks, that got rid of the post_cmake error, however the illegal instruction error remains. When I compile the project on the older CPU (T9600) it runs on the newer one (i5-3450) but not the other way around, which to me seems like the binary is not really generic.

-------------------------

weitjong | 2018-02-03 16:53:23 UTC | #4

This is how we have setup our build system. When the `URHO3D_DEPLOYMENT_TARGET` build option is not explicitly set then it is default to value 'native'. This is good for testing the binary in your own host system because the compiler will generate the binary targeting exactly your system. If you use high end PC then this binary is of no use for lower end or older PC than yours. It is easy to understand why the reverse is fine because newer PC should be able to execute binary targeted for older PC.

However, if you set the build option to target a specific CPU target then the compiler is configured to generate binary compatible for that specific target only. Presumably all the higher CPU model  in the same family should not have problem with this binary too. But again the lower model than this specific target would have problem to run this binary.

Finally, when the build option is set to 'generic' then currently the build system just leaves out setting the compiler flags all together. So, the effective setting is based on the default setting of the compiler toolchain you are using. It may not generate binary as "generic" as it should be, depending on what is being defaulted by the compiler. Perhaps this can be considered as a bug in our build system then. When the build option is set to 'generic', it should have configured the compiler as such instead of leaving it for chance. I see what I can do about it later.

-------------------------

JKGiih | 2018-02-03 16:56:15 UTC | #5

Ok, that explains it, I've definitely set some CPU-specific GCC flags that should be overridden by the build scripts.

-------------------------

weitjong | 2018-02-03 17:47:50 UTC | #6

I have made a commit. Can you help to verity if it fixes your problem. Thanks.

The `-mtune` compiler flags is now set to 'generic' regardless. But it should be preempted by the `-march` compiler flags which is set based on the `URHO3D_DEPLOYMENT_TARGET` build option. The `-mtune` flag is configured in such a way that it is still possible to be optionally overwritten via CMake. e.g.

`rake cmake URHO3D_DEPLOYMENT_TARGET=core2 CMAKE_CXX_FLAGS='-mtune=sandybridge' CMAKE_C_FLAGS='-mtune=sandybridge'`

This build configuration will emit two `-mtune` flags, but since the user provided one comes last, it should be the one in effect.

-------------------------

JKGiih | 2018-02-03 19:15:27 UTC | #7

Still doesn't work. What's weird is that when I run `gcc -c -Q --help=target` it shows -mtune being set to generic and -march set to x86-64 -- so I guess it must be some other flag causing the problem?

I'm running Gentoo so GCC is likely compiled with some non-standard default options. I'll try playing around with my system configuration and see if I can figure this out.

-------------------------

weitjong | 2018-02-05 08:18:38 UTC | #8

I am sorry to hear that. For what it's worth, each GCC version may have its own meaning of 'generic', so setting the lowest denominator CPU model as your target explicitly may have more deterministic result.

-------------------------

