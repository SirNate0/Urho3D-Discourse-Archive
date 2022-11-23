ucupumar | 2017-01-02 01:00:52 UTC | #1

I want to iterate through technique passes on AngelScript, but I can't seems to get it's length. 

I access the length using:
[code]StaticModel@ model = node.GetComponent("StaticModel");
Material@ material = model.materials[0];
Technique@ technique = material.techniques[0];
int length = technique.passes.length; [/code]
But, it gives me error:
[code]'passes' is not a member of 'Technique'[/code]
What happens?

-------------------------

thebluefish | 2017-01-02 01:00:53 UTC | #2

This is because of how the Passes are stored:

From Technique.h:
[code]
/// Passes.
    HashTable<SharedPtr<Pass>, 16> passes_;
[/code]

From HashTable.h:
[code]
/// Hash table with fixed bucket count. Does not support iteration. Should only be used when performance is critical, as HashMap is much more user-friendly.
[/code]

As you can see, it is simply not possible to iterate over the passes. Instead you can get named passes with the following function:
[code]
"Technique", "Pass@+ get_passes(StringHash)"
[/code]

However this is a poor alternative as it assumes you know what the passes are named as.

-------------------------

weitjong | 2017-01-02 01:00:53 UTC | #3

At first I thought It was an AngelScript binding error on the "passes" property, but on closer inspection I believe it is intentional. In this case the property is being exposed as an array of Passes indexed by a StringHash but it is not implemented by actually constructing the array internally, so your line to access array's length property failed. As pointed out, currently you can only get a single Pass handle one at a time indexed by a StringHash. e.g.: [code]Pass@ pass = technique.passes[StringHash("base")][/code]
I am working now to see whether I can bind a few more convenient read-only properties for Technique class.

-------------------------

weitjong | 2017-01-02 01:00:53 UTC | #4

I have just committed the changes into the master branch. I am a little bit hesitate to break the existing AngelScript API in regard to the "passes" property but in the end go ahead with it because I believe on the scripting side only a few peoples would be interested and using the exposed API for the technique. If I am wrong, please let me know and I will revert it back. With this change, the "passes" property is changed from "Pass@[] passes // readonly" to "Pass@[]@ passes // readonly". Meaning, it has been changed from an indexed property of type Pass to an array of type Pass. They are all "handles", meaning the array members are properly reference counted. It also means one should not use the array variant if he/she really is only interested in getting one Pass due to the overhead of constructing the vector/array internally.

@ucupcumar, now you have a few ways to "iterate" through all the passes in a Technique without first knowing or hard-coding the pass types (StringHash). Just that as per documented, you should not expect the iteration order to be the same as original passes order in the technique XML definition file. Semoga bermanfaat. :slight_smile:

-------------------------

ucupumar | 2017-01-02 01:01:01 UTC | #5

Sorry for late late response.  :blush: 

Thanks weitjong! It works now! I can iterate the passes using technique.numPasses as length. Actually, I just want to check all object passes in scene initialization. So, overhead can be ignored in my case.
Now, the problem is how can I get pass name/type? It looks like AngelScript API can't return pass type.

-------------------------

weitjong | 2017-01-02 01:01:02 UTC | #6

It can only return the pass types as StringHash (see passTypes readonly property) and not as the String name itself because that info is already lost in the Technique class internally.  We don't want to change its internal just for this purpose.

-------------------------

ucupumar | 2017-01-02 01:01:02 UTC | #7

Oh, I see. So, it's impossible to retrieve pass type string. 
It looks like I should use technique's own HasPass() if I want to check pass availability. That's okay.
Thanks weitjong.

-------------------------

weitjong | 2017-01-02 01:01:02 UTC | #8

You are welcome. You can use HasPass() like you proposed or alternatively create a reverse name mapping yourself before hand so you can map those StringHashes back to their names during iteration.

-------------------------

