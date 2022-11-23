thebluefish | 2017-01-02 01:00:31 UTC | #1

Hi all,

I'm attempting to transfer complex data using events. Some of this data can have any number of children, so I've decided to use VariantVector for this purpose.

My problem stems from using a VariantMap within the VariantVector.  I construct the map as normal, then add it to the vector:

[code]vec->Push(new Urho3D::Variant(map));[/code]

If I read the map back (I've even tried this in the same function I add it in)

[code]
for (Urho3D::VariantVector::Iterator itr = vec.Begin(); itr != vec.End(); itr++)
	{
		Urho3D::VariantMap map = itr->GetVariantMap();
[/code]

 then anything I attempt to read from the VariantMap is null. I've attempted to debug this in Visual Studio, and found that it shows the correct capacity.

Any ideas on what I'm doing wrong?

-------------------------

cadaver | 2017-01-02 01:00:31 UTC | #2

You should not "new" the variant, because pushing to a vector creates a copy of it in any case (new'ing it would leak memory, as there's no matching delete). If you want to optimize, you should be able to "pre-push" a VariantMap to the vector and then access it via reference and continue filling it with data. The code below is the most straightforward use without any optimization, and it should work:

[code]
    VariantVector vec;
    
    for (int i = 0; i < 5; ++i)
    {
        VariantMap map;
        map["a"] = i*10;
        map["b"] = i*10+1;
        map["c"] = i*10+2;
        vec.Push(Variant(map));
    }
    
    for (VariantVector::ConstIterator i = vec.Begin(); i != vec.End(); ++i)
    {
        LOGINFO("Iterating VariantMap within vector");
        const VariantMap& map = i->GetVariantMap();
        for (VariantMap::ConstIterator j = map.Begin(); j != map.End(); ++j)
        {
            LOGINFO(j->first_.ToString() + ": " + j->second_.ToString());
        }
    }
[/code]

-------------------------

thebluefish | 2017-01-02 01:00:32 UTC | #3

I am ashamed to call myself a programmer after that trivial mistake. I think the heavy use of C# at work is dulling my senses. Thanks much for pointing that out.

-------------------------

