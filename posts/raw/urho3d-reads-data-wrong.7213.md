Kest | 2022-03-08 21:13:42 UTC | #1

Hello,

So I'm working on an importer for a map file. But the deserializer reads the data wrong.
Let me give an example.

For the header in the map file, it has some data then states a name that declares it's a valid file, such as:
[Some data] MAPFILE [More data]. Instead, I have to do file.ReadLine().Contains to make sure it contains it which I don't think it's an approach I'd like, especially since I need to do a lot more reading with Strings, such as texture images and entity data, and when I do ReadString, it treats all data as a String.

All I'm asking is how would I approach this and fix this, as it's causing my a big headache and pushing back development.

Thanks,
Kest

-------------------------

JSandusky | 2022-03-09 03:34:32 UTC | #2

Toss a *map* file onto pastebin or a github gist so someone can see it.

There's nothing inherently wrong with the `ReadLine().Contains(...)` though as a quick failure check but you do need to be aware that you need to Seek(0) later to reset the position if you're going to be feeding a lexer with `ReadAll()` or so on.

`ReadString` does exactly what it should, it eats every character until a null terminal. `Deserializer` is fairly raw and not meant for tokenizing and other lexer tasks. If you need to do lexing consider using stb_c_lexer or another lexer.

If there are no quoted strings (that could contain spaces) in the map format in question then you could chop into words like `ReadIES(...)` does in the RampGenerator. That's only viable for really really simple text formats, beyond that you need a tokenizer.

-------------------------

Kest | 2022-03-09 17:41:59 UTC | #3

Thank you for the reply.

For the map file data, it's structured like the RMesh in SCP: Containment Breach. Here's a file that I picked out: [Example RMesh file](https://github.com/Regalis11/scpcb/blob/master/GFX/map/173_opt.rmesh) 

I'm glad you pointed these functions out, as I was really just confused about any other option. I'll experiment some more.

-------------------------

JSandusky | 2022-03-09 22:47:53 UTC | #4

It's a binary file so deserializer will work, it looks that format is using sized strings instead of null terminated strings like Deserializer expects. In which case a uint32 is storing the size of the string that follows.

Something along the lines of this should do:

```
String ReadSizePrefixedString(Deserializer& src)
{
    static char tempBuffer[512];
    const unsigned strSize = src.ReadUInt();
    src.Read(tempBuffer, strSize);
    return String(tempBuffer, strSize);
}
```

Do be aware that Deserializer knows nothing about endianness so if the format isn't in the system's natural endianness you're going to have problems.

-------------------------

Kest | 2022-05-13 01:26:46 UTC | #5

Thanks for the reply, and thank you for the helpful start!

-------------------------

