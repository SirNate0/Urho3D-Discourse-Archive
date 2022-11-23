Leith | 2019-04-09 08:29:17 UTC | #1

I have a question about something simple - the world position of objects. It sounds simple, yes?

I have a 3D animated model, here's how it slots into the game scene:
[quote]
		<node id="7">
			<attribute name="Is Enabled" value="true" />
			<attribute name="Name" value="Jack" />
			<attribute name="Tags" />
			<attribute name="Position" value="0 1 0" />
			<attribute name="Rotation" value="1 0 0 0" />
			<attribute name="Scale" value="1 1 1" />
			<attribute name="Variables" />
			<component type="KinematicCharacterController" id="13">
				<attribute name="Animation Descriptors" value="PlayerAnimations.xml" />
			</component>
			<node id="8">
				<attribute name="Is Enabled" value="true" />
				<attribute name="Name" value="Adjustment" />
				<attribute name="Tags" />
				<attribute name="Position" value="0 0 0" />
				<attribute name="Rotation" value="-4.37114e-08 0 1 0" />
				<attribute name="Scale" value="0.01 0.01 0.01" />
				<attribute name="Variables" />
				<component type="SoundListener" id="10" />
				<component type="AnimatedModel" id="11">
					<attribute name="Model" value="Model;Models/PatientZero/TestModel.mdl" />
[/quote]

So, in the DelayedStart method, I note the starting world position of the node that owns KinematicCharacterController - it reports the world position as <0,1,0>
And in the Update method, I detect the difference between the current world position of (owner node), and the starting position. Current world position is <0,8,4>, yet the animation controller should not have run yet - this is the update method of the first frame - also physics has not yet run - so why has my node moved?
Could it be that physics is running one frame before update, and doing my head in?

-------------------------

Leith | 2019-04-10 06:06:14 UTC | #2

I solved this one - my model's node was being teleported to match that of the character's physics hull, which had a hardcoded starting position.

-------------------------

