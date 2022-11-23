syjgin | 2017-01-02 01:04:42 UTC | #1

I must create tool, which can load and display 3D model from command line argument, which will be filesystem path. So, maybe you know:
1)It's possible to load model from absolute path in Urho?
2)Can Model class load model in .obj format, or I must do some conversion in runtime to Urho's internal format?

-------------------------

cadaver | 2017-01-02 01:04:42 UTC | #2

Urho's engine runtime itself does not contain code to load anything else than the .mdl internal model format.

Take a look at the AssetImporter tool included in Urho build, which uses assimp library to load various model files and save Urho .mdl's. Some options that you have:
- Invoke AssetImporter in your utility
- Copy the relevant code from AssetImporter into your utility and link to assimp.

-------------------------

godan | 2017-01-02 01:04:44 UTC | #3

You can also check out Sample 34 - Dynamic Geometry. There is a some code there that demonstrates how to create a model at runtime. You'll have to write some code to parse the obj file, though. Fortunately, this is [url=https://www.google.ca/search?q=c%2B%2B+obj+parser&rlz=1C1ASUC_enCA588CA588&oq=c%2B%2B+obj+parser&aqs=chrome..69i57.1847j0j7&sourceid=chrome&es_sm=122&ie=UTF-8]well documented[/url].

-------------------------

