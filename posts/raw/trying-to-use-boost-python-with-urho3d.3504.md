allked | 2017-08-29 02:42:50 UTC | #1

I got them compile together, now I have to expose class to python,but every urho3d class comes with a context pointer as constructor parameter,how to avoid use that to let cop handle context only? Is it possible? I Have created a tiny library which has instance pointer of class everywhere, but when deal with context,I have no clue how to do it,thanks for help.

-------------------------

S.L.C | 2017-08-29 04:56:03 UTC | #2

Off: Might aswell go for https://github.com/pybind/pybind11

-------------------------

allked | 2017-08-29 05:24:54 UTC | #3

Thanks I will try it

-------------------------

JoelStienlet | 2017-12-20 17:02:24 UTC | #4

I'm interested in bindings for python too.
Indeed there're many tools to simplify building a c++ <-> python interface, Pybind11 seems more complete than PyCXX. I don't like boost because it's so cumbersome.
In my opinion it may be better to keep an explicit context pointer as the user may want to create multiple contexts (don't know why he would do that, but keeping code as flexible as possible is certainly a good choice)
For the rendering window: do you want to build a new tk widget or will you keep the SDL display?

-------------------------

