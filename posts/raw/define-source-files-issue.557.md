OvermindDL1 | 2017-01-02 01:01:21 UTC | #1

The default glob options for `define_source_files` are a little odd, only looking for *.cpp and *.h files.  The common file extensions should likely be:
Source Files glob:  *.c *.c++ *.cxx *.cpp *.cc *.C
Header Files glob:  *.h *.hh *.H *.h++ *.hxx *.hpp *.hcc

I have submitted a pull request to make that change (just a two line change).  Is this acceptable or did I miss any?

[url]https://github.com/urho3d/Urho3D/pull/527[/url]

-------------------------

