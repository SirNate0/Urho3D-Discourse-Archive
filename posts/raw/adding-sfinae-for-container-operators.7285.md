SirNate0 | 2022-06-22 02:05:49 UTC | #1

Presently the code for containers like Vector and HashMap define `operator ==` and `operator !=` using `operator !=` for the value types. This generally works fine - you just get an error when comparing the containers with types that don't support the operator, but that can generally be fixed in the user code.

However, the existence of the operators is throwing off some template magic used by the sol3 Lua binding library I am trying to use to make new Lua bindings with - it should fall back to a pointer comparison when the operator isn't defined, but it finds that it is defined, but then that produces a compiler error for numerous classes (e.g. `CustomGeometryVertex`, in a vector with `Urho3D::CustomGeometry::GetVertices`) because there is no `operator !=` defined for the class. Adding some SFINAE magic to the `operator ==` for the container classes fixes the issue, though it doesn't look to great (could be improved a bit with some helper classes, and I'm no expert in template magic, so perhaps it can be done better even without them). Here's an example for Vector:
```

    /// Test for equality with another vector.
    template<class U=T>
    bool operator ==(std::enable_if_t<std::is_same_v<std::void_t<decltype(std::declval<const U&>() != std::declval<const T&>())>, void>,
                     const Vector<U>&> rhs) const
    {
        if (rhs.size_ != size_)
            return false;

        T* buffer = Buffer();
        T* rhsBuffer = rhs.Buffer();
        for (i32 i = 0; i < size_; ++i)
        {
            if (buffer[i] != rhsBuffer[i])
                return false;
        }

        return true;
    }
```

---
**What are your thoughts on adding such a change to Urho?** We don't need to - it just means more work in the tool generating the bindings, and maybe missing some functions from the result, but it is certainly doable.

By all means, feel free to suggest more elegant ways to make it happen as well.

-------------------------

