hunkalloc | 2022-08-10 13:34:33 UTC | #1

I've noticed that the asset workflow around Urho seems to revolve around the AssetImporter tool, which uses Assimp for most of the process, and then spits out MDL or ANI. I've been curious about that flow and wondering if the engine supports custom model loaders without requiring conversions.

-------------------------

SirNate0 | 2022-08-10 17:24:07 UTC | #2

You can always write such importing code in your own application. Generating a Model is not that difficult, there's some example code on the forums and I believe in one of the samples. Loading another model format is merely filling in the appropriate data for the model based on the other file.

But what would be the advantage of doing this rather than converting with another application, especially when the importing process can take a significant amount of time?

-------------------------

hunkalloc | 2022-08-12 13:54:56 UTC | #3

I don't want to modify Assimp and I need to support old game data since I'm doing an engine re-implementation.

-------------------------

