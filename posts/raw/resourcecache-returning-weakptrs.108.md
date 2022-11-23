Azalrion | 2017-01-02 00:58:02 UTC | #1

I was wondering whether it would be worth moving the ResourceCache to use WeakPtrs instead of raw now we've moved Events and Variant over? If there are any implications around it (haven't tried, currently on a trip).

[code]
template<typename T>
WeakPtr<T> GetResource(String name);

template<typename T>
WeakPtr<T> GetResource(char* name);
[/code]

-------------------------

cadaver | 2017-01-02 00:58:02 UTC | #2

It's slightly different. Variant pointers in the events used to be void pointers, which would need to be unsafely cast to an object type you had to practically guess. In this case it's good to have the object references as WeakPtr's because the lifetime of the Variant or VariantMap is unknown, and can possibly outlive the object being pointed to.

On the other hand, when we're requesting a resource, we can be sure it won't be immediately be blown away from under our feet, because the ResourceCache itself holds a SharedPtr to it. Using raw pointers in the majority of function parameters or return values (scene manipulation, resources etc.) makes the functions easier to expose to script. The caller can also immediately convert the raw pointer to a SharedPtr or WeakPtr at will, because they're intrusively counted and the refcount structure always comes with the object itself.

As a summary: I don't see a need for this change now.

-------------------------

Azalrion | 2017-01-02 00:58:02 UTC | #3

Good enough for me, the only case where they could be considered unsafe is after ReleaseAllResources but I expect that could be classed as a programming error trying to access a saved raw pointer after calling that.

-------------------------

cadaver | 2017-01-02 00:58:03 UTC | #4

Right, certainly I would never recommend holding a raw pointer to a resource for example as a member variable, in that case either SharedPtr or WeakPtr is more appropriate.

In AngelScript a handle will automatically act like a SharedPtr. The Lua bindings, on the other hand, are somewhat evil in this respect, because either an object will be auto-garbage collected (this is never used for something the engine returns to you, like resources) or it simply doesn't care of the object lifetime and expects the pointer to stay valid.

-------------------------

OvermindDL1 | 2017-01-02 00:58:03 UTC | #5

The LUA bindings I have used before (the ones that were ported from boost::python, whatever it was called, this was years ago), handled lifetime management better than that as I recall?  Maybe see how it did it?

-------------------------

weitjong | 2017-01-02 00:58:03 UTC | #6

[quote="cadaver"]Right, certainly I would never recommend holding a raw pointer to a resource for example as a member variable, in that case either SharedPtr or WeakPtr is more appropriate.[/quote]

I agree with that and your summary in earlier post. That said, I have observed in a very few places in our code that a raw resource pointer is being converted into SharedPtr in a locally scoped variable. I am asking myself whether that is really necessary. The reference count would be decremented when the variable goes out of scope but, as you said, the actual resource is still being cached in the ResourceCache as it still holds a SharedPtr to it. For example:
- In Texture3D::Load(Deserializer& source) method. The pointer conversion is required could be because of Texture3D::Load(SharedPtr<Image> image, bool useAlpha) needs it. But why the latter needs it to be SharedPtr?
- In HelloGUI::Start() method.

-------------------------

cadaver | 2017-01-02 00:58:03 UTC | #7

The Texture2D load function uses SharedPtr to automate memory management when it needs to request lower sized mips from Image. In that case the initial image pointer is overwritten with each smaller mip, and as the loading proceeds, each previous intermediate mip is automatically freed. That could however be refactored to take the initial image as a raw pointer, and use the SharedPtr in the mip loading loop only.

HelloGUI code is simply non-idiomatic code and needs to be refactored so that unnecessary refcount management and giving an overly convoluted example is avoided.

EDIT: took a detailed look, having Texture2D/3D/Cube take in an image raw pointer would potentially be dangerous, or need making the code a lot more complicated. As the mip loop promotes the image to shared pointer, it has the danger of deleting the image if it was not held in a shared pointer to begin with, and in that sense it's better to make it explicit in the function signature that a SharedPtr is being used.

-------------------------

weitjong | 2017-01-02 00:58:04 UTC | #8

Many thanks for the detail explanation, I have overlooked the mip looping part.

-------------------------

