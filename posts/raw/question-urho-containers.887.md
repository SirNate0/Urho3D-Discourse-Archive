TikariSakari | 2017-01-02 01:03:49 UTC | #1

Hello, I noticed that urho has its own containers such as hashmap etc. I was wondering if there is any kind of problem if I would use stl-container such as std::map. I am trying to make a map of all the buttons on my interface, so that I can resize them easier when resizing window on desktops. The problem I ran into with Urho3D-hashmap is that UIElement or Button-type components do not have parameterless constructor and therefore fails on build.

I tried to read the document about containers, it only had benefits on using urhos own containers, but if I correctly understood it, the stl-containers should work on all build systems?

On the other hand my method of having to resize every single component + font based on window size might be wrong way to approach resolution independent user interface. Basically I am planning on doing something like buttons text height is 1/20 pixels of the height of the screen, and then just add the text to a button. Then go through every single ui-component and resize them based on the "default" button height.

Edit: A random side note, the default font: "Anonymous Pro" is invisible at font height of 36, 47, 48 and 72. I made an issue in the github about this.

-------------------------

thebluefish | 2017-01-02 01:03:49 UTC | #2

There's nothing inherently wrong with using stl's containers, but they do have some downsides. The main issue is that you don't get to use the Reference Counter that all Urho3D objects are built on, and that can create weird issues with objects being unintentionally deleted.

Honestly, I wouldn't use this approach for resolution independence. What I do, and what I did successfully with LibGDX, was to design my interface around a "target" resolution. Then I would calculate the scaling differences, and apply those to my object creation. In Urho3D, my approach has been to create the UI like normal, and use the setter functions to set the size. I would calculate the actual size by multiplying my target size with the scalar, and that would achieve resolution independence without deviating from the Urho3D way of managing things.

-------------------------

cadaver | 2017-01-02 01:03:49 UTC | #3

Regardless of whether you use STL containers or Urho containers, you should not try to contain RefCounted subclasses like UI elements as value types; they're not meant to be copied around, so the failure you observe is intentional. The containers actually don't participate in the reference counting in any way, so from that point it's not important which you use. But you should never use std::shared_ptr with Urho refcounted classes, as that uses its own (extrusive) reference counting and doesn't work right with RefCounted intrusive counting.

The UI hierarchy already contains your UI elements and keeps them alive via SharedPtr vectors of child elements, so depending on which degree of safety and lifetime semantics you want you should use one of these:

HashMap<key, UIElement*>
HashMap<key, SharedPtr<UIElement> >
HashMap<key, WeakPtr<UIElement> >

The font rendering bug is likely due to FreeType itself, as the fonts seem to be correct sized but do not have any content. So updating FreeType seems like the only course of action to try.

-------------------------

