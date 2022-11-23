nickwebha | 2019-10-10 16:03:18 UTC | #1

I have been working on an Emscripten issue for ~24 hours now and can not seem to figure this out.

I got sample *23_Water* working under GCC and everything looks great. However when I try the same code with Emscripten it compiles fine but running it gets me
> Uncaught emscripten_get_num_gamepads() can only be called after having first called emscripten_sample_gamepad_data() and that function has returned EMSCRIPTEN_RESULT_SUCCESS!

Adding `emscripten_sample_gamepad_data()` to the `Sample` constructor does not help. Adding it to `Sample::Setup()` does not help.  It just still spits back the same error. I tried removing all references to anything called *joystick* or *input* as a test and I still get the same error. The same is true for `Water::Water()` and `Water::Setup()`.

I did find [a reference](https://github.com/urho3d/Urho3D/issues/2324) to an SDL-related issue but I do not think it is of any help.

My command looks like
> emcc																\
> 	-o water.html													\
> 	source/*.cpp													\
> 	lib/emscripten/libUrho3D.a										\
> 	-std=c++17														\
> 	-Wall															\
> 	-s USE_PTHREADS=1												\
> 	-s WASM=0 -s LEGACY_VM_SUPPORT=1 -s ENVIRONMENT="web,worker"	\
> 	-Iinclude/														\
> 	-I../include/													\
> 	-O0

It appears to me, based on this error, that I just need a pre-initialization place to call `emscripten_sample_gamepad_data()` but can not figure out where that is after pouring through the docs. Really not sure where to go from here.

-------------------------

weitjong | 2019-10-11 04:23:54 UTC | #2

I cannot reproduce this error. I am mostly using DBE nowadays when targeting platforms that are supported by my ["dockerized"](https://github.com/weitjong/dockerized) project. In your case, this is how I built the `23_Water` sample just now.

```
$ script/dockerized.sh web rake make web target=23_Water
```

-------------------------

