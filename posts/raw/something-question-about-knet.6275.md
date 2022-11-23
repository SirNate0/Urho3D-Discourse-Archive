ChunFengTsin | 2020-07-18 16:09:25 UTC | #1

Hi everyone!
I am rewriting a online game with Urho3D_1.7.1, and the original project is writed use Unity3D(C#, TCP).

1. So I want to know if possible use kNet in client without the [Subsystem Network Of Urho3D],(the server side does not need to be modified).


2. And when I do a test like this : 
> void GameTest::Start() {
> 
> 	GetSubsystem<Input>()->SetMouseVisible(true);
> 	GetSubsystem<Input>()->SetMouseMode(MM_FREE);
> 
> 	kNet::TCPMessageConnection tcp_test();
> 
> }

the error is :

> #error:  Error: Trying to include winsock2.h after windows.h! This is not allowed! See this file for fix instructions.	client_	C:\Users\tsin\Desktop\Urho3D-1.7.1\include\Urho3D\ThirdParty\kNet\win32\WS2Include.h	33

I have no experience on win socket，who can help me? I just want to build a demo that works well.

-------------------------

Lys0gen | 2020-07-18 19:31:55 UTC | #2

Check where the winsock inclusion is and just remove it? Pretty sure windows.h already has a #include for winsock.

-------------------------

jmiller | 2020-07-18 22:02:16 UTC | #3

Perhaps this can help?
https://discourse.urho3d.io/t/building-a-simple-example-using-mingw-from-command-line/6136/4

-------------------------

ChunFengTsin | 2020-07-19 01:05:21 UTC | #4

I solved this by add:

> #define  _WINSOCKAPI_

and I will try mingw also, thanks

-------------------------

