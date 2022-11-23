rogerdv | 2017-01-02 01:01:34 UTC | #1

Im trying to underestand the correct use of dictionaries and I havbe a doubt about the combination of classes and dictionaries. In my code, I have something like this:

[code]
class Entity {
 Node@ n; 
String Name;
*****
}

class ListOfEntity {
Dictionary D;
Entity Find(String id)
{
 if (D.Exists(id)) {
  retval = entity();
  D.Get(id,retval)
  return retval;
}
}
[/code]

After reading about handles, classes and such, I made myself a mess and now I dont know if that is the correct way to do it. Will Find() return a "pointer" to an Entity instance, or just a new copy of it? If id doesnt exists, what should I return? I have tried null, 0, and all of them produces an error.

-------------------------

Azalrion | 2017-01-02 01:01:34 UTC | #2

Try something like:

[code]
Entity@ Find(String id)
{
    Entity@ retval;

    if (D.Get(id, @retval))
    {
        return retval;
    }

    return null;
}
[/code]

Not totally certain it works out the box but should be close, if it doesn't work try without the at symbol in the Get call.

-------------------------

rogerdv | 2017-01-02 01:01:34 UTC | #3

Ok, no errors now. Im not so sure if it is working because I cant get the Entity instance, but I will work out that later at home.

-------------------------

Azalrion | 2017-01-02 01:01:35 UTC | #4

You need to set it in a similar way if using handles. 

[code]
Entity@ handle = Entity();

D.Set('id', @handle);
D['id'] = @handle;
[/code]

See for an example, its practically the same we just changed the method names in urho: [angelcode.com/angelscript/sd ... onary.html](http://www.angelcode.com/angelscript/sdk/docs/manual/doc_datatypes_dictionary.html).

-------------------------

