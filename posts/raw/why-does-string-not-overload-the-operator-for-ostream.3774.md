SeeSoftware | 2017-11-23 20:40:05 UTC | #1

String doesnt overload the << operator for ostream so you cant do this:

    std::cout << String("hi") << "\n";

you have to get the raw string to print it:

    std::cout << String("hi").CString() << "\n";

-------------------------

Eugene | 2017-11-23 20:40:52 UTC | #2

Urho avoids bloating headers with STL dependencies (including iostream).
If you want to use streams instead of Urho logging, you could define all serialization operators that you need as free functions.
I think we could add separate header with this stuff in main repo tho...

-------------------------

johnnycable | 2017-11-24 08:35:20 UTC | #3

Other info here: http://floooh.github.io/2016/08/27/asmjs-diet.html

-------------------------

