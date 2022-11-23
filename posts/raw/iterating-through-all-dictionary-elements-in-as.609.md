rogerdv | 2017-01-02 01:01:38 UTC | #1

Seems that dictionaries are not used at all in samples, or even editor, and neither Google returns many results. How can I iterate through all the values stored in a dictionary? I guess I have to use the keys property to get all keys, as I dont see any iterator in the docs.

-------------------------

Azalrion | 2017-01-02 01:01:38 UTC | #2

[code]
Dictionary d;
for (int i = 0; i < d.length; i++)
{
    Object@ objGet;
    d.Get(d.keys[i], @objGet);

    Object@ objOp = cast<Object>(d[d.keys[i]]);
}
[/code]

[urho3d.github.io/documentation/H ... Dictionary](http://urho3d.github.io/documentation/HEAD/_script_a_p_i.html#Class_Dictionary)

-------------------------

