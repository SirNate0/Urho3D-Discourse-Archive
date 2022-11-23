mcra3005 | 2017-01-02 01:10:27 UTC | #1

Hi All,

I noticed you have the Urho3DPlayer, but how do you encript your .as code so know one can grab it without your permission.
Any ideas ??

Thanks.

-------------------------

1vanK | 2017-01-02 01:10:27 UTC | #2

[quote="mcra3005"]Hi All,

I noticed you have the Urho3DPlayer, but how do you encript your .as code so know one can grab it without your permission.
Any ideas ??

Thanks.[/quote]

[code]ScriptCompiler.exe GameData/Scripts/*.as[/code]

-------------------------

Sir_Nate | 2017-01-02 01:10:34 UTC | #3

That should compile it to the angelscript byte code, which is probably enough, but true encryption would likely require an additional cryptography library and modifying Urho's resource/filesystem code to read from the outputs of that library (I think it's been discussed a little before on the forum in relation to 3d assets).

-------------------------

gawag | 2017-01-02 01:10:34 UTC | #4

It seems Urho can also add "packages" (archives?) as ressources: [urho3d.github.io/documentation/1 ... 9e44d69cf3](http://urho3d.github.io/documentation/1.5/class_urho3_d_1_1_resource_cache.html#a286aba429fd463fbc3eba29e44d69cf3)
Ogre had the feature of being able to read resources from encrypted .zip-archives. I guess that would be sufficient? Also for protecting game assets. Many games have some kind oi huge foo.data files with all of the game data in it. Would be a cool feature. Maybe make a feature request?

Maybe one can load "raw" files from an encrypted archive by himself and let Urho load that decrypted file from memory?

Edit: Doh! [topic1871.html](http://discourse.urho3d.io/t/packagefile-open-from-memory/1792/1) Someone made such a request already.

-------------------------

