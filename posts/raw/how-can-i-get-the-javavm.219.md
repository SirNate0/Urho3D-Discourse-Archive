att | 2017-01-02 00:58:56 UTC | #1

Hi, 
I encountered a problem, I want to call java methods from c++ code, so I need the javavm, but the sdl already has one, then how can I access this javavm, or I need modify the sdl function?
thank you.

-------------------------

cadaver | 2017-01-02 00:58:56 UTC | #2

If you include SDL_android.h, you'll have access to the function JNIEnv *Android_JNI_GetEnv(void) which returns the environment object through which JNI calls happen. I've not personally tested this from outside SDL but I don't see why it shouldn't work. In case you need the actual JavaVM object, then you'll need to add a function into SDL that returns it for you.

-------------------------

