ghidra | 2017-01-02 01:15:21 UTC | #1

Updated to HEAD tonight.
Built just fine on my specific Arch install.
But when trying on Ubuntu.. I ran into some issues.

Went back and checked the docs.. and tried to thouroughly go through the requirements on linux (Which looks like the list has gotten a bit longer and a little more diffucult to parse).
My bases are covered in that area, I think.
Still however, after looking at the libs, and just starting from a fresh clone, kept getting road blocked at the same place.

Is there something obvious that I am missing?

[code]
[ 15%] Building C object Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/mir/SDL_mirdyn.c.o
In file included from /Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirdyn.c:27:0:
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirsym.h:55:82: error: unknown type name ?MirPointerConfinementState?
 SDL_MIR_SYM(void,mir_surface_spec_set_pointer_confinement,(MirSurfaceSpec *spec, MirPointerConfinementState state))
                                                                                  ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirdyn.h:40:37: note: in definition of macro ?SDL_MIR_SYM?
     typedef rc (*SDL_DYNMIRFN_##fn) params; \
                                     ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirdyn.h:41:12: error: unknown type name ?SDL_DYNMIRFN_mir_surface_spec_set_pointer_confinement?
     extern SDL_DYNMIRFN_##fn MIR_##fn;
            ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirsym.h:55:1: note: in expansion of macro ?SDL_MIR_SYM?
 SDL_MIR_SYM(void,mir_surface_spec_set_pointer_confinement,(MirSurfaceSpec *spec, MirPointerConfinementState state))
 ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirdyn.h:40:17: error: expected declaration specifiers or ?...? before ?*? token
     typedef rc (*SDL_DYNMIRFN_##fn) params; \
                 ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirsym.h:118:1: note: in expansion of macro ?SDL_MIR_SYM?
 SDL_MIR_SYM(MirOutputGammaSupported,mir_output_is_gamma_supported,(MirOutput const* output))
 ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirdyn.h:41:12: error: unknown type name ?SDL_DYNMIRFN_mir_output_is_gamma_supported?
     extern SDL_DYNMIRFN_##fn MIR_##fn;
            ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirsym.h:118:1: note: in expansion of macro ?SDL_MIR_SYM?
 SDL_MIR_SYM(MirOutputGammaSupported,mir_output_is_gamma_supported,(MirOutput const* output))
 ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirdyn.c:86:35: error: unknown type name ?SDL_DYNMIRFN_mir_surface_spec_set_pointer_confinement?
 #define SDL_MIR_SYM(rc,fn,params) SDL_DYNMIRFN_##fn MIR_##fn = NULL;
                                   ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirsym.h:55:1: note: in expansion of macro ?SDL_MIR_SYM?
 SDL_MIR_SYM(void,mir_surface_spec_set_pointer_confinement,(MirSurfaceSpec *spec, MirPointerConfinementState state))
 ^
In file included from /Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirdyn.c:88:0:
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirsym.h:55:1: warning: initialization makes integer from pointer without a cast [-Wint-conversion]
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirdyn.c:86:35: error: unknown type name ?SDL_DYNMIRFN_mir_output_is_gamma_supported?
 #define SDL_MIR_SYM(rc,fn,params) SDL_DYNMIRFN_##fn MIR_##fn = NULL;
                                   ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirsym.h:118:1: note: in expansion of macro ?SDL_MIR_SYM?
 SDL_MIR_SYM(MirOutputGammaSupported,mir_output_is_gamma_supported,(MirOutput const* output))
 ^
In file included from /Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirdyn.c:88:0:
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirsym.h:118:1: warning: initialization makes integer from pointer without a cast [-Wint-conversion]
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirsym.h: In function ?SDL_MIR_UnloadSymbols?:
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirdyn.c:104:44: warning: assignment makes integer from pointer without a cast [-Wint-conversion]
 #define SDL_MIR_SYM(rc,fn,params) MIR_##fn = NULL;
                                            ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirsym.h:55:1: note: in expansion of macro ?SDL_MIR_SYM?
 SDL_MIR_SYM(void,mir_surface_spec_set_pointer_confinement,(MirSurfaceSpec *spec, MirPointerConfinementState state))
 ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirdyn.c:104:44: warning: assignment makes integer from pointer without a cast [-Wint-conversion]
 #define SDL_MIR_SYM(rc,fn,params) MIR_##fn = NULL;
                                            ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirsym.h:118:1: note: in expansion of macro ?SDL_MIR_SYM?
 SDL_MIR_SYM(MirOutputGammaSupported,mir_output_is_gamma_supported,(MirOutput const* output))
 ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirsym.h: In function ?SDL_MIR_LoadSymbols?:
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirdyn.c:142:47: error: ?SDL_DYNMIRFN_mir_surface_spec_set_pointer_confinement? undeclared (first use in this function)
 #define SDL_MIR_SYM(rc,fn,params) MIR_##fn = (SDL_DYNMIRFN_##fn) MIR_GetSym(#fn,thismod);
                                               ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirsym.h:55:1: note: in expansion of macro ?SDL_MIR_SYM?
 SDL_MIR_SYM(void,mir_surface_spec_set_pointer_confinement,(MirSurfaceSpec *spec, MirPointerConfinementState state))
 ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirdyn.c:142:47: note: each undeclared identifier is reported only once for each function it appears in
 #define SDL_MIR_SYM(rc,fn,params) MIR_##fn = (SDL_DYNMIRFN_##fn) MIR_GetSym(#fn,thismod);
                                               ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirsym.h:55:1: note: in expansion of macro ?SDL_MIR_SYM?
 SDL_MIR_SYM(void,mir_surface_spec_set_pointer_confinement,(MirSurfaceSpec *spec, MirPointerConfinementState state))
 ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirdyn.c:142:66: error: expected ?;? before ?MIR_GetSym?
 #define SDL_MIR_SYM(rc,fn,params) MIR_##fn = (SDL_DYNMIRFN_##fn) MIR_GetSym(#fn,thismod);
                                                                  ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirsym.h:55:1: note: in expansion of macro ?SDL_MIR_SYM?
 SDL_MIR_SYM(void,mir_surface_spec_set_pointer_confinement,(MirSurfaceSpec *spec, MirPointerConfinementState state))
 ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirdyn.c:142:47: error: ?SDL_DYNMIRFN_mir_output_is_gamma_supported? undeclared (first use in this function)
 #define SDL_MIR_SYM(rc,fn,params) MIR_##fn = (SDL_DYNMIRFN_##fn) MIR_GetSym(#fn,thismod);
                                               ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirsym.h:118:1: note: in expansion of macro ?SDL_MIR_SYM?
 SDL_MIR_SYM(MirOutputGammaSupported,mir_output_is_gamma_supported,(MirOutput const* output))
 ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirdyn.c:142:66: error: expected ?;? before ?MIR_GetSym?
 #define SDL_MIR_SYM(rc,fn,params) MIR_##fn = (SDL_DYNMIRFN_##fn) MIR_GetSym(#fn,thismod);
                                                                  ^
/Urho3D/Source/ThirdParty/SDL/src/video/mir/SDL_mirsym.h:118:1: note: in expansion of macro ?SDL_MIR_SYM?
 SDL_MIR_SYM(MirOutputGammaSupported,mir_output_is_gamma_supported,(MirOutput const* output))
 ^
Source/ThirdParty/SDL/CMakeFiles/SDL.dir/build.make:2606: recipe for target 'Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/mir/SDL_mirdyn.c.o' failed
make[2]: *** [Source/ThirdParty/SDL/CMakeFiles/SDL.dir/src/video/mir/SDL_mirdyn.c.o] Error 1
CMakeFiles/Makefile2:444: recipe for target 'Source/ThirdParty/SDL/CMakeFiles/SDL.dir/all' failed
make[1]: *** [Source/ThirdParty/SDL/CMakeFiles/SDL.dir/all] Error 2
Makefile:149: recipe for target 'all' failed
make: *** [all] Error 2
[/code]

-------------------------

sabotage3d | 2017-01-02 01:15:21 UTC | #2

Looks like SDL issue with MIR. Can you try and change it to Wayland or X11?

-------------------------

ghidra | 2017-01-02 01:15:21 UTC | #3

[quote="sabotage3d"]Looks like SDL issue with MIR. Can you try and change it to Wayland or X11?[/quote]

Makes sense.
The docs say this:
[quote]Display server (essential). One or more of these can be installed at the same time. When multiple display servers are available, X11 takes precedence (overridable using SDL_VIDEODRIVER environment variable during application runtime).[/quote]
Which says that x11 takes precedence. But maybe i am not understanding this right either. Because it goes on t say you can override it at runtime.
But I am dealing with build time. And I didnt see a urho3d_* flag to specify not building with mir.

So there in lies my confusion. Not sure how to "change it to X11".

-------------------------

Lumak | 2017-01-02 01:15:21 UTC | #4

I had the same issue: [url]https://github.com/urho3d/Urho3D/issues/1685[/url]

-------------------------

ghidra | 2017-01-02 01:15:22 UTC | #5

Solved 
[quote]Passing -DVIDEO_MIR=0 did the trick.[/quote]

That was it.

-------------------------

