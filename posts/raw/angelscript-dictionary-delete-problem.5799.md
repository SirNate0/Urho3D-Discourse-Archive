devhang | 2020-01-07 11:42:34 UTC | #1

When I try to use Dictionary as the usage of Haspmap (is it right replacement in AS?)
Exists, Set or Get function are work as the document said
https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_c_script_dictionary.html
but Delete or DeleteAll functions are not working, I find very hard to find the syntax or document for AS, any resources can provide? Thanks!!

-------------------------

Sinoid | 2020-01-07 11:42:43 UTC | #3

They're bound as:

```
engine->RegisterObjectMethod("Dictionary", "void Erase(const String &in)", asMETHOD(CScriptDictionary,Delete), asCALL_THISCALL);
engine->RegisterObjectMethod("Dictionary", "void Clear()", asMETHOD(CScriptDictionary,DeleteAll), asCALL_THISCALL);
```

So it's `Erase(string)` and `Clear()` - they *should* work.

-------------------------

devhang | 2020-01-06 02:30:44 UTC | #4

Yes, it's work, thanks for your information, it seems that I cannot totally depend on the class API on the website if I am using AngelScript
https://urho3d.github.io/documentation/HEAD/annotated.html

-------------------------

Sinoid | 2020-01-06 03:19:42 UTC | #5

Angelscript basic reference is here (still requires referring back to core docs to understand what things actually do):

https://urho3d.github.io/documentation/1.7.1/_script_a_p_i.html#Class_Dictionary

You can also dump the API from the command-line angelscript compiler, for when you have your own custom stuff bound to AS.

-------------------------

devhang | 2020-01-07 03:21:16 UTC | #6

Thank you for your great information once again :smiley:

-------------------------

