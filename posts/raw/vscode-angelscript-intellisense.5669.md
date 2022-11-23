Askhento | 2019-10-18 00:09:45 UTC | #1

Is it possible to have auto complete in VS code? I have tried to configure c_cpp_properties.json, but  without success(
I have scriptApi.h file with all the things I want to see, but I really don't understand how to connect everything.

-------------------------

orefkov | 2019-10-18 12:11:39 UTC | #2

Hi.
Im use Visual Studio Community Edition for this, not VS Code.
But for this I have to apply some tricks.
First, in Tools\Option\Text editor\File Extension need add extension "as" as Microsoft Visual C++.
Second - Visual Studio not understand symbol '@', and I use '&&' instead it. But it not understand AngelScript :)
I just little modify loading and preprocessing of AngelScript code in my fork:
- skip #pragma once
- skip #include if it end with .h (for connect api.h)
- replace && to @, if it not contain whitespaces around it.
If you do not want modify engine, you can make this by some kind of preprocessing in build work.

For this files Im use ScriptCompiler as CustomBuild.
Also I modified format of error message output, and Visual Studio understand it as usual error message, and found it in file.

Thus, I have a auto complete, navigation through the code, the ability to run a check and go to the errors.

https://youtu.be/OHD2hrVlC3Y

-------------------------

Askhento | 2019-10-21 20:40:10 UTC | #3

Does it work for macOs?

-------------------------

orefkov | 2019-10-22 12:16:31 UTC | #4

I do not know, not tested it.

-------------------------

