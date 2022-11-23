Leith | 2019-08-08 15:01:17 UTC | #1

I have a CodeBlocks project on Linux that uses Urho3D::File to try to load xml UI and Scene files from a (non-resource) relative path - if not found, it dumps a hardcoded copy in the working directory.

My project has a "Bin" folder, that acts as root. Working directory for both release and debug builds are set to that folder - it contains Data and CoreData and so on... so far, so good.

If I run the Release version of the app, I get my xml files dumped in the Bin folder - the working directory. All good.

But if I run the Debug version, I get my xml files dumped in the Project Root folder - not the working directory.

Whose fault is this? Is this a "feature" of CodeBlocks, or Urho? Seems like Urho is not at fault?

-------------------------

throwawayerino | 2019-08-08 22:52:13 UTC | #2

In my visual studio my project can't read/write by default - I have to find it and run it out of the IDE
try executing it out of the IDE maybe? It's been a while since I've used code blocks but I'm sure there's a setting somewhere

-------------------------

George1 | 2019-08-08 23:09:28 UTC | #3

Like throwawayerino is saying.  I think there is an option to set your target path in Codeblock.  If it doesn't have it, you can throw it away.

-------------------------

Leith | 2019-08-09 05:37:31 UTC | #4

It turns out to be caused by or at least directly related to GDB - although the arguments that codeblocks passes to GDB appear to be correct... strange :slight_smile:

When I use FileSystem::GetProgramDir to generate an absolute filepath, the issue disappears.

-------------------------

