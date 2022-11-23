cadaver | 2017-01-02 01:04:53 UTC | #1

Any opinions on when the next release should happen? Some things that may or may not happen in the near future, but I don't think any of them are necessarily blocking: (feel free to add to the list)

- The DetourCrowd PR should be coming soon
- I may yet investigate the Emscripten mouse locked mode, which I had some odd issues with
- Freeform vertex declarations is listed on the issue tracker, but it's a fairly major change and in some ways complicating and experimental (as it affects things like vertex buffer binding and morphs), so it can be pushed until later
- Some third party libs are about to update soon, like SDL and AngelScript, but naturally yet another new version can also be made after they update, on a quicker cycle

-------------------------

yushli | 2017-01-02 01:04:53 UTC | #2

looking forward to the new release. Hope to see it soon.

-------------------------

sabotage3d | 2017-01-02 01:04:53 UTC | #3

Are the physically based shaders from hd_ ready to be integrated into the next release ?
Scorvi samples looked like a really nice addition as well.

-------------------------

alexrass | 2017-01-02 01:04:53 UTC | #4

As many have wide monitors, you can use the tweaks from this post [url]http://discourse.urho3d.io/t/some-editor-tweaks/976/1[/url]

-------------------------

cadaver | 2017-01-02 01:04:53 UTC | #5

About the Scorvi samples: for inclusion in Urho3D repo itself, they should be submitted as a pull request. However we already have too many samples for the CI architecture to cope with reliably, so simplification and condensing of existing examples would be necessary first. Also there is nothing wrong with additional examples existing elsewhere outside the main Urho repo.

-------------------------

Mike | 2017-01-02 01:04:53 UTC | #6

I think it's time for a new release, there will always be some good reasons to postpone.

-------------------------

thebluefish | 2017-01-02 01:04:53 UTC | #7

[quote="cadaver"]- Some third party libs are about to update soon, like SDL and AngelScript, but naturally a new version can also be made after they update, on a quicker cycle[/quote]

IMO I believe it would be better to release a new version before integrating newer versions of these libraries. Stability is preferred over bleeding-edge features in my eyes.

I believe that we should push to identify and fix as many bugs as possible for a good, stable release.

-------------------------

cadaver | 2017-01-02 01:04:53 UTC | #8

Good point. There's one thing however that since some people are always using last stable release, we'll get a lot more testing (and possible new issues) after the release :wink: But that's life, there will be always the release after.

-------------------------

friesencr | 2017-01-02 01:04:53 UTC | #9

The nim guys use stable.  Getting the emscripten fix would be good for them if you have time.

3rd party libs i would like to see updated are stb_image and stb_image_write.  There has been some SSE additions to stb_image, I don't know if how that affects the build.  PNG decoding is like 2x faster \m/

Urho keeps getting more feature rich but is still as small as I want it to be.  Unrelated, I have some work I am looking forward to sharing with everyone hopefully next month some time :smiley:

-------------------------

GoogleBot42 | 2017-01-02 01:04:54 UTC | #10

[quote="cadaver"]Any opinions on when the next release should happen? Some things that may or may not happen in the near future, but I don't think any of them are necessarily blocking: (feel free to add to the list)

- The DetourCrowd PR should be coming soon
- I may yet investigate the Emscripten mouse locked mode, which I had some odd issues with
- Freeform vertex declarations is listed on the issue tracker, but it's a fairly major change and in some ways complicating and experimental (as it affects things like vertex buffer binding and morphs), so it can be pushed until later
- Some third party libs are about to update soon, like SDL and AngelScript, but naturally yet another new version can also be made after they update, on a quicker cycle[/quote]

I would really like to see mouse locking working in Emscripten.  :slight_smile:
DetourCrowd would be nice too but I think Emscripten is a must.  :stuck_out_tongue:

-------------------------

weitjong | 2017-01-02 01:04:55 UTC | #11

I don't think we have anything blocking on the issue trackers. Having said that, I see Apple just released their Xcode 6.3.1 and from issue [github.com/urho3d/Urho3D/issues/709](https://github.com/urho3d/Urho3D/issues/709) we know newer Xcode version does not like how we setup PCH for Assimp library. It may be nice to have it sort out before the release though.

On my side when my time and health permit, I am experimenting on the Angelscript scripting support for Emscripten. I don't want to raise any false hope as you know from my track record, so the work may not see the light of day and end up in my git stash instead.

-------------------------

gokr | 2017-01-02 01:04:55 UTC | #12

Hi all!

[quote="friesencr"]The nim guys use stable.  Getting the emscripten fix would be good for them if you have time.[/quote]

Yes, Urhonimo (Nim wrapper for Urho3D) is mainly autogenerated and will eventually be 100% autogenerated - but currently its not so we are basically waiting for a new release before we redo it.

We don't yet use emscripten though (?). And as a sidenote, we are very happy so far with Urho3D. We have made some tweaks, but not something someone else would benefit from, and eventually we will push some of it upstream - like being able to have Urho3D render "offscreen".

regards, G?ran

-------------------------

hdunderscore | 2017-01-02 01:04:55 UTC | #13

[quote="sabotage3d"]Are the physically based shaders from hd_ ready to be integrated into the next release ?
Scorvi samples looked like a really nice addition as well.[/quote]
This isn't and won't be ready for any near release, sorry ! Busy with a university project this semester.

-------------------------

sabotage3d | 2017-01-02 01:04:55 UTC | #14

Would any of the new UI library integrations in Urho3d ready for merging into next release or they are going to be kept separate as add-ons ?

-------------------------

cadaver | 2017-01-02 01:04:55 UTC | #15

If we get a PR which satisfies the requirements for inclusion in the core in a very short time, then yes :wink:

However I don't think any of them are in that state. It's not trivial to integrate external UI libraries to e.g. scripting & events seamlessly; this has been discussed before. Basically, by making Urho so cohesive & tightly bound package, we've raised the bar very high for UI library integrations. The story would be different if Urho was just a loosely bound collection of libraries. 

When the UI library addons remain separate, that can actually be a good thing, as then users can choose what level of readiness they expect, and our QA burden (considering that we haven't suddenly gotten more core contributors) is not increased.

-------------------------

sabotage3d | 2017-01-02 01:04:55 UTC | #16

What about adding SVG support into the existing UI library ?
For example Scorvi's : 
OpenVGRenderer
NanoSVGRendering

Then we can use vector images for the UI or I am missing something ?

-------------------------

cadaver | 2017-01-02 01:04:55 UTC | #17

The NanoVG example seems to be OpenGL only, and the example seems to be hardcoded (if I don't understand wrong)

The NanoSVG example rasterizes to an image on the CPU, and creates an ordinary UI sprite element, which looks like a much more portable approach. This would just need some more effort by Scorvi to make it fitting for Urho library integration; in fact the support could be added to Image class to make the svg's available for both UI & 3D rendering.

-------------------------

boberfly | 2017-01-02 01:04:56 UTC | #18

It would be amazing to get Emscripten in there that's stable!

The PBR/IBL stuff would be a great addition but I'd assume it would change too much stuff and might cause regressions. I think it's easy enough to integrate to your own packages for now, it's mostly data right?

Not to go off-topic, but both those techs could make something like this, or perhaps something even better than it with animation:
[viewer.marmoset.co/test/gdcgallery.html](http://viewer.marmoset.co/test/gdcgallery.html)

Which would be fun!

-------------------------

boberfly | 2017-01-02 01:05:00 UTC | #19

Hi Sinoid,
[quote]I don't think anyone has any PBR or IBL that's anywhere near complete enough for inclusion into master.[/quote]
Agreed. Although I did a rebase of hd_'s stuff and just mapped the new texture defines to make the HLSL work in both DX9 & DX11 but it is untested as I'm in Linux atm. I'll push my changes to my branch when I get home if anyone wants to play around with it. Definitely not in a state to push to mainline yet. :slight_smile:

-------------------------

friesencr | 2017-01-02 01:05:01 UTC | #20

The changelog captain,  I don't think she can take any more!  Divert power from the rear deflectors to shipping!

-------------------------

GoogleBot42 | 2017-01-02 01:05:01 UTC | #21

[quote="friesencr"]The changelog captain,  I don't think she can take any more!  Divert power from the rear deflectors to shipping![/quote]

 :laughing: I agree.  I think all focus (with DetourCroud now added) should be on fixing bugs and getting the next version out there.    :slight_smile:

-------------------------

Hevedy | 2017-01-02 01:05:02 UTC | #22

It's there news about the PBR ?

-------------------------

cadaver | 2017-01-02 01:05:03 UTC | #23

Ok. I've investigated the pointer lock mechanism with windowed mode Emscripten. Fundamentally there's nothing wrong with the Emscripten-facing code, but there's some mismatches happening with Input::SetMouseMode(); it already checks if the same mouse mode is set and does not initiate the mouse locking request in that case. By making a few tweaks I managed to get it working, but the user experience is still rather poor, as the browser pops up a window (in its own top-left) that asks whether you allow the mouse to be hidden / tells you it's going to be hidden. It's a rather poor match for example to the frequent cursor hiding / showing we do, when we show the Urho console. Therefore, at this point I'm not going to commit any changes, I'll rather defer them to hd_ who architected the mouse modes system, and the Emscripten input improvements.

In light of this, from my point of view there's nothing holding back the release, but I committed some texture format related changes today so waiting a day or two for possible further issues to be found may be wise.

-------------------------

thebluefish | 2017-01-02 01:05:03 UTC | #24

FYI I believe someone mentioned in IRC that gray scale images were broken recently, producing some odd results that were resolved by converting to RGB. Personally I haven't had the time to test this myself. I don't see any issues mentioned with it, so wanted to bring this up.

-------------------------

cadaver | 2017-01-02 01:05:03 UTC | #25

That was D3D11 / OpenGL3 specific and was reported twice as an issue in github. It should be fixed now.

-------------------------

cadaver | 2017-01-02 01:05:05 UTC | #26

I committed an initial changelog for the new version. Feel free to amend. Particularly the build system & Urho2D changes would benefit from being more accurately listed.

-------------------------

weitjong | 2017-01-02 01:05:06 UTC | #27

I have supplemented a few entries related to the build system. Speaking of which, there is a bug presently in our build system which prevents it from generating project file correctly with ccache support enabled on Mac OS X host system. I have a working patch but it is still in my own fork. I will merge that in later today. With a little hack I am able to make xcodebuild uses ccache too in my VM. I am currently working on reproducing that on Travis CI VM.

There is one pending update left to do on the build system for supporting shared data file for Emscripten platform (using Emscripten's file_packager.py). I have submitted a PR to Emscripten upstream ([github.com/kripken/emscripten/pull/3410](https://github.com/kripken/emscripten/pull/3410)) to avoid unnecessary costly re-link when repackaging the shared data due to changes in the resource dirs being detected by build system. Judging from the last comment from Alan Zakai, I am confident that the PR will be merged into upstream's incoming branch shortly. The thing is, I can only update the Emscripten version check correctly to enable this file_packager.py option when the PR is merged and tagged. However, this is not critical, so I think you should release Urho3D when you feel it is ready. Emscripten build is anyway only experimental and users who could get caught in between version are those using Emscripten's incoming branch (unstable).

-------------------------

cadaver | 2017-01-02 01:05:06 UTC | #28

I'll wait until the navigation PR is in good shape and merged. Also found a relative mouse mode bug on OSX, which I fixed but probably broke Emscripten in the process, but that should be sorted out today.

-------------------------

