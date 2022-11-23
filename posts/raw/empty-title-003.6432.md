vram32 | 2020-12-11 13:11:32 UTC | #1

Empty content.......

-------------------------

vmost | 2020-12-11 13:11:14 UTC | #2

Here are two ways:
1. Pass a pointer to the Application object into the constructor of Char. Since MyApp is essentially a singleton created as a local variable in `main()`, you'll never run into problems with memory safety unless you try to delete it, or try to store the pointer in a smart pointer (shared or unique, which will delete it when the ptr gets destroyed).
2. Make MyApp an Urho3D::Subsystem, then just call `GetSubsystem<MyApp>()` whenever you want it. I have been pondering if this is architecturally sound or basically flawed/dangerous OO. Note: executing `RemoveSubsystem<MyApp>()` will crash your program.

The correct way to do it (pardon my edits viewers) is to add this macro to your application class declaration:
```
class MyApp final : public Application
{
    URHO3D_OBJECT(MyApp, Application);
    ...
}
```
Then in the constructor register as a subsystem:
```
MyApp::MyApp(Context *context) : Application{context}
{
    context_->RegisterSubsystem(this);
}
```
Then use it as a standard subsystem:
```
GetSubsystem<MyApp>()->Test();
```

Note: in your example `App::Test()` could be declared static, which would allow you to call it from anywhere without needing an instance of `App`.

-------------------------

Pencheff | 2020-10-12 03:09:28 UTC | #3

You could also do [code]DynamicCast<App>(GetSubsystem<Application>())->Test()[/code].

-------------------------

vmost | 2020-10-12 03:10:41 UTC | #4

Yeah it's pretty verbose though. Adding the macro is super easy

-------------------------

Modanung | 2020-10-13 10:02:53 UTC | #6

Also, welcome to the forums! :confetti_ball: :slightly_smiling_face:

-------------------------

weitjong | 2020-12-12 05:49:37 UTC | #8



-------------------------

