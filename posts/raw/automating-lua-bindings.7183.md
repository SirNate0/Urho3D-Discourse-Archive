SirNate0 | 2022-02-03 17:02:43 UTC | #1

The other thread got out of hand and was closed, so here is a new one to keep you up to date on my progress on my attempt to automate the Lua binding generation.

---

## Library Options:
(This is not an exhaustive list)

- [luaaa](https://github.com/gengyong/luaaa): The first library I found for the task, which seemed very similar to pybind11 in syntax and thus a good candidate. However, it seems to possibly be missing basic features that would be required for Urho like [supporting class inheritance](https://github.com/gengyong/luaaa/issues/13). If the author gets back to me about how it works maybe it is actually viable.
- [LuaBridge](https://github.com/vinniefalco/LuaBridge): Seems like a more complete version of what luaaa was aiming for, and has recent (2 months old) activity. Also somewhat similar to pybind11 in syntax, and seemingly simpler to set up than some of the others. It's features include:
    * [MIT Licensed](http://www.opensource.org/licenses/mit-license.html), no usage restrictions!
    * Headers-only: No Makefile, no .cpp files, just one `#include` !
    * Simple, light, and nothing else needed (like Boost).
    * No macros, settings, or configuration scripts needed.
    * Supports different object lifetime management models.
    * Convenient, type-safe access to the Lua stack.
    * Automatic function parameter type binding.
    * Easy access to Lua objects like tables and functions.
    * Written in a clear and easy to debug style.
    * C++11 compliant

  **However, it has a few things that aren't supported that might be important to Urho:**
    * Enumerated constants
    * More than 8 parameters on a function or method (although this can be increased by adding more `TypeListValues` specializations).
    * Overloaded functions, methods, or constructors. *(May be annoying to use, but should be doable with adding some decoration to the names like c code, and may not differ from how it is presently)*
    * Global variables (variables must be wrapped in a named scope).
    * Inheriting Lua classes from C++ classes. *(ScriptObject may become more complicated?)*
    * Passing nil to a C++ function that expects a pointer or reference. *(Note, the documentation later makes it seem that nil gets converted to nullptr for functions expecting a pointer, so I'm not sure that this is correct)*
    * Standard containers like `std::shared_ptr`. *(Note, it supoprts different object management models like an intrusive ref-counted pointer with custom container types, so this should actually be fine for us)*
- [LuaBind](https://www.rasterbar.com/products/luabind/docs.html) (probably [this fork](https://github.com/Oberon00/luabind)): More complete than LuaBridge, but less lightweight with the Boost dependency. But it supports some of the things LuaBridge lacks, based on its list of its features: 
    * Overloaded free functions
    * C++ classes in Lua
    * Overloaded member functions
    * Operators
    * Properties
    * Enums
    * Lua functions in C++
    * Lua classes in C++
    * Lua classes (single inheritance)
    * Derives from Lua or C++ classes
    * Override virtual functions from C++ classes
    * Implicit casts between registered types
    * Best match signature matching
    * Return value policies and parameter policies
- [OOLua](https://github.com/gamedevtech/oolua): Seems the last updates were ~9 years ago and the wiki was on GoogleCode and no longer exists. As such I'll probably stick with one of the above options instead, even though "OOLua slightly outperforms LuaBridge in some tests".
- [tolua++](https://github.com/LuaDist/toluapp): Urho's current solution. I don't plan on using it, as generating pseudo-header files to have a tool generate the binding code sounds  a lot more difficult than some of the other options. I also think that it is no longer maintained, though I'm not sure on that point.

---

## Present plan

Currently I'm planning on trying LuaBridge, with it's easier setup and seemingly more recent maintenance. If I find that too limiting, I'll probably switch to one of the LuaBind forks with more recent work (e.g. one that switched to CMake).

The basic roadmap would be:

1. Simple test project evaluating the library like I did with Luaaa to see limitations like not supporting inheritance and how to do the container types and such.
2. Generating bindings, probably starting with the Math subfolder (no SharedPtr's to deal with, and I can test operator handling). Then extend it to support the Container types (String, Vector, HashMap, Variant) and the Core types (Context and Object mainly). Some simple test files would be involved here.
3. Generate bindings for all of the classes and test the existing samples.
4. If the samples need to be rewritten someone else will have to step up unless it's some find+replace type changes, as I am not committed enough to Lua to hand-edit 50 programs. I'll handle a few to test (e.g. Hello World, Physics Stress Test), but I don't think I'll be motivated to finish all 50 if they involve significant changes. Hopefully they don't, and there aren't too many areas where the current manual bindings would differ from the automatic ones.

As a heads up, note that I may choose to use python to generate the bindings, as I find it a lot quicker to work with than C++. Or I may stick with C++ given the excellent work done making the AngelScript binding generator, we'll see. Or a mix of both using [cog](https://nedbatchelder.com/code/cog).

-------------------------

1vanK | 2022-02-03 18:00:59 UTC | #2

I just want to point out one thing that caused me to rewrite the AS binding generator. Derived classes can hide functions of the parent class.

-------------------------

SirNate0 | 2022-02-03 19:52:48 UTC | #3

Could you give me an example where it happens in Urho so I'm certain I understand what you mean.

-------------------------

1vanK | 2022-02-04 01:10:22 UTC | #5

For example any `UIElement` have function `const IntVector2& UIElement::GetPosition() const`, but `Sprite` hide this function and have `const Vector2& Sprite::GetPosition() const` instead

-------------------------

dertom | 2022-02-04 08:11:34 UTC | #6

I heard that sol should also be a good luabinding. So if you struggle with the others:
https://github.com/ThePhD/sol2

Never used it but it is actively developed.

-------------------------

rku | 2022-02-04 08:35:51 UTC | #7

Just so you know - CLang (since v10 or v11) has a flag which allows exporting entire AST as json. I am using it to generate bunch of stuff automatically. You may use it to generate source code for bindings using whatever library you chose.

-------------------------

Avagrande | 2022-02-06 18:46:56 UTC | #8

I don't want to be too rude but the state of Lua in Urho3D is really really bad, auto generation is the least of its problems.

Some of the classes don't even have binding for some of the functions and often it feels like those bindings have been omitted on purpose, primarily cuz they may leak memory and fixing that isn't easy due to the way tolua++ is hacked together to work with Urho3d. 

I have even had issues related to specific platforms as one of such hacks was built for a specific compiler and tracking that down was a total nightmare.

There are memory leaks in places you wouldn't expect and the whole memory management model is really bad as far as Lua is concerned. I was working on a project a while back and I honestly couldn't continue using Lua in production just because of the huge volume of bugs related to it. Not even the typical rules worked eg call delete yourself. I remember having to make custom bug work arounds for specific scenarios such as re-ordering viewports. 

I have since been forced to switch to C++ despite my love for Lua and abandon all the Lua libs alongside it.

Urho3D is already a small project, why even bother with Lua? Wouldn't resources be better spent elsewhere, like geometry shaders or support for more recent rendering techniques. Why not just discontinue Lua? 

Either way, I have had a very good experience with Sol2 and I would very much recommend it, if you do decide to continue support for Lua.  Sol2 has tons of nice features and writing bindings using it doesn't feel too much like a chore since it's readable unlike tolua++
Sure tolua++ can generate automatic bindings but I wouldn't want to ever use them again.
Why write a script to vomit out total trash while spawning hard to trace bugs, if you can just write good bindings in the first place? 

The dev for sol2 is pretty active, I recall reading somewhere they might be working on automatic binding generator already, but it's been a while so I can't link and I don't think it will be ready anytime soon.

However as it is right now, I would never use the Lua side of Urho3D again and discourage anyone else to use it at all. The hiccups in the web Lua samples should have been a warning loud enough for me to stay away. 

My apologies for being so negative, but I have a really sour taste in my mouth considering I have wasted a considerable amount of time dealing with these types of bugs and I feel that if I didn't voice my opinion more resources would be wasted on terrible buggy bindings that will mislead other devs into wasting time just like I have.

-------------------------

JTippetts1 | 2022-02-06 20:35:50 UTC | #9

The original bindings were done using tolua++, a basically defunct bindings library and the source of most of the problems eg memory stuff, and the reason that they need to be redone. I doubt anyone is suggesting staying with tolua++, hence this thread.

-------------------------

1vanK | 2022-04-12 20:16:32 UTC | #10

Any news here? We have some unfixed problems with lua at the moment:
* <https://github.com/urho3d/Urho3D/issues/2886>
* <https://github.com/urho3d/Urho3D/issues/2717>

-------------------------

SirNate0 | 2022-04-18 14:51:58 UTC | #11

Progress is happening, though is slow. Luaaa did not work, so I switched to trying sol2. I had some issues with it's inability to cast from a pointer to a base class to a derived one (e.g. convert the `GetComponent` result to the `StaticModel` that it actually is). With the issue down, I need to test some of the math classes as well, and then it'll just be the easier and more enjoyable binding generation (vs the debugging of a library I'm not familiar with interacting with a language I'm not familiar with and don't really care about).

-------------------------

1vanK | 2022-04-22 17:32:48 UTC | #12

The author of Box2D made significant changes to his library and broke API. Therefore, LUA bindings are currently broken as well. I temporarily (?) disabled LUA support in the engine. LUA support can be returned by reversing this commit: <https://github.com/urho3d/Urho3D/commit/07db16f526eb5438121aed9f00803c0b1f0be8c4>. LUA samples will also need to be fixed

-------------------------

SirNate0 | 2022-07-04 02:31:23 UTC | #13

Automatic Lua bindings are almost finished (I think - a fair bit of testing still remains). In the process I have discovered that Lua lacks some common sense:

```
if 0 then
    print("Why does this still execute!?!")
end
```

-------------------------

weitjong | 2022-07-04 04:36:54 UTC | #14

Re. the falsy value, both LUA and Ruby consider Boolean false and nil as falsy. The rest are truthy, including literal 0.

-------------------------

Batch | 2022-08-16 20:06:21 UTC | #15

[quote="SirNate0, post:11, topic:7183"]
I had some issues with it’s inability to cast from a pointer to a base class to a derived one (e.g. convert the `GetComponent` result to the `StaticModel` that it actually is).
[/quote]

What did you do to get that working?

-------------------------

SirNate0 | 2022-08-17 18:54:38 UTC | #16

I have a HashMap of functions that take an `Urho3D::Object*` (and hidden `sol::state_view`) and return a `sol::object` that is a wrapper around the correct type. As a summary example:

```

extern Urho3D::HashMap<Urho3D::StringHash, std::function<sol::object(Urho3D::Object*,sol::state_view)>> casters;


void bindClass_Urho3D_Node(sol::state_view& lua)
{
    
using namespace Urho3D;


    casters[Urho3D::Node::GetTypeStatic()] = [](Object*o,sol::state_view lua)->sol::object{
        if (o->IsInstanceOf(Urho3D::Node::GetTypeStatic()))
            return sol::make_object(lua,SharedPtr<Urho3D::Node>((Urho3D::Node*)o));
        return sol::nil;
    };


auto type = lua.new_usertype<Urho3D::Node>( "Node"
// Base Classes
    , sol::base_classes, sol::bases<Urho3D::Animatable,Urho3D::Serializable,Urho3D::Object,Urho3D::RefCounted>()

);

...

type["CreateComponent"] = sol::overload(
        [](Urho3D::Node& self, StringHash type, CreateMode mode=REPLICATED, unsigned id=0, sol::this_state sol_state)->sol::object{
            auto o = SharedPtr<Urho3D::Object>(self.CreateComponent(type, mode, id));
            sol::state_view lua(sol_state);
            auto real_type = o->GetType();
            if (!o || !casters.Contains(real_type))
                return sol::nil;
            return casters[real_type](o,lua);
        },
        [](Urho3D::Node& self, StringHash type, CreateMode mode, sol::this_state sol_state)->sol::object{
            auto o = SharedPtr<Urho3D::Object>(self.CreateComponent(type, mode));
            sol::state_view lua(sol_state);
            auto real_type = o->GetType();
            if (!o || !casters.Contains(real_type))
                return sol::nil;
            return casters[real_type](o,lua);
        },
        [](Urho3D::Node& self, StringHash type, sol::this_state sol_state)->sol::object{
            auto o = SharedPtr<Urho3D::Object>(self.CreateComponent(type));
            sol::state_view lua(sol_state);
            auto real_type = o->GetType();
            if (!o || !casters.Contains(real_type))
                return sol::nil;
            return casters[real_type](o,lua);
        } );

...

}
```

-------------------------

