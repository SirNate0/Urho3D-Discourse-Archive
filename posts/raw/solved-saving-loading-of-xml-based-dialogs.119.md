Xardas | 2017-01-02 00:58:09 UTC | #1

Automatically saving/loading of POD types is easy using the ATTRIBUTE macro inside RegisterObject(Context* context).

But what if I wanted to automatically save/load the changes of a Resource, in this case an XMLFile. I see there is a VAR_RESOURCEREF as part of the VariantType enum, but how would I use it with the ATTRIBUTE macro and my XMLFile?

-------------------------

cadaver | 2017-01-02 00:58:09 UTC | #2

The serialization system doesn't readily extend into saving whole resources automatically. Normally attributes only refer to a resource, which the VAR_RESOURCEREF is for (think of model / material attributes in StaticModel)

However, there's one workaround which is possibly a bit ugly. You can save a binary buffer inside a Variant. Look at how the NavigationMesh component stores its data. 

By using the ACCESSOR_ATTRIBUTE macro you can define get and set functions for the attribute. In several cases those get/set functions are "fictional" -> they're just used for the attribute serialization, not as actual user-callable getters & setters. For example in NavigationMesh, the functions GetNavigationDataAttr() & SetNavigationDataAttr() serialize the navigation mesh into a binary buffer variant. Or a slightly more normal example, GetModelAttr() & SetModelAttr() in StaticModel, which form a ResourceRef variant from the current model.

Another way is to just load and save your XMLFile into a separate, ordinary file. I'd actually recommend that. If you need that to happen automatically as a part of Serializable load / save, those functions are virtual so you can override them.

-------------------------

Xardas | 2017-01-02 00:58:09 UTC | #3

The thing is, I would like to have only a single save file, where everything is contained, including all the dialogs and also the scene itself. The problem is, I can't successfully load the xml dialog(s) (saving is not a problem) because XMLFile::Load returns false here:

if (source.Read(buffer.Get(), dataSize) != dataSize)
        return false;

It is assuming that the file only contains the xml dialog, but in my case it includes much more.

I tried doing it like in the StaticModel example you mentioned, but that doesn't save the xml. I assume I would have to do it like in the NavigationMesh example (using a buffer) and traverse the whole xml file when implementing my own Get/SetDialogAttr methods.

-------------------------

cadaver | 2017-01-02 00:58:09 UTC | #4

In general resources always assume they're the only thing being read from a Deserializer, because how else would an XML file know how big the actual data is? But you can work around like this:

- Save XMLFile into a temporary buffer (VectorBuffer)
- Get the size of the buffer after save
- Write the size to your save file, followed by data. You can repeat this for as many data files as you wish.
- When loading, read the data size from the file first, then read the data into another temporary VectorBuffer. Perform XML file load from the buffer, not from the file.

-------------------------

Xardas | 2017-01-02 00:58:09 UTC | #5

Ah, that's a good idea. Ok, so I did this but now it can't properly load the dialog components. It says "Component type 013F not known, creating UnknownComponent as placeholder".

Am I overriding Load/Save correctly, or does it interfere with RegisterObject or something?


[code]
bool Dialog::Load(Deserializer& source, bool setInstanceDefault)
{
    unsigned size = source.ReadUInt();

    VectorBuffer temp;
    if (source.Read(temp.GetModifiableData(), size) != size)
        LOGERROR("Load might be corrupted");

    m_dialogXML->Load(temp);

    return Component::Load(source, setInstanceDefault);
}

bool Dialog::Save(Serializer& dest) const
{
    VectorBuffer temp;
    m_dialogXML->Save(temp);

    unsigned size = temp.GetSize();

    if (!dest.WriteUInt(size))
        LOGERROR("Save might be corrupted");
    if (dest.Write(temp.GetData(), size) != size)
        LOGERROR("Save might be corrupted");

    // Write attributes
    return Component::Save(dest);
}
[/code]

-------------------------

cadaver | 2017-01-02 00:58:10 UTC | #6

Component loading expects the data stream to contain type & ID first, because those are actually loaded in Node's code, so that it knows what component to create.

-------------------------

Xardas | 2017-01-02 00:58:10 UTC | #7

Getting closer. Now "source.Read(temp.GetModifiableData(), size" crashes, because GetModifiableData() seems to return null.

When I do this:

[code]
PODVector<unsigned char> buffer(size);
VectorBuffer temp(buffer);
[/code]

it still crashes, and I don't get any debug information (only show disassembly).

-------------------------

cadaver | 2017-01-02 00:58:10 UTC | #8

Perhaps in this case MemoryBuffer is actually more appropriate, for that one you can manually assign the data buffer to use.

The crash likely happens because you're reading to a null size or not large enough buffer. Now that I look at it VectorBuffer doesn't have a convenient function to resize the buffer at once, instead it's usually written to in increments, ie. WriteInt() etc. so that it expands the buffer on demand. I will look into providing a VectorBuffer::Resize() or similar later.

-------------------------

Xardas | 2017-01-02 00:58:10 UTC | #9

Yay. I got it working now. The crash was actually unrelated to the buffer issue. As always, thanks for your help!

-------------------------

cadaver | 2017-01-02 00:58:10 UTC | #10

Nice that you got it working. Hm, VectorBuffer in fact already has Resize(). For some reason I didn't spot it in the morning.

-------------------------

