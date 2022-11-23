Miegamicis | 2019-08-14 09:24:58 UTC | #1

I had some plans to create POC regarding the asset management in Urho. Think of it as something similar to Unity's Asset Store. Don't let the name of it scare you, bear with me. I'm not talking about the C++ components, but rather assets themselves (models, textures, shaders, scripts).

1. We could create master repository which would contain JSON with a list of all community supported plugins. It would contain name, author, GIT repository url and short description. If you would like to publish your plugin, you would create a PR with additional JSON entry for your plugin.

2. Each plugin would have it's own repository which would contain specific JSON file which would explain what files are needed for this plugin. We would use Github API to retrieve all the information about the plugin - main JSON file, released versions etc.

3. In the editor there would be "Plugin Manager" (or whatever name we would think of) window that users could open which would download and parse main plugin repository JSON files and display information about them for the end user. User could decide what plugin he wants's to install and also could choose which version of it he would like to install. After pressing install editor would simply download files from plugin's GIT repository which were mentioned in the plugins description file. Each downloaded plugin would be stored in seperate folder, but under the main Urho's "Data" folder to avoid replacing files with the same name. 

This requires me to finish this PR tho: https://github.com/urho3d/Urho3D/pull/2415 
Github works only over HTTPS and engine currently doesn't support it.
Development there is done, just need to fix CI environments which is kinda tricky. 

Let me know what are your thougts about this.

-------------------------

Leith | 2019-08-14 09:29:42 UTC | #2

If you mean the resource cache?

Well, I have one thing to complain about - collision shapes should be resources, not components. If our scene consists of 500 mushrooms, without local scaling, we don't need 500 copies of the shape data in Bullet.

-------------------------

Leith | 2019-08-14 09:31:07 UTC | #3

what I should really say? our CollisionShape component should wrap a resource.

-------------------------

Miegamicis | 2019-08-14 09:33:24 UTC | #4

I'm talking about the physical resource directory. This functionality would allow a more generic way how the samples could be shared in the comunity.

-------------------------

Leith | 2019-08-14 09:37:37 UTC | #5

You're talking about an online resource repo? Sorry, my mind is in a million places

-------------------------

Miegamicis | 2019-08-14 09:41:22 UTC | #6

Yes, exactly. Cause at the moment it's manual labour to copy paste everything by ourselves when we want to check out what others have created.

-------------------------

Leith | 2019-08-14 09:43:45 UTC | #7

Be sure to support package files

-------------------------

Miegamicis | 2019-08-14 09:44:14 UTC | #8

That's great idea, thanks!

-------------------------

Leith | 2019-08-14 09:45:27 UTC | #9

happy to help in whatever way

-------------------------

dev4fun | 2019-08-14 15:12:52 UTC | #10

Ye, Urho needs something like an "project". Unfortunately today its isn't possible coz the Urho editor is only for edit the scene and some small shits, but I agree with u. :slight_smile:

-------------------------

Modanung | 2019-08-15 17:41:47 UTC | #11

Since most people like to code in their favorite IDE anyway, project wizards _have_ been made for - as far as I know - two of them. 
Check out this wiki page on [**Project Wizards and Templates**](https://github.com/urho3d/Urho3D/wiki/Project-Wizards-and-Templates). :open_book:

-------------------------

Leith | 2019-08-16 08:14:15 UTC | #12

Currently no codeblocks wizard for Linux? Added to todo list, but documented already

-------------------------

