Bluemoon | 2017-01-02 01:05:40 UTC | #1

Is there any possible way to retrieve the return value of an AngelScript method called through ScriptInstance::Execute() ?

( I kind of feel like someone might have asked this question before, if that is the case then a link to the post would be much appreciated )

-------------------------

cadaver | 2017-01-02 01:05:40 UTC | #2

It should work by getting the AngelScript execution context from Script subsystem by calling Script::GetScriptFileContext() directly after the Execute call, then using the asIScriptContext's functions: GetReturnByte(), GetReturnWord() etc. (you need to know the function's return type)

-------------------------

