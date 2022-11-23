codder | 2017-01-02 01:12:05 UTC | #1

Hello,

I want to be able to load a generic file as resource so it can be automatically loaded from package or path.
More or less like XMLFile, Image, JSONFile but an unknown type for Urho3D.
Is that possible without creating a custom Resource class?

Something like that:
[code]
ResourceCache* cache = GetSubsystem<ResourceCache>();
File* file_txt = cache->GetResource<File>("CustomFiles/Test.txt");
File* file_bin = cache->GetResource<File>("CustomFiles/Test.bin");
[/code]

I want to be able to Read, Seek, Tell, ...basic IO operations.

-------------------------

weitjong | 2017-01-02 01:12:05 UTC | #2

IMHO, if you just want to be able to read/seek or other basic file I/O operation then you should just use the File class. If you need to "cache" the file, just hold the file object in a shared pointer and keep it in scope. As its name implies, you can only cache "resources" into the ResourceCache subsytem (unless you made custom modification to it too).

-------------------------

cadaver | 2017-01-02 01:12:06 UTC | #3

You can use cache->GetFile() to get a File with benefits of the ResourceCache path or package search. In this case the file isn't "cached" into memory but is rather an open file handle. For most cases that's probably for the better as it's likely you still need to read & interpret contents into some usable form, and this way an extra memory copy is avoided.

-------------------------

codder | 2017-01-02 01:12:06 UTC | #4

cache->GetFile() seems to work but with big files seems a bit slow when opening.
Is GetFile() asyncronous?

-------------------------

cadaver | 2017-01-02 01:12:07 UTC | #5

Anything regarding files in Urho is synchronous (block until done.) However it should be safe to access GetFile() in a background thread if the blocking is a concern. Also you can check File::Open which it eventually ends up calling. It does a seek to the end to determine file size so that could impact the execution time with large files.

-------------------------

