Bluemoon | 2017-01-02 01:10:34 UTC | #1

I'm considering making a lightweight pull request for extending the script global variable "globalVar" to have an application wide scope. This would mean that the now new globalVars would no longer be a static member of Script but a static member of Context. It would still be exposed as a script variable

-------------------------

thebluefish | 2017-01-02 01:10:34 UTC | #2

I'm 100% against static vars.

Instead, consider making it a member of Context, with a getter/setter for scripting.

-------------------------

Bluemoon | 2017-01-02 01:10:34 UTC | #3

Cool. I'll fix that in right away

-------------------------

