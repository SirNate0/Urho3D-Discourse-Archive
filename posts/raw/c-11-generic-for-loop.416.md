setzer22 | 2017-01-02 01:00:14 UTC | #1

I've just realised that the generic container classes in urho (like Vector) support Iterators but not generic for loops from C++11. Is there a reason to not support them? Just to be clear by generic for loops I mean:

[code]
Vector<SomeObject> v;

//v is filled...

for(SomeObject obj : v) {
    //treat obj as you would treat v[i] in a normal for loop
}
[/code]

Thanks!

-------------------------

cadaver | 2017-01-02 01:00:14 UTC | #2

Due to the coding convention (eg. uppercase functions) the iterators are not compatible with STL and therefore not directly compatible with C++11 generic loops.

It's not exactly the same, but there's an optional include file ForEach.h in Source/Engine/Container which defines a foreach macro you can use.

-------------------------

shu | 2017-01-02 01:01:16 UTC | #3

Wouldn't it make sense to make an exception of the Uppercase convention in this case and just add lowercase functions (begin(), end()) so that the compiler can use the urho container types too? 

I think it's much nicer to write 
[code]for (auto i : c){...}[/code]
than
[code]for (auto iter = c.Begin(); iter != c.End(); iter++) {...}[/code]

-------------------------

Stinkfist | 2017-01-02 01:02:57 UTC | #4

The begin() and end() overloads for Urho containers would be nice indeed. See related discussion here: [github.com/urho3d/Urho3D/issues/561](https://github.com/urho3d/Urho3D/issues/561)

-------------------------

cadaver | 2017-01-02 01:02:57 UTC | #5

Is now in. The old foreach solution is still used on VS2010, as generic for is not available.

-------------------------

