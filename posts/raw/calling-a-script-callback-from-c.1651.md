Enhex | 2017-01-02 01:09:14 UTC | #1

Is it possible to execute a script-side callback function?
I looked in ScriptInstance::GetScriptAttributes() and it only adds Node/Component/Resource handles to the attributes, and AFAIK AngelScript callbacks are handles, so they won't be added.
I also want to use delegates.

A workaround is to have a function that calls the callback, so that function can be executed to execute it.


I see that AngelScript documents how to do that:
[angelcode.com/angelscript/sd ... backs.html](http://www.angelcode.com/angelscript/sdk/docs/manual/doc_callbacks.html)

Any chance it will be added to Urho's API?

-------------------------

