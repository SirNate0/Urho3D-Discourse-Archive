Askhento | 2022-09-20 15:57:17 UTC | #1

I have two files : 
```
// BaseClass.as
shared interface BaseInterface : ScriptObject { ... }
uint SOME_GLOBAL_VAR = 0;
shared class BaseClass : BaseInterface { 
    ... 
   Init(...)
   {
       SOME_GLOBAL_VAR ++;
   }
}

```
and then in
```
// Main.as
#include "BaseClass.as"

BaseInterface@ instance;
...
BaseClass@ instanceClass = cast<BaseClass@>(instance);

//Error : Shared code cannot access non-shared global variable 'SOME_GLOBAL_VAR'
```
So I would like to have **BaseClass** in **Main.as** with methods from class, not the interface. Also, the global variable should be possible to use.
Hope I explained the issue well enough.

-------------------------

SirNate0 | 2022-09-20 14:08:42 UTC | #2

It has been a while since I've looked at AngelScript in any detail. Are you sure you need to use a shared class at all?

And from the AS documentation, it looks like global variables are not possible to use from shared classes/functions at present, though they may add it in the future:

http://www.angelcode.com/angelscript/sdk/docs/manual/doc_script_shared.html#doc_script_shared_2

-------------------------

Askhento | 2022-09-20 15:49:39 UTC | #3

I am not sure, just trying what documentation says.
Do you have an example on how to organize multiple file angelscript project without using shared?

-------------------------

SirNate0 | 2022-09-20 16:24:04 UTC | #4

I would refer you to how the Editor is set up. I don't use AngelScript myself except in smaller contained scripts I call C++ so I can't really help more than that.

-------------------------

count0 | 2022-09-26 14:19:03 UTC | #5

You can't use one AS context from another (they are isolated by design). If you want to share state across your scripts:
- create a component w/ (safe) accessors to your state
- export its interface to AS
- now you can find + tap into that component from any AS context

Hope this helps.

-------------------------

