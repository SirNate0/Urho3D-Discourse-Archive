TheComet | 2017-01-02 01:10:00 UTC | #1

I was tracking down a bug when I came across this section of code in btDescreteDynamicsWorld.cpp:454:

[code]		for (int i=0;i<clampedSimulationSteps;i++)
		{
            // Urho3D: apply gravity and clear forces on each substep
            applyGravity();
			internalSingleStepSimulation(fixedTimeStep);
			synchronizeMotionStates();
            clearForces();
		}
	} else
	{
		synchronizeMotionStates();
	}[/code]

When comparing this to bullet's official repository, we see something different:

[code]		applyGravity();

		for (int i=0;i<clampedSimulationSteps;i++)
		{
			internalSingleStepSimulation(fixedTimeStep);
			synchronizeMotionStates();
		}
	} else
	{
		synchronizeMotionStates();
	}

	clearForces();[/code]

applyGravity() and clearForces() are outside of the for loop. I'm interested why there is a discrepancy here.

-------------------------

Enhex | 2017-01-02 01:10:01 UTC | #2

Are you comparing Urho's Bullet to Bullet's HEAD version?
AFAIK Urho's Bullet is older version.

-------------------------

TheComet | 2017-01-02 01:10:02 UTC | #3

That doesn't matter because the code I speak of was modified explicitly by an Urho3D developer. I'm wondering what the exact reasoning behind this change was.

-------------------------

Enhex | 2017-01-02 01:10:02 UTC | #4

Tried to log the git repo but it only goes back to a version which already had the change (Commit: 02512cecf928c89863d1c5ec6874e5f4abcfaeb6).

-------------------------

weitjong | 2017-01-02 01:10:02 UTC | #5

[quote="Enhex"]Tried to log the git repo but it only goes back to a version which already had the change (Commit: 02512cecf928c89863d1c5ec6874e5f4abcfaeb6).[/quote]

Use the git log with "--follow" option.

-------------------------

Enhex | 2017-01-02 01:10:02 UTC | #6

Commit: ee668a791f5842180d139f60fe4fd8f8c47c2456 [ee668a7]
Clear forces after each physics substep so that rendering framerate doesn't affect code which calls ApplyForce() / ApplyTorque().

Commit: 20c63654e374f8dbc00ef13ddd0b6f717555d42c [20c6365]
Fixed gravity being incorrectly applied if framerate is low.

-------------------------

