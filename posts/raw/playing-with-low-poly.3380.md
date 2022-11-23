Victor | 2017-07-25 05:07:19 UTC | #1

So, I decided to explore a low-poly route for my game after being inspired by Kingdoms and Castles. I think the SSAO post process shader here: https://discourse.urho3d.io/t/ssao-post-process/2390, still needs a bit of work. So I'm trying to tweak it as much as possible.

(edit, updated sampling for SSAO)
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/10ea15f715c54a82395e38607dd2b8614a91dee8.jpg'>

-------------------------

bmcorser | 2017-07-25 09:57:21 UTC | #2

Looks nice. I like the UI styling :+1:

-------------------------

Victor | 2017-07-25 13:44:42 UTC | #3

Thanks @bmcorser!

For anyone interested, here are the tweaks I made to the SSAO shader. They're not crazy tweaks though, just changing the value, and removing the "depth" transition. I can't say I fully understand the shader, however the paper referenced in it does help. The low/high sample settings can cause a performance hit.

    #include "Uniforms.glsl"
    #include "Samplers.glsl"
    #include "Transform.glsl"
    #include "ScreenPos.glsl"
    varying highp vec2 vScreenPos;
    #ifdef COMPILEVS
    void VS()
    {
        mat4 modelMatrix = iModelMatrix;
        vec3 worldPos = GetWorldPos(modelMatrix);
        gl_Position = GetClipPos(worldPos);
        vScreenPos = GetScreenPosPreDiv(gl_Position);
    }
    #endif
    #ifdef COMPILEPS
    uniform highp vec2 cScreenSize;
    // Port from: https://github.com/jsj2008/Zombie-Blobs/blob/278e16229ccb77b2e11d788082b2ccebb9722ace/src/postproc.fs
    // see T M?ller, 1999: Efficiently building a matrix to rotate one vector to another
    mat3 rotateNormalVecToAnother(vec3 f, vec3 t) {
        vec3 v = cross(f, t);
        float c = dot(f, t);
        //float h = (1.0 - c) / (1.0 - c * c);
        float h = (c) / (c * c);
        return mat3(c + h * v.x * v.x, h * v.x * v.y + v.z, h * v.x * v.z - v.y,
                    h * v.x * v.y - v.z, c + h * v.y * v.y, h * v.y * v.z + v.x,
                    h * v.x * v.z + v.y, h * v.y * v.z - v.x, c + h * v.z * v.z);
    }
    vec3 normal_from_depth(float depth, highp vec2 texcoords) {
        // One pixel: 0.001 = 1 / 1000 (pixels)
        const vec2 offset1 = vec2(0.0, 0.001);
        const vec2 offset2 = vec2(0.001, 0.0);
        float depth1 = DecodeDepth(texture2D(sEmissiveMap, texcoords + offset1).rgb);
        float depth2 = DecodeDepth(texture2D(sEmissiveMap, texcoords + offset2).rgb);
        vec3 p1 = vec3(offset1, depth1 - depth);
        vec3 p2 = vec3(offset2, depth2 - depth);
        highp vec3 normal = cross(p1, p2);
        normal.z = -normal.z;
        return normalize(normal);
    }
    void PS()
    {
        const float aoStrength = 2.5;
        highp vec2 tx = vScreenPos;
        highp vec2 px = vec2(1.0 / cScreenSize.x, 1.0 / cScreenSize.y);
        float depth = DecodeDepth(texture2D(sEmissiveMap, vScreenPos).rgb);
        vec3  normal = normal_from_depth(depth, vScreenPos);
        // radius is in world space unit
        const float radius = 0.025;

        //float farClip = 1.0;
        //float nearClip = 0.1;
        //float zRange = radius / (farClip - nearClip);
        float zRange = radius / (cFarClipPS - cNearClipPS);
        // calculate inverse matrix of the normal by rotate it to identity
        mat3 InverseNormalMatrix = rotateNormalVecToAnother(normal, vec3(0.0, 0.0, 1.0));
        // result of line sampling
        // See Loos & Sloan: Volumetric Obscurance
        // http://www.cs.utah.edu/~loos/publications/vo/vo.pdf
        float hemi = 0.0;
        float maxi = 0.0;
        float screenSample = 2;
        int lowSample = -6;
        int highSample = 6;
        for (int x = lowSample; x <= highSample; ++x) {
            for (int y = lowSample; y <= highSample; ++y) {
                // make virtual sphere of unit volume, more closer to center, more ambient occlusion contributions
                float rx = 0.03 * float(x);
                float ry = 0.03 * float(y);
                float rz = sqrt(1.0 - rx * rx - ry * ry);
                highp vec3 screenCoord = vec3(float(x) * px.x, float(y) * px.y, 0.0);
                // 0.25 times smaller when farest, 5.0 times bigger when nearest.
                //highp vec2 coord = tx + (5.0 - 4.75 * depth) * screenCoord.xy;
                highp vec2 coord = tx + (screenSample * screenCoord.xy);
                // fetch depth from texture
                screenCoord.z = DecodeDepth(texture2D(sEmissiveMap, coord).rgb);
                // move to origin
                screenCoord.z -= depth;
                // ignore occluders which are too far away
                //if (screenCoord.z < -zRange) continue;

                // Transform to normal-oriented hemisphere space
                highp vec3 localCoord = InverseNormalMatrix * screenCoord;
                // ralative depth in the world space radius
                float dr = localCoord.z / zRange;
                // calculate contribution
                float v = clamp(rz + dr * aoStrength, 0.0, 2.0 * rz);

                maxi += rz;
                hemi += v;
            }
        }

        float ao = clamp(hemi / maxi, 0.0, 1.0);
        ao = mix(ao, 1.0, 0.4);
        vec3 finalColor = texture2D(sDiffMap, vScreenPos).rgb * ao;
        gl_FragColor = vec4(finalColor, 1.0);
    }
    #endif

-------------------------

Victor | 2017-08-01 09:00:26 UTC | #4

Finished up a few menus, working on the "in-game" map editing.

http://i.imgur.com/cDAAcBd.png

-------------------------

Victor | 2017-08-04 08:22:38 UTC | #5

New color correction and water shader. Also tweaked the values a bit more on the ambient occlusion shader. Wrapped up the map editing system as well, so this weekend I hope to start adding some characters onto the map.

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/6f1cf15c2f1d37b673dcc444d6530bd0558b4e54.png'>

-------------------------

Victor | 2017-08-07 05:43:16 UTC | #6

Over the weekend I decided to use textures for the map instead of solid colors. So now the forest area has more of a dirt texture than a grass texture. However, the buildings will still remain texture-less, and I'll just use the material colors.

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/e8d98f7f0dfa700fd897ac0f74c2b873171544a5.jpg'>

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/6ac44653342ee143ba47ff1629d05fd9e0575843.jpg'>

-------------------------

Modanung | 2017-08-07 08:08:51 UTC | #7

Looking really nice!
Maybe cut down on the AO a bit?

-------------------------

Victor | 2017-08-07 10:52:48 UTC | #8

Yeah, I believe you're right! In my settings.txt file I've added a "high, medium, low" AO setting for anyone to adjust to their taste (or increase FPS on their machine). There is a setting to turn it off completely as well. :-D

-------------------------

Modanung | 2017-08-07 11:55:03 UTC | #9

[quote="Victor, post:8, topic:3380"]
There is a setting to turn it off completely as well.
[/quote]

I do think it adds a lot, but to me it feels wrong for the AO around the buildings to be darker than the shadows.

-------------------------

Victor | 2017-08-07 12:10:45 UTC | #10

Ah, I see what you're saying. Yeah, last night I did make a change to the shadow intensity, but I didn't adjust the AO along with it. I'll try to fix that this week.

-------------------------

smellymumbler | 2017-08-07 13:13:32 UTC | #11

That's so beautiful! Is that cursor pointer a 3D model? If so, kudos for the creativity!

-------------------------

Victor | 2017-08-07 23:13:15 UTC | #12

I cannot take credit for the 3D cursor, that along with the shore edges were inspired by Kingdom and Castles (equally beautiful game). However, my game isn't a city builder, but rather a strategy game. Thanks for the compliment, I wish I could take 100% of the credit :-D

-------------------------

Victor | 2017-08-15 04:46:11 UTC | #13

Been having a lot of fun scripting out some characters and events. This weekend I should proper cities and bandit camps in place.

The northmen know not yet how to die...

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/1b8fc61cdf2a9c1d55f2af005217b10c7f8e2777.jpg'>

But soon they'll know some fear

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/6079a86baef77129042044d165d2f5746d768c3f.jpg'>

-------------------------

Victor | 2017-08-20 16:59:41 UTC | #14

Thinks are starting to feel more like a fully playable game. This week has been redoing/finishing a lot of the UI. Icons are from http://game-icons.net which has one of the best icon repository of icons I've seen :slight_smile:

The city walls are still a work in progress, but I thought I'd display the progress.

[url= http://i.imgur.com/HAbC4Ns.png][img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/82aa99a6478c3cf75edf4033b2b4e260444b780a.jpg[/img][/url]

-------------------------

Don | 2017-08-24 18:14:49 UTC | #15

That UI looks excellent! Is it using the built-in Urho UI system with different textures, or is it entirely separate?

-------------------------

Victor | 2017-08-24 20:01:01 UTC | #16

Yes, this is using Urho's UI :) 

It's mostly just coloring with BorderImage for the icons. To create elements however, I actually created my own scripting engine (before I even knew about Urho) to handle building out and positioning the UI.

So my ui scripts look something like this (which is used to build out the UIElements)

https://gist.github.com/victorholt/d1321c8d3623e167c029e1604b424d44

-------------------------

Victor | 2017-09-17 14:25:29 UTC | #17

I haven't updated in a while, figured I would today. Been mostly working on the different interfaces for the game. Very much inspired by the CK2 style.

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/3f747d9ee823adf86c0dba95baeee38dfd0f0889.jpg'>

<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/0de0e02e6614a8afd1c1c4ac4438ec32004efe25.png'>

-------------------------

TrevorCash | 2017-12-02 18:54:10 UTC | #18

This looks like an awesome project!

-------------------------

voidhawk | 2018-03-09 07:43:29 UTC | #19

Hey this looks really nice!

-------------------------

