rbnpontes | 2017-01-02 01:15:01 UTC | #1

Hello guys, i have a big problem, i migrate my project to Visual Studio 2013 but, if i'm compile will give me this error : [b][color=#FF0000]error C3083: '{ctor}': the symbol to the left of a '::' must be a type[/color][/b]
this error only appears if i use URHO3D_HANDLER to SubscribeEvents

-------------------------

1vanK | 2017-01-02 01:15:01 UTC | #2

check ClassName in URHO3D_HANDLER(ClassName, Method)

-------------------------

rbnpontes | 2017-01-02 01:15:01 UTC | #3

I found error, is because in URHO3D_HANDLER the function call this : URHO3D_HANDLER(className, function) (new Urho3D::EventHandlerImpl<className>(this,[b] &className::function[/b]))
but when im call URHO3D_HANDLER im put Class+Function, in VS 2015 this error is ignored but in 2013 not,
It would be something this :
[b]wrong[/b]
URHO3D_HANDLER(ClassName,ClassName::Update)
[b]correctly[/b]
URHO3D_HANDLER(ClassName,Update)

-------------------------

