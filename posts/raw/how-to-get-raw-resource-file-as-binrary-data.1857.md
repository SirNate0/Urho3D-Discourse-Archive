elemusic | 2017-01-02 01:10:46 UTC | #1

Trying to load binrary file from reousrce fold.

Say Data\Urho2D\myBin.bin

the example project use something like

[code]
Sprite2D* sprite = cache->GetResource<Sprite2D>("Urho2D/Aster.png");
[/code]

to load png resource as Sprite2D object,what if i want to load my own raw bin file?

something like
[code]
unsigned char* rawBuf = cache-GetResource<SomeMagicNameMayWork>("Urho2D/myBin.bin");
[/code]

is there a way to do so,or some other way to do the same thing.

-------------------------

1vanK | 2017-01-02 01:10:46 UTC | #2

[code]SharedPtr<File> file(new File(context_, fileName, FILE_READ));
if (file->IsOpen())
{
    ...
}[/code]

-------------------------

1vanK | 2017-01-02 01:10:46 UTC | #3

[code]auto file = cache->GetFile(name);[/code]

-------------------------

cadaver | 2017-01-02 01:10:46 UTC | #4

ResourceCache::GetFile() if you want to take advantage of the resource paths / packages, instead of specifying the full absolute filename. This just opens the file from the filesystem and doesn't do any caching, after which you can do your own reading.

-------------------------

elemusic | 2017-01-02 01:10:46 UTC | #5

Thank you,guys,just figure it out myself.

[code]
ResourceCache* cache = GetSubsystem<ResourceCache>();
SharedPtr<File> myfile = cache->GetFile("Urho2D/xxx.bin", true);
unsigned int bufSize = myfile->GetSize();
unsigned char* buf = new unsigned char[bufSize];
myfile->Read((void*)buf, bufSize);
[/code]

for some reason,i found it's hard to work with Urho build-in xml and json parser.
Now i'm trying to load file as binrary and parsing them with boost.that could save me a lot of time to figure out the Urho document.
just a lazy guy :smiley:

-------------------------

