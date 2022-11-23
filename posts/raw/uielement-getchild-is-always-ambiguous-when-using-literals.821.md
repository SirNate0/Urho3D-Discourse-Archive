setzer22 | 2017-01-02 01:03:09 UTC | #1

The function offers several overrides, but when called like:

UIElement.GetChild("ChildName")

It's interpreted as ambiguous by clang++ (and I assume every other compiler out there).

The ambiguity comes from both String and StringHash being able to be constructed with a string literal, so there's no way for the compiler to differentiate from the different overrides:

UIElement* GetChild(const String& name, bool recursive = false) const;
UIElement* GetChild(const StringHash& key, const Variant& value = Variant::EMPTY, bool recursive = false)

It's not that it's a big deal, but it's certainly confusing. I'm not posting this as an issue because I don't think it really is.

Any thoughts on how could this be improved (or if it needs improving at all)?

-------------------------

cadaver | 2017-01-02 01:03:10 UTC | #2

The latter function is quite different in functionality (find child with specific var) so it could be renamed eg. GetChildWithVar().

-------------------------

setzer22 | 2017-01-02 01:03:10 UTC | #3

I think they should really have different names then. They're not really the same thing. GetChildWithVar is a lot less confusing. With GetChild the purpose of the function is not really clear.

-------------------------

