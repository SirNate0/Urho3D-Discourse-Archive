sabotage3d | 2017-01-02 01:07:15 UTC | #1

Hi guys,
Is there any way of preserving the state when changing AngelScript variables while playing in the Urho3DPlayer ?
Similar to this feature: [url]https://youtu.be/yU6lkhjcOp4?t=69[/url]

-------------------------

cadaver | 2017-01-02 01:07:15 UTC | #2

When ResourceCache is set to SetAutoReloadResources(true), script files will be hot-reloaded when changes are detected. There is however no intelligence whatsoever linked to this, the old script module is tossed away with all its state, then it's compiled again.

There is an editor only mechanism that will reload script objects' (ScriptInstances) public variables that are shown in the inspector after a script hot reload. This is based on storing the variable values into a dictionary outside the reloaded script file. Now that I think of it, this store/restore could rather be an engine core feature.

You could also implement your own state restore by e.g. storing variables into node vars and retrieving them on the script object's Start() method.

-------------------------

sabotage3d | 2017-01-02 01:07:15 UTC | #3

Thanks cadaver, but it sound like it won't work if the variables are more dynamic.

-------------------------

cadaver | 2017-01-02 01:07:15 UTC | #4

Sure, it's certainly very hard to preserve an arbitrarily complex script program state. Even something simple like the scripted examples, which typically create scene content on startup, easily run into trouble: if you hot-load them, they will create the content again, unless the code contains logic to avoid that.

-------------------------

magic.lixin | 2017-01-02 01:07:15 UTC | #5

node vars is not working if scene is created by script, maybe engine core can expose some api to set/get global variant.

-------------------------

cadaver | 2017-01-02 01:07:15 UTC | #6

You will probably have better luck when you reload only object scripts and not the main program script. Though we could have a persistent variantmap e.g. in the Script class, that would not need an extra API as such.

-------------------------

sabotage3d | 2017-01-02 01:07:16 UTC | #7

Would that work if we call AngelScript file containing some functions using C++ ?

-------------------------

cadaver | 2017-01-02 01:07:16 UTC | #8

Resource (script) reload works just the same regardless if the main program is C++ that is calling script functions, or is Urho3DPlayer running a script, if that's what you asked. If the script only contains functions and not variables there's nothing to preserve and reloading should work fine.

-------------------------

cadaver | 2017-01-02 01:07:16 UTC | #9

In master branch AngelScript API there now exists a "globalVars" VariantMap for data storage between scripts or through script reloads. For example:

[code]
globalVars["MyGlobalVar"] = "Test!";
[/code]

-------------------------

sabotage3d | 2017-01-02 01:07:16 UTC | #10

Awesome I will try it out :slight_smile:

-------------------------

