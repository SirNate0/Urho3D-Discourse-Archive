smellymumbler | 2017-05-29 17:15:20 UTC | #1

I'm having some trouble porting some Unity scripts to Urho, but nothing really fancy. Could anyone point me to the right direction when it comes to the equivalence of these calls?

* Unity allows you to get the gravity from scripts via Physics.gravity.y, Physics.gravity.x, etc. What's the Physics object in Urho?
* What would be the equivalent of Mathf.Max?
* What would be the equivalent of Controller.transform? Can i get the X/Y/Z of a node? What about its velocity?
* Vector3.Scale. Is there something similar in Urho?
* Vector3.sqrMagnitude: https://docs.unity3d.com/ScriptReference/Vector3-sqrMagnitude.html

-------------------------

Eugene | 2017-05-29 15:59:16 UTC | #2

1. Something like physicWorld in AS, GetScene/GetComponent<PhysicWorld> in C++
2. Max?
3. Check Controller's code, there shall be something like RigidBody
4. *
5. LengthSquare or like this.

-------------------------

smellymumbler | 2017-05-29 16:13:05 UTC | #3

1. So, something like scene->GetComponent<PhysicsWorld>()->GetGravity().y_?
2. Max... ? max()?
3. I've checked the controller code, but what's the equivalent of the transform? myRigidBody->GetPosition().x_? 
4. Any vec3 * vec3 will multiply all the components of the vector?

-------------------------

smellymumbler | 2017-05-29 16:26:45 UTC | #4

Also, is there an equivalent of this? 

https://docs.unity3d.com/ScriptReference/Transform.TransformDirection.html

-------------------------

Modanung | 2017-05-29 17:11:42 UTC | #5

[quote="smellymumbler, post:4, topic:3175"]
Also, is there an equivalent of this?
[/quote]
That would be `Node::LocalToWorld`.

-------------------------

smellymumbler | 2017-05-29 17:14:38 UTC | #6

Thank you so much! :)

-------------------------

Modanung | 2017-05-30 06:44:43 UTC | #7

To use `Max()` you need to include `Math/MathDefs.h`
[quote="smellymumbler, post:3, topic:3175"]
Any vec3 * vec3 will multiply all the components of the vector?
[/quote]
[Yup](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Math/Vector3.h#L264-L265)

-------------------------

smellymumbler | 2017-05-29 21:33:39 UTC | #8

Thanks a lot for the info. There's another thing confusing me which is the fact that Unity has too global variables: Time.deltaTime and Time.time. 

https://docs.unity3d.com/ScriptReference/Time.html

It seems that Urho only has a deltaTime, that is called timestep and it's sent to all Update() functions. How do i get Time.time?

-------------------------

Modanung | 2017-05-29 21:47:09 UTC | #9

`GetSubsystem<Time>()->GetElapsedTime()` gives you the time in seconds the program has been running. Calling `GetSystemTime()` on the `Time` subsystem gives you the system time in msec.
In Urho3D time scales are set per scene.

-------------------------

smellymumbler | 2017-05-29 21:51:12 UTC | #10

What about the time since the beginning of the frame?

-------------------------

Modanung | 2017-05-29 21:54:15 UTC | #11

Well... the timestep is the amount of time since the last frame. Which means according to that measurement the current frame just started and has been lasting for about 0 seconds. Does that answer your question?

-------------------------

smellymumbler | 2017-05-29 22:24:26 UTC | #12

Not really... i thought that the timestep was the time in seconds it took to complete the last frame. Urho3D timestep = Unity Time.deltaTime. If that's not it, then timestep is the time since the frame started?

-------------------------

smellymumbler | 2017-05-30 02:27:45 UTC | #13

Is there an equivalent for https://docs.unity3d.com/ScriptReference/Vector3.ClampMagnitude.html?

-------------------------

Lumak | 2017-05-30 02:56:49 UTC | #14

[code]
Vector3 ClampMagnitude(const Vector3 &vec, float maxLen)
{
    Vector3 retVec = vec;

    if (retVec.Length() > maxLen)
        {
            retVec = retVec.Normalized() * maxLen;
        }

        return retVec;
}


[/code]

-------------------------

smellymumbler | 2017-05-30 03:54:20 UTC | #15

Thanks! Is it possible to extend the original Vector3 class with such additions? Monkey-patch it?

-------------------------

Modanung | 2017-05-30 05:54:39 UTC | #16

[quote="smellymumbler, post:15, topic:3175"]
Is it possible to extend the original Vector3 class with such additions?
[/quote]
You could maintain your own fork of the engine or send in a pull request. For consistency's sake I'd name this function `ClampLength`.

-------------------------

smellymumbler | 2017-05-30 13:11:21 UTC | #17

Oh, i couldn't do that. Lumak wrote the amazing code. He should send a PR, this is an amazing addition. Thanks a lot for the help and the attention, guys. 

Hope this thread helps other Unity guys coming to Urho.

-------------------------

Eugene | 2017-05-30 13:30:15 UTC | #18

[offtop]
I think that inbuilt C# scripts in Urho would be perfect...
Unfortunatelly, those clever volunteers somewhy always create hard-to-reuse forks like Atomic or UrhoSharp.

-------------------------

