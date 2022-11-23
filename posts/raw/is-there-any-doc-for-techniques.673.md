abcjjy | 2017-01-02 01:02:02 UTC | #1

Urho3d comes with a bunch of built-in techniques. Many of them are named as "Diff*". By reading the document about render path, material and technique, I basically understand what they are used for. However, I still don't know the meaning of each built-in techniques. Where can I find a doc which has some high-level descriptions on builtin techniques? Or what is the recommended way for learning these techniques? 

By the way, what is the meaning of "Diff" in the techniques' file names?

-------------------------

JTippetts | 2017-01-02 01:02:02 UTC | #2

Diff means diffuse, meaning it uses a diffuse texture. You can infer most of the techniques from the names, once you know what the various abbreviations mean. Most of the techniques are permutations on a given set of concepts. Diff uses a diffuse texture. Spec uses a specular texture. Normal uses a normal map texture. AO uses an AO texture. Add uses additive blending. Alpha uses alpha blending. Emissive uses an emissive texture. Unlit uses no lighting. VCol uses vertex colors. And so on.

-------------------------

