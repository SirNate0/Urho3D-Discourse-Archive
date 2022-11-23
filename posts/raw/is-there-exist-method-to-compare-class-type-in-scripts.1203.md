codingmonkey | 2017-01-02 01:06:02 UTC | #1

Is there exist method to compare class type? 
I mean I need something similar 
if (component is Drawable) 
{
 // todo something
}

but now I do this check like this with cast<baseclass> and if cast<> successful the result is not null
[code]
Component@ component = components[componentIndex];
Drawable@ drawable = cast<Drawable>(component);
if (drawable !is null) 
{
  // todo something
}[/code]

-------------------------

