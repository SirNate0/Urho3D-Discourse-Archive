Zaroio | 2020-03-09 07:34:00 UTC | #1

Hi, I'm having an issue building the engine.![Screenshot from 2020-03-08 22-44-18|583x500](upload://1N94y7kpqiBxzin8p60ixEflps8.png)  
For some reason it's not recognizing it as a executable binary, tho I can execute it in a terminal

-------------------------

weitjong | 2020-03-09 02:02:46 UTC | #2

There must be a mistake in one of your steps earlier, but of course we cannot tell you what/where if you just showed us a picture of your end result.

-------------------------

tarzeron | 2020-03-09 19:13:33 UTC | #3

try to open the terminal and execute ./01_HelloWorld (in the same directory or specifying the full path '/full/path/to/01_HelloWorld')

or click yes in your question with a screenshot and select open with the command
/bin/sh -c

-------------------------

Zaroio | 2020-03-09 22:50:07 UTC | #4

yes, I ca run it from the terminal, thanks.

well, I've just created a "build" directory, moved in and called cmake there "cmake ..", then just make -j4

-------------------------

