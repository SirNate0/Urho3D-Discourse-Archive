practicing01 | 2017-01-02 01:09:03 UTC | #1

Hello, I would like to enable ASSET_DIR_INDICATOR to be able to use ScanDir() on android.  How can I do that, thanks for any help.  History of commits that I couldn't make sense of, relating to the subject: [github.com/urho3d/Urho3D/commit ... System.cpp](https://github.com/urho3d/Urho3D/commits/master/Source/Urho3D/IO/FileSystem.cpp)

-------------------------

weitjong | 2017-01-02 01:09:04 UTC | #2

If I recall correctly then you just need to define it as an environment variable. The value of the variable is the character indicator itself. If it works for you, you can help to send a PR to update the doc. I believe it is an undocumented feature at the moment.

-------------------------

practicing01 | 2017-01-02 01:09:04 UTC | #3

I added the line "export ASSET_DIR_INDICATOR=_" to .bashrc but the results of ScanDir() are not the same as in native.  The results are so odd that I need some time to look through things to try and figure out what's happening.

-------------------------

weitjong | 2017-01-02 01:09:04 UTC | #4

It relies on an ant custom rule (custom_rules.xml), so make sure you don't miss out that file. Last time I use the feature, it worked as expected for me. Good luck.

-------------------------

practicing01 | 2017-01-02 01:09:10 UTC | #5

I copy/pasted the custom_rules.xml from urho android build directory to my projects android build directory. I'm not getting the right results.  Am I missing anything else?

-------------------------

weitjong | 2017-01-02 01:09:10 UTC | #6

Obviously you also need to reference the file somewhere in your default Ant build script (build.xml).

-------------------------

practicing01 | 2017-01-02 01:09:11 UTC | #7

Edit: Found I luajit was set for native but not for android.  After setting for android I got an error.  I'm opening a new thread for that error.

I think I got it working somewhat.  DirExists() isn't working though.  Not sure if the following is related because of paths but I'm getting "Could not find resource bit.lua" (I'm using luajit).

-------------------------

