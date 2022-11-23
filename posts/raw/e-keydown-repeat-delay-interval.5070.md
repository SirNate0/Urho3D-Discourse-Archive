Lunarovich | 2019-04-03 22:58:00 UTC | #1

Hello! Is there a way to set a repeat delay/interval when holding a key down?

When I handle input->GetKeyDown in E_KEYDOWN handler, I get a key press reported immediately. There's a short time period ~250ms before I get a second key down event reported, and afterwards interval gets shorter and is ~100ms.

Thank you.

-------------------------

Leith | 2019-04-04 05:29:47 UTC | #2

Sorry this does not directly answer your question about rate of repeated keypress...

Input->GetKeyDown() is an instantaneous test of the state of a particular key ... You can call it any time, eg from inside the Update() method - you don't need to register for E_KEYDOWN event in order to check the state of keys.

If you do choose to use E_KEYDOWN event, be aware that the event data can tell you exactly which key is being pressed:
[code]
void GameMainMenuState::HandleKeyDown(StringHash eventType, VariantMap& eventData)
 using namespace KeyDown;
            int key = eventData[P_KEY].GetInt();
            if (key == KEY_SPACE)
            ...
[/code]

-------------------------

Lunarovich | 2019-04-04 08:46:20 UTC | #3

 @Leith Thank you. Actually, in *InputEvents.h* I've found 

    /// Key pressed.
    URHO3D_EVENT(E_KEYDOWN, KeyDown)
    {
        URHO3D_PARAM(P_KEY, Key);                      // int
        URHO3D_PARAM(P_SCANCODE, Scancode);            // int
        URHO3D_PARAM(P_BUTTONS, Buttons);              // int
        URHO3D_PARAM(P_QUALIFIERS, Qualifiers);        // int
        URHO3D_PARAM(P_REPEAT, Repeat);                // bool
    }

This P_REPEAT could be probably useful for my purposes. However, it does not set a key repeat delay.

Another question. Is it possible to poll, by means of Input, whether ANY key is down and just for a SPECIFIC key?

-------------------------

Leith | 2019-04-04 10:21:52 UTC | #4

Internally, Urho3D caches the entire keyboard state, and sends events for keys that are pressed as a bonus - you can query the state of any key, pretty much any time, at low cost. The keydown event was meant to act as a catch-all, so you didn't need to poll for keys. But polling cost is low. You're effectively querying the internal cached state.

-------------------------

Leith | 2019-04-05 19:07:54 UTC | #5

Closer to answering your question, I believe Urho is using SDL for input, and I know SDL has a way to set the delay on initial and repeated keydown events - but I feel it needs to be called early, and I am not certain Urho supports this...

[quote]
 calling SystemParametersInfo (SPI_SETKEYBOARDDELAY, 0, 0, 0) at the start of the program and SystemParametersInfo (SPI_SETKEYBOARDDELAY, 1, 0, 0) at the end, to return to standard key repeat delay.
[/quote]

-------------------------

Lunarovich | 2019-04-04 13:49:41 UTC | #6

I've solved the problem by using HashSet instance defined as **HashSet\<int> keysDown**:

    void Game::HandleKeyDown(StringHash eventType, VariantMap& eventData)
    {
        using namespace KeyDown;

        int key = eventData[P_KEY].GetInt();

        if (key == KEY_ESCAPE)
            {
                engine_->Exit();
            }

        keysDown.Insert(key);
    }

    void Game::HandleKeyUp(StringHash eventType, VariantMap& eventData)
    {
        using namespace KeyUp;

        int key = eventData[P_KEY].GetInt();

        keysDown.Erase(key);
        if (keysDown.Empty()) {
        // do something
        }
    }

-------------------------

Leith | 2019-04-05 01:38:58 UTC | #7

That's certainly a valid approach. Internally, Urho's Input class contains a member called KeyDown_, which is indeed a HashSet<int>, but unfortunately it's private, and you're expected to call GetKeyDown() in order to access that array. You're duplicating an existing array, but the standard practice seems to be to query the state of a specific subset of possible keys, and to cache the results in your program, so your solution is slightly more costly, but a lot more flexible, than the typical implementation.
HashSet is a sparse unordered container, which means that queries/lookups require a search of the keyspace - I don't remember the numerical range of SDL keycodes, but it seems to me, it might be more efficient to use a flat array of booleans? Anyway, glad you found a solution that works for you :)

-------------------------

