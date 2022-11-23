jzpekarek | 2020-07-05 01:12:12 UTC | #1

Not a support question, but wanted to make sure what I found was easy for others to find if they have the same problem. After spending a lot of time trying to figure out why my touch events stopped working on iOS after I upgraded from Urho3D 1.5 to Urho3D 1.8 alpha, I found out that is was related to my code being setup to run on both desktop and touch platforms. Apparently in SDL2.0.4, iOS (and presumably Android), generate mouse messages for touch events by default (I don’t think that was true in the earlier version of SDL that Urho3D 1.5 used). In my application, I run the same code on Windows and iOS, so I had both mouse and touch event handlers, and they started both getting called on iOS, which caused a lot of bad behavior. I found this link that talks about the problem.

https://stackoverflow.com/questions/34465681/sdl2-events-on-mobile

So for me, the fix was to call the following in my initialization code. Even though the hint appears to be specific to Android, it fixed my problem on iOS as well.

#include <SDL/SDL_hints.h>

//In initialization code
SDL_SetHint(SDL_HINT_ANDROID_SEPARATE_MOUSE_AND_TOUCH,“1”);

-------------------------

weitjong | 2020-07-05 04:27:23 UTC | #2

That hint has been removed since SDL 2.0.10 and replaced by two new hints. See SDL 2.0.10 release notes and also below changes in Urho3D code base.

https://github.com/urho3d/Urho3D/blob/66095e0e0d9d201e1dc910e2dab47e6b429f7b9e/Source/Urho3D/Input/Input.cpp#L389-L395

Are you suggesting we need the same hints to be applied for iOS and tvOS?

-------------------------

throwawayerino | 2020-07-05 10:48:56 UTC | #3

Don't bother with the releases. They're old and buggy and master has more features. 1.8 is fine I think. Also don't forget that android can use a mouse via usb-otg. I like this feature, but you don't have to support it

-------------------------

jzpekarek | 2020-07-05 17:17:32 UTC | #4

I'm assuming that it is needed for iOS, but not sure about tvOS (does tvOS support touch?). I added an extra defined(IOS) as shown below, and it fixed the problems I was seeing.

    #if defined(__ANDROID__) || defined(IOS)
        // Prevent mouse events from being registered as synthetic touch events and vice versa
        SDL_SetHint(SDL_HINT_MOUSE_TOUCH_EVENTS, "0");
        SDL_SetHint(SDL_HINT_TOUCH_MOUSE_EVENTS, "0");
    #elif defined(__EMSCRIPTEN__)
        emscriptenInput_ = new EmscriptenInput(this);
    #endif

As the next poster pointed out, I think setting these values to zero might not always be what you want, but it is probably a reasonable default (and matches the old behavior of Urho3D, so should avoid breaking apps like it did for me). In my application, I handle mouse events and touch events separately, which I thought I needed to do to handle multi-touch when it is available, but maybe if you set SDL_HINT_MOUSE_TOUCH_EVENTS to 1, then the mouse works like a single touch? In any case, I'm assuming that you could override these hints anywhere in the setup code that is called after the code above.

-------------------------

weitjong | 2020-07-06 15:44:19 UTC | #5

Yeah, after making that comment, I also realized I might have made mistake by putting tvOS in the same line but then again I have not been following Apple closely recently.

Care to submit your one line change above as PR?

-------------------------

jzpekarek | 2020-07-07 02:28:27 UTC | #6

It might take me a few days, but I'll try to submit a PR. I need to learn Git first, my total knowledge to date on it was just enough to clone the repository.

-------------------------

