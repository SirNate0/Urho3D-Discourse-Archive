CrazySnail-LLLL | 2021-07-30 04:06:26 UTC | #1

I use Urho3D-1.7.1-macOS-64bit-STATIC.tar.gz. But there are a lot of header files missing. How can I solve it? Do I need to copy in the source directory?

-------------------------

S.L.C | 2021-07-30 06:00:46 UTC | #2

I think you need to add the `ThirdParty` folder into your include paths. Not just the `include` directory. Because the headers are included relative to that.

Also, as many will end up suggesting is to use the code straight from repository as it is (*likely*) more stable. Unless you need to maintain some kind of compatibility. Maybe even disable some of the features you don't need (*like one or both scripting components for example or databases*).

-------------------------

