Kanfor | 2017-01-02 01:10:45 UTC | #1

Hi, urhofriends.

I have other problem today  :cry: 

I don't know why but I can't load a font to a Text.

[code]ResourceCache * cache2 = GetSubsystem<ResourceCache>();
SharedPtr<Text> helloText(new Text(context_));
helloText->SetFont(cache2->GetResource<Font>("Fonts/Anono.ttf"));[/code]

But i can load a XML

[code]ResourceCache* cache = GetSubsystem<ResourceCache>();
XMLFile* xmlFile = cache->GetResource<XMLFile>("UI/DefaultStyle.xml");[/code]

The error in the compilation is:
[color=#FF0000]../Urho3D-1.5/build_debug/include/Urho3D/Resource/ResourceCache.h: In instantiation of ?T* Urho3D::ResourceCache::GetResource(const Urho3D::String&, bool) [with T = Urho3D::Font]?:
Engine.cpp:53:67:   required from here
../Urho3D-1.5/build_debug/include/Urho3D/Resource/ResourceCache.h:263:40: error: incomplete type ?Urho3D::Font? used in nested name specifier
     StringHash type = T::GetTypeStatic();
                                        ^
../Urho3D-1.5/build_debug/include/Urho3D/Resource/ResourceCache.h:264:71: error: invalid static_cast from type ?Urho3D::Resource*? to type ?Urho3D::Font*?
     return static_cast<T*>(GetResource(type, name, sendEventOnFailure));[/color]

In an old project I could use fonts, but not now. It's a mistery  :unamused: 

Thank you!

-------------------------

gawag | 2017-01-02 01:10:45 UTC | #2

"incomplete type" does mean that the compiler doesn't know the definition of the type. It has only seen a "class foobar;" (a class declaration, also called "forward declaration", see [en.cppreference.com/w/cpp/language/class](http://en.cppreference.com/w/cpp/language/class)).
Try
[code]#include <Urho3D/UI/Font.h>[/code]

-------------------------

Kanfor | 2017-01-02 01:10:45 UTC | #3

OOuch....

It's true!

 :blush: 

Thanks again!  :wink:
I had only #include <Urho3D/UI/Text.h>

-------------------------

