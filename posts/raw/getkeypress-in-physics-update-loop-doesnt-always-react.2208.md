TheComet | 2017-01-02 01:13:55 UTC | #1

It seems like the physics update is asynchronous to the normal update - that is, there's no guarantee on the order in which FixedUpdate() and Update() will be called. Sometimes Update() could be called twice before FixedUpdate() is called and vice-versa.

This is a problem when using GetKeyPress() inside of FIxedUpdate(). It doesn't always respond. Some example code:

[code]class Foo : public Urho3D::LogicComponent {
public:
    virtual void Update(float timeStep) override {
        if(input_->GetKeyPress(KEY_SPACE))
            puts("key pressed in Update()");
    }
    virtual void FixedUpdate(float timeStep) override {
        if(input_->GetKeyPress(KEY_SPACE))
            puts("key pressed in FixedUpdate()");
    }
};[/code]

Output after pressing space a few times:

[code]key pressed in FixedUpdate()
key pressed in Update()
key pressed in FixedUpdate()
key pressed in Update()
key pressed in FixedUpdate()
key pressed in Update()
key pressed in Update()
key pressed in Update()
key pressed in FixedUpdate()
key pressed in Update()
key pressed in Update()
key pressed in FixedUpdate()
key pressed in Update()
key pressed in Update()
key pressed in Update()
key pressed in FixedUpdate()
key pressed in Update()
key pressed in Update()
key pressed in Update()
key pressed in FixedUpdate()
key pressed in Update()
key pressed in Update()
key pressed in FixedUpdate()
key pressed in Update()
key pressed in FixedUpdate()
key pressed in Update()[/code]

What's the best way to approach this problem? I suppose you could argue that asking for keypresses in FixedUpdate() is wrong, but I [i]have[/i] to put my physics code in FixedUpdate().

-------------------------

1vanK | 2017-01-02 01:13:55 UTC | #2

FixedUpdate always calls with fixed rate (60 fps by default). You can independently detect keyressing

[code]
bool oldKeySpaceDown = false;

void FixedUpdate()
{
    if (KeyDown(KEY_SPACE) && !oldKeySpaceDown)
    {
        ReactKeySpacePress();
    }
    ...
    oldKeySpaceDown = KeyDown(KEY_SPACE);
}
[/code]

-------------------------

TheComet | 2017-01-02 01:13:58 UTC | #3

Thanks, that worked!

-------------------------

cadaver | 2017-01-02 01:13:59 UTC | #4

GetKeyPress() can be reliably called only in Update() which is called once per engine frame. FixedUpdate() may be called multiple times or not at all on some frame, so the keypress state change may have already happened. The workaround by 1vanK is fine to use, though.

-------------------------

