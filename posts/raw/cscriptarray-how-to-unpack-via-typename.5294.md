Leith | 2019-07-11 09:23:33 UTC | #1

So, AngelScript has returned an array type to C++ caller.... it's a CScriptArray
I can tell the subtype is Node@.
ie, the script returned an Array<Node@>

I want to unpack the CScriptArray to a Vector<Node*>, and/or VariantVector.
I know the typename is Node.
How can I get there?

-------------------------

SirNate0 | 2019-07-11 11:58:29 UTC | #2

Does something like `Vector<T> ArrayToVector(CScriptArray* arr)` work from the AngelScript/APITemplates.h file? 

Or is the idea to do it with a non-template function that takes a String[Hash] of the typename? If the latter, I would go with putting everything in a Variant and use a VariantVector, as you've already basically solved how to do that from just the type name for generic return values, right?

-------------------------

Leith | 2019-07-12 04:00:16 UTC | #3

I can't use template methods such as ArrayToVector because I can't presume to know in advance what data type(s) I'll be working with - I do have access to name strings...

I think I have solved the issue... required some further changes to ScriptFile.cpp but essentially I'm leveraging the fact that angelscript arrays can only hold two kinds of objects: handles and values. With one special exception case, handles typically represent pointers to Urho objects that derive from RefCounter. Values are typically types whose Urho type info can be queried from Variant::GetTypeFromName, with the only notable exception being that Variant itself is a supported value type.

If I give up on template specialization at runtime, and restrict myself to VariantVector, it looks like I'll be able to handle angelscript array<T> runtime specialization with what little type information I have.

This effectively means that angelscript array<T> will always be unpacked into a VariantVector when returning arrays from angelscript to c++ caller.

-------------------------

Sinoid | 2019-07-13 02:56:22 UTC | #4

It's a bit painful but the [asPEEK debugging code](https://gist.github.com/JSandusky/51f12192f40b90b4a09ee9138820e74c) shows more of the nitty-gritty of accessing Angelscript objects C++ side. Can't for the life of me remember how much array handling there was ... I do recall it and remembering it sucked.

> If I give up on template specialization at runtime, and restrict myself to VariantVector, it looks like I’ll be able to handle angelscript array runtime specialization with what little type information I have.

That's probably the smarter choice. Restricting to VariantVector / StringVector / ResourceRefList returns implies a lot in regards to constraints and reduces how robust you might have to be. 

If a returned CScriptArray contains exclusively angelscript defined types then any C++ code attempting to store them will have to bump/dec the reference counts for those objects. Obviously you don't look to be after going that far, but using the generic type looks like you could be.

VariantVector (and kin) makes it a lot clearer ... provided Variant `VoidPtr` isn't supported for Angelscript objects, but that isn't that bad as it would still be clear that ref-counts are the end-user's responsibility.

I'm warning you of those points specifically because of your BehaviorTree thread - from my own experience with a C++ side BT-core that supported tree-nodes defined in angelscript.

---

I've done this before, from what I saw in the other thread you're on the right track. There is no getting this *truly* right, so pick a point and settle on it.

-------------------------

