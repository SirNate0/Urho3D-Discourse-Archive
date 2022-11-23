Leith | 2019-08-14 09:55:28 UTC | #1

Very early days.

We're not using Urho Player to launch from script... this is a dedicated in-game editor solution.
It could be a single component, so far it is not.

The purple circle indicates where my mouse cursor was, when I took the screen shot (when the gui is visible, so is the cursor), and the surface normal under it at the time... I'm still using a system cursor, so it does not show up in the screen shot.

The editor is somewhat different to the regular Urho editor, but the files it produces are interchangeable, and can be hotloaded, without closing the app you can edit the files externally, and then bring in the changes.

![MousePickNormal|690x332](upload://g8nHXy3eBqrZfSLdpBBbEmYnkhU.jpeg)

-------------------------

Leith | 2019-08-14 11:01:59 UTC | #2

For those who may be interested, this is Lesson 8 in my rad (rapid application development) tutorial series for urho beginners who can already code in c++... (there are a futher 17 lessons for coders who want to learn c++)...
sourcecode on request.

-------------------------

Modanung | 2019-08-14 11:10:07 UTC | #3

[quote="Leith, post:2, topic:5466"]
sourcecode on request.
[/quote]

Why not make a repository for this?

-------------------------

Leith | 2019-08-14 11:14:53 UTC | #4

If there is demand, I might do that. Why hide what I am doing?
This is just an experiment in realtime editing - there is a lot I am not showing... but what is the difference between a git repo, and an offsite link to full source?

-------------------------

Leith | 2019-08-14 11:18:09 UTC | #5

The main invention in this example is that you can take control over, in a character controller sense, anything you can point at, including the ground - the surface normal indicator was a luxury

-------------------------

Modanung | 2019-08-14 12:49:53 UTC | #6

[quote="Leith, post:4, topic:5466"]
...what is the difference between a git repo, and an offsite link to full source?
[/quote]
Believe me, you'll find out with no regrets.

-------------------------

Leith | 2019-08-14 13:13:03 UTC | #7

Given nobody has asked, I won't lift a finger... other things to do. Should that change, then yes, I probably will make a repo - all the same, a picture can be useful and helpful on its own.

-------------------------

Modanung | 2019-08-16 01:31:48 UTC | #8

It's like a public space, an open door where people don't have to knock for a look inside.

-------------------------

dev4fun | 2019-08-14 15:10:17 UTC | #9

I would like to see the repo. Yesterday I was thinking to try an editor too on C++, or migrate all AngelScript code to C++ lol.

-------------------------

TheComet | 2019-08-15 13:02:39 UTC | #10

It should be standard practice for all developers these days to put any new project under version control.

It's possible to launch the standard Urho3D editor in-game. I did this in one of my older projects. It pretty much just involves running ```Scripts/Editor.as``` and making a few modifications so the editor can exit back to the game when it quits.

Having your own in game editor can be helpful in some situations, but I feel like with Urho being able to hot reload everything, an external editor is just as quick to use.

-------------------------

Leith | 2019-08-16 08:10:47 UTC | #11

I am under the hammer trying to earn a teaching qualification, but I will try to find time to automate my repo updates and in this case I will publish a link. It makes me sad. I don't want to maintain a whole fork of the engine, and chances are high that as time goes on, most people won't be able to build my projects without pulling down my changes. This is not what I want at all.

-------------------------

bejer | 2019-08-17 12:29:43 UTC | #12

How can I do hot reloading in Urho?
What would the workflow/setup in Urho look like? Can I ask it to watch for changes in the resources / assets and automatically reload them?
If there is a wiki page describing this, then I have missed it, and would like a pointer to it.

-------------------------

Modanung | 2019-08-17 13:54:25 UTC | #13

You can do this with:
`GetSubsystem<ResourceCache>()->SetAutoReloadResources(true);`

-------------------------

suppagam | 2019-08-17 15:12:43 UTC | #14

Does that apply to scenes too?

-------------------------

Modanung | 2019-08-17 16:01:29 UTC | #15

It applies to the `ResourceCache`, but yes, the effect will be visible for any of the reloaded `Resource`s that are present in a `Scene`.

...or do you mean scene `XMLFile`s? If so the `XMLFile` *will* be reloaded, as it is a resource, but constructing a `Scene` from it is a step that should be manually added.

-------------------------

Leith | 2019-08-18 12:00:21 UTC | #16

Hotloading is an option for resource files, but we can set up FileWatches on folders other than the resource path folders, should we choose. My application does not save scenes to the resource path by default, it saves them in the resource root folder, the one that holds Data and CoreData and such...
PLEASE! Experiment with hotloading! You can edit your scene outside your app, and go back to your app and see the changes! Without restarting your app! It's very RAD...

-------------------------

TheComet | 2019-08-23 09:28:13 UTC | #17

What @Modanung said. If you have a scene XML file, Urho will reload the file but it won't automatically parse/create the scene. For this you have to subscribe to E_FILECHANGED. For example:

```cpp
void ServerApplication::LoadScene()
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();

    scene_ = new Scene(context_);
    planet_ = scene_->CreateChild();
    planetXML_ = cache->GetResource<XMLFile>("Prefabs/ShizzlePlanet.xml");
    planet_->LoadXML(planetXML_->GetRoot());
}

void ServerApplication::HandleFileChanged(StringHash eventType, VariantMap& eventData)
{
    if (eventData[FileChanged::P_RESOURCENAME].GetString() == planetXML_->GetName())
    {
        planet_->LoadXML(planetXML_->GetRoot());
    }
}
```

-------------------------

dertom | 2019-08-23 12:00:09 UTC | #18

[quote="TheComet, post:10, topic:5466"]
It’s possible to launch the standard Urho3D editor in-game. I did this in one of my older projects. It pretty much just involves running `Scripts/Editor.as` and making a few modifications so the editor can exit back to the game when it quits.
[/quote]

Yeah, I like the AS-Editor for this as well(although I didn't use it heavily and only in my scene-previewer so that was no real game). Pretty straight forward with almost no modification.Only thing to do is to use the current scene instead of creating a new one. Afterwards you can just hide the editor...
https://github.com/dertom95/urho3d-blender-runtime/blob/master/bin/Data/Scripts/Editor/EditorScene.as#L61

-------------------------

Leith | 2019-08-29 10:15:20 UTC | #19

![Screenshot%20from%202019-08-29%2019-07-17|690x388](upload://USDSD6Ya1YL3AOP15hv8yMMATA.jpeg) 
Oh Lordy, Pick a bail a day

-------------------------

Modanung | 2019-08-29 12:51:46 UTC | #20

[quote="Leith, post:19, topic:5466"]
Oh Lordy, Pick a bail a day
[/quote]

Only if you feel like it. Although fluffy, this is no cotton farm.

-------------------------

Leith | 2019-08-29 12:57:59 UTC | #21

Probably not :D still, its nice to see progress- the headers on each section of the inspector, can be collapsed, and the state is serializable - also, its completely based on introspection - no special treatment - it can see itself, and edit itself, in terms of attributes, and given its a component - latest news, this component, can load a new scene - and survive it

-------------------------

Modanung | 2019-08-29 12:57:42 UTC | #22

When can the Notyous see the code?

-------------------------

Leith | 2019-08-29 12:59:52 UTC | #23

Oh, yeah, the code :) I'll please and thank you to push it in today or tomorrow. Probably a new repo, for urho beginners, containing my rapid acceleration lessons for people who can sort of kind of already code

-------------------------

Modanung | 2019-08-29 13:01:01 UTC | #24

Are you familiar with branches? They could make possible future pull requests a lot easier to organize.

-------------------------

Leith | 2019-08-29 13:01:37 UTC | #25

Are you telling me to branch my fork? :slight_smile:

-------------------------

Leith | 2019-08-29 13:02:34 UTC | #26

The app, and the urho codebase, are kinda separate - I don't think I rely on any changes I made in this branch

-------------------------

Modanung | 2019-08-29 13:03:50 UTC | #27

Well, it seems like a habit that would increase the chances of achieving your goals, as I perceive them.

-------------------------

Leith | 2019-08-29 13:03:41 UTC | #28

This is not my main branch of my project, this is my sandbox and training ground

-------------------------

Leith | 2019-08-29 13:06:46 UTC | #29

If you think people could benefit, and hell, theres a lot just in the UI stuff that had me fluxed, well, I will make an effort to post it all - by all, I mean, my sandbox, not my main branch

-------------------------

Modanung | 2019-08-29 13:10:19 UTC | #30

That's kind of the trick here: Sharing *opens up the possibility* of people benefiting from your work.

When *not* sharing you can be certain that none other will benefit.

-------------------------

Leith | 2019-08-29 13:08:16 UTC | #31

I have made a lotta comments about what you need to do BEFORE X in UI stuff, and what you need to do AFTER, its not well documented, maybe it could be useful

-------------------------

Leith | 2019-08-29 13:13:17 UTC | #32

I mean, before and after adding a child or subitem, and what you do after adding it, the side effects vary, and its well under documented - to be honest, theres still a crapload I don't understand about Urho's UI implementation, but I am rapidly learning, and willing to share in some way. I am definitely past the samples, and ready to replace the defaults.

-------------------------

Leith | 2019-09-19 04:40:35 UTC | #33

I've extended Urho's DebugRenderer to provide what I need for meshless widgets, which include (oriented) solid cylinders, solid cones, and solid arrows based on a cylinder and a cone.
I've also had to write some extra intersection tests (ray/cylinder and ray/obb) in order to implement my Translate, Rotate and Scale widgets.
It's nice have the basic manipulator tools done, now I need to work more on the UI - while not cluttered like Urho's editor interface, it is far from where I want it to be.

-------------------------

