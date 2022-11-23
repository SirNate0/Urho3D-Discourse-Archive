Enhex | 2017-04-06 20:20:51 UTC | #1

Memory mapped files can improve file I/O speed.
Useful for file reading.
Need to know the size for file writing, so it's more tricky.

A library for example:
https://github.com/yhirose/cpp-mmaplib

My benchmark(hopefully correct) results for reading:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/1bfa8a3537df959d18cbd76659f6ff2dfafd94d5.png'>
boost one is boost.iostreams.

Urho currently uses fread.

-------------------------

