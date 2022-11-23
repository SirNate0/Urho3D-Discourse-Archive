Don | 2017-07-13 05:29:27 UTC | #1

Good evening,

I noticed that Urho has support for PBR materials (Thank you @dragonCASTjosh). I also noticed that there is support for high-precision framebuffers for HDR. I am in the process of converting my scene to PBR shaders and the HDR pipeline but I have been having some difficulties.

<img src="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/b8aa1333c1e6b372296d006084f2bb0600226d7f.jpg" width="690" height="388">

Clearly I must be doing something wrong here. (Note the low saturation) Right now I have the renderer set to hdrRendering=true and have appended BloomHDR and Tonemap to my render path.

I have read about the advantages of PBR (which in Urho seems to use IBL as well) and HDR in OpenGL rendering, but I am unsure as of now how to set up all my materials and coefficients correctly to achieve a satisfactory result.

In general, what I am asking is what is the current workflow in Urho for making HDR textures (such as skyboxes) and setting realistic lighting parameters. If there are any integral parts that are missing currently, I don't mind getting my hands dirty, but I would like to know before going further.

One last thing, are there any current large-scale projects using these sort of shaders that someone could point me towards for reference?

Thanks in advance,
-Don

-------------------------

Don | 2017-07-14 05:24:10 UTC | #2

Just bumping this thread.

-------------------------

dragonCASTjosh | 2017-07-17 11:44:02 UTC | #3

can you PM me a copy of your project so i can investigate deeper. Im also planning a full breakdown on how to use it soon i just need to find time

-------------------------

Don | 2017-08-14 01:38:17 UTC | #4

Sorry for the extremely late follow-up. We ended up resolving the issue (IIRC enabling gamma correction was involved).

-------------------------

dragonCASTjosh | 2017-08-14 09:48:37 UTC | #5

Gald you found a solution, i imagine it was more then just gamma correction that solved my assumption is the colour was being clipped as it fell outside of the colour space, but very unsure.

If there is anything you need adding to the PBR pipeline let me know as i will hopefully get time to work on it again after the 22nd, I first plan to improve area lights with what kojima productions covered at siggrapgh but anything else feel free to request.

-------------------------

Don | 2017-08-14 19:07:29 UTC | #6

I agree that gamma correction alone was probably not what fixed the issue (it seemed strange at the time).

On another note, I remember at one point you had mentioned generating cube maps from scenes in the editor. I was looking through the docs and didn't find anything related to this, but I do see an option in the editor for "Cubemap Gen Path". Could you shed some light on how to achieve this?

Thanks.

-------------------------

dragonCASTjosh | 2017-08-15 09:12:35 UTC | #7

Im supprised its not documented as cubemap generation as that was provided as part of the editor before i did PBR.

Under View/Editor Prefrences you need to set a path and size for the cubemaps, the PBR pipeline targerts 1024x1024. You then need to have a zone selected then go Edit/Render Zone Cubemap.

Once this is done it should spit out a cubmap in the directory selected, for the PBR pipeline to use it correctly it will need filtering exernally to the engine (filtering code is outside the scope of the engine from what i have been told)

-------------------------

