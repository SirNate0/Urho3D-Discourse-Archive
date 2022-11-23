JimMarlowe | 2017-01-02 01:05:55 UTC | #1

The PackageFile class uses ToLower() to list and use the contents of the package file. On the Linux/RPI/OSX platforms, the capitalization of files has meaning, and it makes it difficult to retrieve assets from the (mounted) package with a cache.GetResource(). Is this a feature or a bug?

-------------------------

cadaver | 2017-01-02 01:05:55 UTC | #2

Welcome to the forums.

The purpose of tolower in PackageFile is to emulate the case-insensitiviness of Windows filesystem. Can you elaborate on how it makes operation difficult? I wouldn't recommend making e.g. Explosion.wav and explosion.wav two different resources, due to possibility of mistyping and incompatibility with WIndows.

-------------------------

JimMarlowe | 2017-01-02 01:05:55 UTC | #3

Tell the windows platform to cowboy up  :smiley: 
This is my use case. I have created a scene, a map for a game, like I would expect users to be able to do. It is constructed to include all files to successfully render the scene, there are Materials, Models, Textures, Scenes. The filenames are mixed case, much like what exists in the Data and CoreData directories. I take my collection, and use PackageTool to make a pak file. Then in the game, the open the pak file, use Packagefile.GetEntryNames() to find out the names of the scene xml files, and make the call cache.GetResource("XMLFile", "MyMap/Scenes/MyScene.xml" ); On windows, it loads without issue, but will fail on most other platforms. Replicating a pak file from a windows server would be a latent problem for non-windows clients.
I can make all directory and file names lowercase, but it would be an high cost to using PackageFiles, when other parts of the system are still case sensitive. Wouldn't the windows platform be unaffected if you didn't lowercase everything?

-------------------------

cadaver | 2017-01-02 01:05:55 UTC | #4

Thanks, understood the problem now. GetEntryNames() can be made to return the mixed-case names, as the data exists in the package file itself in the correct form. As a bonus, it's also possible to make the case-sensitivity behavior depend on the build platform.

-------------------------

cadaver | 2017-01-02 01:05:55 UTC | #5

ToLower is removed in the master branch now, meaning you should get accurate entry names. A fallback case-insensitive search is performed on Windows platform only.

-------------------------

JimMarlowe | 2017-01-02 01:05:56 UTC | #6

Thanks.

-------------------------

