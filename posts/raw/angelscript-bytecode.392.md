alexrass | 2017-01-02 01:00:06 UTC | #1

I found that the bytecode is different on the 32bit and 64bit platforms.
If scripts compiled by ScriptCompiler 32bit, Urho3DPlayer 64bit crash.
This problen in AngelScript.

 	
if the game is distributed in a 64bit and 32 bits, this is a problem...

-------------------------

cadaver | 2017-01-02 01:00:06 UTC | #2

Yes, you will need to have 32 & 64 bit ScriptCompiler toolchains and compile the scripts separately as part of your build packaging.

-------------------------

alexrass | 2017-01-02 01:00:06 UTC | #3

I found info:
[angelcode.com/angelscript/sd ... mpile.html](http://www.angelcode.com/angelscript/sdk/docs/manual/doc_adv_precompile.html)

-------------------------

