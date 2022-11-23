Leith | 2019-01-19 01:40:41 UTC | #1

I've been toying with a simple gamestate manager that basically has three states.

The first GameState is "IntroGameState", a SplashScreen is displayed, and a Sound is played - the SoundSource has Autoremove Component enabled. I listen for the E_SOUNDFINISHED event, which triggers a state change to the "Main Menu" state.

This state sets up some UI, dumps the current scene to XML File, and then sits there spinning its wheels, and displaying the FPS... So I manually quit the application.

Now, when I investigate the XML Scene File, I can see the SoundSource Component is still attached to my IntroGameState's container node.

Is this a bug?


		<node id="3">
			<attribute name="Is Enabled" value="false" />
			<attribute name="Name" value="GameIntroSample" />
			<attribute name="Tags" />
			<attribute name="Position" value="0 0 0" />
			<attribute name="Rotation" value="1 0 0 0" />
			<attribute name="Scale" value="1 1 1" />
			<attribute name="Variables" />
			<component type="GameIntroSample" id="1">
				<attribute name="My Value" value="666" />
			</component>
			<component type="SoundSource" id="4">
				<attribute name="Sound" value="Sound;Sounds/Fanfare.wav" />
				<attribute name="Frequency" value="24000" />
				<attribute name="Autoremove Mode" value="Component" />
			</component>
		</node>


Ugh - nevermind, I found the answer in the Porting Notes for v1.5-1.6

Quote: " [SoundSource](https://urho3d.github.io/documentation/1.6/class_urho3_d_1_1_sound_source.html) autoremove functionality is deprecated and will be removed in the future. The SoundFinished event can be used instead to react to playback finishing and to perform the necessary action, for example to remove the sound component or its owner node."

It would be nice if the docs mentioned this too.

-------------------------

Modanung | 2019-01-19 08:31:58 UTC | #2

Ninja Snow War also contains an example of this.

-------------------------

weitjong | 2019-01-19 08:41:44 UTC | #3

[quote="Leith, post:1, topic:4837"]
It would be nice if the docs mentioned this too.
[/quote]

Yes, it does. Since release 1.6 the online doc contains this new section about audio events.
https://urho3d.github.io/documentation/1.6/_audio.html#Audio_Events

-------------------------

Leith | 2019-01-20 02:10:34 UTC | #4

The docs mention the sound finished event, but fail to mention deprecated functionality lurking in the API.
If we examine the SoundSource class documentation (auto-generated doxygen stuff), the deprecated functionality is described, with no mention of deprecation. This was a source of confusion for me - I would expect deprecated functionality to be clearly marked as such within the relevant docs, and not left as a footnote in an unrelated doc.

-------------------------

weitjong | 2019-01-20 02:48:02 UTC | #5

I understand your point. Our doc is quite spartan. But then again, at the same time I am already admiring the original author (Lasse) even got time and energy to have documented his pet project so well in the first place after all things considered. Contribution is welcome to improve it better of course.

-------------------------

Leith | 2019-01-20 11:29:42 UTC | #6

I would love to contribute to the physics and networking parts of the documentation in particular.
I am a long term user of Box2D, Bullet and RakNet (which I believe is the origin of Slike, which we recently moved onto). I will be soon working with some or all of these systems, and I expect to write some notes, which could act as a foundation for more thorough documents, outside of the doxygen stuff. I'd just like to see (our?) home page not have any missing links, that would make me happy.
When I have something I think is worth contributing (with respect to docs), I will bring it to you first, as you seem to be the defacto lead around here. 
I'm here to help (oh god, yes I worked there, that nameless fruit company).

-------------------------

