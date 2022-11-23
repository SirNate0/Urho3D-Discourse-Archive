AntiLoxy | 2019-01-03 17:05:15 UTC | #1

Hey, i need to wrap an event handler into another one, but without success.

    void ContextMenu::addItem(String name, String text, EventHandler* handler)
    {
        ButtonText* item = CreateChild<ButtonText>(name);
        item->SetStyle("ActionItem");
        item->SetFixedHeight(20);
        item->setLabel(text);
        //item->SetVar(VAR_ITEM_HANDLER, handler);

        SubscribeToEvent(item, "Released", [&](StringHash, VariantMap& eventData)
        {
            handler->Invoke(eventData); // crash at this point !
            close();
        });
    }

The function call :  
`contextMenu_->addItem("open", "Open file", URHO3D_HANDLER(LocalWorldEditorState, handleOpenFile));`

-------------------------

S.L.C | 2019-01-03 18:27:39 UTC | #2

Of course it crashes. You capture a reference to `handler` which is a variable (parameter) on the stack that dies at the end of that function. By the time that lambda gets called. That memory in the stack could be something else. And you still reference it and expect it to be a pointer to an `EventHandler`. Since a reference is a pointer and `handler` is a pointer they occupy the same memory so there's no benefit.

Drop the `&` from `[&]` and capture `handler` by value. Or simply use `[=]` if you want to be a bit more verbose.

And I believe you're supposed to use `E_RELEASED` instead of `"Released"`

-------------------------

AntiLoxy | 2019-01-03 18:32:03 UTC | #3

Ho i see, i was misunderstood lambda capture symbol. thanks you.

-------------------------

rku | 2019-01-05 10:57:25 UTC | #4

Be aware of what you are doing. `String name` and `String text` copy strings for no good reason. You should use `const String& text` to take a string reference.

As for lambdas - they easily can cause memory allocation. `std::function<>` has enough storage for two pointers. If you capture more pointers or use `[=]` - that will definitely allocate memory which depending on where you use this may snowball into something very slow.

-------------------------

AntiLoxy | 2019-01-05 12:57:39 UTC | #5

Ok !

> std::function  is guaranteed to not allocate if constructed from a function pointer, which is also one word in size - Stackoverflow

So, i will use the classic way URHO3D_HANDLER(Class, method).
Thank you for enlightening me about the dangerous objects that are lambdas.

-------------------------

rku | 2019-01-05 13:16:35 UTC | #6

You can safely use lambdas for events, just be aware of these things. `[this](StringHash, VariantMap&) { }` is a good bet. Wont allocate as `this` is one pointer and it is enough most of the time. `URHO3D_HANDLER(Class, method)` is essentially the same.

-------------------------

