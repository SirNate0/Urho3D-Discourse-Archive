cactusmutant | 2017-01-02 01:06:00 UTC | #1

Hello,

I try to develop a 2D game using urho and I have some questions.

I saw there is a class LogicComponent to develop a custom component. But this class uses physic event. So, I want to develop the same class but using the 2D physic events.

These are my questions :
 - What is the difference between E_UPDATE and E_SCENEUPDATE events ?
 - When can I use E_UPDATE, E_SCENEUPDATE and E_PHYSICPRESTEP ?

I don't understand what is the PIXEL_SIZE constant and why is it useful.

Thanks,

Sorry for my bad English.

-------------------------

jmiller | 2017-05-24 03:40:13 UTC | #2

Hello,

(in international spirit, no apologies for English Second Language are necessary... especially if it's perfect :wink: )

Here are specific pages on physics and events:
[urho3d.github.io/documentation/H ... ysics.html](http://urho3d.github.io/documentation/HEAD/_physics.html)
[urho3d.github.io/documentation/H ... ho2_d.html](http://urho3d.github.io/documentation/HEAD/_urho2_d.html)
Those, and the 2D samples, are probably better than my explanations.

E_UPDATE is an application-wide update event.
E_SCENEUPDATE is specific to Scene and scene nodes, and is not sent if scene updates are disabled.
LogicComponent is just a convenience subclass of Component (it makes the samples simpler); you can just create your own Component.

PIXEL_SIZE - I have not used this in Urho, so am not sure. Typically, it's a device/density-independent pixel abstraction, allowing applications to work in pixels while the graphics converts to device/real pixels.

[b]EDIT[/b]: Explained here https://discourse.urho3d.io/t/simple-2d-game-tutorial-for-beginners/1607

HTH

-------------------------

cactusmutant | 2017-01-02 01:06:06 UTC | #3

Thank you for your answer.

Firstly, I think I'm going to do like you and I won't use PIXEL_SIZE. 

I think I will use E_UPDATE like describe in the documentation and if later I see I need the E_SCENEUPDATE I will use it.

-------------------------

