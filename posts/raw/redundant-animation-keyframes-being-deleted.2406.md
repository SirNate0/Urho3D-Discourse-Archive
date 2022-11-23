StarK | 2017-01-02 01:15:13 UTC | #1

I have noticed that the animation importer deletes animation channels or redundant animation key frames on imported models. I understand this is a necessary  animation optimization, but in a case where I reference animations from other models that are posed differently initially, I only get animation from the bone nodes that had some kind of transformation. In other words It won't allow for static pose to pose animation. I have tried to find where exactly this is happening but haven't had any luck - Are there existing settings to toggle the key frame cleanup on and off? Can anyone tell me where exactly this is happening? Thanks!

-------------------------

Lumak | 2017-01-02 01:15:14 UTC | #2

Use AssetImporter from command line with the "-s" option:
[quote]
            "-s <filter> Include non-skinning bones in the model's skeleton. Can be given a\n"
            "            case-insensitive semicolon separated filter list. Bone is included\n"
            "            if its name contains any of the filters. Prefix filter with minus\n"
            "            sign to use as an exclude. For example -s \"Bip01;-Dummy;-Helper\"\n"

[/quote]

To include all, just pass "-s"

-------------------------

