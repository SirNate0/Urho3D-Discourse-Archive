rogerdv | 2017-01-02 01:02:11 UTC | #1

Im trying to test Variant and new ScriptObject support, but this code produces an error of No matching siganture for Variant(Test&):  

[code]
class Test : ScriptObject
{
 void CallScript()
 {
  Variant t = Variant(this);
 }
}
[/code]

What Im doing wrong here?

-------------------------

Azalrion | 2017-01-02 01:02:13 UTC | #2

Just what sinoid said, requires a handle.

-------------------------

rogerdv | 2017-01-02 01:02:15 UTC | #3

Then the error says this: Scripts/RPG/Entity.as:132,19 No matching signatures to 'Variant(Entity@&)'

-------------------------

Azalrion | 2017-01-02 01:02:18 UTC | #4

Angelscrips this passes a reference to a handle which isn't compatible with the function signiture, you'd have to do something like:

[code]
MyObj@ obj = @this;
Variant["bla"] = obj;
[/code]

At the moment.

-------------------------

rogerdv | 2017-01-02 01:02:23 UTC | #5

[code]Entity@ obj = @this;
			Variant["me"] = obj;[/code]

[code][Mon Jan  5 07:13:46 2015] ERROR: Scripts/RPG/Entity.as:133,12 Expected ']'
[Mon Jan  5 07:13:46 2015] ERROR: Scripts/RPG/Entity.as:133,12 Instead found '<string constant>'
[/code]

But Variant t = Variant(obj); works

-------------------------

