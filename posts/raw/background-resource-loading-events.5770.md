Naros | 2019-12-17 02:38:32 UTC | #1

So I have been looking into using the background resource loading semantics in `ResourceCache`, but I've ran into something I'd like to understand if there is a better solution for.

Lets say there are 10 objects that have subscribed to `E_RESOURCEBACKGROUNDLOADED`, and each of these objects have requested different files to be loaded.  In the event callback function, I'm having to write something like this:

```
void Tile::OnResourceLoaded(Urho3D::StsringHash eventType, Urho3D::VariantMap &eventData)
{
  using namespace Urho3D;
  using namespace Urho3D::ResourceBackgroundLoaded;
  if ( eventData[ P_SUCCESS ].GetBool() )
  {
    auto resource = reinterpret_cast<Resource*>( eventDAta[ P_RESOURCE ].GetPtr() );
    if ( resource->GetName().Compare( queuedResourceName ) == 0 )
    {
      // handle it here
    }
  }  
}
```

Is there anyway to actually do it more along the lines of this:
```
void Tile::OnResourceLoaded(Urho3D::StsringHash eventType, Urho3D::VariantMap &eventData)
{
  using namespace Urho3D;
  using namespace Urho3D::ResourceBackgroundLoaded;
  if ( eventData[ P_USERDATA ].GetPtr() == this && eventData[ P_SUCCESS ].GetBool() )
  {
    // do logic
  }
}
```

I can certainly modify the source of the engine or re-implement this in a custom way, but before I go down either of those paths, I was curious if there was any sort of way of actually indicating that only a single recipient is interested in a specific event.

-------------------------

SirNate0 | 2019-12-17 22:20:20 UTC | #2

It's not an answer to your question, but if it's just about the speed of the string compassion you could use GetNameHash() instead for the name comparison.

-------------------------

Naros | 2019-12-18 06:51:05 UTC | #3

Thank @SirNate0, that would definitely be an optimization for sure, but the basis for my question is to better understand if what I am after is outside the scope/usage of the event system.

From what I've gathered, this simply isn't something the system provides out of the box.  I understand in the general sense that multiple recipients may be interested in being notified when the same resource becomes loaded, e.g. multiple objects that share a texture.  

When its explicitly known up front that a single Object is only ever interested in being informed when a resource has been loaded, wouldn't it make sense to offer a way to short-circuit the dispatch of the handlers somehow?

I have considered overloading `BackgroundLoadResource` that accepts a `Urho3D::Object` pointer that the caller can use to provide an intended recipient and when its not-null, that object will be used to masquerade the event dispatch.  This would allow an object to subscribe to the event on itself for my use case and therefore only its event handler would be informed when the resource is loaded.  

While that would work, is there a better way as I'd prefer to avoid engine changes where possible to keep upgrade paths easy and clean where possible.

-------------------------

