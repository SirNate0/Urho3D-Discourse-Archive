Leith | 2019-06-15 04:29:53 UTC | #1

I'm loading / parsing data from JSON files...
I'm trying to automatically deduce JSON value types... my test case is a Number (1).

JSONValue::GetValueType() and JSONValue::GetValueTypeName() seem to work fine - in my test case, they tell me that the type is "Number".

But JSONValue::GetVariant() fails to resolve to a known type, and returns a dud Variant object.

JSONValue::GetDouble() works fine in the case I performed my own typechecking.
What am I missing here?
Is there not a reasonably complete mapping between JSON types and Variant types?

Happy to provide example code and data to reproduce the issue.

-------------------------

Leith | 2019-06-15 16:14:27 UTC | #2

Nevermind - I figured it out.
GetVariant() will only work if SetVariant() was called first.
The type mapping between JSON and Urho is incomplete / one-directional.
I'll just have to bite the bullet and perform my own typemapping, even though I am working with an Urho value container. Seems odd, but there you have it.

I might contribute a PR that contains a more complete type mapping for JSONValue <--> Variant.
Basically I'm suggesting that GetVariant should be able to wrap any JSON type that is easily mapped, and should only fail in complex cases.

-------------------------

