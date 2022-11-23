att | 2018-01-02 18:08:34 UTC | #1

I want to build my android project, but it failed, the error output is below:

-compile:
    [javac] Compiling 9 source files to /Users/att/Work/Temp/candyhero/android/bin/classes
    [javac] warning: [options] source value 1.5 is obsolete and will be removed in a future release
    [javac] warning: [options] target value 1.5 is obsolete and will be removed in a future release
    [javac] warning: [options] To suppress warnings about obsolete options, use -Xlint:-options.
    [javac] /Users/att/Work/Temp/candyhero/android/src/org/libsdl/app/SDLActivity.java:137: error: lambda expressions are not supported in -source 1.5
    [javac]             File[] files = new File(libraryPath).listFiles((dir, filename) -> {
    [javac]                                                                            ^
    [javac]   (use -source 8 or higher to enable lambda expressions)
    [javac] /Users/att/Work/Temp/candyhero/android/src/org/libsdl/app/SDLActivity.java:146: error: diamond operator is not supported in -source 1.5
    [javac]                 ArrayList<String> libraryNames = new ArrayList<>(files.length);
    [javac]                                                                ^
    [javac]   (use -source 7 or higher to enable diamond operator)
    [javac] 2 errors
    [javac] 3 warnings

-------------------------

johnnycable | 2018-01-02 20:40:32 UTC | #2

add 

    compileOptions {
        sourceCompatibility JavaVersion.VERSION_1_8
        targetCompatibility JavaVersion.VERSION_1_8
    }

to your build.gradle file

-------------------------

att | 2018-01-03 07:28:25 UTC | #3

Thank you for your reply, but I have not create a project managed by gradle, just make tool.

-------------------------

weitjong | 2018-01-03 08:00:44 UTC | #4

If you use `ant` tool then put the equivalent options for ant in the local ant properties file. If you use other tool to invoke `javac` then pass the `-source 1.8` explicitly.

We should probably mention this in the migration notes.

-------------------------

johnnycable | 2018-01-05 09:34:33 UTC | #5

ant -Djava.source="1.8" -Djava.target="1.8" debug

which in my case yields

> -compile:
>     [javac] Compiling 9 source files to /Users/max/Developer/Stage/Workspace/Urho/38_SceneAndUILoad/build/android/Debug/bin/classes
>     [javac] An exception has occurred in the compiler (1.8.0_77). Please file a bug against the Java compiler via the Java bug reporting page (http://bugreport.java.com) after checking the Bug Database (http://bugs.java.com) for duplicates. Include your program and the following diagnostic in your report. Thank you.
>     [javac] com.sun.tools.javac.code.Symbol$CompletionFailure: class file for java.lang.invoke.MethodType not found

reports are there about gradle not compiling with 1.8, but I'm not using it...

Any guess?

-------------------------

weitjong | 2018-01-06 11:11:08 UTC | #7

I don't have the old android build tool anymore, so I cannot verify any of these. However, I am pretty sure the way you passed the parameters would not reach the intended ant task. It is not hard to a search to see how other people doing it though.

https://github.com/search?q=ant.build.javac.source&type=Code&utf8=%E2%9C%93

-------------------------

johnnycable | 2018-01-06 14:09:22 UTC | #8

Command line worked for me. The solution you pointed to surely works for java, I don't know where to put that build.properties file... in the app build directory?

Allowed list of properties is in: <android dir>/tools/ant/build.xml (build tools before up to 25.0.2), as pointed in build.xml in android app build directory

Error I posted is due to my setup being broken. Mixed different urho releases...:wink:

-------------------------

yushli1 | 2018-01-06 16:24:28 UTC | #9

[quote="johnnycable, post:5, topic:3908"]
[javac] com.sun.tools.javac.code.Symbol$CompletionFailure: class file for java.lang.invoke.MethodType not found
[/quote]

I encounter this error as well,using command ant debug. How do you fix this error?

-------------------------

johnnycable | 2018-01-06 16:36:14 UTC | #10

As I posted my setup was broken. I mixed urho 1.6 and 1.7 in the same app. That error is related to gradle, and when I did I noticed a gradle-created file in the dir while there shouldn't be. I delete everything and recreated.
Probably you did the same by intermixing ant build and something gradle-build. Apparently, the two don't go well together...

-------------------------

