MadGustave | 2021-10-19 05:09:02 UTC | #1

I downloaded latest version of Urho from git and couldn't import gltf/glb file with AssetImporter. It basically complains that file extension is not supported. I opened assimp code and this is gltf2.0 importer(this function check if given importer can read file):
```
bool glTF2Importer::CanRead(const std::string& pFile, IOSystem* pIOHandler, bool checkSig) const
{
    const std::string &extension = GetExtension(pFile);

    if (extension != "gltf" && extension != "glb")
        return false;

    if (checkSig && pIOHandler) {
        glTF2::Asset asset(pIOHandler);
        try {
            asset.Load(pFile, extension == "glb");
            std::string version = asset.asset.version;
            return !version.empty() && version[0] == '2';
        } catch (...) {
            return false;
        }
    }

    return false;
}
```
I guess it's a bug, it doesn't return true if extension match, i basically added
```
    else {
        return true;
    }
```
after ` if (checkSig && pIOHandler) {` block and now it can import gltf(tho no material imported correctly, but i guess it's always the case?)

-------------------------

MadGustave | 2021-10-19 08:18:58 UTC | #2

Looks like it's old version that doesn't support animations either. Does anybody has fixes for gltf import?

-------------------------

Eugene | 2021-10-19 11:03:36 UTC | #3

I personally consider AssImp as dead end "equally bad for everything"-kind of solution.
I just import GLTF directly via `tinygltf` and convert it to `Model`/`Scene`. It's not an easy task, but it's very doable. And, unlike Assimp, I can actually fix problems when I encounter them.

![image|304x160](upload://vNvNx6UUm6RIASFpPIiqaSIiC7B.png)

-------------------------

elix22 | 2021-10-19 10:53:52 UTC | #4

I have a more recent Assimp library in below branch
I  up-merged it 2 years ago due to some GLTF issues (don't remember which)  ,
Check if it solves your issues.
I might upmerge to the latest version in the near future once I will have some free time (just follow my master branch)

https://github.com/elix22/Urho3D/tree/dev-flimper

-------------------------

MadGustave | 2021-10-19 17:52:43 UTC | #5

Can you share code of how you convert it with tinygltf?

-------------------------

Eugene | 2021-11-10 17:33:24 UTC | #6

My work is far from finished, so I don't have persistent link.
Here is temporary link to the [main](https://github.com/rokups/rbfx/blob/ek/gltf/Source/Urho3D/Utility/GLTFImporter.cpp) file of the importer and to the [model builder](https://github.com/rokups/rbfx/blob/ek/gltf/Source/Urho3D/Graphics/ModelView.cpp). This link will perish after I complete this task.

Update: here are permanent links
 https://github.com/rbfx/rbfx/blob/master/Source/Urho3D/Utility/GLTFImporter.cpp
 https://github.com/rbfx/rbfx/blob/master/Source/Urho3D/Graphics/ModelView.cpp

-------------------------

