Leith | 2019-03-25 11:57:00 UTC | #1

I'm using Mixamo as an example here, but this question is really a lot more general than that.

Mixamo lets you choose to export most animations "in-place". This effectively eliminates root motion translations in the X and Z planes. This is fine for most cases - for example in a walk animation, we still expect the hips to move up and down a bit. But for jumping, falling, prone, and many other cases, we typically need to lock down the translation in Y as well.

Doing this in Blender (or Maya, or MilkShape, etc.) is possible, but repetitive, tedious, and somewhat error-prone. It would be really awesome if our AssetImporter had the ability to cancel root motions on given major axes, and preferable, for some specific Named Bone / subroot node (such as Hips).

How do you guys deal with eliminating unwanted root motions in animations? What do you recommend?

-------------------------

smellymumbler | 2019-03-25 15:00:50 UTC | #2

https://www.youtube.com/watch?v=WXw73tBd1PM

You can follow that, create your own workflow that you feel comfortable with, then script it out with Python. I don't see why the engine should be responsible for cleaning up arcane workflow steps when any DCC tool does the job.

-------------------------

Leith | 2019-03-26 06:32:06 UTC | #3

Hey, thanks for the reply!

Python (or MEL) scripting does sound like a reasonable way to fly - I'll definitely look into it. For a handful of animations, that sounds quite reasonable. One problem I foresee is that my animation count is growing exponentially with the number of unique characters, and so it's likely that I will at some point turn my attention to extending the AssetImporter console application, which is highly suited to batched execution ;)

-------------------------

smellymumbler | 2019-03-26 13:46:40 UTC | #4

You can run Blender from the command line and auto-execute your scripts. You can also use Blender as a module:

https://blender.stackexchange.com/questions/1365/how-can-i-run-blender-from-command-line-or-a-python-script-without-opening-a-gui

-------------------------

Leith | 2019-03-27 06:47:18 UTC | #5

Here's the list of animations for just the player character - of course we expect the list to be larger for the player than for non player characters, and this is far, far from complete...
<<?xml version="1.0">
<Character Name="Patient Zero">

    <Comment> Name of character root node (for manipulation purposes) </Comment>
    <RootNode Name="Adjustment" />
   
    <Comment> Names of character's animations </Comment>
    <Descriptor Name="Models/PatientZero/Idle.ani"           Looping="true"  LayerID="0"> IDLE                    </Descriptor>
    <Descriptor Name="Models/PatientZero/WalkForward.ani"    Looping="true"  LayerID="0"> WALK FORWARDS           </Descriptor>
    <Descriptor Name="Models/PatientZero/WalkBackwards.ani"  Looping="true"  LayerID="0"> WALK BACKWARDS          </Descriptor>
    <Descriptor Name="Models/PatientZero/WalkLeft.ani"       Looping="true"  LayerID="0"> WALK LEFT               </Descriptor>
    <Descriptor Name="Models/PatientZero/WalkRight.ani"      Looping="true"  LayerID="0"> WALK RIGHT              </Descriptor>
    <Descriptor Name="Models/PatientZero/Jump.ani"           Looping="true"  LayerID="0"> JUMPING                 </Descriptor>
    <Descriptor Name="Models/PatientZero/Falling.ani"        Looping="true"  LayerID="0"> FALLING                 </Descriptor>
    <Descriptor Name="Models/PatientZero/CrouchIdle.ani"     Looping="true"  LayerID="0"> CROUCHED IDLE           </Descriptor>
    <Descriptor Name="Models/PatientZero/CrouchForward.ani"  Looping="true"  LayerID="0"> CROUCHED WALK FORWARDS  </Descriptor>
    <Descriptor Name="Models/PatientZero/CrouchBackward.ani" Looping="true"  LayerID="0"> CROUCHED WALK BACKWARDS </Descriptor>
    <Descriptor Name="Models/PatientZero/CrouchLeft.ani"     Looping="true"  LayerID="0"> CROUCHED WALK LEFT      </Descriptor>
    <Descriptor Name="Models/PatientZero/CrouchRight.ani"    Looping="true"  LayerID="0"> CROUCHED WALK RIGHT     </Descriptor>
    <Descriptor Name="Models/PatientZero/CrouchJump.ani"     Looping="true"  LayerID="0"> CROUCHED JUMPING        </Descriptor>
    <Descriptor Name="Models/PatientZero/MeleeAttack.ani"    Looping="false" LayerID="0"> CROWBAR OF DEATH        </Descriptor>
    <Descriptor Name="Models/PatientZero/PickupItem.ani"     Looping="false" LayerID="0"> PICK THAT SHIT UP       </Descriptor>

    <Comment> Names of bones for Foot-IK </Comment>
    <Bone Name="Left Foot"  Value="LeftFoot" />
    <Bone Name="Right Foot" Value="RightFoot" />
    <Bone Name="Pelvis"     Value="Hips" />

    <Comment> TODO: Add ragdoll physics descriptors here </Comment>
 

</Character>>

I'm not sure I want to execute Blender that many times for every game character, when it comes time to polish. But I guess I could live with it. The assimp-based AssetImporter app is a lot smaller, and loads and runs a lot faster (no graphic interface). It's still looking like the better candidate for batching stuff, but I'm lazy, and doing it "your way" is certainly less work for me :slight_smile:

-------------------------

dertom | 2019-03-27 08:00:42 UTC | #6

May I ask where you get your animations from? Some kind of (free/commercial?) mocap-library? Or are you capturing even on your own?

-------------------------

Leith | 2019-03-27 08:15:11 UTC | #7

My question was general, but I used mixamo.com as an example ;)
The animations could have come from anywhere that Assimp can support.

-------------------------

Leith | 2019-03-29 03:14:09 UTC | #8

Basically, I want to eliminate root motion in the Y axis during a Jump animation - the reason is that I use a Dynamic Character Controller, so I expect translation in Y to come from the character's outer physics hull, and not from the animation in question.

I fired up Blender, and tried removing the keyframes on the "Y Translation" of the "Hips".
In Blender, the result was what I wanted, so I exported the animation to FBX, and imported the fbx into Urho (via AssetImporter app). The resulting jump animation appeared to freeze half way through playback - apparently just deleting all the keys in some channel, and so the channel itself, leads to corrupt assets.

I then tried dealing with this problem in code - at the beginning of a Jump, I note the local translation of the hips in Y axis, and during a Jump, I force the local translation of the hips to that value, effectively eliminating the unwanted root motion - it works.
I'm beginning to feel that eliminating unwanted root motions in code is more flexible than editing the assets themselves...

-------------------------

