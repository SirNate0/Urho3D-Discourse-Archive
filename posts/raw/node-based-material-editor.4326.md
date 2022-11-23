glebedev | 2018-06-17 14:46:58 UTC | #1

https://youtu.be/ObS4sd8vdvQ

-------------------------

glebedev | 2018-06-17 14:47:39 UTC | #2

https://youtu.be/otdD5K_d_GY

-------------------------

glebedev | 2018-06-18 21:42:43 UTC | #3

https://youtu.be/OrTJ4VtUTmQ

-------------------------

hdunderscore | 2018-06-19 00:42:37 UTC | #4

Looks impressive ! You obviously put in a lot of work there. Plan to release it ?

-------------------------

glebedev | 2018-06-19 06:27:25 UTC | #5

Yes. One day it will be opensource. Currently it only works with opengl 2. We plan to release it when we finish support for glsl and hlsl. I can provide access to early build for a feedback.

-------------------------

johnnycable | 2018-06-19 12:03:37 UTC | #6

What did you use for UI?

-------------------------

glebedev | 2018-06-19 13:57:12 UTC | #7

WPF + UrhoSharp for preview. There are plans to make it crossplatform with AvaloniaUI.

-------------------------

Omid | 2018-06-19 15:46:02 UTC | #8

Can I ask you what is the node editor you used in WPF?

-------------------------

Virgo | 2018-06-20 02:30:06 UTC | #9

How did you achieve runtime material modification?
just change the values of an existing material object (sometimes i get confused doing so)
or discard the existing object and instantiate a new one?

-------------------------

glebedev | 2018-06-20 06:40:45 UTC | #10

The editor generates material.xml, technique.xml and shaders in background. Then it calls https://developer.xamarin.com/api/member/Urho.Resources.ResourceCache.ReloadResourceWithDependencies/p/System.String/ to update the runtime.

-------------------------

glebedev | 2018-06-27 14:20:52 UTC | #11

Custom one. I'll release it as a nuget package later. It is also suitable for scripting if you are interested in it ;-)

-------------------------

Omid | 2018-06-27 14:38:37 UTC | #12

I using https://github.com/Wouterdek/NodeNetwork and it's have lot of problem and also it's have memory bug from reactiveui . so modified that lot and i removed reactive ui but still that you did it's really nice it's have grouping it's really nice.

-------------------------

glebedev | 2018-06-28 08:25:33 UTC | #13

An early version is avaliable via itch.io by invite. Drop me a message if you want a key. 
Some limitations of the current version:
- desktop OpenGL only
- forward render only, per pixel lighting only
- bugs are expected
- there are no guarantees that the graph you make will be compatible with the final version. Although I made some safe checks so you can always "upgrade" it manually.

-------------------------

Omid | 2018-06-29 07:35:11 UTC | #14

Perfect. It's working really nice. GOOD JOB :+1:
DirectX working much much better with WPF. because WPF is running over directx.
There is a bug in ReactiveUI it's leaking memory and i saw it's effecting your project little.
You need to open menu and submenu lot of times and watch the memory or add lot of nodes and remove them you can see memory will not release after that. Dump memory with visual studio i'm sure you will see lot o IDisposable and ReactiveUI classes. :wink:

https://github.com/Wouterdek/NodeNetwork/issues/6

Actually I removed ReactiveUI finally and it's much faster and no more memory leak. Our application should be run on embedded devices so we are limited on memory that why I found it's good to don't use ReactiveUI.

-------------------------

glebedev | 2018-06-29 08:00:36 UTC | #15

I only use ReactiveUI to throttle user input. Shouldn't be that bad. Otherwise there is a custom commands and the base node graph implementation doesn't have any fancy dependencies.

Anyway I'll run it under profiler later when the architecture gets stable.

-------------------------

Omid | 2018-06-29 10:39:47 UTC | #16

Nice. then it's easy to move from that. really nice. i going to test the new one on my scenes

-------------------------

Omid | 2018-06-29 10:48:58 UTC | #17

@glebedev I didn't success to load my scenes because i have 2 folders. 

``` cs
    DesktopUrhoInitializer.AssetsDirectory = System.IO.Path.Combine(System.AppDomain.CurrentDomain.BaseDirectory, @"../../Assets");
    var options = new ApplicationOptions("Data;Machines")
```

-------------------------

glebedev | 2018-06-29 11:02:07 UTC | #18

I didn't know it's possible! :-)

Ok, I need to do something about it...

-------------------------

Zamir | 2018-06-29 11:24:38 UTC | #19

If programn not run, you must manually C: \ Users \ ____ \ AppData \ Roaming \ Urho3DMaterialEditor change settings or delete folder

-------------------------

Modanung | 2018-06-29 15:16:29 UTC | #20

@glebedev Is there a Linux version available?

-------------------------

glebedev | 2018-06-29 15:28:18 UTC | #21

No, because I had to use WPF to speedup development. There are plans to utilize AvaloniaUI for cross platform but not at the moment.

-------------------------

Omid | 2018-06-29 17:11:12 UTC | #23

Yeh it's possible :wink: 
I think it's more easy to use Xamarin.Forms + GTK+ and WPF.
As you know it's supporting now and i think you can run UrhoSharp on that.

-------------------------

glebedev | 2018-06-30 00:16:19 UTC | #24

New version allows you to pick multiple folders. Unfortunately I had to change file format to make naming consistent. I hope it's the last breaking change for a long time.

-------------------------

Omid | 2018-06-30 20:35:31 UTC | #25

Perfect/ I'll try it at Monday :wink:
thanks

-------------------------

glebedev | 2018-06-30 20:56:24 UTC | #26

Thanks! By that time I hope to finish deferred pass generation and simplified material creation so you won't need manually wire shadow map to light if all you need is a default diffuse lighting model.

-------------------------

Omid | 2018-07-02 07:19:15 UTC | #27

After i added folders i again i cannot open my scene 
![image|690x464](upload://tl8XQCLfO3FwYRkCjxJ7RGIWTwI.png)

-------------------------

glebedev | 2018-07-02 09:24:52 UTC | #28

My I ask you to send me a screenshot of your folder settings?

-------------------------

Omid | 2018-07-02 09:56:34 UTC | #29

@glebedev do you mean asset directory?

![image|569x262](upload://g8m1VIRo1TnbQcHcaNLBIRRSSUt.png)
![image|596x310](upload://iCYERpYFANa3aQqB25c1p2K9uD.png)
![image|577x395](upload://lmy9udF3HXPI2MnhE0KjeeFFJp9.png)

-------------------------

glebedev | 2018-07-02 10:34:12 UTC | #30

No, I mean the dialog window that appear when you click on "set resources dir" in the main menu.

-------------------------

Omid | 2018-07-02 12:57:37 UTC | #31

this one?

![image|690x388](upload://9WXoD33FAA76djqiX3gJasJpRp.png)

-------------------------

glebedev | 2018-07-02 13:32:25 UTC | #32

Hmm... Maybe there is a bug due to space in a folder name. I'll check it tonight.

-------------------------

glebedev | 2018-07-02 13:37:38 UTC | #33

Btw did you restart the editor after setting the path?

-------------------------

Omid | 2018-07-02 13:44:44 UTC | #34

Yes. I did. It's same.

-------------------------

glebedev | 2018-07-02 14:03:27 UTC | #35

Sorry for the big. We'll fix it asap :-)

-------------------------

Omid | 2018-07-02 18:16:55 UTC | #36

It's ok ;)
thanks for responding

-------------------------

glebedev | 2018-07-02 20:14:18 UTC | #37

I can not reproduce the issue :(
![image|478x170](upload://aNSW6ovYt8uQV2K3uLwBc1wPRMQ.png)

And then I use 
![image|462x218](upload://h2iFRmBGavBSvCRnMn9ZBVPPMCs.png)

To load scene
![image|690x148](upload://tH7ZT0FBO9GxZahhFqov3avTxrD.png)

-------------------------

glebedev | 2018-07-02 20:15:02 UTC | #38

Can you spot the difference?

-------------------------

glebedev | 2018-07-02 22:38:03 UTC | #39

I've made a workaround. Now the app offers you to copy file in the right folder. Let's see what happens now.

-------------------------

Omid | 2018-07-03 06:34:43 UTC | #40

I don't know why. but this time worked well. :D
Thanks

-------------------------

glebedev | 2018-07-03 06:44:26 UTC | #41

Good to know :slight_smile:
Btw here is what guys made yesterday with the editor:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/7/77c2ed9118b09d3e95bdb8b7b293ee504466aa8d.jpg'>

-------------------------

glebedev | 2018-07-03 08:02:38 UTC | #42

A live stream of making an effect:
https://www.youtube.com/watch?v=RjrDxjzzKGE

-------------------------

Omid | 2018-07-03 08:10:27 UTC | #43

Really looks perfect. NICE
Do you have plan for DirectX ?

-------------------------

glebedev | 2018-07-03 08:13:37 UTC | #44

Yes, we do. I am not profound in DirectX personally so it depends on my teammates :)

-------------------------

glebedev | 2018-07-03 21:52:37 UTC | #45

@Zamir added a model preview:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/2/23fe0b5845da3bbc05473a3131cd427fc9562624.png'>

-------------------------

glebedev | 2018-07-03 21:51:49 UTC | #46

I'll be streaming another example tomorrow. You can subscribe to the channel to ask questions and comment live :slight_smile:
  https://www.youtube.com/channel/UCWxM_7z4Ab0g5wjN36e2Zqg

-------------------------

glebedev | 2018-07-04 06:32:49 UTC | #47

https://youtu.be/2-IO5BLi6n8

-------------------------

Omid | 2018-07-04 08:04:05 UTC | #48

@glebedev What is the license ? 
I generate something and i want to use it and i need to add license to project.
Also it's good to generate license header in output file.

I Hope you can finish DirectX as soon as possible.

THANKS FOR THIS GREAT TOOLS :pray:

-------------------------

glebedev | 2018-07-04 08:06:47 UTC | #49

The source code will be released under MIT when it's stable. I don't think license applies for the files produced by the app. It's like a Photoshop - you don't need to include Photoshop license file anywhere if you made textures with it, am I right?

-------------------------

Omid | 2018-07-04 10:37:10 UTC | #50

Ok. so simply i'll copy generated file. thanks again

-------------------------

glebedev | 2018-07-05 11:49:15 UTC | #51

Hlsl support and "ifdef" nodes are in progress. Stay tuned :-)

-------------------------

glebedev | 2018-07-05 22:15:51 UTC | #52

Upcoming feature teaser: 

![image|690x455](upload://hjJLeXAs3eYSw1D5BRvkJwQLEQS.png)

-------------------------

glebedev | 2018-07-24 07:49:57 UTC | #53

Just in case you are wondering what's the state of the project. Here is a video to demonstrate new features:

https://youtu.be/AMypkra9Wyo

-------------------------

Omid | 2018-07-26 06:39:06 UTC | #54

Nice. Do you have plan to release it soon?

-------------------------

glebedev | 2018-07-26 06:45:48 UTC | #55

It should go to open source and open beta soon. We improved UI responsiveness, first experience (start material template), some features added. The only thing that bugs me is matrix multiplication. The 4x3 matrix called that after D3D but order of multiplication is following OpenGL pattern. I think I'll keep OpenGL order but should I rename matrix then?

-------------------------

glebedev | 2018-07-26 06:46:33 UTC | #56

And compatibility with previous release is broken :-(

-------------------------

Omid | 2018-07-26 06:48:23 UTC | #57

> And compatibility with previous release is broken

I think this is not a problem from my point of view. i can reproduce what i have.

-------------------------

glebedev | 2018-07-26 20:17:39 UTC | #58

Presets are coming to the editor:
![image|690x300](upload://8sIL5Wc9hWIi8xRkSoamROByvn1.jpg)

-------------------------

glebedev | 2018-07-28 11:39:50 UTC | #59

Default material:

![image|690x291](upload://A2TpurTef6o2Z550opSgr3UpsOg.jpg)

-------------------------

glebedev | 2018-07-28 15:03:47 UTC | #60

itch version is updated now.

![image|690x349](upload://nnhqvIFg4L4UYR7AETnwDCWWJDx.jpg)

-------------------------

smellymumbler | 2018-07-28 17:27:16 UTC | #61

This is really cool. Congratulations on your amazing work!

-------------------------

Omid | 2018-07-29 07:32:05 UTC | #62

This is really great. PERFECT. :clap:
I can see you already start directx :slight_smile: I really need that.

This perfect project should be include into the urho by default.

-------------------------

Zamir | 2018-07-29 08:00:06 UTC | #63

Omid, could you help with the translation to directX?:thinking::slightly_smiling_face:

-------------------------

Omid | 2018-07-29 08:27:50 UTC | #64

what do you mean ? !!!!

-------------------------

Zamir | 2018-07-29 08:51:30 UTC | #65

translation from GLSL to HLSL

-------------------------

Omid | 2018-07-29 09:37:54 UTC | #66

Ah. Yes. sure. why not. :slight_smile:

-------------------------

glebedev | 2018-07-29 09:40:21 UTC | #67

Cool! It goes open source and open beta today. I'll send you a message.

-------------------------

Omid | 2018-07-29 12:50:01 UTC | #68

GOOD NEWS! :slight_smile:

-------------------------

glebedev | 2018-07-29 12:51:32 UTC | #69

It is done.

https://glprojects.itch.io/urho3d-material-graph-editor/devlog/42708/public-beta

-------------------------

Modanung | 2018-07-29 18:50:35 UTC | #70

When I try to watch the video on the page it says:
> "Playback on other websites has been disabled by the video owner."

-------------------------

glebedev | 2018-07-29 19:37:37 UTC | #71

Ok. This is strange.

-------------------------

Zamir | 2018-07-29 19:43:12 UTC | #72

yes, it is, but you can continue viewing in the youtube directly

-------------------------

Modanung | 2018-07-30 08:19:27 UTC | #73

Of course, but this is clearly unintended behaviour. Providing workarounds doesn't equal fixing bugs. :slight_smile:

-------------------------

glebedev | 2018-08-05 11:56:45 UTC | #74

:frowning: 
![image|308x88](upload://duiwn6xoW8dMFTGO8iDVycuruyp.png)

-------------------------

Modanung | 2018-08-05 12:15:19 UTC | #75

@glebedev Might [Vimeo](https://vimeo.com/channels/luckeyproductions) meet your needs?

-------------------------

glebedev | 2018-08-05 12:17:25 UTC | #76

I can't stream to Vimeo, only YouTube and Facebook :frowning:And recording and uploading isn't an options as I don't have much time to do it. It is way easier for me to do it live.

-------------------------

glebedev | 2018-08-05 12:20:16 UTC | #77

https://youtu.be/BtwjStJKa_E

-------------------------

megapunchself | 2018-08-06 21:39:43 UTC | #78

u'll make in the future possible to export to a script like a .glsl/.hlsl/shader/technique too?

-------------------------

glebedev | 2018-08-06 21:45:03 UTC | #79

It already creates a material, technique and glsl shader. Enjoy :-)

-------------------------

glebedev | 2018-08-13 17:47:26 UTC | #80

Here is an example of material made with an editor:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/2/2f149450b98f7feabb97d6d6285aa58fdcb9e73f.gif'>

Each butterfly is a quad with animated "wings". Everything is animated on GPU.

-------------------------

