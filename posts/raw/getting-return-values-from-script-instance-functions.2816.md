Liichi | 2017-02-22 23:41:56 UTC | #1

Hi, im using "Execute" method to call a function from another script, but i don't know how to get return values. Someone knows?
PS: im using angelscript.

-------------------------

jmiller | 2017-02-23 08:16:18 UTC | #2

Hi Liichi,

Perhaps your answer is in this thread:
http://discourse.urho3d.io/t/return-value-from-script-method/1139

*edit: Oops, I misread your issue.

-------------------------

Liichi | 2017-02-23 01:10:06 UTC | #3

The problem it's that asIScriptContext is not exposed to angelscript :confused:

-------------------------

KonstantTom | 2017-02-23 09:12:32 UTC | #4

Hi! In my project I solved this problem using out reference as function parameter.
```angelscript
// AngelScript side.
void Process (/*other parameters*/, /*OutputType*/ &out output)
{
    /*...*/
    output = /*execution  result*/;
}
```
```c++
// C++ side.
Urho3D::VariantVector executionParameters;
/* ... push other parameters ...  then push our output object.*/
executionParameters.Push (Urho3D::Variant (/*create object for output*/));
// Then execute.
/*scriptInstance*/->Execute (functionDecl, executionParameters);
// Then get our object from variant vector.
/*OutputType*/ executionResult = executionParameters.At (lastParamIndex).Get/*OutputType*/ ();
```
It sucessfully works with VariantMap output in my project.

-------------------------

Liichi | 2017-02-23 21:59:33 UTC | #5

I tried it but not seem to work in script (im calling scriptInstance.execute from another script).
Now im using node vars to store return value and then read it from another script, but it would be better to be able to get the returns directly.

-------------------------

Sinoid | 2017-02-26 06:59:02 UTC | #6

Return values aren't what Angelscript or Lua are meant for.

If you need instant return values than you need something like TinyExpr.

> Now im using node vars to store return value and then read it from another script, but it would be better to be able to get the returns directly.

So you have a sequencing problem? Please tell us more so we can help you.

-------------------------

