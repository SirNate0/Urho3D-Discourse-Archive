cap | 2017-04-13 14:38:51 UTC | #1

Suppose there's a third party library function `CoolFunction(FILE* cfile)` taking a C style `FILE*`, and there's a file in the `ResourceCache` that we can get at pretty easily in the form of an `Urho3D::File*`. Is there any direct way to get at an underlying C style `FILE` from the `Urho3D::File*`?

I started to do it as below (which has bugs, but the approach is clear), then began to figure the approach I was using was probably pointless, since if I need to be copying array values like that, I would probably be better off to just create the `FILE` directly from the name of the resource .. but that way we can't take advantage of the fact that the resource is loaded in the cache already. Any tips?
```
void CoolFunctionWrapper(Urho3D::File* ufile)
{
  PODVector<unsigned char> buffer = ufile->ReadBuffer();

  size_t n = (size_t)buffer.Size();
  unsigned char* array = new unsigned char[n];
  for (size_t i = 0; i < (size_t)buffer.Size(); ++i) {
    array[i] = buffer[i];
  }

  FILE* cfile = fopen("tmp_name", "w");
  fwrite(array, sizeof(unsigned char), n, cfile);
  delete array;

  CoolFunction(cfile);
}
```
(Also there is this http://discourse.urho3d.io/t/file-as-an-std-istream/2197 which looks relevant, but I still have to digest it.)

-------------------------

1vanK | 2017-04-13 14:39:02 UTC | #2

Try ```(FILE*)file->GetGandle()```

-------------------------

SirNate0 | 2017-04-12 06:18:18 UTC | #3

Note that the GetHandle() solution will only work for non-packaged files (I'm fairly certain, perhaps for uncompressed package files as well). If you need to use packaged files for it, I'm pretty sure you will have to write some platform-dependent code to create a memory-mapped file (I think that's the right term for this), and it is not as easy to do as for file streams. If you can, I would suggest modifying the library to use either Urho's File class or a stream or your own custom version of the functions like fread that use one of those as a back end. (See http://stackoverflow.com/questions/12249610/c-create-file-in-memory for info about creating a file in memory)

-------------------------

cap | 2017-04-12 17:29:18 UTC | #4

Doing `(FILE)*file->GetHandle()` indeed works! Though due to the likely issue with packaged files, I think I'll try modifying the library function to use Urho's File as suggested. Thanks for the responses.

-------------------------

cap | 2017-04-21 18:58:12 UTC | #5

Small update, I guess some care needs to be taken when using `(FILE*)file->GetHandle()`. One of the third party library functions was a bit too daunting to modify for an `Urho3D::File*`, so I used the `GetHandle()` method. All's well on Windows, but on Ubuntu the same code leads to a segmentation fault.

If I can find out why, I'll share the reason here.

-------------------------

