TrevorCash | 2017-10-02 13:18:49 UTC | #1

Hello,  I'm getting an error while trying to access the scriptObject from a ScriptInstance component:

> ScriptInstance@ scriptInstanceCmp = result.node.GetComponent("ScriptInstance");
> Print(scriptInstanceCmp.className);
> currentSelectedCharacter = cast\<BaseCharacter>(scriptInstanceCmp.scriptObject);

The 2nd line prints out fine while the 3rd line gives a null reference error from angelscript.

This is my global "gamemode" script where I include different .as files for the BaseCharacter.  I already marked all my classes as shared so they should be seen across modules as I understand.

Any ideas on what I could be missing - Thanks in advance!
Trevor

-------------------------

Enhex | 2017-10-02 12:21:13 UTC | #2

[quote="TrevorCash, post:1, topic:3624"]
currentSelectedCharacter = cast(scriptInstanceCmp.scriptObject);
[/quote]
You don't specify what type you're casting to.

-------------------------

TrevorCash | 2017-10-02 13:08:31 UTC | #3

[quote="Enhex, post:2, topic:3624, full:true"]
You don't specify what type you're casting to.
[/quote]


Sorry. I do in fact have them - Forgot to escape the "\<" in the forum editor. - Updated

-------------------------

Enhex | 2017-10-02 13:18:48 UTC | #4

Another reason could be that some types require using `@` prefix for handle assignment.
(see https://urho3d.github.io/documentation/HEAD/_scripting.html#Scripting_Modifications)

Try something like:
`@currentSelectedCharacter = cast<BaseCharacter>(scriptInstanceCmp.scriptObject);`

-------------------------

TrevorCash | 2017-10-02 13:18:48 UTC | #5

That was it.
Thanks Enhex!

-------------------------

Eugene | 2017-10-02 13:17:28 UTC | #6

PS. You could use [v] button to mark answer as solution instead of changing title.

-------------------------

