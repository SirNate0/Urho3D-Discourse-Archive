halcyonx | 2017-06-09 20:38:22 UTC | #1

Hi everyone! I look through https://urho3d.github.io/documentation/HEAD/_main_loop.html, the application framework section and this https://github.com/urho3d/Urho3D/wiki/First-Project as extended application framework. 
Now I want to add some game logic to application. I think I should make some private members to class

class MyApp : public Application {
public:
...
private:
    AppDelegate _appDelegate;
};

Type AppDelegate will be contain some game objects as interface an other instances. Should be AppDelegate inherited from Urho3D::Object, and subscribed to events E_KEYDOWN and etc, as well as MyApp class? What is typical and right application achitecture with U3D? I want to decomposite my application to interface, levels, etc. There is a typical way to do this?

-------------------------

johnnycable | 2017-06-09 07:03:33 UTC | #2

You may want to check any one example first, a partial infrastructure is applied there.

-------------------------

Modanung | 2017-06-09 20:43:02 UTC | #3

[quote="halcyonx, post:1, topic:3228"]
Type AppDelegate will be contain some game objects as interface an other instances. Should be AppDelegate inherited from Urho3D::Object, and subscribed to events E_KEYDOWN and etc, as well as MyApp class? What is typical and right application achitecture with U3D? I want to decomposite my application to interface, levels, etc. There is a typical way to do this?
[/quote]

This seems like a sound approach. The `AppDelegate` might be something to register as a subsystem with `context_->RegisterSubsystem`. You can do this with any `Object`. That way `GetSubsystem<AppDelegate>()` will allow any `Object` in the same `Context` to access it.

-------------------------

halcyonx | 2017-06-10 13:01:49 UTC | #4

There is way to write part of logic in Lua? I want to write main game mechanics in C++, but part of program logic I want write in Lua, interface behaviour, configuring of sounds, configuring game objects start points on the screen and etc. These and other parts can be implemented in Lua and connected to main application. What is common way to do this?

-------------------------

Modanung | 2017-06-10 14:02:03 UTC | #5

You'd have to add lua bindings. I have no experience with this, but Urho's source is full of examples.

-------------------------

slapin | 2017-06-14 18:29:00 UTC | #6

Urho's way to add Lua bindings might be a bit hard to do in local tree though.
I use manual bindings, but this might be a bit extreme for new users.

-------------------------

halcyonx | 2017-06-10 17:11:18 UTC | #7

Could you show an example of manually Lua bindings?

-------------------------

halcyonx | 2017-06-10 19:18:50 UTC | #8

I saw samples 22_LuaIntegration and 21_AngelScriptIntegration, it seems sample LuaIntegration is bit lagging but angel script not on my LG X Power

-------------------------

