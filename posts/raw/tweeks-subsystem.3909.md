TrevorCash | 2018-02-15 17:31:12 UTC | #1

I recently have been working on a class with the goal of allowing easy and fast access to "Tweekable Values" Inside code.  I have been calling this class "Tweeks" and it works great as a subsystem.  Sometimes this is handy when you have a short subroutine that only happens once or twice.

Example In Code Usage:

> float scalar = GetSubsystem\<Tweeks>()->Get\<float>("scalar");
> 
> //use scalar in your routine

You can also reference the the same Tweek elsewhere in code with another call to Get() with the same unique name "scalar".

At any time you can save the state of tweeks or load the state of tweeks.

Get() should work with any Urho3D::Variant type.

For further control you can specify "sections" for tweeks to allow for better separation:

> float scalar = GetSubsystem\<Tweeks>()->Get\<float>("scalar", "myroutine");

Or default values:

> float scalar = GetSubsystem\<Tweeks>()->Get\<float>("scalar", 1.0f);

You can also get more info on the state of a tweek by using GetTweek():

> Tweek* tweek =  GetSubsystem\<Tweeks>()->GetTweek("scalar", "myroutine");

Tweeks have a "Lifetime" whereas they are marked as expired after their lifetime is up.  every call to Get or Update resets the tweek's lifetime counter.

You can check if a tweek is expired using tweek->IsExpired().

default lifetime is 2 seconds.

There are methods for restricting and extending the lifetime of tweeks in the Tweek class, as well as a push/pop stack for sections and lifetimes in the subsystem:

> GetSubsystem\<Tweeks>()->BeginSection("mySection");
> GetSubsystem\<Tweeks>()->BeginLifetime(1000);
>
> //tweeks modified here will be in the section: "mySection" and have a lifetime of 1000 milliseconds.
>
> GetSubsystem\<Tweeks>()->EndLifetime();
> GetSubsystem\<Tweeks>()->EndSection();


Link to code:
https://github.com/TrevorCash/Urho3D/tree/master/Source/Urho3D/Tweeks

-------------------------

johnnycable | 2018-01-03 08:48:49 UTC | #2

Thank you. This is handy for saving global values without having to create a database...

-------------------------

TrevorCash | 2018-01-03 19:31:52 UTC | #3

I just fixed a glaring bug causing the Get() function always setting a tweek with the default value even if it had already existed.  You might want to re-integrate the code.

-------------------------

Eugene | 2018-01-03 19:34:42 UTC | #4

Would it make sence to just add a kind of global variables into context?

-------------------------

TrevorCash | 2018-01-03 21:41:27 UTC | #5

My drive for making this is to provide a way of altering values on run-time using imgui or some other front end.

I want to integrate the concept of minimum and maximum values into the Tweek object as well (which has its problems with some Variant types).  

[quote="Eugene, post:4, topic:3909, full:true"]
Would it make sence to just add a kind of global variables into context?
[/quote]


I like the context's use as providing glue for being able to access subsystems like this, but I'm not sure if its a good place to keep/manage the data, But It could be a nice thing to have for true application wide variables.

Right now you can make multiple Tweeks objects too is you want (without making it a subsystem) which could be nice..

-------------------------

TrevorCash | 2018-01-03 21:44:49 UTC | #6

One Thing that would be nice (and I've added this in my fork) is a shortcut for GetSubsystem\<subsystem>().  Like GSS\<subsystem>()

-------------------------

