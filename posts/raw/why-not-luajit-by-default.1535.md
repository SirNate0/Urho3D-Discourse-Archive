bvanevery | 2017-01-02 01:08:20 UTC | #1

Samples are now built by default, which is a good idea to showcase Urho3D.  This means Lua is built by default.  Why not also build LuaJIT by default?  It's one of things I always have to click when I'm selecting my build options.  Consider all the poor lazy coders out there.  :slight_smile:  Seriously, is there any possible downside to LuaJIT?

The other thing that has mystified me over these past several months, is what the heck is the LuaJIT Amalgamated Build?  I always choose it, but I don't know what good it does.  What is the reason for selecting LuaJIT but not the Amalgamated Build?

-------------------------

Enhex | 2017-01-02 01:08:20 UTC | #2

The info you're looking for can be found here:
[luajit.org/install.html](http://luajit.org/install.html)

I think that defaulting to LuaJIT it the correct choice, since not using LuaJIT requires a special case when the CPU/Compiler isn't supported. (Link has info about what's supported)

At the bottom of the page I linked it says:
"The build system has a special target for an amalgamated build, i.e. make amalg. This compiles the LuaJIT core as one huge C file and allows GCC to generate faster and shorter code."

-------------------------

weitjong | 2017-01-02 01:08:21 UTC | #3

LuaJIT should be better than Lua and it should be used in all the platforms that LuaJIT supports. Having said that, LuaJIT currently does not work on HTML5 platform and iOS platform (although in theory it can be made to work on iOS but there is no point to do so if Apple would reject the app in the end). If we would have LuaJIT enabled by default than we would have to tell our CMake scripts to exclude those platforms and fallback to Lua instead. Not sure it will be even more confusing as the result, especially to new users. At the very least at the moment the situation is crystal clear. You get Lua enabled across the board. It uses JIT only when you explicitly tell it to.

-------------------------

bvanevery | 2017-01-02 01:08:21 UTC | #4

I would argue that most users are not on iOS, so the default should benefit most users.  Not like having it turned off for iOS would be difficult CMake code to write.  Also, issues of what Apple will and won't allow in the iStore, is something that iOS developers cannot avoid understanding.

Aside from promoting checkbox laziness  :mrgreen: I would argue that test coverage of LuaJIT by default is highly beneficial.

An iOS-specific CMake message can instruct users as to why iOS is different, if proactive education is really needed to avoid people's confusion.  Personally I think a short comment in CMakeLists.txt is sufficient.

-------------------------

weitjong | 2017-01-02 01:08:21 UTC | #5

If by test coverage you mean continuation integration testing then LuaJIT has been tested all this while in our CI builds. We did have to fallback to Lua for MinGW CI build due to the MinGW compiler available on Travis CI is really out of date to handle LuaJIT compilation. If something breaks LuaJIT library then our build system would know it immediately before anyone of us do. I think it is easy to understand that whatever the default is, we can always override it in the test setup. So it should not be used as an argument to justify it. I do not strongly oppose the default to be changed. If the majority of comments in this thread are for it then we can consider it.

-------------------------

bvanevery | 2017-01-02 01:08:21 UTC | #6

[quote="weitjong"]If by test coverage you mean continuation integration testing then LuaJIT has been tested all this while in our CI builds. 
[/quote]

I'm glad to hear that.  However, I also consider people building Urho3D "in the wild" on their own machines as part of the testing / kicking the tires of code.  If LuaJIT is not being regularly exercised by users, then that's bug potential.  Especially for some platforms like Windows that you aren't doing continuation integration testing for.

-------------------------

bvanevery | 2017-01-02 01:08:36 UTC | #7

I've created an [url=https://github.com/urho3d/Urho3D/issues/1091]issue[/url]for this.

-------------------------

bvanevery | 2017-01-02 01:08:47 UTC | #8

While on this subject, if the LuaJIT is being built, why not do the amalgamated build by default as well?  I've never seen any problem with it in all the builds I've done.  It would cut down on yet another configuration option and increase "in field" test coverage.  I'm building upwards of 6 builds manually today, for DX9 and OpenGL on 3 different laptops, so from my perspective, cutting down the number of necessary build options does help.

-------------------------

