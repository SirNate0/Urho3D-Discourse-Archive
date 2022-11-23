SirNate0 | 2020-02-09 20:21:31 UTC | #1

This thread is meant to discuss the addition of relative path support to the engine, specifically regarding resource loading (and to keep the EASTL thread from getting off topic). The proposed change allows the grouping of resources more easily by map section or character, so that within, for example, “Map/World1/Level1/node.xml” resources can be identified as “./tree1.mdl”, “./tree1leaves.png” without having to write out the full path for every resource. It also makes some situations of getting resources from the code simpler (I want the clothes.png file from the same directory as this character specification file, for example). Present behavior would be preserved for the most part (technically it would change, as relative path directories `../` and `./` are just stripped from the requested paths, but that I hope is not a feature anyone is relying on or using) -- requesting 'Models/Box.mdl' would still give exactly the same result, but now we could use './normal.png' from a material rather than having to specify a different directory (which I feel is a much better resource layout for an actual game where textures will largely not be re-used between characters and such, though not so much the samples where the resources are rather heavily re-used so dividing by the type of resource is makes more reasonable).

Existing resource loading will be changed (all of the GetResource type functions), requiring an additional parameter (a base path) or switching the String resourceName (i.e. path) parameters to a separate Path class so that the relative paths can be resolved. The extra parameter will be inserted before the bool argument as it should be grouped with the actual resource path requested rather than whether an event is sent on failure. It will have a default empty string parameter, so only the case of specifically requesting an event not be sent on failure will existing user code need to be changed (and possibly also custom resources will need to be modified).

In terms of a cost-benefit, we gain support for relative paths at the cost of a  *slight*  increase in complexity in searching for a resource, which is likely not a bottleneck in anyone’s programs, so this should be fine.

I submitted a Pull Request for this addition two and a half years ago that is still open, so with this thread we can hopefully update and merge that shortly (since then I have let it grow out of date with master, but since there seems to be some interest I'll go ahead and bring it up to date over the next couple of 

https://github.com/urho3d/Urho3D/pull/2070

---
There are a few implementation details to discuss, you can see a couple mentioned in the PR comments. One major one that might not have been mentioned is how we should add the base path parameter. I went with just adding a second string, as you may have noticed, but I also favor the addition of an actual Path class in place of just using strings. This Path would either store both the relative and base path itself, or it would just store the final resolved path (not truly an absolute one since we're still using it to search the resource directories) when constructed from a relative and base path strings. If it were implicitly constructable from a String, I believe it should not require any changes to the code to switch to such a class.

If we went with that, we might want to opt for including this in Urho's 2.0 release, and we could also go and move a lot of path-related features into the class (see the resource loading code for some of what I mean).

That said, a separate path class seems rather unnecessary to me since strings work perfectly fine for it, and then you have to decide implementation details like do we store the path as a String with the full path or as a StringVector of every component.

-------------------------

1vanK | 2020-02-09 21:38:40 UTC | #2

We can go another way. The paths to loaded files (base path) user can store in SetVar(). We need only allow users to specify a proxy function (callback), which will modify path before loading.

-------------------------

1vanK | 2020-02-09 21:42:24 UTC | #3

actually we have AddResourceRouter() I haven’t watched yet if this is suitable

-------------------------

Eugene | 2020-02-09 21:51:32 UTC | #4

Thanks for the link, I checked it.
I remember now why this PR was not merged back then.

I see the following issues with this approach:

1) The only way Urho support "prefabs" now is via `Scene::Instantiate*`.
However, if you don't have any mechanism to set base path for node in this case, you will be unable to load prefabs with relative paths. And this is one of important use cases -- to instantiate prefabs.

2) However, if you fix (1) by changing signatures and setting base path, redundant realtime memory consumption will be introduced. It is a lot of wasted strings to keep file name for each node. Nodes in Urho are already fat and there were attempts to make them thinner, not fatter. [There are solutions for this type of problem](https://www.boost.org/doc/libs/1_72_0/libs/flyweight/doc/index.html), but I'm not sure if this approach will help here.

3) Relative paths are very fragile. The only way you can _create_ them is to manually edit text files.
The moment you save anything via Urho facilities, relative paths are gone. It is especially painful for e.g. materials -- the moment you use editor relative paths are ruined.

So far, it doesn't look as self-consistent feature. It will start falling apart the moment you touch it wrong way.

I don't have any _non-radical_ ideas now, but I will post here if I come up with anything.

-------------------------

SirNate0 | 2020-02-09 21:49:23 UTC | #5

If I remember correctly, Resource Routers are not sufficient at present since it is impossible to determine who is requesting the resource, and beyond that the ../ portions of the path have also been sanitized. This sort of approach doesn't sound too bad - we add a third parameter to the Resource Cache along the lines of an Object*

-------------------------

SirNate0 | 2020-02-09 22:16:49 UTC | #6

[quote="George1, post:65, topic:5872"]
What are your plan to execute it? What are the expected timeline… What are the priority?
[/quote]

For relative paths I have already done it (see point 6). Updating it to work with master is an afternoon's work probably, but I'm pretty busy with other stuff at the moment so it might take a few weeks to get to.

[quote="George1, post:65, topic:5872"]
Is relative path hard to do? Can’t you manually support it? Some game uses package pk2 etc.
[/quote]

No, it wasn't that hard to do. I'm not sure what you mean by manually? I don't use an external library if that's what you mean. It's a pretty simple algorithm - if the path starts with ./ or ../ you add it to the base path directory and then split by /, read from outer to inner directories removing all . and removing the top directory whenever there is a ..

For adding spans I'd estimate tentatively a month. How I intend to do it remains to be seen, but since I'm not asking anyone to help with that the method doesn't matter as only the result will affect anyone else.

[quote="George1, post:65, topic:5872"]
package pk2
[/quote]
No idea what this is, and I couldn't find it with a quick Google search. It sounds more like an alternate package file, which is not what my proposal was about (but is what a different pull request of mine is about).

[quote="George1, post:65, topic:5872"]
My concern is putting too many things up without a clear plan, schedule and task allocation is not how things should be operated.
[/quote]

This would apply to very large changes, but I would argue that learning if the changes would be welcome should still be done before this step. In any case, I'm not being paid for this, it's literally just because I want these features and I'm willing to share since others might too. Sometimes it's less than that, more of I kind of want this feature, and I'm pretty sure others do as well, and I like programming, so I'll try this, particularly if others do actually want the feature. Also, I don't really think task allocation fits with a volunteer-based open source project. Who exactly are you allocating tasks to? (To further illustrate my point, and not because I think it will happen: Are you going to tell my that I should work on some other feature like improving networking or PBR because those are considered a 'higher priority'?) 

[quote="George1, post:65, topic:5872"]
I can come up with 20 things, but that won’t help much.
[/quote]

None of the things I've suggested are a wishlist - I wish someone would do the work to make Urho have this feature. They are either things that I intend to do, or they are things that someone else has already done 90% of the work for and has volunteered to finish up if the community is interested.

-------------------------

Eugene | 2020-02-09 22:16:49 UTC | #7

Are relative paths supported in the Scene in your implementation? If so, where do you take the paths from?

-------------------------

SirNate0 | 2020-02-09 22:16:49 UTC | #8

Each node stores it's own file's path (and one or two other things deriving from Serializable), and when loading resources they pass their own path if they request another resource. I don't load scenes, I load lots of nodes (for map sections, for characters, etc.) so I believe it would still work perfectly fine with listing scenes but I've also not rigorously tested that aspect.

If we want to continue discussing this it may be best to start a new thread or continue in the comments on the PR so we don't get too off the topic of EASTL (though I understand this is also basically my fault).

-------------------------

Eugene | 2020-02-09 22:16:49 UTC | #9

Do you maybe have prototype code online? I don’t completely understand how it is implemented just from your words and I’m curious  about certain aspects of implementation.

-------------------------

SirNate0 | 2020-02-09 22:33:45 UTC | #10

I'm not sure what you mean by not a self-consistent feature, and I do think you will always have relative paths fall apart the moment you touch it the *wrong* way (as soon as you move a file to a different folder it falls apart, for example). The only reason it doesn't fall apart like that as we have things now is because there is no such feature.

To try to address your issues:

1. Yes, nodes will have to store paths. This could be done in the User variables or in the NodeImpl class (I went with the latter since it is not a User variable but a library one and this should be slightly more memory efficient than storing it in the HashMap).
2. This could be addressed by only having the parent node of the prefab store the path, but at the cost of a significantly increased lookup time, or by storing the paths in a global HashMap (HashSet?) and only storing the key in the Node, which adds a global variable but saves memory while not being that great an increase in lookup time.
3. Firstly, so what if they are fragile. MDL files are also very fragile, once the model has been imported the only way to get it out to a usable format is to export the Drawable to an OBJ. The point is not to make the filenames of the resources shorter when they are referenced (they're compressed anyways in package files so the difference should be pretty negligible), but to make creating the files referencing the resources easier. While the present architecture prevents us from keeping any sort of 'this was a relative resource loaded from X' information with the resource (as that would render the cache less useful since you'd have to keep a new copy of each resource for every possible relative name, as opposed to just every possible full name as it is now), it is possible to generate relative paths just as much as it is to load them (but then you run into issues of should it be `../../LevelResources/Tree.png` or just `Maps/LevelResources/Tree.png` when saving). To the best of my knowledge, any comments in the XML file are also not preserved when saving from the editor, or which values were just left as the default, so I don't have any problem with this fragility: Use the editor, lose the commented out old diffuse texture. Likewise, use the editor, lose that it was './Skin.png' as opposed to 'Characters/Warrior/Skin.png'.

-------------------------

Eugene | 2020-02-09 23:51:20 UTC | #11

[quote="SirNate0, post:10, topic:5911"]
MDL files are also very fragile, once the model has been imported the only way to get it out to a usable format is to export the Drawable to an OBJ
[/quote]
Bad example. MDLs (as `Model`) does not support save at all.
However, `Material` does support save. Moreover, it is _guaranteed_ that if you load material you can save it and it will be functionally the same. This guarantee is critical for proper work of tools like material editor and so on.

> Firstly, so what if they are fragile

When user try to use material editor on the material from their prefab, save it with or without changes, and get relative paths corrupted, they will report a bug and I wouldn't argue with them.
Why "corrupted"? Because user will think that everthing is ok until they try to move their folder with relative (as they think) paths. Then things will explode.

[quote="SirNate0, post:10, topic:5911"]
’m not sure what you mean by not a self-consistent feature
[/quote]
I mean amount of places marked as TODO or "doesn't work", and general complexity in API changes.
This is a sign that currently this feature doesn't work together with the rest of the code, but against it.
Do you know this feeling? When you are trying to solve some problem, but every fixed issue greatly increase complexity of changes and you feel like you are sinking deeper and deeper?

I think I just found a chunk of code that is probably screwed due to changed meaning of "name", and there may be more
 https://github.com/urho3d/Urho3D/pull/2070/files#diff-7b9673cfc396212ff55f1c1bee79ab6eR1342

If we claim that relative paths are supported, we need to support them as well as absolute paths.
I.e. if I load scene from file in any way and then instantiate prefab (in any way), I expect relative paths be resolved, if their support is declared.

---

This part is just a speculation

I believe that most of the complexity here are caused by the fact that relative paths are handled by scene hierarchy, while said hierarchy should not care about relative/absolute paths at all. Paths are responsibility of Resource subsystem.

Generally speaking, `Node` does not have a file name. Only special types of nodes have it.
And I don't mean there should be empty strings for the rest of the nodes. There should be no string at all.

In perfect world `Scene` and `Prefab` should be `Resource`s and handle all relative-path stuff on their own, leaving `Node` and `Serializable` untouched. All paths coming to scene hierarchy should be already converted to absolute.

---

PS. I'm sorry beforehand if you consider my replies nitpicking for some reason. I'm just reviewing your code with the exactly same attention to details as I review with my own code I merge into master of Urho (or now rbfx), or as I review the code of my colleagues. I just cannot do it in any other way and ignore issues I consider important. Maybe others will find this solution appropriate.

-------------------------

Modanung | 2020-02-10 02:21:46 UTC | #12

Supporting relative paths for resource dependencies should be possible *without* modifying function signatures in a way that breaks backwards compatibility. Maybe the `ResourceCache` and `FileSystem` could work together to achieve this by keeping track of the master resource location, which would then be used to supplement relative paths. When saving a resource I imagine the option to save relative paths could be passed as a `bool` which defaults to `false`. The resource itself would not have to be aware of its path's relativity.

-------------------------

SirNate0 | 2020-02-10 05:24:27 UTC | #13

@Eugene you're probably right about the mdl's, saving them is not something I've ever wanted to do. However, I disagree with your critique regarding the editor, if the resource is simply loaded and saved it will behave exactly the same. It is only if the file is then moved that there would be a difference in behavior, which I don't see as an issue. (I also don't really like or use the editor, and wish we would just make the blender exporter slightly better to use it as the default editor, so feel free to take that as you will). If I'm not mistaken (I also haven't tried it in the editor to see), the texture paths displayed for the material will be the full paths, so there should be no confusion. 

Thank you for the clarification about what you meant by self-consistent feature. I see your point, and I mostly agree - at present the feature is half-baked (maybe a bit more than that, but certainly not polished and complete). I don't see the broken thing in the diff, but I also didn't scroll all the way through it so you'll have to be a little more detailed. If it's using the resource name as a path I disagree, as the name is set when it is loaded based on the path, but I have no idea if that was what you were meaning. If it's about the JSON support, I'm fine with fixing it, but we have to add a WeakPtr to the JSONFile to every JSONValue just like we can access the XMLFile from an XMLElement (or you may propose an alternate solution).

[quote="Eugene, post:11, topic:5911"]
I believe that most of the complexity here are caused by the fact that relative paths are handled by scene hierarchy, while said hierarchy should not care about relative/absolute paths at all. Paths are responsibility of Resource subsystem.
[/quote]

I half agree, as generally paths are the domain of the resource cache. I half don't, because Nodes and Components are Serializable, and can thus be deserialized from some source, which generally implies a path (potentially a network update). 

[quote="Eugene, post:11, topic:5911"]
In perfect world `Scene` and `Prefab` should be `Resource` s and handle all relative-path stuff on their own, leaving `Node` and `Serializable` untouched. All paths coming to scene hierarchy should be already converted to absolute.
[/quote]

Sounds mostly doable to me, if we wanted to. We have a prefab resource that will load a node, we add an optional basePath parameter to Serializable's Load functions*, and it passes those on to the resource cache whenever is loads something. We add a Prefab component or variable to the node that keeps track of whether the node was created from a prefab so that on Serialization the node gets inserted into the file as a prefab instead of the full heirarchy for it. Saving the prefab is done through the prefab resource and not the node itself, just as the material xml does not get embedded in the scene xml (nor does saving the scene save changes to the material).

*Yes, this does mean the paths aren't absolute before the node gets them, but it also makes it possible to load a node from an arbitrary base path from code, which seems better to me than forcing the user to create a prefab resource to support any relative paths in the node. But we may also have slightly different ideas of what a prefab is.

Addressing your PS, no, I don't really consider them nit-picking, just detailed feedback. It's a good thing that everyone knows in more detail what is being proposed, and also good to work out how we want to address the details I haven't. I don't share your polish-then-share philosophy, I finish it until it does what I need it to and then the edges I haven't gotten to yet (like polishing the JSON aspect) I will finish with feedback from the community (then I don't have to write a second implementation if they didn't like the first.

@Modanung it's entirely possible to do without breaking backwards compatibility, we just use multiple overloads of the functions (unless everyone else insists, I refuse to separate the name (path) and base path parameters in the arguments list since they are closely related. Alternatively, we go with making a separate Path class implicitly constructable from a String (with optional base path). As to "keeping track of the master resource location" I assume you are envisioning some sort of stack that would be queried so resources that request other resources pick the right base path? If so, I don't think it would be a good idea because 1) that seems to result in Serializable's like Node not being able to use relative paths and 2) it would make it harder to load a resource from a base path from code.

Also, I like the proposed saving solution.

For the record, I favor the `class Path` approach, as it would be easier to add features to later, but it is also more work and a bigger change. I'm willing to make those changes if you guys want, but I don't intend to unless you think it would be accepted, as what I have already meets my needs.

-------------------------

1vanK | 2020-02-10 05:52:30 UTC | #14

In fact, I see no problem in storing ABSOLUTE file path for a loaded resource. Just as a user can save a text document with Save button, the user may want to save the previously loaded scene / node / material. A pointer to a string does not greatly increase size of the class. At the same time, I do not see anything wrong with the fact that when loading a resource, is passed additional information about who requested this resource (pointer to an object as SirNate0 said earlier).

-------------------------

Eugene | 2020-02-10 08:44:37 UTC | #15

[quote="SirNate0, post:13, topic:5911"]
I don’t see the broken thing in the diff, but I also didn’t scroll all the way through it so you’ll have to be a little more detailed.
[/quote]
Oh, sorry, I always forget that github diff links are wonky in big PRs.
https://github.com/urho3d/Urho3D/blob/f764aca5b36eb68a1efbb21702115af89ffb0e2c/Source/Urho3D/Scene/Scene.cpp#L1337-L1343
You see, this code assumes that if you pass sanitated resource name into ResourceCache and get back a resource, the name of said resource would be exactly the same as you passed.

Moreover, sanitation kills relative paths, so this code just will not work.

https://github.com/urho3d/Urho3D/blob/f764aca5b36eb68a1efbb21702115af89ffb0e2c/Source/Urho3D/Resource/ResourceCache.cpp#L841-L846

Actually, it may be a sign that you don't need basePath support in _all_ functions of resource cache. You need it only in SanitateResourceName that will resolve relative paths into absolute. Then you just use this function to get absolute resource path every time you may have relative one.

-------------------------

dertom | 2020-02-10 09:44:20 UTC | #16

I have to say that I didn't read this thread fully and I didn't realize the problems,yet. (I will take some time after work). But I have another suggestion. 
Wouldn't it be possible to let the resource-cache create sub-resourcecaches as needed. Every single one of them would again be a resource-cache pointing to the relative folder. They would be managed by the parent-resource-cache and would need to be connected in some way to the parent.... (if that is needed at all)
Any resource accessing object would have an additional relative resource-cache poiting to folder it was loaded from. On any resource access we would need to check if a relative prefix is present or not  and choose between the relative or the global resourcecache.
I'm not sure if that approach is possible at all,maybe there are some oppions and hints from the more experienced users before I start looking deeper into it.

-------------------------

Modanung | 2020-02-10 14:01:24 UTC | #17

[quote="SirNate0, post:13, topic:5911"]
1) that seems to result in Serializable’s like Node not being able to use relative paths and 2) it would make it harder to load a resource from a base path from code.
[/quote]
Would (relative) paths not always reside in XML or JSON files? I think relative paths could be fixed as they are read. There is no need for a `Path` class in that case.

For the sake of consistency, functions that refurbish paths should reside over at the `FileSystem`. Have a look at [these functions](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/IO/FileSystem.h#L126-L152) in `FileSystem.h`. Maybe something like `String AppendRelativePath(const String& relativePath, const String& mainPath)` and `String GetRelativePath(const String& path, const String& from)` could be added to the list and used when saving and loading resources.

-------------------------

SirNate0 | 2020-02-11 00:24:47 UTC | #18

I don't think adjusting the paths as they are read is a good solution, because that makes the XMLFile and JSONFile very specific to Urho -- the code has to determine what is considered a path and what is not, and then selectively changes some of the content accordingly. If you are simply advocating we add another GetInt type method that is a GetPath, and patch it based on that I would be more comfortable, as then it is the code that is using the XML/JSON to save the file and read it and the XML/JSONFile doesn't have to be aware of what is a path and what is not.

I do think adding such a function is the right idea -- I believe I added what would be the AppendRelativePath with a different name already, though I don't think I did the reverse (creating a relative path from two absolute ones).

TODO: Replies to other posts (I'm too busy right now to get to the rest, sorry guys).

-------------------------

Modanung | 2020-02-11 01:17:28 UTC | #19

[quote="SirNate0, post:18, topic:5911"]
...that makes the XMLFile and JSONFile very specific to Urho...
[/quote]
Well, they _are_ Urho3D `Object`s.

[quote="SirNate0, post:18, topic:5911"]
...the code has to determine what is considered a path and what is not...
[/quote]
I'm not sure what you mean by that. Since the paths would point to resources from inside another resource - to which the path is relative - aren't the relevant values expected to be paths anyway?

-------------------------

Eugene | 2020-02-11 06:19:45 UTC | #20

[quote="Modanung, post:19, topic:5911"]
Since the paths would point to resources from inside another resource - to which the path is relative - aren’t the relevant values expected to be paths anyway?
[/quote]
How would you find relative paths in generic XML or JSON without known structure?
It might be material, or node, or cube texture. Or something else, like custom resource.

-------------------------

Modanung | 2020-02-11 13:18:55 UTC | #21

What if the `ResourceCache` would set the `FileSystem` working directory to that of the resource being loaded? It could be added to any relative paths for nested resources and restored when loading is completed or interrupted.

-------------------------

Eugene | 2020-02-11 13:51:26 UTC | #22

[quote="Modanung, post:21, topic:5911"]
It could be added to any relative paths for nested resources and restored when loading is completed or interrupted.
[/quote]
Global state for such simple thing as reading a file is bad idea.
Multithreading will be broken for sure, and nested resource loading will require internal stack of working directories.
And other reasons I'm too lazy to list...

-------------------------

Modanung | 2020-02-11 16:41:51 UTC | #23

Looking at the PR again, why not instead of:

`GetResource(name, basePath)`

do

`GetResource(CompletePath(name, basePath))`

String CompletePath(const String& path, const String basePath = String())

?

-------------------------

Eugene | 2020-02-11 17:16:33 UTC | #24

[quote="Eugene, post:15, topic:5911"]
Actually, it may be a sign that you don’t need basePath support in *all* functions of resource cache. You need it only in SanitateResourceName that will resolve relative paths into absolute. Then you just use this function to get absolute resource path every time you may have relative one.
[/quote]
@Modanung mostly agree

-------------------------

1vanK | 2020-02-11 17:21:10 UTC | #25

We need allow users register inherited ResourceCache subsystem instead default. It's also very useful when user wants add its own container for resources (zip file instead pak for example).

-------------------------

SirNate0 | 2020-02-11 17:35:02 UTC | #26

I agree. I have another PR (probably a bit less complete than this one) that pursues that idea. The package file functionality is extracted to a separate class from the (system) file one and the package file has an added abstract FileSource users can inherit from. I believe I made an example with it supporting gzipped files.

(Unless this is meant as a comment favoring fewer changes to the function signatures to maintain users existing implementations of such an idea, in which case I'm ambivalent either way)

-------------------------

1vanK | 2020-02-11 17:44:05 UTC | #27

I tend to favor maximum engine flexibility. Ideally, the engie should be a just collection of cool libraries. And a user can replace any subsystem with his own without changing the engine. For example, replace scene graph / renderer with your own implementation with support of BSP trees and use only the audio and the input subsystems from the engine

-------------------------

SirNate0 | 2020-02-11 22:47:30 UTC | #28

What do you all think of the idea of adding a separate class to handle paths? It would be implicitly constructible from a String and a const char* so that existing code should work with few-to-no changes. This class can then handle resolving the relative paths, as well as forming relative paths from two absolute ones, and we can put all of [these functions](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/IO/FileSystem.h#L126-L152) in that class (with deprecated global functions to minimize immediate changes for the user).

If you guys aren't opposed, I would like to change what I've done to follow this route, as I think we're starting to approach (or perhaps are already are at) the point where we're treating paths as just strings with the result being more complicated and not less. 

Thoughts?

---
As a tentative way to allow the JSONFile and XMLFile to handle paths, I also have this proposal (if we want to go down that road): 
We add a new attribute type and flag to go with it that is a "Path". XML this is straightforward, since the elements already know about the file (if I remember correctly). JSON we support it by adding a WeakPtr to the file which will be set when we read JSON from a file. On reading, then, we know about the file and any relative paths found get resolved when the user calls GetPath(). On writing, absolute paths are stored and flagged as being paths when the JSONValue is created, then when the JSONFile saves it it goes through and creates the relative paths. Absolute paths can be stored just as strings and need no special treatment.

-------------------------

Eugene | 2020-02-12 09:30:30 UTC | #29

[quote="SirNate0, post:28, topic:5911"]
What do you all think of the idea of adding a separate class to handle paths?
[/quote]
Before you go this way, you need to clearly determine _what_ this path class is going to be. What guarantees it will give for user?

Can I always pass said path into ResourceCache and resolve it into resource if resource exists?
Can I be sure that every Resource have only one path pointing to it?
Can I be sure this is the same as resource name?
If no, what are conditions? Is is easy to check if said conditions are met when *reading* the code?

Also, resource path is not the same thing as file path.
They work differently and are used in different places, even if they are converted from/to each other.

I do like the idea to stop using `String` in place of paths, but I have a feeling we may need _more than one_ class for paths. Or we may not and one Path will suffice, I have no idea.

[quote="SirNate0, post:28, topic:5911"]
As a tentative way to allow the JSONFile and XMLFile to handle paths, I also have this proposal (if we want to go down that road):
[/quote]
Honestly, I cannot say how bad it will be just from the description. 
Maybe it would be ok, maybe it will screw the whole idea of XML/JSONFile.

-------------------------

SirNate0 | 2020-04-03 02:02:03 UTC | #30

[quote="Eugene, post:29, topic:5911"]
1. Can I always pass said path into ResourceCache and resolve it into resource if resource exists?
2. Can I be sure that every Resource have only one path pointing to it?
3. Can I be sure this is the same as resource name?
If no, what are conditions? Is is easy to check if said conditions are met when *reading* the code?
[/quote]

1. That would be the goal, otherwise it's not of much use.
2. No, nor can you at present as SanitateResourceName will already return different paths based on the presence of "./" and "../". A modified version of this function will need to exist accepting a `Path`. There should only be one `Path` per resource after Sanitation.
3. After Sanitation, yes, you can be sure that the sanitized `Path` will match the resource name.

[quote="Eugene, post:29, topic:5911"]
Also, resource path is not the same thing as file path.
They work differently and are used in different places, even if they are converted from/to each other.
[/quote]

I think I mostly disagree. A resource path is effectively a possible relative file path that may or may not refer to an actual file (with the possible exception of certain packed resources, possibly?). If your point is that resource paths are simpler (no drive letters/network locations) and use the internal forward slash representation then I agree that they are different, but I see it more as resource paths are a subset of possible filenames.

I could be completely wrong about that, though, so if you have some points that would show me where I would gladly look into it more.

---
That said, I have also created a first draft of a Path class. It is incomplete, and I did not check to see that it compiled, but if anyone wishes to look at it you can find it here:

https://github.com/SirNate0/Urho3D/blob/path-class/Source/Urho3D/Core/Path.h

Comments are welcome, including on things like "which directory in Source/ should it be placed in?"

-------------------------

Eugene | 2020-04-03 08:51:27 UTC | #31

[quote="SirNate0, post:30, topic:5911"]
A resource path is effectively a possible relative file path that may or may not refer to an actual file (with the possible exception of certain packed resources, possibly?). If your point is that resource paths are simpler (no drive letters/network locations) and use the internal forward slash representation then I agree that they are different, but I see it more as resource paths are a subset of possible filenames.
[/quote]

What I mean is that some places in the engine accept file paths, and other places accept resource paths.
These uses are not interchangeable. You cannot pass resource path where the engine expects file path, and vice versa. Therefore, file path and resource path are different abstractions. In the same way as Vector4 and Color are different things even tho they are both just 4 floats and Color is a subset of Vector4.

-------------------------

SirNate0 | 2020-04-03 16:19:31 UTC | #32

I understand now. I don't think it will end up being a concern, as while it is true there is a bit of a difference, I don't think it will prove to be too significant. At present, the largest difference I can think of is that resource names are never absolute (I think) but are relative to the assigned resource paths, while tru file paths can be absolute or are relative to the current working directory.

That said, aside from opening some files to save things, I haven't really messed with the real file side of things, so I may find out that's not the case when going through the rest of the code.

-------------------------

SirNate0 | 2020-04-04 07:32:31 UTC | #33

Significant progress has been made in integrating the Path class into the engine. Script bindings still remain, and there are some API decisions that should be made in regards to the Path class. Comments are welcome now, but I'll issue a PR in a couple days once I'm pretty confident things are working alright, at least on Linux (I may have the CI check the other platforms, I may do a cross compile build, we'll see).

-------------------------

Eugene | 2020-04-04 09:02:43 UTC | #34

Can you remind me what's your end goal?
My guess is that you need relative paths for (1) resource refs in prefabs and (2) for textures referenced by materials.
Is it correct?

I feel very conflicted now. Relative paths are the feature that I want for a long time. On the other hand, I’m still afraid that the second PR will not be too different from the first one, and I’m concerned about code quality.

-------------------------

George1 | 2020-04-04 11:51:22 UTC | #35

I think code quality is subjective.

If you have beautiful code but it contain bugs, then it is useless.
If you have ugly code, but it run fast, always work and without bug, then why not add it.

-------------------------

Eugene | 2020-04-04 13:14:55 UTC | #36

[quote="George1, post:35, topic:5911"]
If you have ugly code, but it run fast, always work and without bug, then why not add it.
[/quote]
Because current pitiful state of Urho codebase is the direct result of exactly this feature adding policy.
Except we sometimes have ugly code with lots of bugs and w/o any performance profiling done.

I'm not really taking about the code itself. By "code quality" I mean design aspects.
Like, classes shall have clear and separate responsibilites, and interfaces shall have expected behavior, and so on.

If we ignore high-level design aspects, we will just end with code that is nearly impossible to extend or maintain. It has already happened with Networking, it has already happened with Renderer too. It's close to happening with Scene and Serialization. If things go this way, we will end up with the project that cannot be extended and/or fixed anymore. Or we are already in this state and we need to _cut features_ instead of adding. I don't know.

---

I don't really know anything about the current version of this PR, but the previous version from 2017 had a lot of design issues. I don't know if they are relevant now.

Since I want this feature myself, I have spent some time looking for solution, but I didn't get any new bright ideas yet.

-------------------------

SirNate0 | 2020-04-04 15:01:31 UTC | #37

[quote="Eugene, post:34, topic:5911"]
My guess is that you need relative paths for (1) resource refs in prefabs and (2) for textures referenced by materials.
Is it correct?
[/quote]
Yes, that's basically the goal. A couple other custom resources as well, but those are the main examples from Urho (as well as scripts referencing materials, I suppose).

A secondary goal is to improve the quality of Urho's handling of paths, as they really are not ordinary strings, so we can remove the `.Replace("/./","/")` and such that are strewn around the Engine.

In terms of high level design, this is not that much of a change with the exception of how we handle the Variant class. Pretty obviously, I added the class to Variant. However, in order to facilitate greater backwards compatibility, I want to make GetString also return the string when the Variant holds a Path. As that changes the making of GetString (though not that significantly since we do the same for Color and Vector4), I added a separate GetPathString instead. Unrelated to the goal of supporting relative paths, I think a separate Path class is the correct design decision, as right now a path is basically just a string that has been passed through one of the "magic" path functions located in FileSystem.h (I say magic because the functions take a string and return a string, but the new string is now Urho's internal parth representation). I have mixed feelings about the global functions. I'm tempted to include them and just have them call the functions in the Path class, maybe change them to a Path return type. That fixes most of the backwards comparability issues other than the API change to use Path (which is not too significant since Path can be constructed from String) and the more annoying one that logging a path, or any such conversation to a string, requires calling Path::ToString.

-------------------------

Eugene | 2020-04-04 15:24:17 UTC | #38

I just realized I don't entirelly understand the idea behind `Path`.

What _is_ the `Path` exactly in your current implementation?
I mean, what are the semantics of this class? What kind of path is represented by this class?
Given the instance of `Path`, where I can use it? What API will accept it?

Is it the most generic path possible, or something more specific?
Is resource name a `Path` too?

-------------------------

SirNate0 | 2020-04-04 15:37:02 UTC | #39

Path is a class that holds a String contains the Urho internal representation of a path (i.e. forward slashes, and /./ And the like resolved to /). It implements the features of all of the functions found at the bottom of FileSystem.h, as well as a few functions like Length and Compare (basically borrowed from String). It is not the most generic path possible (it doesn't allow backslashes, for example), but should be generic enough to represent any possible file on the filesystem.

I'm actually deciding about `Resource::name_` right now. I'm inclined to make it one, even though that would mean some resource names would be excluded, because at present such resources could not be obtained from the resource cache anyways (though it could be added to the cache, because of SanitateResourceName it could not be obtained with GetResource). 

I'm also thinking about having it internally be stored as a path and have a GetName and SetName interface to the Path (as well as Get/SetPath with the Path class). Though that would mean that `r.SetName("../a.txt); r.GetName() == "../a.txt"` would be false.

Thoughts?

-------------------------

Eugene | 2020-04-04 17:53:47 UTC | #40

Since you name it “Path”, let’s use it everywhere where path things are used, including resource names.
Implicit conversion from string is probably needed.
I cannot really say much without seeing diff in existing code.

Since this change is going to have very wide scope, external code changes need to be minimized.
I hope it shall be enough to replace type name and fix actual uses of the path.

-------------------------

Modanung | 2020-04-04 21:09:24 UTC | #41

Allowing relative paths in resource names does not make much sense to me: *What* would they be relative to? In my view relativity is most useful _inside_ resources that refer to other resources, as the `TmxFile2D` already does for its tile sets: `TmxFile2D::LoadTSXFile` should be generalized so it can be used with *all* resources. I think `FileSystem::SetCurrentDir` could be utilized to elegantly achieve this generalization; by setting and restoring it, before and after loading a nested resource. As you can see, `LoadTSXFile` already assumes the `name_` of `TmxFile2D` to be an absolute foundation suitable for resolving relative paths. `ResourceCache::SanitateResourceDirName` applies a similar approach, and it would not require a specialized `Path` class.
Concerning prefabs, this seems to asks for a _`Prefab`_ resource/component, *not* increasing all `Node`s' complexity. It understanding relative paths would follow naturally from the aforementioned implementation.

-------------------------

Eugene | 2020-04-04 23:08:49 UTC | #42

[quote="Modanung, post:41, topic:5911"]
Concerning prefabs, this seems to asks for a *`Prefab`* resource/component, *not* increasing all `Node` s’ complexity. It understanding relative paths would follow naturally from the aforementioned implementation
[/quote]
I actually have very similar thoughts. Scene graph itself doesn't need to know about file paths if it's all moved into resources (like Prefab).

[quote="Modanung, post:41, topic:5911"]
Allowing relative paths in resource names does not make much sense to me: *What* would they be relative to?
[/quote]
How about this pattern:
Resource paths within Resource may be relative to this resource.
Resource paths outside of Resource cannot be realtive.
So... that's probably what you said, if I get it right.

[quote="Modanung, post:41, topic:5911"]
I think `FileSystem::SetCurrentDir` could be utilized to elegantly achieve this generalization; by setting and restoring it, before and after loading a nested resource
[/quote]
This approach has major issue:
Resource cache doesn't care about what you do with `SetCurrentDir`, it works relative to cache dirs from setup params.

-------------------------

Modanung | 2020-04-04 23:14:34 UTC | #43

[quote="Eugene, post:42, topic:5911"]
Resource paths withing Resource are relative to this resource.
[/quote]
I see no reason to remove support for absolute paths in these cases.

[quote="Eugene, post:42, topic:5911"]
Resource cache doesn’t care about what you do with `SetCurrentDir` , it works relative to cache dirs from setup params.
[/quote]
What kind of issues do you think this would introduce, and where?

-------------------------

SirNate0 | 2020-04-04 23:14:35 UTC | #44

First draft of a PR for a Path class has been created.

https://github.com/urho3d/Urho3D/pull/2619

-------------------------

Eugene | 2020-04-04 23:14:49 UTC | #45

[quote="Modanung, post:43, topic:5911"]
I see no reason to exclude absolute paths.
[/quote]
Yeah, I realized that my wording was obscure and I edited my reply.

[quote="Modanung, post:43, topic:5911"]
What kind of issues do you think this would introduce, and where?
[/quote]
Do you mean "what kind of issues we will get it we use `SetCurrentDir` to get relative paths"?

-------------------------

Modanung | 2020-04-04 23:18:34 UTC | #46

Yes, I do mean that. The `ResourceCache` currently not caring, seems like good news as there would be no conflicts with existing operations.

-------------------------

Eugene | 2020-04-04 23:19:36 UTC | #47

[quote="Modanung, post:46, topic:5911, full:true"]
Yes, I do mean that
[/quote]
`SetCurrentDir` will have no effect on the behavior of `cache->GetResource<T>(path)`.
Therefore, I don't see how it will help us with relative paths.

-------------------------

Modanung | 2020-04-04 23:20:51 UTC | #48

Well, applying the suggested approach would then mean changing that. How is that an issue?

-------------------------

Eugene | 2020-04-04 23:21:02 UTC | #49

[quote="SirNate0, post:44, topic:5911"]
First draft of a PR for a Path class has been created
[/quote]
I'm already terrified by its scope. But I'll check it... when I gather courage.

-------------------------

Modanung | 2020-04-04 23:26:05 UTC | #50

I'll see if I can put my words to code, on [Dry](https://gitlab.com/luckeyproductions/dry) land.

-------------------------

