kidinashell | 2021-07-09 18:47:52 UTC | #1

Hello y'all. I've been looking at Urho3D from time to time again and recently decided to give it another go to set everything up to feel comfortable in it.

Since I'm planning to use the Editor I set it up the way I wanted it to, which also included changing a little bit of the scripts themselves. Something I realized, after restarting the editor after some changes, which weren't "hot-swapped", that the sRGB setting or visualization doesn't work the way I would expect.

But first: Does sRGB in Urho3D mean the same as what sRGB mean in general in other applications/graphics settings etc? (e.g. sRGB -> RGB Full -> Black Level HIGH etc.)

With that in mind I have my systems and monitors always set up for RGB Full/Black Level HIGH.
So, with that in mind, the first time I started the editor everything looked fine, nothing washed out or anything. The sRGB setting in the editor settings was turned off and I let it stay that way for now, since I wanted to get to know the editor first.

When I started the Editor the next time, I saw immediately the typical symptoms of mismatched sRGB settings: washed out visuals. Especially on the UI it was prominently evident.

I checked the editor settings again and saw, that sRGB was now checked. I was kinda confused, because that would mean, that now sRGB would be active (in Full mode) and so would actually align with my graphics and monitor settings.

So I unchecked it, restarted the Editor again, but the same thing happened: washed out visuals, sRGB setting again checked (automatically).
I closed the editor, removed the Config.xml file and started the Editor again but still the same.

I thought maybe, that I had changed something during stumbling through the scripts but couldn't remember changing anything connected to sRGB or the settings loading procedure or anything like that. So I cloned the repository fresh to another location and tried it fresh out of the box: same behaviour.

Even tried another computer (also a Linux OS) but still the same behaviour.

Is it possible, that something checks if sRGB is available and sets it automatically and even disabling it doesn't matter on the next startup of the Editor?
And even if that was the case, I only get the right visuals if sRGB is disabled in the Editor, even though I run my things with sRGB enabled.

What I could find out is, that the setting of sRGB in the Config.xml does get set to true again on closing the Editor. I didn't see that in code or the scripts but I did the following:

* Set the sRGB setting in Config.xml manually to false
* Started the Editor (sRGB was enabled in settings and washed out visuals present)
* Unchecked sRGB
* Closed the Editor
* Checked Config.xml: sRGB is set to true

For a little comparison on how it looks just to make sure, I'm not crazy here and what I think to be the right visual is actually the wrong one.

First start of the Editor/or setting sRGB off manually affter each start (sRGB setting off, in contradiction to my graphics settings):<
_1st picture at the bottom, since I'm a new user (means only 1 embedded media)_

Second start of the Editor/or every start of the Editor (sRGB setting on automatically or manually):
_2nd picture at the bottom, same reason as above_

Also to make sure, I'm not looking at it wrong in any kind, I checked the image the EditorUI uses for it's symbols and background and it indeed does look like the first picture is how the editor is supposed to look like:
_3rd picture at the bottom, you know why_

So basically my question is, did any of you ever have that "problem", am I misunderstanding something about the use of sRGB in Urho3D? (If that's the case, it's still not that practical if the setting doesn't get saved or automatically assigned "wrongly")

I'm really sorry for that long post, but I just wanted to make sure I get as detailed as possible. Also, I'm not a native english speaker/writer and apologize for any mistakes.

Thank you very much in advance and I hope you all have a nice day :blush:

1 embedded media:
![urho3d_editor|458x500](upload://59b1TX1bV3B17Zu32Lna3lgI4iY.png)

-------------------------

Eugene | 2021-07-09 19:53:56 UTC | #2

[quote="kidinashell, post:1, topic:6914"]
am I misunderstanding something about the use of sRGB in Urho3D?
[/quote]
sRGB setting in Urho affects _only_ the physical format of back buffer texture.
Literally *nothing* in the rest of the engine handles it properly. Sooo... If you want to use sRGB, you need to build your assets around it. I.e. set sRGB in UI texture resource so UI changes are compensated. And in all other color textures as well.

[spoiler]Incorrect behaviour of sRGB and gamma correction literally triggered me to reimplement Urho renderer from scratch, so it's kind of sore point for me.[/spoiler]

-------------------------

kidinashell | 2021-07-09 20:12:36 UTC | #3

Ah ok, thank you very much for clarifying that :slight_smile: 
So I'll just work with the setting turned off then. Is it possible to keep the setting true or false without it checking or unchecking it automatically on each exit of the editor?

Edit: For now I'll just hardcode **`graphics.sRGB`** to **`false`** in **`Editor.as`**, I was just wondering if the saving of the setting is somewhat hinky.

-------------------------

