Uid351324 | 2017-03-17 19:51:52 UTC | #1

Hello,
I was trying to make simple detector for character, that already has rigidbody, by adding child node with trigger rigidbody and  subscribing to event E_NODECOLLISIONSTART. Scene looks like this:
```
<node id="4">
	<component type="CollisionShape" id="8" />
	<component type="RigidBody" id="18">
	</component>
	<node id="14">
		<component type="CollisionShape" id="37" />
		<component type="RigidBody" id="38">
			<attribute name="Is Trigger" value="true" />
                </component>
        </node>
```
The problem is that trigger always stay in same place, do I need to add some constraint for child node, manually change position of trigger based on parent node, or better option drop trigger  idea and use ray cast?

-------------------------

Modanung | 2017-03-17 19:47:59 UTC | #2

Try setting the trigger body to kinematic.

-------------------------

Uid351324 | 2017-03-17 19:46:04 UTC | #3

Thank you, it worked, now I fill like an idiot.

-------------------------

Modanung | 2017-03-17 20:08:53 UTC | #4

Don't: You just got wiser! ;)

..and welcome to the forums, btw. :confetti_ball:

-------------------------

