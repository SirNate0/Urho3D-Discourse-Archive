setzer22 | 2017-01-02 01:03:06 UTC | #1

I'm trying to query a user variable through AngelScript. That is, set up a custom variable in a node through the editor and then getting its value having a reference to that node,

In C++ the documentation mentions the function:

[code]const Variant& GetVar (StringHash key) const
    Return a user variable. [/code]

But that doesn't appear (nor it's recognised by the compiler) on the script API. 

What am I missing?

Thank you!

-------------------------

cadaver | 2017-01-02 01:03:06 UTC | #2

This is another case where Get / Set functions are converted to array accessor on the AngelScript API side. You can use node.vars with String or StringHash indexing. For example:

[code]
node.vars["Score"] = 0;
int score = node.vars["Score"].GetInt();
[/code]

-------------------------

setzer22 | 2017-01-02 01:03:07 UTC | #3

I had missed that somehow while looking in the documentation. Thank you!

-------------------------

