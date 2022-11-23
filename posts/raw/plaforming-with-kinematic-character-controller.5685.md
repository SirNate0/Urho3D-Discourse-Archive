Lumak | 2019-10-26 13:23:49 UTC | #1

Repo posted - https://github.com/Lumak/Urho3D-KinematicCharacterController


https://youtu.be/IyEY2IIJGAU

This was the last item on my to-do-list related to Bullet Physics implementation for Urho3D, something I wanted to complete for a while and finally done, yay!

-------------------------

Miegamicis | 2019-10-25 08:55:15 UTC | #2

Glad to see you coming back with more amazing features!

-------------------------

suppagam | 2019-10-25 15:48:43 UTC | #3

That looks awesome! Would love to see some ledge-grabbing action there.

-------------------------

Lumak | 2019-10-26 13:30:27 UTC | #4

repo created. post if you encounter any problem.

-------------------------

glitch-method | 2019-10-27 05:00:47 UTC | #5

seconded, adding ledge-grab (and maybe climb for small objects) would make this a practically usable model out-of-the-box.

-------------------------

Modanung | 2019-10-27 09:11:39 UTC | #6

Depending on the use case, it already is.

-------------------------

elix22 | 2019-10-27 16:58:36 UTC | #7

Awesome demo .
Do you plan to submit a P.R. ?

Besides the changes in PhysicsWorld.h and PhysicsWorld.cpp

I did several modifications to make it work on the latest branch . 

1-
In **playGroundTest.xml** , changed the hash from "3025579211"  to "1301124395"

    `<node id="34">`
        <attribute name="Variables">
    				<variant hash="1301124395" type="Bool" value="true" />
    	</attribute>
    </node>


2 - Added at the end of the function :

    void MovingPlatform::Initialize(Node *platformNode, const Vector3 &finishPosition, bool updateBodyOnPlatform)
    {
    ....
    ....
          platformVolumdNode_->SetVar(StringHash("IsMovingPlatform"), true);
    }

-------------------------

Lumak | 2019-10-27 18:08:53 UTC | #8

Did the hashing function change since 1.7?

-------------------------

elix22 | 2019-10-27 19:51:37 UTC | #9

Looks like it did 

Current  =>  Case sensitive hashing

    unsigned StringHash::Calculate(const char* str, unsigned hash)
    {
        if (!str)
            return hash;

        while (*str)
        {
            hash = SDBMHash(hash, (unsigned char)*str++);
        }

        return hash;
    }  

1.7 => case insensitive hashing ,`tolower(c)`

        unsigned StringHash::Calculate(const char* str)
        {
            unsigned hash = 0;

            if (!str)
                return hash;

            while (*str)
            {
                // Perform the actual hashing as case-insensitive
                char c = *str;
                hash = SDBMHash(hash, (unsigned char)tolower(c));
                ++str;
            }

            return hash;
        }

-------------------------

Lumak | 2019-10-27 21:25:01 UTC | #10

Ok, thanks for the info. 
I am done with my work on the kinematic char controller platforming and have moved onto another project on my to-do list. You are more than welcome to submit a PR of that work as if it was your own, or enhance it, or whatever you desire.

-------------------------

Valdar | 2019-10-29 10:03:15 UTC | #11

@Lumak Really nice work, as usual :+1:

-------------------------

GodMan | 2019-11-05 18:42:00 UTC | #12

@Lumak Great job. I have seen some of your other work. You are great with the physics API.

-------------------------

SuperVehicle-001 | 2020-09-17 18:26:15 UTC | #13

Woooo, look at the robot go down the ramp without bouncing all over the place! That feature alone makes this incredibly useful, and it honestly should be part of the core Urho3D package...

In truth, this is **too** useful. I've been working on a small personal project which is a platformer, and the difference between this kinematic controller and a "normal" character controller is like night and day. But this is all C++ code, and my project mainly uses Lua scripts...

I've been trying to port this controller to Lua myself but I'm having terrible luck with it. I even tried including the component inside the executable and then calling it within the scripts, but that didn't work either :( . So I wanted to ask if anyone else has managed to successfully incorporate this kinematic controller in a Lua project?

-------------------------

