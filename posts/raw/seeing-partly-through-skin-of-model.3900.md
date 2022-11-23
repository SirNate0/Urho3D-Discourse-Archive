CodeCrafty | 2017-12-30 01:19:39 UTC | #1

Hi I have a UrhoSharp app that when I load a model that has material list etc... 
All that loads, but there are aliasing artifacts and you can see, (just barely) through the skin to the other body parts (muscles veins etc...)

Why would my materials have a partial transparency?

![image|508x138](upload://8cblwb1i31849LxKW2uW5SFSTAN.jpg)

-------------------------

CodeCrafty | 2017-12-30 04:14:26 UTC | #2

Also: The model does NOT seem transparent when loaded into the urho editor and light added.

-------------------------

Modanung | 2017-12-30 09:06:59 UTC | #3

Did you add materials in the editor? [spoiler]Maybe material lists are not applied in-editor.[/spoiler]
The obvious path to take here, I'd say, is checking the materials in the material list. Although I'm not sure what artefacts you mean from the image. Since you speak of aliasing, did you add AA to the renderpath?
Any missing resources being logged?

Also, welcome to the forums! :confetti_ball:

-------------------------

