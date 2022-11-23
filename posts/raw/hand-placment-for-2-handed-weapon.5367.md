GodMan | 2019-07-30 00:22:13 UTC | #1

I have an AI that use a two handed weapon. I have the weapon attached to his left hand by using the below code.

	handBoneNodeAI = jackNode->GetChild("#left_hand_weapon", true);
	AnimatedModel* hammer = handBoneNodeAI->CreateComponent<AnimatedModel>();
	hammer->SetModel(cache->GetResource<Model>("Models/hammer.mdl"));
	hammer->SetMaterial(cache->GetResource<Material>("Materials/hammer.xml"));

The only issue it that when he swings the two handed weapon I'm not sure how to tell his right hand to stay with a marker set on the hammer, like and IK Joint for his right hand.

-------------------------

Modanung | 2019-07-30 00:52:18 UTC | #2

@TheComet is our IK expert.

-------------------------

GoldenThumbs | 2019-07-30 04:05:29 UTC | #3

Was gonna say Inverse Kinematics are made for these kinds of situations.

-------------------------

GodMan | 2019-07-30 15:04:10 UTC | #4

Is this in the samples?

-------------------------

Modanung | 2019-07-30 17:54:28 UTC | #5

Have you seen *sample 45*?

-------------------------

TheComet | 2019-07-30 22:04:55 UTC | #6

The IK components should be of use to you. See here for an overview: https://urho3d.github.io/documentation/1.7/_i_k.html

If you have any questions or need help getting it to work we're happy to help!

-------------------------

GodMan | 2019-07-30 23:23:13 UTC | #7

Okay thanks guys. I will look at sample 45 as well.

-------------------------

Leith | 2019-07-31 06:50:33 UTC | #8

Hi, GodMan!

I recently dealt with this issue, it involved a two-handed axe attack.. and a solution came about rather accidentally...
I got around this issue without using IK on the arms.
Here's a brief description of how I achieved it..

I created a locator node as a child of one of the hands.
I attached my weapon to that node, and used it to orient and position the weapon relative to the hand.
Thereafter, no matter what animation was happening, the weapon would be glued to that hand...
For two handed attacks, I used animations that suggest both hands become attached to the weapon, but they are simply crafted to appear so - it's visually plausible, and cheaper / more stable than IK.

"If the hands are oriented and positioned appropriately during animation, and the axe is glued to one of the hands, then the axe will naturally follow the hand to which it is truly attached"

I had some fun swapping out the axe for a teapot, the Urho Fish model, and various other things - the same attack animation, where the hands come together, we swing, then the hands come apart, one attack animation, worked for any number of weapons we could potentially use in a two handed attack.

By all means, try IK, but be warned there are some caveats with respect to our current implementation of IK, including that Scale in the node hierarchy and/or animations causes crazy things to happen to the IK and to its debugdrawing as well.

-------------------------

GodMan | 2019-07-31 19:31:02 UTC | #9

@Leith I have done that in the past just like you did, but this won't work in this case because the hammer handle is pretty long so you can see the AI's right hand is off when he swings the hammer. It's the gravity hammer from halo.

-------------------------

Leith | 2019-08-01 06:41:17 UTC | #10

Fair enough!:) 
If you need accurate hand placement, you have two options - one is to use IK (I recommend sticking with two-bone solvers as they seem to be both fastest and most stable), the other is to adjust your animations, using an imposter axe handle object to model what will happen at runtime. That of course means that the animation is tied to that weapon, but in practice I tend to find that is the relationship we end up with anyway.

-------------------------

George1 | 2019-08-01 06:54:01 UTC | #11

Another idea

Attach two nodes to the weapon if two handed is needed.
Attached a node to the hand where the weapon will be attached to.   

Attach one of the node on the weapon to one of the hand.

Next do ik on the second hand to the second node on the weapon. This way less chance of error.

-------------------------

Leith | 2019-08-01 06:59:29 UTC | #12

For IK, you're going to need two attachment points, but for a dedicated animation you only need one.
IK is a more flexible solution, when applied after animation as a corrective measure, and my experiences using IK for foot placement have generally been positive... yes you have a point, you really only need IK on the second hand, given the first hand is already attached...

-------------------------

Ka-Wiz | 2019-08-01 15:06:20 UTC | #13

I studied how things worked in Chivalry: Medieval Warfare for awhile when I was working on a sword game. Their (amazing) animations are baked in the 3D software using the technique Leith is describing, and thus different for every class of weapon (but not every weapon)

Because of the possible errors in IK, I think baking is the way to go. It's really a choice of where you want your work to be, in content generation (3D) or coding (IK). Generally I think a baked animation is more likely to look good, but it's also really hard to animate well if you're not experienced in it (another lesson from that sword project...)

-------------------------

GodMan | 2019-08-01 21:55:37 UTC | #14

Thats actually what I am doing. I have already added a marker for the AI's right hand to the hammer.

-------------------------

Leith | 2019-08-02 06:08:51 UTC | #15

Here's a quick video that shows a two handed attack animation that I added a weapon to - no ik was used (including the feet! I extracted motion data from the animation), and I was able to convincingly swap out the weapon for new, unintended ones
It's not new work, despite the name...
<https://www.dropbox.com/s/1r3z9xdi0293ecv/WIP_Latest.mp4?dl=0>

-------------------------

