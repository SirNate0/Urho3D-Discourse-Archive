Mike | 2017-01-02 00:59:07 UTC | #1

I'm trying to load a VectorBuffer using following code (AngelScript):

[code]
        VectorBuffer buffer;
        buffer.WriteString("some text");
        buffer.Seek(0);
        XMLFile@ xmlFile = XMLFile();
        xmlFile.Load(buffer);
[/code]
I get a "No matching signatures to 'XMLFile:Load(VectorBuffer)'" error.

-------------------------

cadaver | 2017-01-02 00:59:07 UTC | #2

Exposing the Deserializer / Serializer class hierarchy is problematic in AngelScript because some of them are refcounted and some are not. This means that in many cases the load functions have been exposed to accept only a File handle. In this case I believe a manual overload for Resource::Load() with a vectorbuffer can be added.

-------------------------

Mike | 2017-01-02 00:59:08 UTC | #3

Many thanks for the bindings. :slight_smile:

-------------------------

