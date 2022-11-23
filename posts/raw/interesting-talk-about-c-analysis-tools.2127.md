Enhex | 2017-01-02 01:13:18 UTC | #1

[video]https://www.youtube.com/watch?v=JSjoCisIHcM[/video]
(Originally from Microsoft's Channel 9: [channel9.msdn.com/Events/GoingN ... -s-Dragons](https://channel9.msdn.com/Events/GoingNative/2013/The-Care-and-Feeding-of-C-s-Dragons))

[github.com/google/sanitizers](https://github.com/google/sanitizers)

Anyone tried these tools?

-------------------------

sabotage3d | 2017-01-02 01:13:18 UTC | #2

I have been using AddressSanitizer it is really useful. Now it is part of Xcode as well.

-------------------------

Enhex | 2017-01-02 01:13:18 UTC | #3

Is it available for Windows?

-------------------------

sabotage3d | 2017-01-02 01:13:19 UTC | #4

It should work you need to compile Clang and LLVM with address-sanizier enabled. 
It is part of GCC 4.8 now also there might be ready binaries but I followed this steps for OSX.

I followed this guide: [url]https://github.com/google/sanitizers/wiki/AddressSanitizerHowToBuild[/url]
This is for LLVM might be out of date: [url]http://homes.cs.washington.edu/~bholt/posts/building-llvm.html[/url]

After that you need to compile your application with this flag: [b]-fsanitize=address[/b]
And you need to run your application like this in my case it is IOS app.
[code]ios-sim launch SDLGame.app 2>&1 |asan_symbolize.py | c++filt[/code]

-------------------------

Enhex | 2017-01-02 01:13:19 UTC | #5

It doesn't seem to build the sanitizer libs on window and give an error saying they're missing.
A workaround could be using a virtual machine with Linux.

Well, at least Clang-Format works.

-------------------------

sabotage3d | 2017-01-02 01:13:19 UTC | #6

What about GCC 4.8 through cygwin?

-------------------------

Enhex | 2017-01-02 01:13:20 UTC | #7

[quote="sabotage3d"]What about GCC 4.8 through cygwin?[/quote]
Too much hassle and mess.
Might as well use it with LLVM/Clang for Linux builds, when I'll need them.

-------------------------

