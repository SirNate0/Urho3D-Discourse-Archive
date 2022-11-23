OvermindDL1 | 2017-01-02 00:57:51 UTC | #1

It seems an SDL bug has been hit, just pushing a lot of the keys on my keyboard reveal that they are not working and this gets spammed to the console:
[code]The key you just pressed is not recognized by SDL. To help get this fixed, please report this to the SDL mailing list <sdl@libsdl.org> X11 KeyCode 175 (167), X11 KeySym 0x1008FF1C (XF86AudioRecord).
The key you just pressed is not recognized by SDL. To help get this fixed, please report this to the SDL mailing list <sdl@libsdl.org> X11 KeyCode 176 (168), X11 KeySym 0x1008FF3E (XF86AudioRewind).
The key you just pressed is not recognized by SDL. To help get this fixed, please report this to the SDL mailing list <sdl@libsdl.org> X11 KeyCode 177 (169), X11 KeySym 0x1008FF6E (XF86Phone).
The key you just pressed is not recognized by SDL. To help get this fixed, please report this to the SDL mailing list <sdl@libsdl.org> X11 KeyCode 178 (170), X11 KeySym 0x0 ((null)).
The key you just pressed is not recognized by SDL. To help get this fixed, please report this to the SDL mailing list <sdl@libsdl.org> X11 KeyCode 182 (174), X11 KeySym 0x1008FF56 (XF86Close).
The key you just pressed is not recognized by SDL. To help get this fixed, please report this to the SDL mailing list <sdl@libsdl.org> X11 KeyCode 183 (175), X11 KeySym 0x0 ((null)).
The key you just pressed is not recognized by SDL. To help get this fixed, please report this to the SDL mailing list <sdl@libsdl.org> X11 KeyCode 184 (176), X11 KeySym 0x0 ((null)).
The key you just pressed is not recognized by SDL. To help get this fixed, please report this to the SDL mailing list <sdl@libsdl.org> X11 KeyCode 185 (177), X11 KeySym 0x1008FF78 (XF86ScrollUp).
The key you just pressed is not recognized by SDL. To help get this fixed, please report this to the SDL mailing list <sdl@libsdl.org> X11 KeyCode 186 (178), X11 KeySym 0x1008FF79 (XF86ScrollDown).
The key you just pressed is not recognized by SDL. To help get this fixed, please report this to the SDL mailing list <sdl@libsdl.org> X11 KeyCode 187 (179), X11 KeySym 0x28 (parenleft).
The key you just pressed is not recognized by SDL. To help get this fixed, please report this to the SDL mailing list <sdl@libsdl.org> X11 KeyCode 188 (180), X11 KeySym 0x29 (parenright).
The key you just pressed is not recognized by SDL. To help get this fixed, please report this to the SDL mailing list <sdl@libsdl.org> X11 KeyCode 189 (181), X11 KeySym 0x1008FF68 (XF86New).[/code]
That is not an exhaustive list, but for some reason SDL seems to be doing something very stupid.  In essence it is mapping 'known' keys to its own platform independent mapping, however it then does something very stupid, for keys it does not know it does not pass them on as some type of 'UNKNOWN' key with a platform dependent additional value (thus gamers could map them to functions by pressing them, regardless of if we know what they are or not).  Any way this could be working around?  Other input libraries I use handle unknown keys just fine by doing what I just described that SDL should do (technically the Input systems I often use do something like give you an integer value of the key (with a set of DEFINE's for mapping known keys) and the known keys fall within 0 to (2^15)-1, and 'unknown' keys are mapped to the upper range of 2^15 to (2^16)-1, thus known keys you can treat as normal, but unknown keys are still useful.  Unknown keys are basically just the platform dependent integral value mapped to that range so the same mappings will always end up the same on any given computer, but different computers may map different depending on hardware.  Thus this method makes sense.

Ignoring them, however, does not make sense.  Many keys on my keyboard as well as some of my testers keyboards are not functioning, they just spew those above messages.

Also, I have not finished going through the API yet, but I am not immediately seeing a way to get multiple input devices.  For example, I want to map keys on both the main keyboard (which maps to keyboard 0) and keys on my glove (which maps to keyboard 1) to different functions, but how do I determine which input devices they come from (a standard functionality of other input systems I use).

If the first issue is not fixable (should be easily fixable) and the second does not exist (also easily fixable) then how would I hook the platform dependent input loop events so I can handle them manually as there are simple ways of doing all the above on all windows, mac, linux, and yes, even android (maybe iOS?  Does it even support external controlling devices like Android?  Never programmed for iOS...).

EDIT:  I love the component design, very convenient.

-------------------------

cadaver | 2017-01-02 00:57:51 UTC | #2

I think you have hit a usecase of SDL (multiple keyboards) that the authors simply haven't thought about. Your options are basically:

- Take this up on SDL's own discussion forum
- Modify Urho's version of SDL directly. I don't think it provides a nice hook into the platform specific event pump, so you'll have to touch the code of each platform separately. I would say this is better so that the platform-specific code stays inside SDL. We already have modified SDL where necessary.

We are naturally happy to incorporate fixes into Urho's SDL & input subsystem if you make a pull request (provided it doesn't break stuff :wink: )

-------------------------

OvermindDL1 | 2017-01-02 00:57:55 UTC | #3

Actually if you already edit the included version then that will be the easiest way to fix it by far.  I shall start a pull request and work on it as I get time.

-------------------------

friesencr | 2017-01-02 00:57:55 UTC | #4

I wish we had a friend over at sdl.  The linux porters seem like a tight lot.  I would send ryan, sam, & co my wifes brownies but then i think that would kill any chances we have.

-------------------------

OvermindDL1 | 2017-01-02 00:57:55 UTC | #5

I am unsure how it is now, but SDL was not friendly to things like this years ago, one big reason I have avoided it.

However I have worked on it a bit tonight and got SDL passing in the raw code in the Uint32 sized 'unused' argument (now renamed to 'raw') in the keysym struct, it seems that there might have been support for this at one point but it was removed, interesting...

Time for sleep now, will mess with this more on the Urho3D side and test it properly when I get another hour free.

Will push before I go to sleep, just going to make a couple last changes before committing (check the branch I added):  [github.com/OvermindDL1/Urho3D](https://github.com/OvermindDL1/Urho3D)

EDIT:  It even has the 'invalid' key check in an #ifdef 1 (now 0)

-------------------------

OvermindDL1 | 2017-01-02 00:57:55 UTC | #6

And submitted changes to handle raw inputs, see the fixed SDL with the minimal (and quite tiny) changeset at:  [github.com/OvermindDL1/Urho3D/c ... 3feace5cab](https://github.com/OvermindDL1/Urho3D/commit/dba4216c86cc775096b6f6690d5f1b3feace5cab)

Only done for linux so far, other platforms will not compile (though adding a simple ', 0' as the middle argument will fix that).  Adding such things to another push here soon if I do not pass out first.

EDIT1: Adding in multiple keyboard support will be a pain, may not be motivated enough to that, such is the poor design of the SDL input system...

EDIT2: Added support for raw keyboard keys to all other platforms, passes 0 for ones where there is not a raw code that makes sense, else passes in something sensible.  Pushed:  [github.com/OvermindDL1/Urho3D/c ... c18eec0065](https://github.com/OvermindDL1/Urho3D/commit/d7f3c9ae66c14c7e41f782b6887bf8c18eec0065)

Can anyone test the latest one and make sure it at least compiles on non-linux systems?  Maybe run a sample or two?

Should be backwards compatible, only changed an SDL internal function signature, and no structure size changed, just using the unused field renamed to raw.

-------------------------

OvermindDL1 | 2017-01-02 00:57:55 UTC | #7

And fixed Urho3D to handle the raw instead of silently ignoring it, but now where should I stuff it, in a field on Input that can be queried, or should I add a new field to the E_KEYDOWN and E_KEYUP events.  I did the adding a field on the variant as per this commit for now, seems simple enough:  [github.com/OvermindDL1/Urho3D/c ... 19beff7f82](https://github.com/OvermindDL1/Urho3D/commit/34fb88990691733ccdaedbbfb93e8f19beff7f82)

If that looks good, and if others can test compile on all platforms, this should be fully backwards compatible unless anyone uses internal calls (bad bad), but if this looks good then feel free to pull the pull request, I am submitting it now in case it seems good.

EDIT:  Pull request: [github.com/urho3d/Urho3D/pull/191](https://github.com/urho3d/Urho3D/pull/191)
Remember, not tried compiling other platforms, but they 'should' compile?  Need testers.

-------------------------

cadaver | 2017-01-02 00:57:55 UTC | #8

You can add a new field to the events.

-------------------------

OvermindDL1 | 2017-01-02 00:57:56 UTC | #9

This fixes the issue I was having though, I can now map any unknown key in my action mapper now.  Thus far not hit an issue or bug.  Has anyone else tested?

-------------------------

cadaver | 2017-01-02 00:57:57 UTC | #10

I can test on Windows & Android. I believe we can merge the request and then check the rest of the platforms one by one, it's not end of the world if eg. OSX or iOS build is broken for a few commits.

-------------------------

cadaver | 2017-01-02 00:57:57 UTC | #11

It's merged now.

-------------------------

