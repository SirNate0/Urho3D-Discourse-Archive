Eugene | 2017-01-02 01:14:24 UTC | #1

It looks that these functions just compare passed type to Object because GetTypeInfoStatic() will always return Object.
Why does Urho need this function?
I don't see any usage of it and its name is confusing...
[code]Model::IsTypeOf<Model>() // o_o false?? [/code]

-------------------------

cadaver | 2017-01-02 01:14:24 UTC | #2

Good catch, the author probably didn't think it quite through. IsInstanceOf() is rather the more useful case of checking TypeInfo's.

-------------------------

