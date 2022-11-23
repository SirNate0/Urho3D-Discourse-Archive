mcnito | 2020-12-24 08:01:14 UTC | #1

Hi all,

First of all, thanks to all the community for this great framework.

I've playing the last week with Urho 3D.

My internal route map was:

0) Compile Urho3D (windows), and create a simple project so I can start coding (C++, on windows, vs2019) calling Urho3D as external library (URHO3D_HOME).

1) On the same simple project, export to emscripten (HTML5). So when I advance coding, I can easily share my progress.

2) The same, for Android.

3) Lastly, the same for iOS. I say lastly, because this forces me to change OS. Here I have the question (or I will have the question, when arrive) about if I need to setup and compile OSX to get OSX Urho3D lib or can I simply copy Urho3D.lib from windows, and then work directly on the iOS version.

0, success!
1, error... stop. :frowning: 

This is very strange (at least for me) since I managed to compile and publish the core of Urho3D with emscripten, with all the working examples and so. Also, If I copy my code (replace files and names) inside 01_HelloWorld example, I get it working (so It will be a minor problem but well...)

![image|690x198](upload://2f3JEy4k2x37xLvRTUbTDIZobw0.png) 

This is stopping me a little. Everyday I think: Let's go to code a little! And I end trying to get emscripten working. My plan is to have 0-1-2 and code a complete (scalable) App, and then go also for 3.


Thanks for the help, and excuse me if I make idiot questions, im relatively new to cmake based projects.

-------------------------

SirNate0 | 2020-12-24 19:03:48 UTC | #2

Hello @mcnito, welcome to the forum!

My guess is that your error is because your Urho 3D build directory is for the regular C++ windows build. If you want to compile your project with emscripten you need to compile both the Urho3D library with emscripten, and use that build directory as URHO3D_HOME for your project's build with emscripten.

-------------------------

mcnito | 2020-12-29 21:27:25 UTC | #3

Hi @SirNate0,

Thanks for the reply, and for the solution. This also replies my future question on point 3.

My fail was think that compiled urho3D library on windows will work for all deploys on windows (windows itself, android, html5...).

I've tested and it's working right now :slight_smile:

Thanks a lot!

-------------------------

