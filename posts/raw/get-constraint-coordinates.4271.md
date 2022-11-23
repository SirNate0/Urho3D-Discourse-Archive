capelenglish | 2018-05-30 18:13:17 UTC | #1

I'm trying to log some coordinates associated with constraints. For example:

    plateConstraint->SetWorldPosition(plateNode->GetPosition());

How do I extract these coordinates for logging with URHO3D_LOGINFO?

-------------------------

TheComet | 2018-05-30 20:55:27 UTC | #2

`URHO3D_LOGINFOF("The coordinates are: %s", plateConstraint_->GetWorldPostion().ToString());`

-------------------------

capelenglish | 2018-05-31 11:15:18 UTC | #3

    URHO3D_LOGINFO("The World Position coordinates for the plate constraint are: %s", plateNode->GetPostion().ToString());

returns

    [Thu May 31 07:12:08 2018] INFO: The World Position coordinates for the plate constraint are: %s

If I do a QuickWatch on plateNode->GetPostion() VS2017 tells me class "Urho3D::Node" has no member "GetPostion"

What am I missing?

-------------------------

TheComet | 2018-05-31 11:18:16 UTC | #4

It's `URHO3D_LOGINFOF` not `URHO3D_LOGINFO` and you spelled "Position" wrong, i.e. I spelled it wrong in my last response.

-------------------------

capelenglish | 2018-05-31 11:26:47 UTC | #5

The dangers of copy and paste!

So QuickWatch evaluates plateNode->GetWorldPosition().ToString() correctly, but now String.h throws an exception: Exception thrown at 0x0137FB7C (ucrtbased.dll) in Urho3D_Test_d.exe: 0xC0000005: Access violation reading location 0x0000000E.

-------------------------

capelenglish | 2018-05-31 11:34:46 UTC | #6

Looks like it's a format specification issue. Where the heck can I find those?

-------------------------

TheComet | 2018-05-31 12:09:14 UTC | #7

That particular error means you are dereferencing a nullptr. Most likely, plateNode is NULL. Have you checked with a debugger?

-------------------------

capelenglish | 2018-05-31 12:11:56 UTC | #8

Yes. 
    Vector3 coords = plateNode->GetWorldPosition();
returns a vector with the correct coordinates.

-------------------------

TheComet | 2018-05-31 12:15:39 UTC | #9

Something is NULL, it's up to you to debug it.

-------------------------

capelenglish | 2018-05-31 13:30:29 UTC | #10

I'm missing something more fundamental here. I get the same exception when I do this:

    for (int i = 0; i < plateNodes_.Size(); ++i)
    {
      if (DEBUG) URHO3D_LOGINFOF("Reset plate %s", String(i));
      plateNodes_[i]->SetRotation(Quaternion(0.0f, 0.0f, 0.0f));
    }

This compiles fine, but I get a run-time exception. How do I convert int and floats to strings in Urho3D?

Sorry for the stupid questions, I'm a C# guy trying to come up to speed on C++...

-------------------------

Lumak | 2018-05-31 13:35:11 UTC | #11

try
[code]
if (DEBUG) URHO3D_LOGINFOF("Reset plate %s", String(i).CString());
[/code]

-------------------------

capelenglish | 2018-05-31 13:45:53 UTC | #12

@Lumak thanks! To confirm I understand what's going on: String(i) converts the int to an Urho3D string and then .CString() converts it into a C++ string?

-------------------------

Lumak | 2018-05-31 13:52:08 UTC | #13

Correct, the String is Urho3D::String, and String.CString() returns const char* , see Urho3D/Container/Str.h

Most of *string-to-value or value-to-string* conversions can be found in: Urho3D/Core/StringUtils.h

-------------------------

TheComet | 2018-05-31 14:33:12 UTC | #14

You'll want to do

`URHO3D_LOGINFOF("Reset plate %d", i);`

for integers.

I thought you could pass String to the log macros without having to first convert it to const char* but I was wrong.

-------------------------

capelenglish | 2018-05-31 14:39:41 UTC | #15

Where do I find the documentation for the formats like %s and %d? I assume there are others for floats etc...

-------------------------

TheComet | 2018-05-31 14:58:48 UTC | #16

Great question, we can't answer it because the documentation is lackluster.

The best I can do is link you do the function that gets called: https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Container/Str.cpp#L1087

It appears to support a subset of what printf() supports, `d, i, u, l, f, c, s, x` and `p`

This could actually be improved on if we just forwarded everything to vsnprintf()

-------------------------

capelenglish | 2018-05-31 15:08:29 UTC | #17

Along these lines, how do you convert an Urho3D::string to a std::string?

    string nodeName = String(hitNode->GetName().CString()); // doesn't work

I need to use boost::starts_with() and it pukes on an Urho3D string.

-------------------------

TheComet | 2018-05-31 15:11:23 UTC | #18

You did it correctly, you just accidentally capitalized "String" so you're converting it back to an Urho3D string.

`std::string nodeName = std::string(hitNode->GetName().CString()); // does work`

-------------------------

capelenglish | 2018-06-04 17:54:45 UTC | #19

Now I need to go the other way std::string to Urho3D::string formatted to 2 places.

    x = 45.12345
    string strHitTimeInSec = boost::str(boost::format("%.2f") % x); // works fine (45.12)
    URHO3D_LOGINFOF("hit at %s seconds ", strHitTimeInSec); // doesn't work

It's not obvious to me how to convert this...

-------------------------

kostik1337 | 2018-06-05 09:48:39 UTC | #20

`URHO3D_LOGINFOF("hit at %s seconds ", strHitTimeInSec.c_str());`

-------------------------

capelenglish | 2018-06-05 11:19:47 UTC | #21

@kostik1337 Thanks! This is just what I was looking for.

-------------------------

