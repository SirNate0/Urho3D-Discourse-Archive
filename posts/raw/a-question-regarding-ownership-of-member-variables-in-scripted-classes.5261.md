Leith | 2019-06-28 06:34:17 UTC | #1

I'm looking for a way to leverage the existing mechanisms in Urho, rather than reinvent the wheel.

[quote]
After instantiation, the script object's public member variables that can be converted into [Variant](https://urho3d.github.io/documentation/1.7/class_urho3_d_1_1_variant.html), and that don't begin with an underscore are automatically available as attributes of the [ScriptInstance](https://urho3d.github.io/documentation/1.7/class_urho3_d_1_1_script_instance.html), and will be serialized.
[/quote]

I understand that this means I can read public attributes of script classes from c++, by querying same named attributes of the ScriptInstance component. My question is: if I write to these attributes from C++, will these changes be readable in Angelscript?

-------------------------

Leith | 2019-06-29 10:52:08 UTC | #2

I found one option.
Node variables can be accessed from both sides of the language barrier - ownership rests with c++ and scripts can access, this will do.

I am still not sure whether attributes generated from script to c++ are writeable from c++ and readable back in script, but I am really no longer worried. Node vars will do what I want - cross the border.

-------------------------

