urnenfeld | 2019-11-28 22:47:49 UTC | #1

The exercise described [here](https://discourse.urho3d.io/t/embedding-urho3d/5222/36), somehow succeeded. The existing work on RPI and ARM, has been really helpful.

*Summary: Embedd our engine in a Linux Embedded System that could be trimmed to only play urho3d games. Deploy the system on specific popular Hardware. In other words, the **Urho3d-Only** Video Game Console.*

I am in the process of converting this exercise in a project, small website for downloading the images, instructions for building your own, etc etc. So I’d like to gather your comments (polluting the forums as less as possible) regarding:

**Name**: Propose a name for this. You can comment if some other proposal in this thread you specially like or dislike(indicate the reasoning in this case). As the background intention is to promote our engine, proposals containing **urho** are preferred.

**Targets**: If you would like to test or be involved, indicate which Raspberry PI models you own. Other boards are also welcome, but they must be *yocto supported*. Each build takes several hours, and ~50GB of disk space, therefore I need to go for the most relevant targets.

**Project templates:** The games would need to follow some standard, this standard we can be based in our already existing templates. Indicate if there is any template missing in this thread.

**Game definition**: Eventually there will be some kind of game selector(name wanted), as such, the project template should contain some kind of Game-Manifest. (Name, Desc, Genre, ...)

**Comments**: Feel free to add your comments & Questions

Topics regarding games distribution like:
-	*“How do I build my game for this platform?”*,
-	*“How will the system fetch/download my Game”* 

Will be addressed later on a third loop. My initial intention is maintain myself the opensourced and most close to a determined *official template* as part of the project, even preinstall them in the image.

**Please read other users before posting, I beg you, 1 reply per user**(edit your post as long as the following 2 weeks). As a start, I will give my own:

------------------------------

**Name**: UrhoTank(from fishTank, might sound warlike in many languages or relate to Tank games, which would be misleading)
**Targets**: Rasp 0w
**Project Templates**: 
- https://github.com/ArnisLielturks/Urho3D-Project-Template
- https://gitlab.com/luckeyproductions/QtCreatorUrho3DWizards
- https://github.com/BlueMagnificent/Urho3D_CodeBlocks_Wizard

**Game Definition**: I don’t know previous exercises, or already defined standards, maybe from other gamming hubs. Initial proposal: Xml containing (Name, SubName, Description, Version, Genre, Sample Pictures, Requeriments Benchmark) Pictures should be contained in the Resources folder.
**Comments**: I already spoke way too much, hope this way of gathering information is ok, once everything is setup I can move most of discussions out.

-------------------------

Modanung | 2019-09-20 10:27:20 UTC | #2

**Name**:
* **The _Fin_** -- "powered by Urho3D"

Because this project (and it's variations/installments) will be an important part of the fish, pushing it forward. This name also lends itself for a fin-shaped case design, like an organic Wii. Lastly it points to Finland, where it all began, while meaning "end" in French: [**α** & **ω**](https://en.wikipedia.org/wiki/Alpha_and_Omega) [:fish: ](https://en.wikipedia.org/wiki/Ichthys)

**Project templates**:
About the QtCreator wizards I would like to add that they have by no means acquired their final form; suggestions and pull requests are welcome. [[ forum thread ]](https://discourse.urho3d.io/t/wrench-class-and-project-wizards-for-qtcreator/2076)
For instance it currently expects qmake is used to build the project. This could be extended with cmake for instance. Also, as I made these wizards in isolation (without collaboration) their code should basically be considered unreviewed.

-------------------------

urnenfeld | 2019-10-18 16:58:13 UTC | #3

A little update update on how things are going:

**Game Definition:** As the the whole environment used for this is python based, currently a JSON file was the more [straight forward](https://github.com/urnenfeld/meta-urho3D/blob/thud/classes/urho3dgame.bbclass#L20) way. 
On how each game will be present in disk, I let the build environment dictate. A sample how the resulting structure is [can be seen here](https://github.com/urnenfeld/meta-urho3D/blob/thud/files/sample_disk.zip) and [how it is created](https://github.com/urnenfeld/meta-urho3D/blob/thud/classes/urho3dgame.bbclass)

**Project Template**: @Miegamicis Template has been [integrated](https://github.com/urnenfeld/meta-urho3D/blob/thud/recipes-games/Urho3D-Project-Template/urho3d-project-template_git.bb), and will be the base at least in this early beggining. 

**NAME**: As seen in the post title, things urged to be named to create repositories and so on. I finally went with the initial name in the very first proposal: ***UrhoBox***
*Logos of a fish inside a semi-transparent box are welcome.*

**Game Distribution**: The current idea on how games can be distributed  is using already existing packaging (rpm, deb, ipk), as yocto creates them automatically. It will be necessary to be able to install in alternatives paths other than /.


**Game Selector**: I have started the development of a *game selector* is a very important piece. Will be the starting up program. It needs to:
- Scan the available games on available disks, network, repositories, stores...
- Be able to browse, download and launch them
- Preferences (*would be interesting if they could be shared among games...*)
- Reboot / Shutdown / Park the UrhoBox

What is Park? Park would turn UrhoBox into a standard linux system so people could install other application & services while UrhoBox does not act as a Gamming Machine.

Oh! and this piece of software will be called *[theFin](https://github.com/urnenfeld/theFin)*

After now, Feel free to comment on any point.

-------------------------

urnenfeld | 2019-11-28 22:47:18 UTC | #4

This is @Miegamicis template game launched from the x init session. 

https://www.youtube.com/watch?v=eDagar8lF6Q

-------------------------

Miegamicis | 2019-11-28 23:11:02 UTC | #5

Nice! Glad to see that it's actually used somewhere. :+1:

-------------------------

urnenfeld | 2020-05-29 16:11:23 UTC | #6

Here is another loop.
I might now say all the key components are now in place.

The system now boots in a game selector([thefin](https://github.com/urnenfeld/theFin)) which is very simple and there is room for improvement and collaboration. It is using only urho3d provided assets, and a custom scene file(obviously derived from a known example). It is based on the @Modanung QTCreator template.

Then you will see in the video launching 2 games:
* Second seen in the video is the same as can be seen in my previous post. 
* First one was my initial playground on urho3d engine. But the important part here is that this is an example of how a game can be deployed to the system without having to release the sources or keeping a git repository somewhere. [Here](https://github.com/urnenfeld/meta-urho3D/blob/2790a3d59f53488a02974d70b4db801b00d87720/recipes-games-prop/madtunnel/madtunnel_0.1.bb#L7) can be seen of the location of the source code is actual a local filesystem path. Note as well the ~21 fps for such a low spec hardware :slight_smile: 

Anyone could build the complete image, or a simple game. In the second case a rpm/deb/ipk file is generated and that could be distributed (this part is the initial idea, but is currently functional). A [wiki](https://github.com/urnenfeld/meta-urho3D/wiki) is on the way to explain these steps.

https://www.youtube.com/watch?v=xm6zyBjhE7o

The image found in the video can be downloaded [here (follow Скачать word)](https://cloud.mail.ru/public/4zjz/9ZnFruxfJ)

Feedback is welcomed to know how and where to go :thinking: ...

PS: Yes, reflex on screen show me avoiding children from getting the keyboard to play...

-------------------------

dertom | 2020-05-28 11:48:08 UTC | #7

@urnenfeld Do you have an image for the rpi0 somewhere? I will try to give it a shot next week as I have a week holiday. 
Sry I didn't read everything (yet). And still have to wrap my head around that whole process....
EDIT: Not sure my pi zero is working at all!? :D
At least I already printed everything for the "Switch Killer" aka The Fin ;)
![grafik|666x500](upload://mQiIbXL6cbhd6wbzb3hwdX8E49R.jpeg)

-------------------------

urnenfeld | 2020-05-29 07:35:29 UTC | #8

@dertom of course I keep the images. I can publish the very same that was shown in the video. Let me some days until I get my fiber service fixed. I am on mobile internet right now.

Current image is very minimalist, I added a ssh server and some wifi required tooling but have not tested, if that is enough to connect. Would you find useful to have something more already bundled?

These printing are really interesting and motiving :open_mouth: Is one of those cross acting as the pointing device/mouse? Can't wait to see all together!

-------------------------

dertom | 2020-05-29 08:49:15 UTC | #9

No need to hurry, it seems my rpi0 is broken?! It is just not booting up. Tried everything. It worked once a bit but with errors concerning mmc-something. Since then nothing...A new one is one the way...let's see how long that will take to arrive.

The crosses are the dpad. Not sure about how that will be mapped to the device. Would more guess like cursor-keys,...
Not sure how well that works(mechanically), felt a bit awkward on the 'dry-test'. Maybe I will change that to single buttons. But this 3d model I found in the internet is a good base. I already experimented with flexible Print-Material(tpu) for the top parts which made it feel a bit better and not so clunky... But first I want the thing to boot up... 

No need for you to customise the image for me. I will try to run that meta-urho3d thingy on my own. Maybe I will ask about that some times....thx so far

-------------------------

urnenfeld | 2020-05-29 10:07:53 UTC | #10

[quote="dertom, post:9, topic:5601"]
It worked once a bit but with errors concerning mmc-something
[/quote]

Have you tried another uSD card? there is no mmc integrated in the board AFAIK.

[quote="dertom, post:9, topic:5601"]
A new one is one the way…let’s see how long that will take to arrive.
[/quote]

If you own a rpi2 or rpi3, it might be a good moment to enable support.

[quote="dertom, post:9, topic:5601"]
Not sure about how that will be mapped to the device. Would more guess like cursor-keys,…
[/quote]

If the kernel publish that device as normal keyboard/mouse events, must work. If it is some other type of input device, we might need to add something more...

[quote="dertom, post:9, topic:5601"]
I will try to run that meta-urho3d thingy on my own.
[/quote]

Cool! I will complement the building steps in the wiki during the weekend. I just got the fiber fixed!

-------------------------

dertom | 2020-05-29 10:19:15 UTC | #11

Yeah, I tried several SD-cards with different versions of raspbian and a prebuilt one for that gaming addon,... I flashed so much yesterday I needed sunglasses :D I also tried the plug the rpi0 in as a usb-device in the computer. That actually did work,...it was recognized so the thing as a whole seems to work (which kept me trying for some more hours :D ) Burnt lots of time and decided to wait for the new one. ;) 

I acutally have a whole armada of SoCs (lots of Orange PIs, some RPis and one Odroid) but since I have this gaming device that fits directly on the rpi I do want it to work with that. The other ones are more or less (more less) working in my 'mega' arm-cluster ;) (That was another time burner-project: setting up a kubernetes cluster on arm....:D )

[quote="urnenfeld, post:10, topic:5601"]
Cool! I will complement the building steps in the wiki during the weekend. I just got the fiber fixed!
[/quote]

That would be epic....

-------------------------

urnenfeld | 2020-05-29 16:21:17 UTC | #12

@dertom I have updated the [wiki](https://github.com/urnenfeld/meta-urho3D/wiki). There are better details on the building process. There should be no errors so feel free to report any surprise, to improve the guide.

As for the image, I have edited the [previous post](https://discourse.urho3d.io/t/rfc-the-urhobox-was-embedding-urho3d/5601/6?u=urnenfeld). Check link below the video.

-------------------------

dertom | 2020-05-30 08:01:54 UTC | #13

Thx for the detailed wiki. Very appreciated and thx for uploading the image.

So it is right, that this image is pi0 only, yes?  Nontheless I tried the image on my an rpi3b and rpi4. On the rpi3 you saw only the typical initial rainbow-colored rectangle....on rpi4 nothing. ;) 

Then I started with following the wiki. Everything went quite smooth until the very last step, where you pointed out to:
```
bitbake urhobox
```
But I only get an error:
```
ERROR: Nothing PROVIDES 'urhobox'
```

I could start some process using:
```
bitbake core-image-minimal`
```

Actually not sure that is the intended process, at least it tells that meta-urho3d is in the build-config:

```
`Parsing of 823 .bb files complete (822 cached, 1 parsed). 1295 targets, 82 skipped, 0 masked, 0 errors.
NOTE: Resolving any missing task queue dependencies

Build Configuration:
BB_VERSION           = "1.40.0"
BUILD_SYS            = "x86_64-linux"
NATIVELSBSTRING      = "ubuntu-18.04"
TARGET_SYS           = "arm-poky-linux-gnueabi"
MACHINE              = "qemuarm"
DISTRO               = "poky"
DISTRO_VERSION       = "2.6.4"
TUNE_FEATURES        = "arm armv5 thumb dsp"
TARGET_FPU           = "soft"
meta                 
meta-poky            
meta-yocto-bsp       = "thud:958427e9d2ee7276887f2b02ba85cf0996dea553"
meta-raspberrypi     = "thud:4e5be97d75668804694412f9b86e9291edb38b9d"
meta-urho3D          = "thud:2790a3d59f53488a02974d70b4db801b00d87720"``

```
Obviously I don't know what I'm doing, yet. But I'm curious what the result will be :smiley:

Thx so far

EDIT: first build ran through but obviously not with the result as wanted. Now trying: 
```
bitbake core-image-urho3d
```

Oh,...ok. Found out that I used the wrong machine. I used one of the predefined but would have to use one of those:
```
raspberrypi0  raspberrypi0-wifi  raspberrypi2  raspberrypi3-64  raspberrypi3  raspberrypi-cm3  raspberrypi-cm  raspberrypi
```
Next try ;)... ah, now I know what it was meant with main-table in the wiki :+1:

-------------------------

urnenfeld | 2020-05-30 11:21:58 UTC | #14

[quote="dertom, post:13, topic:5601"]
Thx for the detailed wiki.
[/quote]

I wrote it very fast there might mistakes from all sorts... orthographic, grammar ...

[quote="dertom, post:13, topic:5601"]
So it is right, that this image is pi0 only, yes?
[/quote]

Yes, the pi0W actually, even the build system would generate only for this as it is now :frowning: but it is the next topic I will work. It must be very easy reach that stage. 

[quote="dertom, post:13, topic:5601"]
Everything went quite smooth until the very last step, where you pointed out to:

```
bitbake urhobox
```

But I only get an error:

```
ERROR: Nothing PROVIDES 'urhobox'
```
[/quote]

My fault :cry: sorry, I missed to commit the very last stuff. Just pull the latest changes from meta-urho3d repo again. To recover the environment, you only need to repeat the:

> source sources/poky/oe-init-build-env my-urhobox-r0w-build

As you already realized, you need to setup the **MACHINE** var (in conf-/local.conf) to **raspberrypi0-wifi**.

Judging by your output, everything is correctly setup, you are good to go with:

> bitbake urhobox

Thanks for giving a try!!

-------------------------

dertom | 2020-05-30 12:27:07 UTC | #15

cool,...got it completely compiled for pi0. Maybe I will give it a try with rpi3 later.

-------------------------

urnenfeld | 2020-05-30 12:43:52 UTC | #16

[quote="dertom, post:15, topic:5601"]
I will give it a try with rpi3 later.
[/quote]

Great! I have tested locally, and verified the resulting ouput, but no test... It wasn't supossed to be that easy... 

So to make the yocto apply the same patching for any Raspberry MACHINE try this: 

https://gist.github.com/urnenfeld/b024287b88b5bf1bd6ab1d3dd79fd9d4


Note *meta-raspberrypi* does not support the pi4 in *thud* branch. :pensive:

-------------------------

dertom | 2020-05-30 17:22:14 UTC | #17

Well,...I could actually create an rpi3-image. 
![image|666x500, 50%](upload://7GYv5wt0MBj5hd00uaZgfULEjr1.jpeg) 
But now comes the but ;)
After the loader-screen, it first told me:
```
init id s0 respawning too fast disabled for 5 minutes
```
I could come around this by disabling uart in config.txt on the device itself....

After that I get some other error, see image:
![image|666x500](upload://izAhwzRruKueUlJa3QIOXzUBK0h.jpeg) 

Not sure what to do about this. I'm a bit lost. Btw, do you have a good way to test those images on the desktop or did you test all on your rpi0?`

I guess I will start over after a break... maybe on an other Yocto branch...and first with some samples. One step after another ;)

-------------------------

urnenfeld | 2020-06-01 11:03:15 UTC | #18

[quote="dertom, post:17, topic:5601"]
Not sure what to do about this. I’m a bit lost.
[/quote]

So the xsession will launch the script */etc/mini_x/session* (what is called *thefinloop*) and that script for some reason could not launch **thefin**. I assume there exist */usr/bin/thefin* in your image as well...

I wonder if the `Error: No calibratable devices found.` is shown/triggered by urho3d engine...

You can always CTRL+ALT+F1 and get a tty. root is without password

Other option is to remove file */etc/mini_x/session* then you will boot to a simple x terminal, where you can launch thefin/template/samples manually, but you would need to take care of the environment vars for locating resources(check `ls /usr/bin*-launcher` scripts).

[quote="dertom, post:17, topic:5601"]
Btw, do you have a good way to test those images on the desktop or did you test all on your rpi0?
[/quote]

We can say there is, I can set the MACHINE to qemux86 and run on PC, this is extremely slow, so I have not actually checked in deep how functional it is... I just saw it reaches thefin.

![Screenshot_20200601_120733|686x500, 50%](upload://9u7vTtIcs9tWOP7TRTmpnX2N6kr.png)

-------------------------

dertom | 2020-05-31 14:55:07 UTC | #19

Ok,...I will check this out someday. For now I wait for the rpi0 to arrive,..I think I understood what steps you took but without deep knowledge of linux and its boot-process and how X11 egl and co play together it was a bit too much if something does not work. The problem is that I tested too much and the image that worked is lost (the thing that I copied was just a symbolic link :D ) 
At the moment I play a bit with buildroot. A similar project. ~~I find the mini_x interesting cause I also wondered what would be the best setup to just start one opengl application....~~
Thx so far, when the rpi0 arrives I will be back on yoctus.... :+1:

-------------------------

dertom | 2020-06-19 12:06:02 UTC | #20

Well finally the rpi0 arrived (I should have looked at the delivery date before). 
Too bad I have no time for this stuff atm. But I could test two things:
1) UrhoBox - TheFin image you provided works:
![image|666x500](upload://vmHg8xf2rseLHVmqN3CokKMzXiz.jpeg) 
- Bad thing I my usb2otg blocks the 2nd usb. So all I could do so far is starting and watching the box start. ;) (In the photo you see another effort to use a normal micro-usb and conect the device via UsbFemale-adapter)

2) Obviously it doesn't work with this game-hat I bought. I would have to install some drivers,....and to do this via yoctu would cost me 2 weeks and still won't work ;) The gamehat works with a provided image though...and one thing I can say....the display is tiny. Guess 1.5" is not enough :D ;)
 ![image|666x500](upload://al2rv2ffdUNw1dHz6MlKmfeecTE.jpeg) 

Again thanks for your efforts. I can't imagine how many hours and days you must have burnt for this to work. :+1:  Still I do love the yoctu project and how you can create your own linux-distribution. Wouldn't it be great to have a fully setup and ready to go for developing UrhoOS :D ;) 

Now I order me a better usb2otg-adapter and we will see. I have some holiday in july...I guess then I will play with it again.

-------------------------

urnenfeld | 2020-06-19 13:43:14 UTC | #21

[quote="dertom, post:20, topic:5601"]
Bad thing I my usb2otg blocks the 2nd usb
[/quote]

My usb2otg was not special, it came with a set with the microhdmi... I had to use a self supplied USB hub to be able to connect a Mouse & KB though

[quote="dertom, post:20, topic:5601"]
Obviously it doesn’t work with this game-hat I bought. I would have to install some drivers,…
[/quote]
Do you have any reference to take a look at this product?

[quote="dertom, post:20, topic:5601"]
the display is tiny. Guess 1.5" is not enough
[/quote]
Here my code could be wrong, and not responsive enough to the screen size... Is [a separated](https://github.com/urnenfeld/theFin) project which can developed in a host PC.

[quote="dertom, post:20, topic:5601"]
Again thanks for your efforts. I can’t imagine how many hours and days you must have burnt for this to work.
[/quote]
Thanks! A big part of it has been done with my 1yr old son sleeping in my arms. So it has been coded with 1 hand :smiley:. However It should have worked in the RPi3 :thinking:

-------------------------

dertom | 2020-06-20 09:53:08 UTC | #22

[quote="urnenfeld, post:21, topic:5601"]
Do you have any reference to take a look at this product?
[/quote]

Here is some wiki with access to the working images for various rpis: 
https://www.waveshare.com/wiki/GamePi15

[quote="urnenfeld, post:21, topic:5601"]
However It should have worked in the RPi3
[/quote]

Hehe, yeah it should, but not out of the box. I obviously had to alter urhobox's .bb files to work for rpi3-machine (_raspberry3 postfix instead of _rpi0....) . Just copy and paste didn't work because I had to add a  patch for Angelscript(cmakefile) to compile. (I had to add this not sure what it does ' `-Wa,-mimplicit-it=thumb` ) 
Don't recall what more I did (try). Every much try'n'error which is very time-consuming in this project ;) I actually managed to create an image, but  with the box and the progressbar showing up but then nothing...
 I also jumped back and forth in those yocto-versions....(which is veeeery time consuming :D ) 
In the end everything is more or less straightforward and this project is amazing, but when something does not work it is hard (for me) to figure out what the problem was...maybe when I start with more knowledge from scratch again, it might work directly. Not sure when I have time to give it another try...

Have fun

-------------------------

urnenfeld | 2020-07-01 15:56:32 UTC | #23

[quote="dertom, post:22, topic:5601"]
Here is some wiki with access to the working images for various rpis:
https://www.waveshare.com/wiki/GamePi15
[/quote]

There is information how to integrate in retropie and recalbox, not yocto based, but should be possible. If you mange, let me know as the source code of the kernel module [is available](https://github.com/recalbox/mk_arcade_joystick_rpi)

[quote="dertom, post:22, topic:5601"]
Hehe, yeah it should, but not out of the box.
[/quote]

Now it should :slight_smile: it did for me. I added the generic postfixes, but as well introduced [what you faced](https://github.com/urnenfeld/meta-urho3D/commit/bc453a2c0c95a206eed5a9771e062e16eb99bbec) **-Wa,-mimplicit-it=thumb**, you could pull the latest *thud* branch.

Let me know any other build issue.
Being honest there is a known problem with thefin. If it not built at first stage just make.

`bitbake thefin -c cleanall -f`

and go ahead again with 

`bitbake urhobox`

-------------------------

Modanung | 2020-07-07 15:04:05 UTC | #24

Is there a reason for the target name to be `thefin` instead of just `fin`?

-------------------------

urnenfeld | 2020-07-07 16:36:34 UTC | #25

[quote="Modanung, post:24, topic:5601, full:true"]
Is there a reason for the target name to be `thefin` instead of just `fin` ?
[/quote]
Hmm, I guess it felt short to me... & unconsciously taking it out of its translation to my mother tongue (_end_).
I think empathizes we are speaking about a determined thing.. that fish that creator of this engine....

-------------------------

dertom | 2020-07-07 16:40:29 UTC | #26

@Modanung  Didn't you call it 'The fin' ;)

[quote="Modanung, post:2, topic:5601"]
**Name** :

* **The *Fin*** – “powered by Urho3D”
[/quote]

-------------------------

Modanung | 2020-07-07 17:06:04 UTC | #27

If there's no naming conflict I'd say - here - short is good. Also, I like the irony of a system _starting_ with the _fin_. It's a bit like how you use the _start_ menu in Wondiws to *end* your session; the _alpha_ and the _omega_. :wink: 

...and would it by any chance make technical sense in some cases to have multiple `fin`s running simultaneously? For frozen games in the background or something.

@dertom Yes, but thankfully the *The Rise of the Triad* binary was named `rott`. :slightly_smiling_face:
...and actually I suggested it as a name for the whole thing, not a part of it. Rather seeing the console as a part of Urho(3D) by which the *engine* would move forward.

-------------------------

Modanung | 2020-07-07 17:10:29 UTC | #28

@urnenfeld Furthermore, fin also means _end_ in the sense of _purpose_ or _goal_; *fin*ish.

-------------------------

urnenfeld | 2020-07-08 10:58:46 UTC | #29

[quote="Modanung, post:27, topic:5601"]
…and would it by any chance make technical sense in some cases to have multiple `fin` s running simultaneously? 
[/quote]

Given these devices are short on resources, in the current implementation: **urhobox** is launching **thefin** in loop, he is required to inform the system [which is the game to launch next, but it is also required to complete and quit its execution](https://github.com/urnenfeld/meta-urho3D/blob/thud/recipes-urhobox/thefin/files/thefinloop.sh) after that it will be launched again when the game quits. By this way there are more resources available for the game. Therefore there would not be multiple instances.

[quote="Modanung, post:27, topic:5601"]
For frozen games in the background or something.
[/quote]

This part is uncovered and interesting. Which makes me think... Is there some kind of *heartbeat*(#cycles,...) in the engine which could be checked from another process? Or some other reliable way to check if the game is *alive*... and not stuck in some hook?

-------------------------

Modanung | 2020-07-10 11:17:12 UTC | #30

But wouldn't you want to access The Fin _during_ a game?
Possibly for imaginable future features.

And although it's good to include resource-limited devices in the list of targets, I think this shouldn't limit the functionality. Just as the maximum number of bones in a single model depends on the target, so could the number of concurrent UrhoBox processes.
Handhelds and consoles could run the same software, while still using their hardware to the fullest; where something like watching a movie with a game paused in the background might be something only a console (and future handhelds) can do.

-------------------------

urnenfeld | 2020-07-10 13:56:52 UTC | #31

[quote="Modanung, post:30, topic:5601"]
Possibly for imaginable future features.
[/quote]

Share them please :slight_smile:

I have some features in mind which might require more a wider framework on top of *urho3d* to ease the game development(common configuration for screen/controllers)

But none that would require leave the game selection running in background...

[quote="Modanung, post:30, topic:5601"]
And although it’s good to include resource-limited devices in the list of targets, I think this shouldn’t limit the functionality.
[/quote]

I agree with that. Decisions currently made are prioritizing having something *functional to show & play* so people can jump in, taking into account the current level involvement to set feasible milestones.

[quote="Modanung, post:30, topic:5601"]
where something like watching a movie with a game paused in the background might be something only a console (and future handhelds) can do.
[/quote]

This is a reasonable feature... :thinking:

-------------------------

Modanung | 2020-08-06 22:40:31 UTC | #32

Another shared configuration that may be interesting to consider is accounts/users/players to couple to a name, save states, colors/symbol maybe, highscores/achievements and input preferences... which may be convenient to modify during play.

As an extension to that, I think the characters I made for [KO](https://gitlab.com/luckeyproductions/KO/-/tree/master/Blends) might make for nice Mii-like entities ([itse](https://en.wiktionary.org/wiki/itse)/[oma](https://en.wiktionary.org/wiki/oma#Finnish)?), if I may say so myself. They could race around, play volleyball, meet up, explore space 'n all that while providing a sense of continuity and identity throughout these activities. There's a male and female character, both have morphs for customization/variation, some animation, hair and clothing.
![KO_characters1|505x431](upload://6D768zLQPvjbdiPXyTUUtbaBBdT.png)

-----

**EDIT:** @urnenfeld I realized, that with all the different Pi versions out there, it would be nice to have some API for games to communicate (Pi dependent) default graphics settings to the Box. But maybe you had already thought of that. :slightly_smiling_face:

-------------------------

Modanung | 2020-08-05 13:16:25 UTC | #35

5 posts were split to a new topic: [Urho Pihvin: Raspberry Pi Case](/t/urho-pihvin-raspberry-pi-case/6298)

-------------------------

urnenfeld | 2020-08-07 15:23:56 UTC | #36

[quote="Modanung, post:32, topic:5601"]
API for games to communicate (Pi dependent) default graphics settings to the Box.
[/quote]

You mean, like supported resolutions? or preferred Engine parameters?... both I guess :slight_smile:

I kinda thought that some Engine Parameters should be overridden by Urhobox, given the potential off the underlying HW and the requirements(fps?) of the game... Is part of what I meant when:

[quote="urnenfeld, post:31, topic:5601"]
I have some features in mind which might require more a wider framework on top of *urho3d* to ease the game development(common configuration for screen/controllers)
[/quote]

-------------------------

Modanung | 2020-08-07 16:55:17 UTC | #37

In this case I mainly meant graphics settings like light/particle count, texture, shadow and model quality along with the screen resolution and postprocessing. Given the fact that games can be quite different, I don't think it would make sense to apply the "same settings" to all games, that would maybe even pose a greater challenge of standardization. Instead I think this asks for a more general and bundled "graphics quality" setting; defaults for each Pi that developers could define and include with their game.

These defaults could perhaps be tweaked by the gaming community as well, and people could pick a preferred default settings bundle (say _medium_) in the Fin dashboard. This does not mean getting rid of detailed settings, but it could avoid turning the tweaking into a hurdle to play.

Commercial consoles don't have this "problem" of forwards compatibility.

----

But this might also be useful engine feature outside of the UrhoBox' scope, making it - at least its core functionality - an engine modification that the UrhoBox could profit from.

-------------------------

