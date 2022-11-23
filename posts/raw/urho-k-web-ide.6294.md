Modanung | 2020-12-03 19:40:56 UTC | #1

https://gitlab.com/luckeyproductions/tools/tank

> # :hammer_and_wrench: https://Urho3D-Tank.Arnis.dev/

> # :art: https://Tank.LucKeyProductions.nl/

----
Wouldn't it be cool to have a [CodePen](https://codepen.io/pen/)-like Urho3D web environment for script?

[poll type=regular results=always public=true chartType=bar]
* Yes... yes it *would* be cool
* No, it would be lame
* Huh?
[/poll]

-------------------------

Modanung | 2020-08-02 14:34:35 UTC | #2

@Miegamicis Any thoughts on the feasibility and implementation?

-------------------------

Miegamicis | 2020-08-02 18:54:10 UTC | #3

> @Miegamicis Any thoughts on the feasibility and implementation?

One thing that I haven't yet checked/implemented is the ability to do resource reloading in the web builds, but I have been thinking about it by using browser local and session storage. But don't see any reason why it couldn't work. Everything else is straightforward, I would estimate that it could take couple of weeks to make,

You got my attention on this, maybe I could draft some sort of POC for this. :boom:

-------------------------

Modanung | 2020-08-03 12:44:59 UTC | #4

Once functional, it should be *relatively* easy to extend it to an open community-driven arcade network, with the possibility to even link scripts as consecutive mini games or otherwise interconnected virtual worlds.

-------------------------

throwawayerino | 2020-08-03 12:02:11 UTC | #5

You have the weirdest ideas.
If the script subsystem works on HTML then the editor would be viable. But for storage, you could add auto package loading to the editor and have people share .paks here on the forums. When I made my snake pak the editor had little regarding to package support and has to load them via console.

-------------------------

Modanung | 2020-08-03 13:27:26 UTC | #6

Ah yes, I hadn't even thought about the editor. Indeed there's *many* different possible forms, modules and levels of complexity to consider within this potential ecosystem.

Initially I think it would be neat if the Urho3D website were to host the latest version(s) of the _player_ along with a concealable text area and/or upload button for running scripts.

Ooooh, and (it) just (gets weirder;) imagine being able to embed scripts as a [onebox](https://github.com/discourse/onebox) on the forums! :crazy_face:

`https://player.urho3d.io?script=https://all.mine/craft.as&preview=default`

Any Discourse thread could be its own (themed and curated) arcade. This would ask for a preview image - defaulting to Urho3D logo with play button - which would be the only resources loaded until it is clicked[spoiler], and could possibly define the (clamped) ratio of the frame[/spoiler].

-------------------------

throwawayerino | 2020-08-03 13:06:54 UTC | #7

It doesn't get more ambitious than this! You pass a package(?) to the web build and it downloads/load scene.xml automatically. Once the urhobox project works out you have the most portable game engine ever!

-------------------------

Miegamicis | 2020-08-03 18:38:41 UTC | #8

Version 0.0001
Not a designer but some ideas about the layout would be great. For now focusing only on base functionality
![image|690x244](upload://z9ZGRS7i5r6GaZVicFlFTffhwDj.jpeg)

-------------------------

Modanung | 2020-08-03 22:45:57 UTC | #9

[quote="Miegamicis, post:3, topic:6294"]
I would estimate that it could take couple of weeks to make
[/quote]

Next day: "*Done!*" :wink:
Awesome.

[quote="Miegamicis, post:8, topic:6294"]
Not a designer but some ideas about the layout would be great.
[/quote]

Got repo?

-------------------------

Modanung | 2020-08-04 13:10:17 UTC | #10

@Miegamicis This thing needs a name. What do you think of the _Tank_?
It's something that contains fish *and* can be rolled out because it also holds an engine. :slightly_smiling_face:

[![](https://external-content.duckduckgo.com/iu/?u=https%3A%2F%2Famazingfishtanks.files.wordpress.com%2F2013%2F04%2Faquarium_prachtschmerle_neons.jpg)](http://www.mikseri.net/artists/urho/disciples-of-urho/417235/)

Of course, if anyone else has (better) naming suggestions, please _do_ share them.

-------------------------

Miegamicis | 2020-08-04 07:21:08 UTC | #11

> Next day: “ *Done!* ” :wink:
Awesome.

Well there's still a lot of things that needs to be added + debugging and finetuning will take the most time I think.

> Got repo?

Since I used already existing templates and libs the repo is bit of chaotic, will make it public sometime this week when there's something useful to actually use.

> This thing needs a name. What do you think of the  *Tank* ?

Sounds good.

-------------------------

Miegamicis | 2020-08-04 07:24:57 UTC | #12

btw I used this code editor https://microsoft.github.io/monaco-editor/
Looks like it has a support for LUA and maybe we can provide it for AS too.

-------------------------

Modanung | 2020-08-04 12:33:48 UTC | #13

[quote="Miegamicis, post:11, topic:6294"]
Well there’s still a lot of things that needs to be added
[/quote]

Yea I know, seemed like a big leap though.

[quote="Miegamicis, post:11, topic:6294"]
Since I used already existing templates and libs the repo is bit of chaotic, will make it public sometime this week when there’s something useful to actually use.
[/quote]
I can handle chaos, it's other people's _logic_ I don't follow... but I'll just sit back, then. :slightly_smiling_face: 

[quote="Miegamicis, post:12, topic:6294"]
[...] [https://microsoft.git](https://microsoft.github.io/monaco-editor/)...
[/quote]

:fearful:



GitLab uses [**Ace**](https://ace.c9.io/).

-------------------------

Miegamicis | 2020-08-04 12:48:28 UTC | #14

> GitLab uses [ **Ace** ](https://ace.c9.io/).

Since the editor is not yet fully integrated into the project, switching and testing out other options are easy. Already tried bunch of them but somehow didn't notice the `Ace` editor. Will give it a spin.

Also I'm using VueJS to put this all together.

-------------------------

Modanung | 2020-08-04 13:59:56 UTC | #15

[quote="Miegamicis, post:14, topic:6294"]
Also I’m using VueJS to put this all together.
[/quote]

What a beautiful list of [sponsors](https://vuejs.org/#sponsors) I've never heard of. :relieved:

The [first tank design](https://en.wikipedia.org/wiki/Leonardo%27s_fighting_vehicle) - by Leonardo da Vinci - was inspired by a turtle, btw. Bringing us back to the ocean.
[spoiler]...and Discword... :telescope:[/spoiler]

-------------------------

Miegamicis | 2020-08-05 20:39:26 UTC | #16

demo: https://urho3d-tank.frameskippers.com/
Still work in progress, but at least it's somewhat useful, very rough around the edges but maybe you'll understand how it works sooner or later.

Don't be shy to point out bugs!

![image|690x268](upload://7QLwyZfsQCy5NTYJxVUAKqFNXSj.png)

-------------------------

Modanung | 2020-08-07 01:47:43 UTC | #17

Quick mockup:

![mock0.001|690x323](upload://1RcHgYnSFSqsvmUvIxWzN1QfRWq.png)

-------------------------

Miegamicis | 2020-08-13 15:35:04 UTC | #19

So almost 2 weeks have passed since I and @Modanung  began working on a POC for this amazing idea. There was some bumps along the 
way but I believe the result for it is pretty impressive. You can check it out here: https://urho3d-tank.arnis.dev/

There are 3 seperate repositories for this tool:
1. The actual IDE: [Urho3D-Tank-Web-IDE](https://github.com/ArnisLielturks/Urho3D-Tank-Web-IDE)
2. The engine sample with required JS bindings: [Urho3D-Tank-Web-IDE-Sample](https://github.com/ArnisLielturks/Urho3D-Tank-Web-IDE-Sample)
3. The Tank design repo: [luckeyproductions/tank](https://gitlab.com/luckeyproductions/tank)

---

Some technical details:
* IDE uses [ACE](https://ace.c9.io/) editor
* Current implementation supports JSON, XML, GLSL, AngelScript file editing 
* All edited/created files are stored locally in the browsers local storage so you can save your progress between sessions
* You can download your progress as a ZIP archive which will contain all your edited files and the actual sample so the project can be used outside the Tank.

---

How to use it?
As a starting point I recommend opening already existing AS samples in the editor. Once you save it (either by pressing CTRL+S or using the UI `save` button) it will automatically mark it as an edited file, meaning that it will be automatically uploaded to the engine and the sample will be launched.

In the same way you can change any GLSL shaders, materials and some XML, JSON files but some changes may require you to restart the sample (by using the "Restart" button in the UI)


---

Some problems that are not yet solved:
* Scripts and shaders heavily rely on the built in filesystem to resolve the include statements. This means that the editor does not fully support creating new files which are linked together using the `#include` statements. Some changes to FileSystem are required to allow adding in-memory-only files to it. This is the main reason why LUA is not yet supported.
* There is of course some delay once the sample has been launched to allow the browser to upload all the required assets to the engine, maybe we should implement some sort of a loading screen in the sample before all assets are loaded and hide it once it's done

---

Possible future improvements:
* Usage of multiple browser windows to allow running the sample in one of them, and the code editor in the other with the help of websockets
* Project sharing between users - this would require some sort of backend database solution, but it's very doable
* Code complete for the GLSL, AngelScript and LUA files with the actual data from the engine.
* Binary file support to allow uploading textures, models, etc. dynamically
* File preview window - models, textures, materials

---

Overall I'm very happy with the results. The code might not be top quality, but this is just a POC to see if the proposed idea could work.

What are your thoughs on this? Is is usable? Would you use it? Is there something that you'd like to see in it?

-------------------------

lebrewer | 2020-08-28 16:27:06 UTC | #20

I think this is an amazing project that brings a lot of attention to the project. One could done a "play.urho3d.io" where anyone can see the engine in action and start prototyping. 

This is also great for sharing knowledge and debating implementations, since we can just link to a snippet from the forums, chat, discord, whatever.

-------------------------

Miegamicis | 2020-11-10 20:31:40 UTC | #21

Been working on this project lately and I have few updates for it:

**1. Javascript files are now supported**
If you add file with .js extension to the project structure, scripts are automatically launched on save.

**2. Resource loading over HTTP/HTTPS (in javascript files). Currently supports all files mentioned [here](https://urho3d-tank.arnis.dev/tutorial.txt)**
```
Module.LoadResourceFromUrl("https://urho3d.github.io/assets/images/logo.png","Textures/StoneDiffuse.dds");
```
**3. Resource loading from base64 encoded string (in javascript files)**
```
var content = "data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAQAAAAEAAgMAAAAhHED1AAAADFBMVEUAAAAA/wD/gAD///9GPgw8AAAAt0lEQVR42u3auw3DMAwFQC6pJbVkUhkwCH3iuDJ9ryShKwmJUHxuJgAAAAAAALwOaK01AADwLiBS8uFRHwAA1AX6KRERBzDqAQCAmsAxJHrKrH5GAABAPSA3RwcAAEBtIA+N86NiVct1AABQA+h/BgAA1AV24HTQAACAMsAvyOUbCgAAeByQFxCxyXaDAQAAygAr5NJGEwAAPBIYIbtsf0AAAIBSwOrxAQAA6gLLT82TOgAAKAV8AZOgiB0hDSCxAAAAAElFTkSuQmCC";
Module.AddResourceFromBase64("Textures/StoneDiffuse.dds", content);
```

**4. Sample used by the WEB IDE created as a separate subsystem**
All the functionality which is exposed in the IDE is also available for other platforms too, repo - [Urho3D-Dynamic-Resource-Subsystem](https://github.com/ArnisLielturks/Urho3D-Dynamic-Resource-Subsystem)

---

[Live demo](https://urho3d-tank.arnis.dev/)

-------------------------

Miegamicis | 2020-11-10 16:20:15 UTC | #22

Also I think I broke the project "Download" button since it doesn't copy all the needed files in the generated .zip archive.

-------------------------

Eugene | 2020-11-10 17:42:26 UTC | #23

How do you implement having both AS and JS in the same text file?

-------------------------

Miegamicis | 2020-11-10 17:55:15 UTC | #24

What? There Isn't such functionality. Did you find some weird bug or something? File extension is used to detect file type so it shouldn't be possible.

-------------------------

Eugene | 2020-11-10 18:03:56 UTC | #25

Sorry for crappy cut, but I was talking about it:
![image|434x500](upload://vSfVwEOpnc77uOoUiw8ba0rQzKm.jpeg) 

I got an impression that <line 35 is JS and >line 35 is AS

-------------------------

Miegamicis | 2020-11-10 18:16:20 UTC | #26

Oh this. It's jus a text file loaded from /tutorial.txt
It basically just shows working code snippets from some languages. It's meant as a README.
My designer skills are questionable so the look of it might not be clear at first.

-------------------------

Modanung | 2020-12-03 19:41:33 UTC | #27

I updated the [OP](https://discourse.urho3d.io/t/urho-tank-web-ide/6294) to include links to the repository and the design-focused instance. [:egg: ](https://tank.luckeyproductions.nl/)

[![](https://i.ytimg.com/vi/2RKUBgvHwtA/maxresdefault.jpg)](https://gitlab.com/luckeyproductions/tools/tank/activity)

Forward, ever forward! :wink:

-------------------------

Miegamicis | 2020-11-10 23:20:15 UTC | #28

Few hours later...

Added ability to share your projects via Github. Other git services will be added later because of technical difficulties.

To share a Github repository you must provide 2 arguments to the Urho Tank: 
* provider=github
* repository=username/repository_name

The link in the end would be https://urho3d-tank.arnis.dev/?repository=ArnisLielturks/Project-Sample&provider=github

There are 1 requirement for the shared repositories - it should contain `urho_tank.json` file which should have specific structure:

```json
{
  "name": "Name of your sample",
  "files": [
    "Textures/Mushroom.dds",
    "OtherFile/That/Should/Be/Added/To/Preview"
  ]
}
```
file array should be relative to the specific repository, see comlete sample [https://github.com/ArnisLielturks/Project-Sample](https://github.com/ArnisLielturks/Project-Sample)

Let me know if you notice any issues and/or have any questions or suggestions :slight_smile:

**Beware:** When loading other projects your local changes will be discarded

**Edit:**

1. I also think I fixed the download button.

-------------------------

brokensoul | 2020-11-19 12:57:35 UTC | #29

Actually, this project is a good idea to advertise Urho3d. Maybe you guys can send a link to GamesFromScratch so he can take a look

-------------------------

