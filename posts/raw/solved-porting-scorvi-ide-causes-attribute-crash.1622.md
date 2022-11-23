vivienneanthony | 2017-01-02 01:09:02 UTC | #1

Hello

I'm attempting to make [github.com/scorvi/Urho3DIDE/tree/master/IDE](https://github.com/scorvi/Urho3DIDE/tree/master/IDE) work in Urho3D in a engine. Previously I worked on Existence and due to cross-faction compiling issues me and another programmer decided to build from scratch but for better capacity and cross platform coding. Now we are making a full engine add-on with more networking capacity, custom components, and other things and game.

Back to the program, we ported the code to a new build to a engine. It works but I'm getting crashes that deals with attributes. I'm not sure if it is because the original code was made for the previous version of Urho3D

[github.com/vivienneanthony/MyFo ... /Attribute](https://github.com/vivienneanthony/MyForkEditor/tree/master/Source/EngineIDE/Core/UI/Attribute)

The full gdb backtrace is below
pastebin.com/tu7zHM4h



The Git is at [github.com/vivienneanthony/MyForkEditor](https://github.com/vivienneanthony/MyForkEditor)

Vivienne



[code]#0  0x0000000000911471 in operator!= (rhs=..., this=0x0) at /media/home2/vivienne/Urho3D-Hangars-MyForkEditor/Source/Urho3D/Container/Str.h:265
No locals.
#1  Urho3D::LineEdit::SetText (this=0x29bfec0, text=...) at /media/home2/vivienne/Urho3D-Hangars-MyForkEditor/Source/Urho3D/UI/LineEdit.cpp:488
No locals.
#2  0x0000000000705dd0 in ResourceRefAttributeUI::SetVarValue (this=0x29befb0, var=...)
    at /media/home2/vivienne/Urho3D-Hangars-MyForkEditor/Source/EngineIDE/Core/UI/Attribute/AttributeVariable.cpp:790
No locals.
#3  0x0000000000709872 in BasicAttributeUI::UpdateVar (this=0x29befb0, serializable=0x2948f80, serializable@entry=0x31323c0)
    at /media/home2/vivienne/Urho3D-Hangars-MyForkEditor/Source/EngineIDE/Core/UI/Attribute/AttributeVariable.cpp:161
        var = {static EMPTY = {static EMPTY = <same as static member of an already seen type>, static emptyBuffer = {<Urho3D::VectorBase> = {size_ = 0,
                capacity_ = 0, buffer_ = 0x0}, <No data fields>}, static emptyResourceRef = {type_ = {static ZERO = {
                  static ZERO = <same as static member of an already seen type>, value_ = 0}, value_ = 0}, name_ = {static NPOS = 4294967295,
                static MIN_CAPACITY = 8, static EMPTY = {static NPOS = 4294967295, static MIN_CAPACITY = 8,
                  static EMPTY = <same as static member of an already seen type>, length_ = 0, capacity_ = 0,
                  buffer_ = 0x1435680 <Urho3D::String::endZero> "", static endZero = 0 '\000'}, length_ = 0, capacity_ = 0,
                buffer_ = 0x1435680 <Urho3D::String::endZero> "", static endZero = 0 '\000'}}, static emptyResourceRefList = {type_ = {static ZERO = {
                  static ZERO = <same as static member of an already seen type>, value_ = 0}, value_ = 0}, names_ = {<Urho3D::VectorBase> = {size_ = 0,
                  capacity_ = 0, buffer_ = 0x0}, <No data fields>}}, static emptyVariantMap = {<Urho3D::HashBase> = {static MIN_BUCKETS = 8,
                static MAX_LOAD_FACTOR = 4, head_ = 0x14a78f0, tail_ = 0x14a78f0, ptrs_ = 0x0, allocator_ = 0x14a78d0}, <No data fields>},
            static emptyVariantVector = {<Urho3D::VectorBase> = {size_ = 0, capacity_ = 0, buffer_ = 0x0}, <No data fields>},
            static emptyStringVector = {<Urho3D::VectorBase> = {size_ = 0, capacity_ = 0, buffer_ = 0x0}, <No data fields>}, type_ = Urho3D::VAR_NONE,
            value_ = {{int_ = 0, bool_ = false, float_ = 0, ptr_ = 0x0}, {int2_ = 0, float2_ = 0, ptr2_ = 0x0}, {int3_ = 0, float3_ = 0, ptr3_ = 0x0}, {
                int4_ = 0, float4_ = 0, ptr4_ = 0x0}}}, static emptyBuffer = {<Urho3D::VectorBase> = {size_ = 0, capacity_ = 0,
              buffer_ = 0x0}, <No data fields>}, static emptyResourceRef = {type_ = {static ZERO = {
                static ZERO = <same as static member of an already seen type>, value_ = 0}, value_ = 0}, name_ = {static NPOS = 4294967295,
              static MIN_CAPACITY = 8, static EMPTY = {static NPOS = 4294967295, static MIN_CAPACITY = 8,
                static EMPTY = <same as static member of an already seen type>, length_ = 0, capacity_ = 0,
                buffer_ = 0x1435680 <Urho3D::String::endZero> "", static endZero = 0 '\000'}, length_ = 0, capacity_ = 0,
              buffer_ = 0x1435680 <Urho3D::String::endZero> "", static endZero = 0 '\000'}}, static emptyResourceRefList = {type_ = {static ZERO = {
                static ZERO = <same as static member of an already seen type>, value_ = 0}, value_ = 0}, names_ = {<Urho3D::VectorBase> = {size_ = 0,
                capacity_ = 0, buffer_ = 0x0}, <No data fields>}}, static emptyVariantMap = {<Urho3D::HashBase> = {static MIN_BUCKETS = 8,
              static MAX_LOAD_FACTOR = 4, head_ = 0x14a78f0, tail_ = 0x14a78f0, ptrs_ = 0x0, allocator_ = 0x14a78d0}, <No data fields>},
          static emptyVariantVector = {<Urho3D::VectorBase> = {size_ = 0, capacity_ = 0, buffer_ = 0x0}, <No data fields>},
          static emptyStringVector = {<Urho3D::VectorBase> = {size_ = 0, capacity_ = 0, buffer_ = 0x0}, <No data fields>},
          type_ = Urho3D::VAR_RESOURCEREFLIST, value_ = {{int_ = 1497956967, bool_ = 103, float_ = 3.53619448e+15, ptr_ = 0x59490267}, {int2_ = 0,
              float2_ = 0, ptr2_ = 0x0}, {int3_ = 0, float3_ = 0, ptr3_ = 0x0}, {int4_ = 36354000, float4_ = 1.25423791e-37, ptr4_ = 0x22ab7d0}}}[/code]

-------------------------

vivienneanthony | 2017-01-02 01:09:02 UTC | #2

"int_ = 1497956967, bool_ = 103, float_ = 3.53619448e+15, ptr_ = 0x59490267 " looks odd to me. Like either inaccessible memory or bad memory area(hinting to the segfault)?

-------------------------

vivienneanthony | 2017-01-02 01:09:07 UTC | #3

Do anyone know how I can reach Scorvi? I'm been looking at the code for days and I can't troubleshoot whats wrong.

-------------------------

vivienneanthony | 2017-01-02 01:09:08 UTC | #4

Or thebluefish, any help appreciated...

-------------------------

gwald | 2017-01-02 01:09:09 UTC | #5

[quote="vivienneanthony"]Do anyone know how I can reach Scorvi? I'm been looking at the code for days and I can't troubleshoot whats wrong.[/quote]

[scorviblog.tumblr.com/ask](http://scorviblog.tumblr.com/ask)

-------------------------

vivienneanthony | 2017-01-02 01:09:10 UTC | #6

[quote="gwald"][quote="vivienneanthony"]Do anyone know how I can reach Scorvi? I'm been looking at the code for days and I can't troubleshoot whats wrong.[/quote]

[scorviblog.tumblr.com/ask](http://scorviblog.tumblr.com/ask)[/quote]

Thanks. I got it to run better.

[imgur.com/a/FYe51](http://imgur.com/a/FYe51)

Still probably contact Scorvi if I run into more problems.

-------------------------

thebluefish | 2017-01-02 01:09:14 UTC | #7

My derivative from Scorvi's work was made to fit into the frame that I was using at the time. Thus, it is somewhat different than what Scorvi gave out.
[url=https://github.com/thebluefish/Urho3DEditor]You can check it out here[/url], but no guarantees that it's any help.

-------------------------

vivienneanthony | 2017-01-02 01:09:14 UTC | #8

[quote="thebluefish"]My derivative from Scorvi's work was made to fit into the frame that I was using at the time. Thus, it is somewhat different than what Scorvi gave out.
[url=https://github.com/thebluefish/Urho3DEditor]You can check it out here[/url], but no guarantees that it's any help.[/quote]

I looked at your version and made some adjustments using it plus some additional code. I added.

It worked. The window on the side is not fully rendering like there is left window borders on the window but generally it works. I did not fully include the drag and drop code.

I added delete in the hierarchy functionality and additional menu bar menus.

-------------------------

