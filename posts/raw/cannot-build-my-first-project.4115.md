ook | 2018-03-22 13:33:43 UTC | #1

I have followed everything described in the link below

https://github.com/urho3d/Urho3D/wiki/Setting-up-a-Project-(CMake)

However I couldn't build my project and received the message as follows:-

> CMake Error at CMake/Modules/FindUrho3D.cmake:346 (message):
>   Could NOT find compatible Urho3D library in Urho3D SDK installation or
>   build tree.  Use URHO3D_HOME environment variable or build option to
>   specify the location of the non-default SDK installation or build tree.
> Call Stack (most recent call first):

I set the URHO3D_HOME to my Build directory in my project directory from my system variables on Windows 10

Is the information in the link update or did I miss anything?

Thanks

-------------------------

Eugene | 2018-03-22 11:38:37 UTC | #2

It may be not what you exactly want, but I've always used CMake GUI to set `URHO3D_HOME` path instead of Windows paths.

-------------------------

weitjong | 2018-03-22 13:02:28 UTC | #3

I cannot see the reason why CMake variable works while host environment variable would fail.

https://github.com/urho3d/Urho3D/blob/64b69474bc04be1af47b0aaa3854a6382abc0cd6/CMake/Modules/FindUrho3D.cmake#L76

When the CMake variable is not set explicitly then it is initialized with the value from the environment variable (when it is defined).

@ook Try use a path without spaces and see that was the caused of your problem.

-------------------------

ook | 2018-03-22 13:43:48 UTC | #4

[quote="Eugene, post:2, topic:4115"]
URHO3D_HOME
[/quote]
![1|511x500](upload://rbyJg2JCnfzszSP9PEDyElNb7oN.png)

This is what I have set

![2|690x386](upload://dXnklDwmVmuL5WsYa0cXXqgWHrn.png)

![6|690x383](upload://cxUl2lGcAnMuR0s7tLHN11vxAEp.png)

![7|690x383](upload://o2i7EAW6LdUFKjVkeOlaszkYtii.png)

![3|690x460](upload://cTBXxbTSKX8LOWryxweIczrf6sR.png)

![4|690x460](upload://yPhHru7pzcHkx1kHlOLpkGiBb1R.png)

![5|587x499](upload://kus8xBnTdbIbY65WkWG9mMtL8w2.png)

This is no space in the path and I cleared cache before trying to rebuild it.

-------------------------

weitjong | 2018-03-22 13:47:53 UTC | #5

The value should be set to where URHO3D build tree or custom installation of the SDK located. What you have shown does not look like it and that’s the root cause of your failure. Read the docs instead of just following the wiki page without understanding what it actually does.

-------------------------

ook | 2018-03-22 15:00:32 UTC | #6

I have changed the URHO3D_HOME location to my C:\Users\patara\apps\Urho3D-1.7\Build that has both include and lib directories and still it produced the same error messages. Could you please guide me a little. I used to built it successfully on Linux but not Windows.

-------------------------

weitjong | 2018-03-22 15:03:26 UTC | #7

Have you tried to regenerate your own project build tree again. Sometime the CMake may cache the old and invalid values.

-------------------------

ghidra | 2018-03-26 20:43:07 UTC | #8

I ran into this issue this week myself.
What I did to fix it was to not mess with the Environment variables.. But to actually send it along with the bat file.
i.e:

`cmake_vs2017.bat D:\MYBUILD -DURHO3D_HOME=D:\URHOBUILDTREE`

etc

-------------------------

weitjong | 2018-03-27 05:04:27 UTC | #9

When trying, don’t use URHO3D_HOME environment variable. This, I agree. Because, there is no way you can invalidate it when you got it wrong due to how the CMake cache works. Modifying the URHO3D_HOME as a CMake variable always works even after the initial build tree has been generated or partly generated. It is easy to see why from the code snipet above. 

But once you get over the trying/testing stage and assuming you don’t keep changing the Urho home then you can either pass the variable again and again each time you generate a new build tree, or hardcode that in your batch file or just put it in your host environment variable, just like JAVA_HOME or GRADLE_HOME.

-------------------------

RCKraken | 2018-03-27 05:54:20 UTC | #10

I have had the environment variable issue 3 times while building urho on 3 seperate windows computers.

You can see details for adding environment vars here>https://www.twilio.com/blog/2017/01/how-to-set-environment-variables.html

Also, environment variables do NOT update until the windows OS is restarted. For me, this was my only non-documented issue I had while building.

Orion

-------------------------

weitjong | 2018-03-27 07:53:46 UTC | #11

On Linux we can test out new env var as easy as this: my-var=my-value ./my-program

No need to relogin. But if that is put inside the .bash_profile or something then of course the situation is not much different with Windows OS or any other OS. In Nix we can still manually source in that file though.

Bottom line, if you don’t know how to deal with environment vars then don’t use them. But also stop pointing finger at them.

-------------------------

