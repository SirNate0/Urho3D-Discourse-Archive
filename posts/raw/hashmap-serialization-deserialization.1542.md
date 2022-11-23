ToxikCoder | 2017-01-02 01:08:22 UTC | #1

Hello, guys, can you help me?
I have a singleton class which should load and save HashMap. I can't get how to do it. As far as I understood, I should use Serializer and Deserializer, but I can't get how.
Can you give me some example of saving/loading HashMap from file?

-------------------------

cadaver | 2017-01-02 01:08:22 UTC | #2

Take a look at Deserializer::ReadVariantMap() and Serializer::WriteVariantMap(). The format is up to you, but typically you would write the number of elements first, then iterate the map and write each key and value.

-------------------------

ToxikCoder | 2017-01-02 01:08:22 UTC | #3

Thanks. And one more question. How to set output file where I would write my data?

-------------------------

cadaver | 2017-01-02 01:08:22 UTC | #4

The class File inherits from Deserializer & Serializer.

So you'd do something like:

[code]
File file(GetContext());
file.Open("MyFileName", FILE_WRITE);

file.WriteUInt(hashMap.Size());
...
[/code]

-------------------------

