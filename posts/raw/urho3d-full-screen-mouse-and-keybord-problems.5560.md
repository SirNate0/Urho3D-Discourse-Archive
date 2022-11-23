Nejtron | 2019-09-09 21:51:11 UTC | #1

Hi, every one. How you doing i have spend a lot time loking for some solution of my problem. 
The problem is that when i run Urho3d in the Arch Linux full screen it losing focus of my program. And my program do not see the Keybord and Mouse. 

Thank you.

-------------------------

Modanung | 2019-09-10 20:02:13 UTC | #2

Does the same problem occur when running the samples or Urho3DPlayer in fullscreen?

Welcome to the forums, btw! :confetti_ball: :slightly_smiling_face:

-------------------------

Leith | 2019-09-11 06:00:01 UTC | #3

Welcome, friend!
I doubt this issue is Urho's fault - arch linux is a lightweight linux solution, and its input system may not be fully compliant? We have SDL in the middle as an input lib - Reminder, backtracing. I am not running arch, but I am willing to attempt to reproduce your issue in a vm, if nobody else will help you, I will try to do so. I am running Cinnamon 19.2 here

-------------------------

Miegamicis | 2019-09-11 06:50:42 UTC | #4

I'm having the same issues running fullscreen Urho applications on Linux Mint. Don't know how to fix it at the moment.

-------------------------

Nejtron | 2019-09-11 19:18:24 UTC | #5

Hello! Thank you for responding, yes it the same problem all the time(

-------------------------

Nejtron | 2019-09-11 19:21:15 UTC | #6

Hello! Firs of thank you for the answer. It is my first time i writing in some forum.
I have try a lot of staff. But it do not work.(
This problem only he pans i. Full screen(

-------------------------

Leith | 2019-09-12 08:42:06 UTC | #7

I'm running linux mint, with some kernel updates - I have no issues running in fullscreen... are you using the urhoplayer app, or your own app?? re Linux Mint, in the update manager, check under the Edit menu to see if any kernel updates are available - occasionally, you'll see something extra in that menu.

-------------------------

