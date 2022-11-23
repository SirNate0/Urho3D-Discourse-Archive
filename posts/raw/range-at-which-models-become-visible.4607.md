mrchrissross | 2018-10-29 23:51:21 UTC | #1

Hi everyone,

I'm creating a space game and i want to increase the range where models become visible. Currently if I start the game, everything that close by is visible and if I slowly go backwards a shadow falls over them as if fogged over. How can I increase the range? or possibly disable it?

I've tried increasing or decreasing the functions below:

    zone->SetFogStart(100.0f);
    zone->SetFogEnd(300.0f);

However this does not work so I think I may be wrong.

I've looked in the samples and it seems that some of them do not fog over when at a great distance but I was unable to find out how this happens.

Thanks,

-------------------------

Modanung | 2018-10-20 16:19:02 UTC | #2

Did you increase the camera's far clip as well using `Camera::SetFarClip(float)`?
Also, welcome to the forums! :confetti_ball: :)

-------------------------

mrchrissross | 2018-10-20 16:26:06 UTC | #3

Thanks for the welcoming :slight_smile:

I've tried them separately, should I try them together?

-------------------------

Modanung | 2018-10-20 16:33:40 UTC | #4

If you don't want objects to disappear before fading into the fog the `Camera`'s far clip should be the same as the fog end or greater.
Also, did you connect the zone to the camera node? This will ensure the camera is always inside this `Zone`. If the camera is _not_ inside a zone a default zone with default parameters will be uses, according to the [documentation](https://urho3d.github.io/documentation/HEAD/_zones.html).

-------------------------

mrchrissross | 2018-10-20 16:33:24 UTC | #5

Thats fixed my problem, thank you so much for the help. Really appreciate it :)

-------------------------

Modanung | 2018-10-29 23:52:03 UTC | #6

You can also access the default zone through `Renderer::GetDefaultZone()`.

-------------------------

