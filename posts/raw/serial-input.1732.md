nicos | 2017-01-02 01:09:46 UTC | #1

Hello !
Firstly, I'm sorry you'll have to translate my poor english, and for my limited knowledge of 3D vocabulary  :blush:

I'm a Raspberry Pi fan, and I'm currently working on a "virtual puppet" project for a show.
I'm happy to see that a 3D Engine can run on it. I'ld like to thanks the Urho3D Team for that :slight_smile:

Is there a way to read serial input so as to move objects ? 
Do i need to extends or add functions to Input class and rebuilt the engine ?
Maybe someone has already code it ?
Any links to help me understand how to do it ?
Once done, how could I share it with you ?

Models have been made with Blender3d, and skeletal animation. There's a bone on the mouth to make it speak and turn head.
Will it work on Urho3D ?

Thank you, have a good day :slight_smile:

-------------------------

codingmonkey | 2017-01-02 01:09:46 UTC | #2

Hi, nicos!

[quote]Models have been made with Blender3d, and skeletal animation. There's a bone on the mouth to make it speak and turn head.
Will it work on Urho3D ?[/quote]

I suppose what for raspberry pi urho supports - 32 bones per skeleton (dx9-gl2.1 = 64 bones and gl3/dx11 - 128 bones )
also urho support morph target and probably you prefer use blender's Shapekeys to make face animation for character.

my test with shapekeys
[video]https://www.youtube.com/watch?v=QBnMz90g78Q[/video]
 

you may use AssetImporter for converts yours models into *.mdl format or urho-blender plugin

-------------------------

nicos | 2017-01-02 01:09:46 UTC | #3

Hi CodingMonkey !

Thank you for your reply !

I've ever coded a "test game" so as to learn how to deal with arduino. I've scripted it in Blender's game engine.

[video]https://vimeo.com/149532948[/video]

As you can see, the thought of the art director is to have a low-poly 3d rendering, because it will be better for the staging (we also work with old machines on the scene, and we'll have an old school computed soundtrack...)

I want to switch to raspberry bacause we want actors to move with their own controller and their own model on the scene, just changing HDMI cable on different TVs depending of where they are. (I'm not sure with the quality of this explaination...)
With your vid?o, I'm quite sure raspberry + Urho3d can deal with it. Thank you :slight_smile:

I just have to add code to the Input class of the engine to deal with serial connection.

Thank you Codingmonkey ! ! !

-------------------------

weitjong | 2017-01-02 01:09:47 UTC | #4

[quote="nicos"]I want to switch to raspberry bacause we want actors to move with their own controller and their own model on the scene, just changing HDMI cable on different TVs depending of where they are. (I'm not sure with the quality of this explaination...)[/quote]
Welcome to our forum. Interesting project. CodingMonkey is correct that Urho3D only support maximum 32 bones per model for Raspberry Pi platform. Other platforms at least have double that number. To answer your other questions. I don't think there is a need to rebuild (read customize) the game engine to have a custom serial input class, but that certainly is one way to go. For fast prototyping, I think you can just code in your application to override its main loop to read from a serial port in a non-blocking mode. i.e. reading serial port in between frame rendering. You should be able to find how to read a serial port using C/C++ easily on the web. And since Pi is so cheap and Urho3D supports client/server setup out of the box, probably you may consider to use two Pis per puppeteer and have them work in a client/server mode. The server connected with HDMI cable to TV set while the client connected with a serial controller and a Wifi USB double. Voila, untethered.

-------------------------

nicos | 2017-01-02 01:09:47 UTC | #5

Thank you wetijong.

 :blush: I'll put my serial read in the main loop, didn't though about it...
 
I previously thought about an Arduino <-> Raspberry system so as to set Raspi free from dealing with gyroscope and other hadware I/O.

Thank you

-------------------------

