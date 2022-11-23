thebluefish | 2017-01-02 01:00:25 UTC | #1

So I'm not sure of the "proper" way to handle a connection's identity using the following:

[code]
// Connection::GetIdentity
const VariantMap& GetIdentity() const { return identity_; }
[/code]

What I want to do:

[code]
const Urho3D::VariantMap& identity = connection.GetIdentity();

Urho3D::String user = identity["username"].GetString(); // Both lines will throw an error
Urho3D::String authToken = identity["token"].GetString();
[/code]

Since "identity" is constant, I cannot use the operator[] with it. Instead I'm forced to use:

[code]
Urho3D::VariantMap& identity = const_cast<Urho3D::VariantMap&>(connection.GetIdentity());

Urho3D::String user = identity["username"].GetString(); // Now works
Urho3D::String authToken = identity["token"].GetString();
[/code]

IMO it seems more that we need to add a "const operator[]" function to the VariantMap class. Alternatives would be to not declare it as const in GetIdentity, or simply use identity->find() instead. What would be the best way to do this?

-------------------------

cadaver | 2017-01-02 01:00:25 UTC | #2

Const operator[] for VariantMap could be confusing when compared to STL, it would need to return a ref to an empty Variant somewhere in memory if the lookup fails, which I don't particularly like.

That said, there shouldn't be a reason for the identity map to be const. The server is The Man, so there's no problem for it also modifying the values or inserting extra metadata if it wants to. In fact the map is already non-const accessible in AngelScript. I'll push a change shortly.

-------------------------

thebluefish | 2017-01-02 01:00:26 UTC | #3

Awesome, thanks for the quick update.

I ran into this while trying to implement my login server scheme, and it really threw me off for a bit about its intended use.

I'll go ahead and use const_cast for now, and I'll update my code when I pull the new changes later on.

-------------------------

