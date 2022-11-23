rku | 2017-08-15 13:59:06 UTC | #1

I ran into most unexpected issue - subclassing `UIElement` breaks layout. I have nothing-out-of-ordinary UI layout loading which into `UIElement` works fine. Everything is displayed in the middle of the screen. Then i try to subclass `UIElement` and loading this layout into my subclassed object sticks all controls at top-left corner. Layouting breaks.

My class:
```cpp
class WindowAnimated
    : public UIElement
{
    URHO3D_OBJECT(WindowAnimated, UIElement);
public:
    WindowAnimated(Context* ctx) : UIElement(ctx) { }
    void RegisterObject(Context* context)
    {
        context->RegisterFactory<WindowAnimated>(UI_CATEGORY);
        URHO3D_COPY_BASE_ATTRIBUTES(UIElement);
    }
};
```
And i do call `WindowAnimated::RegisterObject()` in `Setup()` of my application.

I load ui something like this:
```cpp
auto window = ui->GetRoot()->CreateChild(WindowAnimated::GetTypeNameStatic());
auto xml = cache.GetResource<XMLFile>(resource);
window->LoadXML(xml->GetRoot());
window->SetStyleAuto();
```

Are there any other requirements when subclassing UI elements?

My layout: <a class="attachment" href="//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/6f4ac5ebd2f38512816b7b919c7bdc5eec5761bd.csv">MainMenu.xml.csv</a> (3.5 KB) (Rename to `MainMenu.xml`).

-------------------------

rku | 2017-08-16 14:13:58 UTC | #2

Answer is that there are no other requirements, only that `RegisterObject()` is called *after* UI subsystem was initialized. I tripped on this since i use urho3d ui in another engine. Since this can not possible be an issue with Urho3D thread can be deleted.

-------------------------

