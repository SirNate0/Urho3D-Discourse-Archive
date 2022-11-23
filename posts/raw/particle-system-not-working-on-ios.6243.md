jzpekarek | 2020-07-05 23:31:37 UTC | #1

After upgrading (form version 1.5) to the latest master branch, I'm now having problems with the particle system on iOS. I currently build my application for both iOS and Windows. The particle system on Windows is working fine (see the picture below of the rocket flames implemented as a particle system).

![image|598x500](upload://ia6DRU47abAyINoDJRuHOF1p4NE.jpeg) 

On iOS, the particles either draw much, much smaller as shown below. 

![image|690x486](upload://ncs4G4CzxCmvE0l1uUFZVDYcs9u.jpeg) 

Or when I change the angle of view, sometimes like below:
![image|690x486](upload://bTDUp9uorlYQp25BGFjSUzpXzXX.jpeg) 

The particle file is shown below. Any ideas what might be wrong here (seems like a bug since it works on Windows, and used to work on iOS in version 1.5). EDIT - I went back to a 1.6 version that I built to help debug another regression on iOS, and found that the particle systems wasn't working on iOS for my example in 1.6 either (so I'm assuming it is a regression from 1.5 to 1.6).

    <?xml version="1.0"?>
    <particleeffect>
	<material name="Materials/Particle.xml" />
	<numparticles value="100" />
	<updateinvisible enable="false" />
	<relative enable="false" />
	<scaled enable="true" />
	<sorted enable="false" />
	<animlodbias value="0" />
	<emittertype value="Box" />
	<emittersize value="0.3 0 0" />
	<direction min="-0.1 0.5 -0.1" max="0.1 4 0.1" />
	<constantforce value="0 2 0" />
	<dampingforce value="1" />
	<activetime value="0" />
	<inactivetime value="0" />
	<emissionrate min="80" max="80" />
	<particlesize min="0.14 0.14" max="0.5 1" />
	<timetolive min="0.1" max="0.4" />
	<velocity min="6" max="8" />
	<rotation min="0" max="0" />
	<rotationspeed min="0" max="0" />
	<sizedelta add="0" mul="0.8" />
	<colorfade color="0.3 0.4 0.7 1" time="0" />
	<colorfade color="0.7 0.5 0.2 1" time="0.1" />
	<colorfade color="0 0 0 0" time="0.4" />
    </particleeffect>

-------------------------

Modanung | 2020-07-07 16:16:40 UTC | #2

Seems like something worth opening an issue on GitHub for.

-------------------------

jzpekarek | 2020-07-08 04:11:12 UTC | #3

Since I have both a Windows and iOS build that I work with, I'll spend some time stepping through the code in both builds to see if I can figure out where the iOS build is going wrong.

-------------------------

jzpekarek | 2020-07-12 02:29:52 UTC | #4

I figured out the problem, mostly operator error on my part. After stepping through the creation of the vertex buffers on both Windows and iOS, and finding that there was no difference, I realized that the main difference between the two is that they use different shaders. On the Windows build, I had updated to the newer shaders, but I apparently forgot to do the same thing for the iOS build, so I was using shader code from version 1.5 with the latest master version, and changes in the billboarding weren't being handled correctly. Anyway, maybe this post will help someone else out that makes the same mistake!

-------------------------

