pleduc | 2019-03-20 15:00:46 UTC | #1

hye, i test the master with the last apple ios sdk 12.1,
and i see this, on device and simulator: 

     the gl context is not adjusted to screen...

![55|690x368](upload://ezHaIGcQ3pPKV8TYnNjYKYmdwLk.jpeg) 

on any device/simulator version or format.
i do not remember this behaviour last time i check...
is it a known issue this last apple sdk update ?
thanks

-------------------------

weitjong | 2019-03-21 00:19:12 UTC | #2

[quote="pleduc, post:1, topic:5041"]
the gl context is not adjusted to screen...
[/quote]

Is that the exact message string you saw? Where did you see it? Urho3D log or Apple own diagnostics? Never seen that before, but I haven’t upgraded to latest SDK yet.

-------------------------

pleduc | 2019-03-21 11:17:29 UTC | #3

it's not a log, sorry, just an highlight.
is this behaviour normal ? i get a same behaviour on 1.7 tag and master on last apple sdk/xcode.
i also get  a issue on native macos, where i need to move one time the window to get the render visible in it after a sample launch...
i hope this will be noticed by others. not sure how to help solve both points.
i could try to look deeper ( SDL cocoa update ? ).

-------------------------

weitjong | 2019-03-21 11:31:58 UTC | #4

For sure it is not supposed to be like that. You can check the log which should state the screen mode being chosen for your display device and verify that against your expectation. Usually the “fullscreen” flag should take care of this, not sure why it didn’t for your case.

-------------------------

weitjong | 2019-03-21 12:17:38 UTC | #5

I am commuting but I just quickly browsed the code in our repo, the fullscreen flag is added programmatically based on the compiler define condition. Which come back to my initial hunch in your other thread about your build that it has a problem with compiler defines not correctly set.

-------------------------

pleduc | 2019-03-21 12:53:18 UTC | #6

i am just testing the urho3d project samples there, not my surcharge ( working well all platform now ).
i checked the fullscreen flag too:
on simulator xr (screenshot):

> Set screen mode 960x640 fullscreen monitor 0 resizable

i ll try to downgrade sdk, but it seems to be a regression introduced by the last sdk.

-------------------------

weitjong | 2019-03-21 14:18:07 UTC | #7

I see. Sorry for jumping conclusion.

-------------------------

pleduc | 2019-04-03 14:44:51 UTC | #8

well for update, adding on my plist

> <key>UILaunchStoryboardName</key>
> <string>Storyboard</string>

did the trick...
i did not test on urho3d samples for now !

-------------------------

weitjong | 2019-04-03 16:43:38 UTC | #9

Thanks for the update. The current plist that we have for iOS was copied (with slight local adaptation) from CMake (or from somewhere else, I am not that sure now) quite some time back and has not been synced ever since. PR is welcome.

-------------------------

