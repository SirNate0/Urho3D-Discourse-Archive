Mike | 2017-01-02 00:59:21 UTC | #1

I have some trouble with SoundSource component.
For example, adding a SoundSource in sample 11_Physics.lua:

[code]
    scene_:CreateComponent("Octree")
    scene_:CreateComponent("PhysicsWorld")
    scene_:CreateComponent("DebugRenderer")

	-- Create a sound channel
	local musicNode = scene_:CreateChild("Music1")
	local source = musicNode:CreateComponent("SoundSource")
	local music = cache:GetResource("Sound", "Music/Ninja Gods.ogg")
	source.soundType = SOUND_AMBIENT
	music.looped = true -- Loop play
	source:Play(music)
	print(source.sound)
[/code]
source.sound returns nil and source path is not created in the saved xml file when pressing 'F5' key (no "Sound" attribute).
Same issue with AngelScript.

I've tried to create the same SoundSource in the Editor then save it and it works fine:
[code]
source path is saved as
<attribute name="Sound" value="Sound;Music/Ninja Gods.ogg" />
[/code]

-------------------------

cadaver | 2017-01-02 00:59:21 UTC | #2

It was an issue of compressed sound resource ref not being serialized, as the sound_ variable was not assigned in that case. Should be fixed now.

-------------------------

Mike | 2017-01-02 00:59:21 UTC | #3

Works great, as usual  :stuck_out_tongue:

-------------------------

