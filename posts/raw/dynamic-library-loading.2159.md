godan | 2017-01-02 01:13:32 UTC | #1

In one of my projects with Urho, it would be very nice to allow users to create their own plugins and have them be loaded dynamically. After some research, I've found plenty of nice examples for cross platform dll/.so loading ([sourcey.com/building-a-simple-cp ... in-system/](http://sourcey.com/building-a-simple-cpp-cross-platform-plugin-system/)), and I don't think it would be too hard to get something working. I think the main thing is just that it is a bit tedious to write all the pimpl versions of the loading logic. However, my two main questions for this are:

- What happens with Emscripten? I know it "can" do dynamic loading, but it seems a bit risky ([github.com/kripken/emscripten/wiki/Linking](https://github.com/kripken/emscripten/wiki/Linking)). Does anyone have experience with this?
- Is this something that would be have benefit to Urho as a whole?

-------------------------

cadaver | 2017-01-02 01:13:32 UTC | #2

In the realXtend Tundra application platform we did a plugin system too, it also has its Urho-based port [url]https://github.com/realxtend/tundra-urho3d.git[/url]. It's quite dead simple, there's basically just a Windows path and a non-Windows path. If interested in the actual code, see [github.com/realXtend/tundra-urh ... ginAPI.cpp](https://github.com/realXtend/tundra-urho3d/blob/master/src/TundraCore/Framework/PluginAPI.cpp)

It'd probably be more feasible as a simple addon library / wiki example than an actual part of Urho for maintenance, platform support and quality expectation reasons, also considering that Urho itself strictly doesn't need it.

Note that C++ user plugins are a very potential minefield unless you provide the source for your main application too, as there is no ABI standard and the user might be required to use the same compiler as you used. Preferable is to have a C API for plugins, for then the ABI is standard for each platform.

-------------------------

godan | 2017-01-02 01:13:33 UTC | #3

Hey this is great. Thanks for the reference.

So, just to be sure - does this work ok with emscripten? Or is there some special ASM stuff I'd need to do?

-------------------------

cadaver | 2017-01-02 01:13:33 UTC | #4

They should support dlopen() but I'm not at all sure of the details. Someone more experienced needs to fill in, or you need to search the net for more detailed info.

-------------------------

godan | 2017-01-02 01:13:33 UTC | #5

I think emscripten does support dlopen() - [github.com/kripken/emscripten/w ... ic-linking](https://github.com/kripken/emscripten/wiki/Linking#dlopen-dynamic-linking)

However, there are some details about compiling the dll as a side module or something. Not really sure about this.

-------------------------

