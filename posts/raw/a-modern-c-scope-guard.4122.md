ricab | 2018-03-25 20:13:43 UTC | #1

Just sharing an utility I recently put together and others may find useful: a [scope guard](https://ricab.github.io/scope_guard/) implementation that is meant to be public, general, simple, and fast.

It is written in C++11 and compatible with C++14/17. It defends against implicitly ignored returns, and optionally enforces `noexcept` at compile time (in C++17), all in a SFINAE-friendly way.

While it is not directly related to Urho3D it may be quite useful to handle early returns, which are used a lot in urho's code. But I would hope it can be found useful in general in C++.

-------------------------

