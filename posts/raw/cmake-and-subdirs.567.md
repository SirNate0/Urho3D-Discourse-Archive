rogerdv | 2017-01-02 01:01:25 UTC | #1

I have been successfully using the cmake file included in the docs to compile my tests projects, but now I need to organize the code in a few directories, like this:

Source
  Whatever1
  Whatever2
  Etc

What changes should I introduce in the cmakelist?

-------------------------

OvermindDL1 | 2017-01-02 01:01:25 UTC | #2

Just add_subdirectories as normal.

-------------------------

