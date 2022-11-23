SirNate0 | 2017-04-19 19:10:40 UTC | #1

ResourceCache's Exists() does not find manually added resources. Is there a better way around this than GetExistingResource(). I guess it makes sense that it can't check if it exists, as the names only have to be unique within a type of resource.

Also, for the documentation, should
```cpp
/// Add a manually created resource. Must be uniquely named.
    bool AddManualResource(Resource* resource);
```
be something like
```cpp
/// Add a manually created resource. Must be uniquely named within it's type.
    bool AddManualResource(Resource* resource);
```
given that, e.g., and XMLFile and a Material resource could have the same name (I think).

-------------------------

cadaver | 2017-04-21 09:23:18 UTC | #2

We can at least clarify the function documentation. Exists() is meant as a filesystem / package existence check without regard to the resources in memory. GetExistingResource() looks fine for your usecase.

-------------------------

