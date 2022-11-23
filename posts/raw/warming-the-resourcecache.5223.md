Leith | 2019-06-09 02:26:32 UTC | #1

I have several weapon models that I instantiate at runtime (typically from .mdl files).
One in particular takes an exceptional amount of time to load - and it's not a big model, it's the urho fish model. I think the main cause of the delay is texture loading. When the model instance is destroyed and recreated, there is no noticeable delay (resourcecache still has the assets loaded).

What is the best way to "warm the resourcecache" in order to eliminate the initial delay?

-------------------------

jmiller | 2019-06-09 05:39:54 UTC | #2

It has been a little while -- when @cadaver had mentioned it in   https://discourse.urho3d.io/t/async-loading-help/1120  I thought `ResourceCache::BackgroundLoadResource()` might be useful for background precaching.  :slight_smile: 
.. async methods should potentially be nicer than `GetResource()`.

For a directory I might try something like

```
FileSystem* fs(context_->GetSubsystem<FileSystem>());
Vector<String> files;
String texDir("Data/Textures"));
fs->ScanDir(files, texDir, "*.tga", SCAN_FILES, true);
Vector<String>::ConstIterator file(files.Begin());
```

-------------------------

Leith | 2019-06-09 06:03:50 UTC | #3

I am not convinced this is enough for my use-case. But I very much appreciate the feedback, so I thank you. I am not sure this solves my problem, but I like to learn, and I do use asynch loading already, again thanks very much, I will make of this what I can.

-------------------------

jmiller | 2019-06-09 11:44:36 UTC | #4

Profiler should tell more, but maybe image decoding is eating a fair bit of CPU?
TGA and RLE compression are fast, JPEG is probably a few times slower than most HDs, and (compressed) PNG usually slower still.

On dev rig, I have put resources on tmpfs/RAM with symlinks in `bin/Autoload` to good effect.

-------------------------

Leith | 2019-06-10 10:44:38 UTC | #5

I don't want to scan for and load every possible texture from some pathway, there has to be a nicer way, even if i need to make my own data driven solution for entire scenes (effectively, a set of per scene data that was not serialized with the scene)

-------------------------

jmiller | 2019-06-10 22:31:35 UTC | #6

good luck with roll-your-own. :)
On delays: In addition to texture decoding there's texture uploading to GPU (that's on main thread).

-------------------------

