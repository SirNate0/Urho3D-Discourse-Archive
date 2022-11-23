viya | 2018-03-16 10:12:15 UTC | #1

Is there any ways to include precompiled scripts?
I am trying to call function defined in precompiled script. "ScriptFile::Execute(declaration, params)" works, but how to get function return value?
For example, I have "functions.asc" file, which contains "int SomeFunc(int)". How to call "int SomeFunc(int)" and get result?

-------------------------

Sinoid | 2018-03-16 18:40:35 UTC | #2

Do you mean like a `#include "functions.asc"` sort of thing?

You can't do that, you have to use an import as each compiled script is a module.

`import void MyFunction(int a, int b) from "Another module";` the documentation for which is [Angelscript: Imports](http://www.angelcode.com/angelscript/sdk/docs/manual/doc_global_import.html)

You'll also want to familiarize yourself with [Shared Script Entities](http://www.angelcode.com/angelscript/sdk/docs/manual/doc_script_shared.html).

You'll have to manually load an Urho3D::ScriptFile for your compiled .asc code as well if I'm not mistaken as Urho3D can't really know about what sort of external dependencies you have ... at least not at the present.

-------------------------

viya | 2018-03-16 20:35:11 UTC | #3

Thank you for reply! 
Yes, like a `include "functions.asc"` or any other way to call functions from precompiled scripts.
Can you write simple demo for UrhoPlayer using "Imports" or/and "Shared Script Entities"?
Sorry for my English

-------------------------

Sinoid | 2018-03-19 03:02:07 UTC | #4

I looked around and I don't have anything immediately accessible using these features. The samples and the editor all use a monolithic approach.

---

On language issues, you do get what this below means right?

> You’ll have to manually load an Urho3D::ScriptFile for your compiled .asc code as well if I’m not mistaken as Urho3D can’t really know about what sort of external dependencies you have … at least not at the present.

That's basically all you have to do in order to use `import` or `external shared`, just load a specific script first and define what you want to get from it.

The use of regular shared classes and shared functions you just mark them as shared and include the relevant source files. So if your `shared class SharedDataObject` is in `SharedDataObject.as` in the source you want to use it you just say `#include "Data/Scripts/SharedDataObject.as"` and it will be a shared type, 1st come 1st serve for the type definition.

-------------------------

viya | 2018-03-19 10:42:42 UTC | #5

Thank you for explanation! Your answer was very helpful for me!

-------------------------

