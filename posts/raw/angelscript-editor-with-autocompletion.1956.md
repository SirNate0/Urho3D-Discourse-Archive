Bananaft | 2017-01-02 01:11:47 UTC | #1

For almost a year I was using CodeLite with ScriptAPI.h to get AngelScript functions autocompletion. It worked great, until suddenly stopped. And I can't fix it even after installing older version and setting everything up from scratch. I have a very little hope someone will help me with that, but I want once again rise a very disturbing for me question :

What with the AngelScript IDE?

I've seen two projects, One by scorvi
[github.com/scorvi/Urho3DIDE](https://github.com/scorvi/Urho3DIDE)
Another by JSandusky:
[github.com/jacmoe/UrhoAngelscriptIDE](https://github.com/jacmoe/UrhoAngelscriptIDE)

Both seems canned more than a year ago.

What other options is there? What is everyone using for scripting? I feel like I would prefer a plugin for regular text editor like N++ or Atom(which advertises itself as super-duper customizable, and already has plugins for some uncommon languages).

What do you guys think? How much this situation better with LUA?

-------------------------

codder | 2017-01-02 01:11:47 UTC | #2

LUA came like 10 years before AngelScript. I think that's the reason why is like the standard embedded scripting language for games.
Alot of console/desktop games uses that.

You will find more tools for LUA than AS. For example ZeroBrane Studio, CryENGINE Lua Debugger, LuaEdit, ecc...
If you need just a text editor that supports AS syntax + autocompletion you can use Sublime Text or Atom as you said.

-------------------------

Bananaft | 2017-01-02 01:11:48 UTC | #3

[quote="codder"]a text editor that supports AS syntax + autocompletion you can use Sublime Text or Atom as you said.[/quote]
That would be simple word autocomplition, that looks for words in same file. And I'm talking about finctions autocomplition like I had with ScriptAPI.h .  And in regard to LUA I'm interested in same thing. Is any of those tools can be aware of Urho engine functions?

-------------------------

weitjong | 2017-01-02 01:11:48 UTC | #4

Are you confused it with AngelScriptAPI.h? This is the actual dummy header that you should use to get auto completion in IDE.

-------------------------

hdunderscore | 2017-01-02 01:11:48 UTC | #5

You can use atom and extend it to support a higher level auto completion, but it won't be as good as visual assist in visual studio.

I still choose atom for scripting, since it was easier for me to set up an urho linter, plus it's a lot lighter weight.

Now that xamarin studio is open source, it could be worth checking out- I enjoyed the auto complete that was available in monodevelop.

-------------------------

rku | 2017-01-02 01:11:48 UTC | #6

[quote="hd_"]Now that xamarin studio is open source, it could be worth checking out- I enjoyed the auto complete that was available in monodevelop.[/quote]
It is not opensource. Monodevelop is opensource. Xamarin sdk is opensource. XamarinStudio is Monodevelop + 4 proprietary plugins. Those plugins are not opensource.

-------------------------

Bananaft | 2017-01-02 01:11:49 UTC | #7

[quote="weitjong"]Are you confused it with AngelScriptAPI.h? This is the actual dummy header that you should use to get auto completion in IDE.[/quote]
Oh wow, I'm actually am. Thank you. Setting it up with  AngleScriptAPI.h fixed it for some time, then it broke again.  :confused: 

[quote="hd_"]I still choose atom for scripting, since it was easier for me to set up an urho linter[/quote]
Oh wow, never heard of it. I will definitely check it out.

I like Atom, despite some of it quircks (JavaScript related, I suspect).

-------------------------

weitjong | 2017-01-02 01:11:50 UTC | #8

[quote="Bananaft"][quote="weitjong"]Are you confused it with AngelScriptAPI.h? This is the actual dummy header that you should use to get auto completion in IDE.[/quote]
Oh wow, I'm actually am. Thank you. Setting it up with  AngleScriptAPI.h fixed it for some time, then it broke again.  :confused: 
[/quote]
I think I understand you, not .  :wink:

-------------------------

Xardas | 2017-01-02 01:11:52 UTC | #9

AS completion works just fine on my machine. I'm using the latest CodeLite version 9.1.0.

-------------------------

