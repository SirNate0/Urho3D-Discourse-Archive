rogerdv | 2017-01-02 00:58:45 UTC | #1

I found that problem while trying to import some meshes, seems that the editor or the importer cant properly handle the file path if it contains spaces, is that correct or Im doing something wrong?

-------------------------

cadaver | 2017-01-02 00:58:45 UTC | #2

When you have paths with spaces, they should be wrapped in double quotes when being given to the AssetImporter utility command line. The editor should handle that automatically when you use the import menu commands.

For example, I tested an import of a model from the directory "D:\Docs\Sample Collada Files" into an Urho3D checkout located at "D:\Projects\Urho 3D" (space deliberately added) and that worked. What is the exact operation that's failing for you and what are the paths involved?

-------------------------

