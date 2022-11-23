sphaero | 2017-01-02 01:00:47 UTC | #1

I know this is probably been discussed all over before... but how much effort would it be to add Python as a scripting interpreter? I know there is already Lua and Angelscript which are leaner than Python. However I'm confronted with situations in which a lot of things are already done in Python hence the question.

How much work would it be, and where would one start?

-------------------------

boberfly | 2017-01-02 01:00:48 UTC | #2

Hi Sphaero,

This may be a lot of work to make the initial bindings. First I guess you'd need to find your ideal binding helper code/library and there's many to choose from (boost::python, shiboken, swig, cython, Py++) or just the vanilla API. Or, you could make a C-API to Urho3D and use ctypes. Lots of ways to go about it.

I for one would really _really_ like bindings for Python for easy integration into 3D DCC packages. I wouldn't use it for anything runtime though due to performance. I'd recommend boost::python, and Py++ would make it even easier (it sits on top of boost::python and uses gcc's xml backend to generate the bindings) but it isn't maintained. Shiboken is what Qt uses but the library is LGPL unless you don't mind dynamic linking.

To start, I'd look into the C++ public headers of Urho3D and see what you need to bind. There's also:
[url]https://github.com/urho3d/Urho3D/tree/master/Source/Engine/Script[/url]
Which shows the AngelScript binding which could be a good place to study and adapt to Python instead.

-------------------------

sphaero | 2017-01-02 01:00:48 UTC | #3

Thanks for the reply and thanks for the pointers. I don't think Urho depends on boost, right? Having Python support could be just a 'plugin'. Is there any 'plugin' support or directives for Urho?

I'm still in the process of reviewing Urho. I'm also looking at the fact that DCC's and many other programs have Python support. I'm having a hard time getting devs to support LUA or AngelScript outside of game development fields.

-------------------------

cadaver | 2017-01-02 01:00:48 UTC | #4

There is no official plugin structure so far in Urho. Rather, at the moment it's expanded by just linking any additional functionality (such as the python bindings) as part of your application. That can be in a static lib, dynamic lib, or just directly part of your executable, Urho doesn't care. 

Urho has not / should not have any knowledge of the additional things, but there are certain hooks (like registering event listeners, new subsystems and new object factories) that allow the additional functionality to be bound to the rest of the system.

-------------------------

OvermindDL1 | 2017-01-02 01:01:17 UTC | #5

Python would not be hard, but if someone were to make another binding layer it might be useful to use one of those that can bind to 'many' languages at once, including Python.  Even as it stands the LuaJIT binding is *extremely* inefficient.  LuaJIT reaches at or near C speed with both code and calling through its binding when bound properly, but when binding through the LUA API it is *extremely* inefficient, more so than stock LUA as it has to convert from native code to the LUA layer, just for your binding layer to do the opposite.  LuaJIT's FFI bindings are just raw pointer bindings into the tracing JIT and as such can be optimizes as expected.  Personally I would look forward to a proper LuaJIT binding layer as it has immense capabilities and speed, outdoing even V8.

-------------------------

