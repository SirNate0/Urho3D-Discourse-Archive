chenjie199234 | 2018-07-26 03:31:22 UTC | #1

when change scene,i need a load bar ui,change from 0% to 100%.
how to do this?
i create a load bar and change it manully.
but change scene will finish in one frame and this ui will not work!
how to do this

-------------------------

jmiller | 2018-07-26 18:48:00 UTC | #2

Hello,

Perhaps to help get you going, there have been a number of forum threads ([url=https://discourse.urho3d.io/search?q=loading+screen]loading screen[/url]), some things in https://github.com/urho3d/Urho3D/wiki (Background loading) and a working recent example in https://github.com/ArnisLielturks/Urho3D-Empty-Project

-------------------------

chenjie199234 | 2018-07-27 02:55:24 UTC | #3

im creating scene by code...not by load from file/xml/json.
every element in my scene was created by c++ code.
the load bar will add 0.1% when each element was created!
how to do this async?

-------------------------

jmiller | 2018-07-27 05:08:04 UTC | #4

I think those approaches should be relevant if using the usual Create*, Scene::LoadAsync(), Scene::LoadAsyncXML(), if I understand what you mean.

https://discourse.urho3d.io/t/background-scene-loading-thread/1394/2

My C++ state manager is inspired by a nice Urho-flavored one by **OvermindDL1**. A State subclass can handle incremental scene creation while displaying updates, for example.
https://discourse.urho3d.io/t/overlib/762
https://github.com/OvermindDL1/Urho3D-OverLib

-------------------------

