att | 2017-01-02 01:14:59 UTC | #1

Hi, I saved my node as node prefab, but don't  know how to load it in code. I want to load it as follow:
[code]
File *data = GetSubsystem<ResourceCache>()->GetFile("Objects/myPrefab.bin");
GetScene()->Instantiate(*data, pos, Quaternion::IDENTITY);
[/code]

but failed.

-------------------------

cadaver | 2017-01-02 01:14:59 UTC | #2

You should hold the file in a SharedPtr. ResourceCache::GetFile() returns a SharedPtr and there's nothing else to keep it alive, so the code as it is is accessing a destroyed object.

It's also possible there are bugs in binary serialization, since it's very little tested by most users.

-------------------------

