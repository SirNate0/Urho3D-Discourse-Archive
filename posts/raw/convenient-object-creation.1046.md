rku | 2017-01-02 01:05:02 UTC | #1

This is very minor bit but for me personally makes creating objects 10-fold more comfortable:
[code]
    /// Create an object by type hash. Return pointer to it or null if no factory found.
    template<typename T>
    inline SharedPtr<T> CreateObject()
    {
        SharedPtr<Object> obj = CreateObject(T::GetTypeStatic());
        return SharedPtr<T>(static_cast<T*>(obj.Get()));
    }
[/code]
Add this to Context.h and objects can be created like:
[code]context_->CreateObject<TypeName>()[/code]

-------------------------

