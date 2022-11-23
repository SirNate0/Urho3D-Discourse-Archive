att | 2018-01-23 12:15:55 UTC | #1

I found following code in class Object,
```
bool TypeInfo::IsTypeOf(const TypeInfo* typeInfo) const
{
    const TypeInfo* current = this;
    while (current)
    {
        if (current == typeInfo)
            return true;

        current = current->GetBaseTypeInfo();
    }

    return false;
}
```
I think it should be
```
bool TypeInfo::IsTypeOf(const TypeInfo* typeInfo) const
{
    const TypeInfo* current = this;
    while (current)
    {
        if (current->GetType() == typeInfo->GetType())
            return true;

        current = current->GetBaseTypeInfo();
    }

    return false;
}
```
or 
```
bool TypeInfo::IsTypeOf(const TypeInfo* typeInfo) const
{
     assert(typeInfo ~= nullptr);
     return this->IsTypeOf(typeInfo->GetType());
}
```

-------------------------

Sinoid | 2018-01-23 20:31:11 UTC | #2

Not a bug. The TypeInfo's are static and produced within the URHO3D_OBJECT macro.

If there's a bug with comparing two static pointers that have never seen any sort of erroneous conversion (ie. to int/uint instead of intptr_t), then it's a bug with the compiler used.

-------------------------

