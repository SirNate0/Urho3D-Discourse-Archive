weitjong | 2019-06-30 07:32:40 UTC | #1

Since Lasse left the project there is nobody who has the same level of commitment and competency to fill his former role in the project yet. Still, the community has not stopped contributing to the project, albeit at much slower pace and (some might say) in lower quality. In the past it was also Lasse who assessed the readiness of the master branch before tagging it for release. So now I would like propose a change to make the quality of release becomes the responsibility of the community itself. English is not my primary language, so I hope I get my points across correctly.

The change should actually bring Urho3D project closer to other OSS  project doing the releases. Instead of tagging the master branch when it is deemed ready, it will be tagged as often as possible. The postfix of the tag ('-ALPHA' or '-BETA or '-RC') or the absence of it will indicate the maturity of the tags. In other words, do not expect future tags to always work out of the box for you, but instead you are encouraged to test out the tags against your own use case and platform, and send back bug fixes as PR timely if you want them to get fixed and incorporated in the next release. On the maintainer side, this tagging often does not actually add any significant work because our release/tagging deployment mechanism is already fully scripted/automated. And since the maintainers will be freed from the burden for the quality assurance, we would not hesitate to "click the button" for tagging more often than in the past. In the end of the day it is the responsibility of ALL to get the release right.

Some of you do not want to build on top a moving ground and avoid master branch. I have observed the download stats for release tag is always higher than the snapshot on any release (not just 1.7). So having a pre-release tag should hopefully address the concerns of these peoples. Getting the tags constantly push out should also give the impression that the project is still alive and hopefully that could attract a right person to fill the vacancy.

-------------------------

Leith | 2019-06-30 08:19:51 UTC | #2

Lasse has stepped down, but he has not left! It's nice to recognize that he does occasionally drop by, and still is connected to this work. I'm happy that you feel you can loosen the reins a little, and let the community have a proactive voice in the future direction of this engine. Nobody can really ever replace Lasse, but the spirit of Urho lives on.

-------------------------

weitjong | 2019-06-30 10:09:04 UTC | #3

If you don't know the fact about this project, you can keep your big mouth shut! I have getting tired of your antics. Considered this as my last warning to you (showing my staff color).

And in case you cannot read between the line, you will never be the one accepted to replace Lasse. Prove me wrong but so far what I can see from your posts were just noise and falsehood.

-------------------------

Modanung | 2019-06-30 10:23:40 UTC | #4

@weitjong I understand how @Leith's post might have come over as sarcastic, given your earlier encounters. But you seem to have read something between his lines that I do not see.

-------------------------

weitjong | 2019-06-30 11:10:18 UTC | #5

[quote="Leith, post:2, topic:5265"]
I’m happy that you feel you can loosen the reins a little, and let the community have a proactive voice in the future direction of this engine.
[/quote]

This is the line. Since when I/we have a reins over this project? It is an accusation that I won't accept. The truth is I have almost left the project too after Lasse left, but I find myself always come back to this project just to kill my time.

-------------------------

Modanung | 2019-06-30 10:37:12 UTC | #6

Maybe that _was_ a bad choice of words. I sure greatly appreciate how you've been around all this time to keep things running.

-------------------------

weitjong | 2019-06-30 10:38:08 UTC | #7

Probably I should kill my own time in my own fork.

-------------------------

Modanung | 2019-07-02 19:55:37 UTC | #9



-------------------------

throwawayerino | 2019-07-24 21:32:11 UTC | #10

When I first started I immediately downloaded the 1.7 release. The one with the gcc bug, old UI, and weird editor. Making releases a bit more frequent is definitely a good step

-------------------------

Modanung | 2019-07-25 10:27:09 UTC | #11

Changing the website to reflect common advice (to use the latest master) could also help.

-------------------------

throwawayerino | 2019-07-24 21:59:58 UTC | #12

And updating the wiki on github! No body likes to open a wiki and see WIP everywhere. I made the physics one and preparing to make an xml one

-------------------------

Modanung | 2019-07-24 22:07:22 UTC | #13

>「大事化小，小事化了」
"*Make big things small, solve the small things*"

-------------------------

weitjong | 2019-09-30 13:59:45 UTC | #14

Should we release the 1.8-ALPHA now or never?

-------------------------

Bluemoon | 2019-09-30 14:56:02 UTC | #15

I say we release it now :smiley:

-------------------------

Modanung | 2019-09-30 17:09:51 UTC | #16

To me, _now_ sure sounds better than _never_. :slight_smile:

-------------------------

weitjong | 2019-10-06 10:53:47 UTC | #17

OK. Ready or not the 1.8-ALPHA tag will be made tomorrow with whatever we have on the current master branch. I am retesting the `latest` (also tagged as `master`) DBE images after fixing a missing package issue causing failure in artifact upload. And also bumping the EMCC version for the Web platform.

EDIT: The new 1.8-ALPHA tag has just been pushed.

-------------------------

weitjong | 2019-10-06 16:05:37 UTC | #18

Unfortunately there was an issue with the site update task in the new docker container, so the alpha release was only partially completed. However, it is not the end of the world. Another attempt will be made again after the corrective measures are in place.

-------------------------

PsychoCircuitry | 2019-10-06 19:02:40 UTC | #19

Thanks for your continued efforts, weitjong. Looking forward to 1.8 alpha

-------------------------

weitjong | 2019-10-13 15:12:20 UTC | #20

You are welcome. I think I have fixed the site update issue while in tagging mode but I will only know that for sure after the next attempt. I plan to just re-tag the 1.8-ALPHA and force push it. But before I do that, I want to fix the Web CI build running out of time issue. The Web build using WASM is very slow. So much so that most of the time the Web CI builds were actually being terminated either by Travis or by our own script. It is so bad that the last successful build with complete Web sample upload was actually happened on August last year!

-------------------------

weitjong | 2020-01-13 01:46:54 UTC | #21

With new LLVM WASM backend the Web CI build is able to produce the build artifacts and upload them to main website within the CI build time limit. So, I am good to make another attempt to retag 1.8-ALPHA now. Or wait till we get the PR for the GLES 3 in and call it 1.8-BETA?

-------------------------

