Mike | 2017-01-02 01:14:06 UTC | #1

Knowing the base path and the relative path (../../xxx), is there a convenient function to get the full path ?

-------------------------

cadaver | 2017-01-02 01:14:07 UTC | #2

I don't think there's a function which knows to strip directories from an absolute path if you go relatively backwards. Adding a path to an absolute base path has been done with just simple string concatenation.

-------------------------

Sir_Nate | 2017-01-02 01:14:07 UTC | #3

Writing your own shouldn't be too hard. Just concatenate them, split on '/', iterate over the vector from splitting, and push the path segment to a separate vector if it is not .. (Or . ), and pop if it is ..

-------------------------

Mike | 2017-01-02 01:14:07 UTC | #4

Thanks for replies, for now I won't use relative paths.

-------------------------

