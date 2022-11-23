thebluefish | 2017-01-02 01:07:43 UTC | #1

I've been playing around with Godot a bit to get a feel for how other people tackle some issues, and I found one feature that I think we need for Urho3D: Path URLs.

It would look something like:

"res://models/box.mdl" - Looks in the resource folders or packages for "models/box.mdl"
"usr://settings.cfg" - Looks in the user writable directory
"app://settings.template.cfg" - Looks in the application root directory

Additionally, the ResourceRouter class could be changed appropriately. A ResourceRouter could be tied to a specific URL type and "res", "usr"/"user", and "app" would all be default ResourceRouters provided out-of-the-box.

Understandably this is a bit of work. So before I go about implementing this, I wanted to get other's opinions on this idea.

The purpose of this is to allow greater flexibility. Plug-n-play ResourceRouters would allow people to share their own schemes. Additionally it allows us the benefit of storing file locations in scripts and data. Currently a file path in the editor can only point to a resource, it's not easy to point to a game save location or a path for logs without building the path in C++ or in a script.

-------------------------

cadaver | 2017-01-02 01:07:44 UTC | #2

If you want to go all-out with this, you would tie it directly to Files, meaning you could open a File directly with a "usr://" path. However, this would be a large rework, and I'm not sure if it's justified. On the other hand, the ResourceCache's current file-related purpose is to offer access to read-only files for reading resource data, so if the URL rework would make it also hand out writable files for e.g. configs and savegames, we'd somewhat dilute that purpose.

When you imperatively build the paths using GetUserDocumentsDir() etc. you are 100% sure what's going on.

-------------------------

thebluefish | 2017-01-02 01:07:46 UTC | #3

What about adding a ResourceRouter to FileSystem? Then File could do a route based on a FileSystem-wide ResourceRouter. That would also allow people to use the same ResourceRouter class for both FileSystem and ResourceCache if they'd want.

I don't think that having writable resources in ResourceCache would be appropriate. So this is the next best idea IMO. I did a quick'n'dirty addition of a ResourceRouter to FileSystem, then made File route through it. It seems to work OK, if not a little confusing due to the naming. My main concern is how ResourceCache interacts with File, setting two ResourceRouters could have some odd issues if someone doesn't realize that it would be processed twice. However I'm certain this isn't going to be a problem for *most* people.

Still, I like the idea of having uniform file paths. I would like to have some sane way of being able to define a path and know where it's going to go. It's just part of some of my gripes with trying to flesh out data-driven development with the engine. I don't want to expect a user to build a path in C++ or scripting every time they want to access a file. Instead they should be able to just take a path, and be able to know where that file is going to be. So allowing them to prefix the path with where they want the file (User, App, Res, etc...) would allow convenient access without the need for scripting.

-------------------------

cadaver | 2017-01-02 01:07:47 UTC | #4

That would work for the usr:// and app:// paths. However for the res:// paths I don't want FileSystem to start calling into ResourceCache. 

Instead (if you want to make that work) you could shift the responsibility of handling resource directories and packages to FileSystem, then ResourceCache's task would just be caching resources like the class name says, and it would be asking the files from FileSystem.

-------------------------

