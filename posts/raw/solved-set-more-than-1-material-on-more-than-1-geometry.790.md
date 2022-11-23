devrich | 2017-01-02 01:02:54 UTC | #1

** I am using the "PhysicsStressTest.lua" script to test how things work **

I have made a model of a cube that I have made two different materials and set some faces to one material and the other faces to the second material.

I have created two material XML files "matA.xml" and "matB.xml" where i just changed one of the colors to a different value so I can see the differences.

I found "SetMaterial()" [url]http://urho3d.github.io/documentation/1.32/class_urho3_d_1_1_static_model.html#a9cf254e2f4535519c8ee06d42d736402[/url] and the second overload is like this:

[quote]SetMaterial (unsigned index, Material *material)
 	Set material on one geometry. Return true if successful. [/quote]

I tried it this way to no avail:

[code]boxObject:SetMaterial(0,cache:GetResource("Material", "Materials/matA.xml")
boxObject:SetMaterial(1,cache:GetResource("Material", "Materials/matB.xml")[/code]


How do I "properly" use this SetMaterial( ) overload from Lua ?

-------------------------

devrich | 2017-01-02 01:02:54 UTC | #2

[quote="devrich"]** I am using the "PhysicsStressTest.lua" script to test how things work **

I have made a model of a cube that I have made two different materials and set some faces to one material and the other faces to the second material.

I have created two material XML files "matA.xml" and "matB.xml" where i just changed one of the colors to a different value so I can see the differences.

I found "SetMaterial()" [url]http://urho3d.github.io/documentation/1.32/class_urho3_d_1_1_static_model.html#a9cf254e2f4535519c8ee06d42d736402[/url] and the second overload is like this:

[quote]SetMaterial (unsigned index, Material *material)
 	Set material on one geometry. Return true if successful. [/quote]

I tried it this way to no avail:

[code]boxObject:SetMaterial(0,cache:GetResource("Material", "Materials/matA.xml")
boxObject:SetMaterial(1,cache:GetResource("Material", "Materials/matB.xml")[/code]


How do I "properly" use this SetMaterial( ) overload from Lua ?[/quote]


I ran this from a terminal window to get the error mesage and it was a bloody typo " expected: ')' near ......... "

It works EXACTLY as intended so I was apparently doing it right the whole time  :blush: 

Here is the corrected code ( with the missing ')' at the ends )

[code]boxObject:SetMaterial(0,cache:GetResource("Material", "Materials/matA.xml")  )
boxObject:SetMaterial(1,cache:GetResource("Material", "Materials/matB.xml")  )[/code]

-------------------------

