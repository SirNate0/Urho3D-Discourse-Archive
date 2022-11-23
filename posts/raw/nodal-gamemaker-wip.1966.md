dakilla | 2017-01-02 01:11:53 UTC | #1

Hi

I'm working on a tool that is both a gamemaker and a demomaker (a realtime animation editor/player).

It use a procedural nodal workflow to create and connect visual bricks ("operators") used to make complete 3d animated scenes from generating textures and meshes to post-processing and clip sequencing. (see original concept : [url]http://pcg.wikidot.com/pcg-software:werkkzeug[/url])

It's a cross platform project using Qt for the editor GUI. The nodal system and editor is based on the enigma studio code (a nice demotool released by Brain Control, a demomakers group see: [url]https://www.braincontrol.org/[/url]). Orginally it has an homemade engine based on dx11, that I replaced by Urho3D.

The project is at earlier step, but the editor and the nodal system is almost fully functionnal, I ported it on linux and fix it to work with urho.
The main work is to fix the editor and internal system to work with urho, build new nodals operators with Urho features and to build a player to replay scenes or play generated games.

[video]https://youtu.be/bN60-5zaNOY[/video]

-------------------------

weitjong | 2017-01-02 01:11:54 UTC | #2

Cool!

-------------------------

godan | 2017-01-02 01:11:54 UTC | #3

Love it! I have also been thinking a lot about node based workflows in app design lately - good to see that I'm not alone :slight_smile:

-------------------------

sabotage3d | 2017-01-02 01:11:54 UTC | #4

Great work! Are you planning on releasing a test version?

-------------------------

rasteron | 2017-01-02 01:11:54 UTC | #5

Looks great!

-------------------------

dakilla | 2017-01-02 01:11:55 UTC | #6

[quote]Great work! Are you planning on releasing a test version?[/quote]
Yes, I will release a test version as soon it will be more stabilized. I'll certainly need feedback about usage, so any help will be appreciated :wink:

-------------------------

boberfly | 2017-01-02 01:11:57 UTC | #7

Very cool dakilla!

I had a similar idea about using another node-based framework ([url=http://imageengine.github.io/gaffer/]Gaffer[/url]), but it looks like you've beaten me to it... :slight_smile: It also uses Qt for the UI, but it's fairly decoupled enough to use without the UI. 

It's very python though, I was going to use it to generate data for Urho and use the network replication to feed into a separate process and not be in the runtime... More of a set of tools for pipeline/dev work.

-------------------------

sabotage3d | 2017-01-02 01:11:57 UTC | #8

I am all for Gaffer is the best node based opensource framework. But this one looks quite cool as well.

-------------------------

umen | 2017-01-02 01:13:51 UTC | #9

@dakilla
i can't see the link to the video can you post direct link ?
also question :
how did you merged the Urho3d event loop and the Qt event loop ?

-------------------------

sabotage3d | 2017-01-02 01:13:52 UTC | #10

Any progress on this? I can't wait to try it out.

-------------------------

