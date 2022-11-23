orefkov | 2018-10-21 17:40:18 UTC | #1

Hi All!
I present my new game - “Brick Break”.
There is old classic puzzle game, moved to 3D, in graphics and gameplay.
[Link to Play Market](https://play.google.com/store/apps/details?id=com.horovo.games.bb.r)

Gameplay video

https://www.youtube.com/watch?v=9WngvCc_Toc

[details="Screenshots"]
![Screenshot_20181015-000046|690x388](upload://qfcNfcrG8l3Tvsbv4ASA5t5oh5l.png) 
![Screenshot_20181015-000518|690x388](upload://leulPB4EvTvr8FwyF8Z1hTU57lp.png) 
![Screenshot_20181014-235951|281x500](upload://iNr10zauhuEnJV5KOvAqH2gWxNN.png) 
![Screenshot_20181015-000355|281x500](upload://8qOZdkcYsVPhWRBjCZHl7cKVut4.png) 
[/details]

Game implemented on AngelScript + Urho3DPlayer.
Later I will github sources - scripts itself and my changes in Urho3D engine.
If there are technical questions on the implementation of the game - I am ready to respond.

From the interesting features of the game I want to note
- 14 procedural live GPU-calculated backgrounds.
- Custom shaders for rendering tiles, optimizing for mobile performance.
At the beginning every tile has model with three materials with different diffuse and specular colors and rendered in 3 drawcalls. Later colors was be assigned to vertexes as attributes, and render at one drawcall. This led to the need to write custom shaders as the standard did not support the work with two colors at the vertex. It also took to create a utility that converts a model of three materials into a model with one material, recording the colors of the materials into vertex attributes. Thanks to the excellent support of scripts, this utility also turned out to write on the AngelScript.
- Pseudo "instancing" for rendering tiles on edges of cube.
Initially, each edge was drawn as 24 individual tiles, because each could have its own color, and the tiles could move. OpenGL ES 2.0 does not have instancing support, and it requared 24 (at the very beginning, even 72) drawcall for each edge - very bad. Therefore, for the cube edge, one common model was created, in which an attribute — the tile index — was additionally set for the vertices of each tile. After that, uniforms were transferred to the shader - an array of 24 vec2, in which the index of the tile color was specified in X, from 0 to 5, and in Y - whether this tile should be drawn at all (0 or 1). The values of colors themselves were transmitted in another uniform. When the tiles on the edges moving, in shader of edge is transferred not to draw this tile, and on this place an individual tile is rendered. This is reduces drawcals for each edge for only One.
- Support in shaders of 3 variants of graphics quality, which user can switch in game settings. Also enable 4Xmsaa in screen mode.
- Integrate android billing and ads. For ads using appodeal sdk, integrating many ads network, also supported admob and unity ad. For appodeal native ads I was able to render native advertising in the game space - on blank cube face. All billing and ads game logic implemented also on AngelScript, java-part of the game only transmit events to urho engine. In Urho3D was added "mbedtls" library for verifying purchase's rsa-signature also in script, not in java-side.

-------------------------

orefkov | 2018-10-24 10:58:35 UTC | #2

Release new version - added "replay mode". Allow look at your gameplay in quick automatic mode.
Make more detail video about it.
https://www.youtube.com/watch?v=pjNWdPVtqwQ&feature=youtu.be

-------------------------

yushli1 | 2018-10-24 14:04:01 UTC | #3

That looks like a nice game. When do you think the source code will be available?

-------------------------

orefkov | 2018-10-24 17:49:42 UTC | #4

First I want make integration with google game services, refactor and clear code. And when install count will be at least 10K :) Optimistic - one month.

-------------------------

yushli1 | 2018-10-25 06:24:43 UTC | #5

Thanks for the information. Wait for the good news. :grinning:

-------------------------

orefkov | 2018-10-25 12:01:24 UTC | #6

For those who just watch the game.
This is a version for Windows - https://yadi.sk/d/J1Um36rBtzh4bw
Just unzip and run Urho3DPlayer.exe.
There are no advertisements or purchases - every time you start, the number of coins is set to 10,000. Hopefully enough :slight_smile:

-------------------------

yushli1 | 2018-10-26 04:41:11 UTC | #7

Thank you for sharing this!

-------------------------

Zamir | 2018-10-30 06:17:05 UTC | #8

But I can’t finish my version of the same game)
https://gyazo.com/a1f10acc5b1aa2d0ce264b1e0e3b5a5f
https://gyazo.com/87c9dc328623101c7b753e9d5e9ea951

-------------------------

orefkov | 2018-10-30 08:16:51 UTC | #10

Great job!
At the beginning (and in the source code, the name still remains) were not "bricks", but "crystals". But I was afraid of performance and battery problems on mobile devices.
Backgrounds yes, from shadertoys. 
Also, to avoid performance problems, they are rendered 30 times per second into a texture four times smaller than the screen (width / 2 x height / 2), and in each frame is simply copied to the background.

-------------------------

Zamir | 2018-10-30 08:36:08 UTC | #11

my version on android 120 FPS (Samsung note 3), but I do not like how it looks, in search of more)

I experimented with shadertoy and shaders with time inside, the pixels gradually turn into cubes, did not meet this - if so how did you win?

-------------------------

orefkov | 2018-10-30 09:04:45 UTC | #12

Due low precession of float on mobile devices, when direct use "time" for animate. In my backrounds parameter for animate slowly changed from 0 to 30 and back from 30 to 0.

-------------------------

orefkov | 2018-11-07 12:05:40 UTC | #13

Update release to 1.8.
Make integration with Google Play Games services - added achievements and leaderbords.
Implements work with subscriptions in billing. Fix some errors.
The total number of installations reached aprox 1.4K. Almost all came from Google ads, which spent about $ 55.
On advertising earned 10 cents, on IAP - 0.

-------------------------

orefkov | 2019-11-21 06:49:25 UTC | #14

Update game to version 1.18.
- Added the ability to select the cube size from 7 to 10, and the number of tile colors from 5 to 8.
- API chages to GLES3, now with instancing all tiles draws at one drawcall, and all edges at another one.
- Fixes UI elements for FHD+ screens.
- Added support for real fullscreen on devices with display cuts, old version was letterboxed.
- Remove Appodeal SDK for ads, use only google admobs.
Feel free to leave feedback and ratings in the playmarket :)

-------------------------

orefkov | 2019-12-19 23:17:09 UTC | #15

Planned release in Steam 2019-12-27
https://store.steampowered.com/app/1203310/Tiles_Shooter_Puzzle_Cube/
Already does not use the Urho3DPlayer, its own executable is made. Part of the logic has been ported to C++, but the main one is still an AngelScript. Integrate Steam library - overlay, achivs, stats, purchases.

-------------------------

QBkGames | 2019-12-20 03:27:45 UTC | #16

Congratulations for the game release! Looks nice and colorful :slight_smile:.

Personally, I would reword the sentence "A simple puzzle that allows you to pass the time.", to something more exciting like "A cool puzzle on the surface of a 3D cube." or leave it out all together, as it sounds like it's a game for old retirees who have nothing to do all day (unless it actually is for them) :stuck_out_tongue: .

How difficult is it to integrate Steam library into Urho?

-------------------------

orefkov | 2019-12-20 06:02:26 UTC | #17

Thanks for the tip, I will change the description of the game as you advise.
Integration with steam was not difficult - their library was originally designed for C / C++, the API was well documented, and the interaction model was well based on the one adopted in Urho3D. The necessary actions are called directly immediately, and information about events comes in callbacks. For Steam to call all registered callbacks, it was enough to do

    SubscribeToEvent(E_ENDFRAME, [&](StringHash, VariantMap&) {SteamAPI_RunCallbacks ();});

Next, in the called callbacks, we use the usual Urho3D SendEvent to all interested subscribers.

-------------------------

