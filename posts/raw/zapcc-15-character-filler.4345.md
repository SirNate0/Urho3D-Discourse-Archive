johnnycable | 2018-06-22 18:01:25 UTC | #1

Did someone of you try this [zapcc](https://www.zapcc.com/) thing?

-------------------------

jmiller | 2018-06-22 19:02:07 UTC | #2

I have not tried that one; it seems similar to [url=https://ccache.samba.org/]ccache[/url] (which I use on Linux, for blurringly fast compiles).
Urho support docs on that; 
  https://urho3d.github.io/documentation/HEAD/_misc__how_tos.html#Using_ccache

Other tools and platforms could be added there as discovered.

-------------------------

weitjong | 2018-06-23 03:43:06 UTC | #3

Thanks for the link. From their landing page I understand that it is a Clang-derivative LLVM frontend with ccache feature included. And since it is a drop-in for Clang, it should slot right in to our build system with no or little modification required on our side. Also since it is Clang, it should support cross-compiling to other platforms too. One just needs to build it from source with the list of desired target platforms specified. From my past experience it is not that difficult to build the upstream LLVM project from source, even the Travis VM with decent computing power can pull it off. I reckon it is still the case for zapcc. Good find!

-------------------------

