sabotage3d | 2017-01-02 01:06:31 UTC | #1

Is it currently possible to override materials inside XML Scene like SetShaderParameter in AngelScript or C++. 
It would be quite convenient for instancing overrides sharing the same material. I guess it won't be efficient to create new material per instance ?

-------------------------

cadaver | 2017-01-02 01:06:31 UTC | #2

There's primitivewaste's per-object shader parameters branch, but it hasn't been touched in a while, or been requested for merging.

The scene's inbuilt loading only handles model components referring to existing materials, not modifying them. For now you could make a postprocessing step, where for example node variables are used to override shader parameters. (When override is defined, clone the original material and set parameters.)

If you're concerned of efficiency, you should use the minimum number of materials possible, which means detecting the situation where several objects have their material overridden in the same way. One example: object color, you could make a hash map key of the original material and the override color, and detect duplicates by seeing if the key already exists.

-------------------------

sabotage3d | 2017-01-02 01:06:31 UTC | #3

Thanks cadaver,
What is the syntax for custom variables in an XML scene is there a convention ?
For example diffuse color, specular color.

-------------------------

cadaver | 2017-01-02 01:06:31 UTC | #4

Try creating node variables in the editor, saving the scene, and looking at the XML output. Warning: as it's a VariantMap where the node vars are held, you don't get string keys, but stringhash keys, so you likely have to do a mapping back to strings on your own, or invent your custom encoding, for example stuff all the parameters inside a single string.

Materials themselves use MatDiffColor for the diffuse color and MatSpecColor for the specular.

-------------------------

sabotage3d | 2017-01-02 01:06:31 UTC | #5

Thanks cadaver,I will try that.
Any plans for merging the branch that you mentioned ?

-------------------------

cadaver | 2017-01-02 01:06:32 UTC | #6

I believe the initiative should come from the author. I wouldn't be comfortable taking potentially abandoned work into the master on my own.

-------------------------

