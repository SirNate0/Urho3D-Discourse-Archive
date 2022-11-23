dragonCASTjosh | 2017-01-02 01:06:16 UTC | #1

After playing with Urho3D for some time now i have ended up resorting to Sublime Text for programming in AngelScript whilst its done the job for now i feel like allot of the time spent flicking to the docs to find the parameters for a method can easily be avoided with a simple IDE that includes code completion.

I also looked at the current suggestion on how to program AS in Urho3D and found a thread suggesting the use of CodeLite although after trying this option i found the overall theme and layout of the IDE was not to my taste making it hard for me to focus, i also tried Sinoid's AngelScript IDE although i really liked the team i found it to be very buggy and did not include code completion.

-------------------------

weitjong | 2017-01-02 01:06:17 UTC | #2

We have included a generated (fake) header file for the purpose of enabling AngelScript code completion. The idea is to fool IDE to think *.as is one of C++ source file extension so the file gets opened up in C++ editor (with code completion feature on and others) within the IDE, then force including the generated header file would import all the symbols that we have exported to AS so the code completion works. I haven't tried it on all IDEs that Urho3D support yet but I know for sure this trick works well on Eclipse besides codelite.

As for Lua, you may try to evaluate ZeroBrain Studio. One of our user (silverkorn) has maintained a "plugin" for this Lua editor to code complete for Urho3D Lua bindings.

-------------------------

dragonCASTjosh | 2017-01-02 01:06:17 UTC | #3

Thanks for the help ill look into setting it up in eclipse.

-------------------------

dragonCASTjosh | 2017-01-02 01:06:22 UTC | #4

[quote="Sinoid"]Hang on a second, you didn't have autocomplete in my editor? Did you follow the troubleshooting instructions linked in the readme.md? Once you get the configuration setup the only serious issues should be bugs that must be reported as they're holes in autocompletion's completeness.

If you did and still had issues, I'd really appreciate issues reports on github so I can fix them.[/quote]

I must of missed that part of the readme, ill give it another go because i really liked the IDE. Also the bug i was having was when selective a project of clicking develop at the top it would take me to an error screen, but if i used the back button and repeated it worked so its nothing serious just a little extra effort, ill post the error report on the GitHub today

-------------------------

