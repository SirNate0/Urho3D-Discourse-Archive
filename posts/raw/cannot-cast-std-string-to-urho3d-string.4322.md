TheGreatMonkey | 2018-06-15 13:04:37 UTC | #1

I'm working with a plugin that isn't compatible with Urho3D strings

so I have need to cast from std::string into String

so something like this should work:

std::string foo = "I"m a string";
String bar = String(foo);

however during compilation I get this error:
'ToString': is not a member of 'std::basic_string<cahr_traits>,std::allocator<char>>

the error throws against line 145 of str.h

-------------------------

DavidHT | 2018-06-15 13:35:49 UTC | #2

Use the non-modifiable standard C character array version of the std::string:
String bar(foo.c_str());

-------------------------

TheGreatMonkey | 2018-06-15 13:36:07 UTC | #3

Yep, that does the trick. Thanks!

-------------------------

S.L.C | 2018-06-16 13:28:25 UTC | #4

In addition to information given by @DavidHT you could use a more explicit constructor that also receives the size and thus avoid a `strlen` operation on the given string.
```cpp
String bar(foo.c_str(), foo.size()); //<- Might get a warning about truncated integer types on x64 since std::string::size yields a size_t value and Urho3D::String uses unsigned int. Just a heads up.
```

-------------------------

Eugene | 2018-06-16 13:35:04 UTC | #5

Btw I never understood complains about redundant strlen in such places. 
You are already copying this string, you have to traverse N bytes to copy it. For small strings within few cache lines one extra data traversal doesn’t change anything.

-------------------------

S.L.C | 2018-06-16 15:58:32 UTC | #6

I guess you are right about that. I stand corrected.

-------------------------

