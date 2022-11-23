Bluemoon | 2017-01-02 01:01:59 UTC | #1

After switching to Urho3D as the game of choice for A Game Project I conceived, I found out that making a simple tutorials would go a long way in helping out those that I will be collaborating understand the basic nuts and bolts of Urho3D. I decided to make a very simple game for the tutorials and share it with everyone. I call it "Drone Anarchy"  :smiley: . It's done in Angelscript but will be translated later to C++ later.

I tried to get it up on GitHub, but just realized that I was still new to that area  :neutral_face: but none-the-less here is a zipped file link for it and some screen shots
[url]https://www.dropbox.com/s/ezt8bsoyjro6x1u/DroneAnarchy.zip?dl=0[/url]

[img]http://i.imgur.com/uRMkjTl.png[/img]
[img]http://i.imgur.com/CAN7hPW.png[/img]

Additional Info are contained in the Readme.txt file. My Gratitude to the Wonderful Urho3D Devs  :smiley:  :smiley:  :smiley:

-------------------------

Bluemoon | 2017-01-02 01:02:12 UTC | #2

I was finally able to make out time to write the C++ implementation of Drone Anarchy as well as creating a GitHub repository for the Project [url]https://github.com/DARKDOVE/Drone_Anarchy[/url]

-------------------------

cadaver | 2017-01-02 01:02:14 UTC | #3

Very nice, thanks for sharing!

-------------------------

Bluemoon | 2017-01-02 01:02:14 UTC | #4

[quote="cadaver"]Very nice, thanks for sharing![/quote]

You are welcomed

-------------------------

sabotage3d | 2017-01-02 01:02:14 UTC | #5

Great work ! Looking forward to try it out :slight_smile:

-------------------------

Bluemoon | 2017-01-02 01:02:27 UTC | #6

[quote="sabotage3d"]Great work ! Looking forward to try it out :slight_smile:[/quote]

Thanks  :slight_smile:

-------------------------

Bluemoon | 2017-01-02 01:02:28 UTC | #7

I've added logic component implementation of the script object in the C++ source with a [code]#define USE_SCRIPT_OBJECT[/code] which determines whether to build using script object or logic component

-------------------------

Bluemoon | 2021-01-15 09:52:17 UTC | #8

Drone Anarchy is now on the web, thanks to the wasm build of Urho3D :blush:. 

You can try it out [here](https://www.bluemagnificent.com/drone_anarchy) 

Tested on Firefox and Chrome

-------------------------

Eugene | 2021-01-15 15:44:33 UTC | #9

Not gonna discuss gameplay and stuff, but on technical side two aspects are missing:

1) Some kind of particle fade-out to help player measure distance
2) Some kind of hit feedback to help player understand hitboxes

-------------------------

Bluemoon | 2021-01-18 09:02:26 UTC | #10

Yeah the hit feedback is definitely necessary, I would look into it in the coming days.

This had actually been an abandoned project I just woke up to , so it's still lacking in a couple of things :sweat_smile:

-------------------------

