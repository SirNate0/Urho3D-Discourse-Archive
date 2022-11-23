dragonCASTjosh | 2017-01-02 01:13:17 UTC | #1

As part of my PBR rendering i was trying to retain importance sampled IBL for ease of use whilst still allowing for pre-filterered for higher performance. ideally id want to do this without forcing the users to add the pre-filtered split-sum texture manually, one solution i came up with was possibly having a split-sum render path that loads this texture as part of the xml although im not sure if this is possible. i didnt want to add the code manually as it will be a very small use case.

-------------------------

cadaver | 2017-01-02 01:13:17 UTC | #2

If the texture is a disk resource, you can refer to it as usual. Example: messed up deferred lighting by using the mushroom texture instead of G-buffer albedo map.

[code]
    <command type="lightvolumes" vs="DeferredLight" ps="DeferredLight">
        <texture unit="diffuse" name="Textures/Mushroom.dds" />
        <texture unit="normal" name="normal" />
        <texture unit="depth" name="depth" />
    </command>
[/code]
If it's something else you need you may need to make C++ engine changes.

Note that in scene passes materials might overwrite the texture unit assignment, and that cannot be "recovered" from, since the renderpath command defined textures are only set once as the command execution begins.

-------------------------

dragonCASTjosh | 2017-01-02 01:13:17 UTC | #3

[quote="cadaver"]If the texture is a disk resource, you can refer to it as usual. Example: messed up deferred lighting by using the mushroom texture instead of G-buffer albedo map.

[code]
    <command type="lightvolumes" vs="DeferredLight" ps="DeferredLight">
        <texture unit="diffuse" name="Textures/Mushroom.dds" />
        <texture unit="normal" name="normal" />
        <texture unit="depth" name="depth" />
    </command>
[/code]
If it's something else you need you may need to make C++ engine changes.

Note that in scene passes materials might overwrite the texture unit assignment, and that cannot be "recovered" from, since the renderpath command defined textures are only set once as the command execution begins.[/quote]

awesome, this is what i was looking for

-------------------------

