xlat | 2021-11-27 12:38:09 UTC | #1

Is there any throw(..) and getExceptionInfo() support in Urho3d for Angelscript?
[I look here...](https://www.angelcode.com/angelscript/sdk/docs/manual/doc_script_stdlib_exception.html)
And I see there that exceptions in Angelscript are, in principle, possible.
If it is true,
Can you link to an example?

If getExceptionInfo is registered with Urho,
Then it will have a different name in AS? Which?

-------------------------

Modanung | 2021-11-27 18:33:26 UTC | #2

`Script::ExceptionCallback` seems to tie AS exceptions to Urho's `Log`. Did you check the check the log? If nothing appears there when you expect it to, maybe try lowering the `Log` subsystem's logging level with `SetLevel(level)`.

-------------------------

xlat | 2021-11-28 12:33:46 UTC | #3

Ok, I'll try to explain:

I plan to do my entire current project on AS.
But I know C ++ well enough,
And got used to handling exceptional situations there through the exception mechanism.

The main feature of this mechanism is the absence of manual transmission of errors.
To the top of the call stack.

I would really like to use the same mechanics in AngelScript.

For example:
```
///----------------------------------------------------------------------------|
/// AngelScript.
///----------------------------------------------------------------------------:

Void foo()
{   bool flag = true;
    ...
    
    If(flag)
    {   throw ("Error: ..."); /// No matching symbol 'throw'
    }
    
    ...
}

///-----------------------------|
/// No errors here.             |
///-----------------------------:
Void func()
{   try
    {   foo();
    }
    catch
    {
    }
}

///-----------------------------|
/// ...                         |
///-----------------------------:
Void func()
{   try
    {   foo();
    }
    catch
    {   String s = getExceptionInfo (); // No matching symbol'getExceptionInfo'
    }
}
```

Further:
throw and getExceptionInfo are identifiers for C ++.
For AS in Urho, as I noticed, names are registered that do not match the C ++ version.

[for example, here the name IsOpen() for C ++ has an alternative get_open() for AS](https://github.com/urho3d/Urho3D/blob/1.8-ALPHA/Source/Urho3D/AngelScript/IOAPI.cpp#L322)

But now I'm interested in the very possibility of using exceptions in AS.

If anyone knows how, then please give me an example of how to do it correctly ...

-------------------------

weitjong | 2021-11-29 03:56:53 UTC | #4

Urho3D does not register those functions which are only available in the add-on scripts provided by AngelScript. But I think there is nothing stopping you from including the add-on into your own project and then call the provided function to register the exception handling routines.

Having said that, I thought most game developers avoid using exception :)

-------------------------

Modanung | 2021-11-29 20:10:46 UTC | #5

[quote="weitjong, post:4, topic:7069"]
Having said that, I thought most game developers avoid using exception :slight_smile:
[/quote]

It would seem there are _exceptions_ to the rule. :wink:

-------------------------

