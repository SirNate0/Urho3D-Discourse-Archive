ChunFengTsin | 2018-01-31 04:49:47 UTC | #1

when I code with urho3d. 
I find a problem about pure c++ language.
![2018-01-31%2000-17-06%20%E7%9A%84%E5%B1%8F%E5%B9%95%E6%88%AA%E5%9B%BE|612x499](upload://yGyAekjyqHLMMchOA4HYg5PUVFh.png)

the "temp" should be null?
thanks.

-------------------------

ChunFengTsin | 2018-01-31 04:51:34 UTC | #2

it is use lasted GCC

-------------------------

Sinoid | 2018-01-31 17:06:15 UTC | #3

It's documented as far back as C89.

The behavior is undefined unless the caller does not use the return value.

> 1844 If the } that terminates a function is reached, and the value of the function call is used by the caller, the behavior is undefined.

source: http://c0x.coding-guidelines.com/6.9.1.html for N1256 (just post C99)

-------------------------

