NiteLordz | 2017-01-02 01:03:37 UTC | #1

So i am trying to retrieve the current value of a script variable.  I can get the AttributeInfo of the variable i am looking for, however, i can not figure out how to get the value that is associated with it.  Looking at the scene file, i see the value is associated with the attribute as expected. 

Thanks much

-------------------------

cadaver | 2017-01-02 01:03:38 UTC | #2

You should use GetAttribute() & SetAttribute() on the ScriptInstance, which return the value as a variant; internally this queries the AngelScript object's memory space directly. Double-check that the script object has been successfully created (when loading a scene or prefab, the script file & script class name attributes get filled first, which should create the object.)

-------------------------

NiteLordz | 2017-01-02 01:03:38 UTC | #3

Thanks, i was calling 

[code]
const Vector<AttributeInfo>* attributes = script->GetAttributes();
[/code]

and then i was using 

[code]
AttributeInfo info = attributes->At(i);
[/code]

to get access to the script variable.  Calling the GetAttribute(unsigned int index) returns me the value i am looking for.

-------------------------

cadaver | 2017-01-02 01:03:38 UTC | #4

I believe it should work also through the AttributeInfo, but then you have to be aware of the attribute access internals; namely use the ptr_ member variable which points to the script object's memory directly, instead of (this pointer) + offset_ used for ordinary memory attributes, where the offsets are same for all instances of the class.

-------------------------

NiteLordz | 2017-01-02 01:03:38 UTC | #5

Seemed cleaner to use GetAttribute and just convert the variant to value.

-------------------------

cadaver | 2017-01-02 01:03:38 UTC | #6

Yes, that should be fine most of the time, the more low-level option should only need to be used if it's performance critical.

-------------------------

