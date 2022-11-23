Sir_Nate | 2017-01-02 01:09:27 UTC | #1

I'm not sure I'd call it a bug, but it was certainly inconsistant behavior:
On my x64 linux computer, an AngelScript method declared without a default argument calling a function with a default parameter, such that the AngelScript code had 1 less argument worked fine, calling the function with the default argument, but on Android, it called it with random values for the unspecified parameter.
That is: [code]e->RegisterObjectMethod("Attack", "void DoDamage(Node@ other, float damage)", asMETHOD(Attack, DoDamage),asCALL_THISCALL);[/code] worked fine on my laptop calling [code]void AddDamage(Node* other, float damage, float fixed = 0.0f, bool preModifiedDamage = false);[/code]with 0.0 for the fixed value, but on android it would have values such as 4e+21. Adding the default parameter to the angelscript declaration fixed this.
(i.e. [code] e->RegisterObjectMethod("Attack", "void DoDamage(Node@ other, float damage, float fixed=0.0)", asMETHOD(Attack, DoDamage),asCALL_THISCALL);[/code])

-------------------------

cadaver | 2017-01-02 01:09:31 UTC | #2

This depends on the binary ABI (assembly code) in function calls, so it's slightly black magic territory. Windows will potentially also fail / crash, have seen this in context of the navigation API functions (in this case it was extra pointer parameters which would only make sense when called from C++, the solution was to use wrapper functions for script.) When binding functions to AngelScript you should always make sure the amount of parameters matches.

-------------------------

