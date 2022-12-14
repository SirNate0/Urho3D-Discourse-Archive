Cpl.Bator | 2017-01-02 01:12:36 UTC | #1

Hello, this topic is related about the documentation. i think the documentation is poorly documented , it's hard for a newbie like me to find information without look at the code source.

example :
[urho3d.github.io/documentation/1 ... 6046506602](http://urho3d.github.io/documentation/1.4/class_urho3_d_1_1_sprite2_d.html#a9941b08d2a48916bdc1b9f6046506602)

for this method : Sprite2D::SetRectangle (const IntRect &rectangle)
Rectangle of what ? texture rect ? shape of the sprite ? the doxygen say : "[i]Set rectangle.[/i]" is not obvious to understand.

I like Urho3D , the engine at first look is simple , the editor is great, but I waste my time on things that should be simple.

i think if the documentation is improved, the community , snippet , etc.. will grow up quickly.  :wink: 

Thank you.

-------------------------

TheComet | 2017-01-02 01:12:36 UTC | #2

I agree. The API documentation is definitely not Urho3D's strong point. The vast majority of docstrings don't reveal any information that can't already be obtained by just reading the function name. Here just a small example of how most of Urho3D's codebase is documented:

[spoiler][code]    /// Set tags. Old tags are overwritten.
    void SetTags(const StringVector& tags);
    /// Add a tag.
    void AddTag(const String& tag);
    /// Add tags with the specified separator, by default ;
    void AddTags(const String& tags, char separator = ';');
    /// Add tags.
    void AddTags(const StringVector& tags);
    /// Remove tag. Return true if existed.
    bool RemoveTag(const String& tag);
    /// Remove all tags.
    void RemoveAllTags();[/code][/spoiler]

I'd rather see comments explaining what tags are, what they could be used for, how they are stored, etc.

The wiki pages do help, but they''re also not as complete as they could be.

-------------------------

hdunderscore | 2017-01-02 01:12:36 UTC | #3

Any documentation improvements would take significant effort, although they would be great to see.

A simple solution I began working on was including code snippets in the documentation: [github.com/urho3d/Urho3D/issues/1185](https://github.com/urho3d/Urho3D/issues/1185)

Although much simpler than writing improved documentation, the large number of classes involved also makes it quite a significant effort involved.

-------------------------

cadaver | 2017-01-02 01:12:37 UTC | #4

Pull requests to improve class documentation would of course be acceptable. However agreed with hd_ on the effort. We'd need to decide the level of improvement, e.g. should every function have a description body, parameter descriptions etc. This can also become tedious.

I have personally tried to strike a balance with the "one-liner" function comments to include conditions for a successful call or other important factors to consider, and meaning of return values. For higher level concepts like what tags are, you still need to refer to the documentation pages, e.g. see the section Identification in [urho3d.github.io/documentation/H ... model.html](http://urho3d.github.io/documentation/HEAD/_scene_model.html)

-------------------------

weitjong | 2017-01-02 01:12:37 UTC | #5

Currently our online C++ API documentation pages for graphics are always generated using OpenGL API. These pages are automatically generated by our Travis-CI job, so that's why it is using OpenGL. On AppVeyor CI side, we do have the possibility to upload the API documentation pages that are generated using DX11 graphics API. However, this is not an ideal solution because we would then have two almost identical documents on our GitHub Pages which only differ in the backend graphics API class reference. So, I wonder are there any Doxygen special commands that we can use to solve this problem by generating all the class references in a single set of documentation and some how has separate groups for each graphics API? Anybody knows? At the moment we do not use "module" groupings, but I am also not sure it can be used for this purpose.

-------------------------

Cpl.Bator | 2017-01-02 01:12:38 UTC | #6

@hd_
[quote]Any documentation improvements would take significant effort[/quote]
Yes, i agree with that , but if you dont create a good documentation , your software / lib / gameengine , etc... will be go to die. 

[quote]A simple solution I began working on was including code snippets[/quote]
Snippets & example is a good idea , examples of urho3D cover many questions , but it is not enough. and for make snippets, we must understand the engine :slight_smile:


@cadaver
[quote]This can also become tedious.[/quote]
Look at another api : SFML , the guy is alone for documentation. : [sfml-dev.org/documentation/2.3.2/](http://www.sfml-dev.org/documentation/2.3.2/) 
and here : [sfml-dev.org/documentation/2.3.2/classes.php](http://www.sfml-dev.org/documentation/2.3.2/classes.php) , it's clean.

i known is a lot of work & tedious, but , it's very important a good documentation also same as the engine itself. stop coding engine and create sfml like documentation ! :slight_smile:

thx & sorry for my poor english, i'm French ^^

-------------------------

yushli | 2017-01-02 01:12:38 UTC | #7

Document is important. But sample projects (real world game projects)are even more important. Improvements to the engine is even more important. I would rather the core team members to code the engine to make it even better, given the limited time. We can always read the source code, and fire issues if something is not clear. 
Learning from sample projects are very useful. I hope we can have more such projects such as flappy urho, dissolving, outline, motion blur, heXon, etc etc.

-------------------------

noals | 2017-01-02 01:12:41 UTC | #8

[quote]really, there should be templates examples for component, logic component, object with their essential requirements. (or not essential as a plus, for common usages, but commented as such !)
here instead of 3 clear examples, i have to deal with 41 of them kinda... [/quote]

that would be an improvement to me.

-------------------------

