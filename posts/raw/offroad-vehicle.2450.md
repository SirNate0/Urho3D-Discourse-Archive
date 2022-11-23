Lumak | 2017-01-20 15:10:44 UTC | #1

Here, [url]https://github.com/Lumak/Urho3D-Offroad-Vehicle/[/url]

### To Build
To build it, **unzip/drop the repository into your Urho3D/ folder** and build it the same way as you'd build the default Samples that comes with Urho3D.

I hope everyone can see the emphasis[b]^[/b]  :slight_smile: 

screenshot
[img]//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/1X/76d1f831efca971f64551ef7a0a83550b33fe548.jpg[/img]

Let me know if I missed anything, thx.

Edit: added instruction on how to build it.

-------------------------

artgolf1000 | 2017-01-02 01:15:27 UTC | #2

Great example!
I use Urho3D because of its excellent document and plenty of useful examples.
Most important, it is one alive project.
I had used GamePlay engine before, but it is almost dead now.
To keep an engine alive, the best way is using it to do some actual projects.

-------------------------

rasteron | 2017-01-02 01:15:27 UTC | #3

awesome work Lumak!

-------------------------

Lumak | 2017-01-02 01:15:28 UTC | #4

@artgolf, Thx, I'm also familiar with GamePlay. I've played around with that for a day then I discovered Urho3D :slight_smile: But I agree, ppl making projects out of the engine is a good way to keep it alive.

@rasteron, thx, I hope you find it useful.

-------------------------

S.L.C | 2017-01-02 01:15:28 UTC | #5

Can't seem to be able to compile. I'm getting some undefined errors. Related to the changes made to Bullet. Perhaps I need to do a clean build.

Also, what version of Urho is this for, 1.6 release? I used the last one from the repository.

-------------------------

Lumak | 2017-01-02 01:15:28 UTC | #6

@SLC, it is 1.6. I think I sync'd to the head about two weeks ago.

My first guess for the Bullet compile errors is that you only grabbed the files in 63_OffroadVehicle folder? There are source/header files in Source/ThirdParty/Bullet and Source/Urho3D folders that are in the repo.

-------------------------

S.L.C | 2017-01-02 01:15:28 UTC | #7

Nah. I actually copied and overwrote everything that was in the source folder. But I'll try a clean build and if the problem still persists.

-------------------------

Lumak | 2017-01-02 01:15:28 UTC | #8

For my testing, I drop the repo into a virgin urho3d 1.6 folder and do the build to ensure all source, header, and data are copied.
But on an existing built folder, I imagine the changes in the header files from the repo would require a rebuild if the dependency make files didn't pick it up automatically.

Good luck with the build and let me know how it turns out.

-------------------------

dakilla | 2017-01-02 01:15:30 UTC | #9

Nice, physics seems sweet in video, I'll test it soon.
thanks

-------------------------

Enhex | 2017-01-20 15:11:24 UTC | #10

Looks like it works very well!

If anyone is looking for a video:
https://www.youtube.com/watch?v=9ZAnvz2f_hU

-------------------------

Lumak | 2017-01-02 01:15:43 UTC | #11

Made changes in the repo to access and scale compound local AABB to allows changing the inertia bbox and reduce the chance of rolling when aabb.y is reduced.

About the video, the dust emitters are not properly placed and were corrected in the repo, but I kinda like how it looks in the video :wink:

Merry Christmas :slight_smile:

edit: keeping positive attitude toward the holidays

-------------------------

Miegamicis | 2017-01-02 01:15:47 UTC | #12

Found a bug with the offroad vehicle code. The problem appears when vehicle node is destroyed, raycast vehicle is not removed from the physics world and in the next physics step update application crashes.

To fix this you need to change

[code]RaycastVehicle::~RaycastVehicle()
{
    if (sphShape_)
    {
        delete sphShape_;
        sphShape_ = NULL;
    }
    if (vehicleRaycaster_)
    {
        delete vehicleRaycaster_;
        vehicleRaycaster_ = NULL;
    }
    if (raycastVehicle_)
    {
        delete raycastVehicle_;
        raycastVehicle_ = NULL;
    }
}[/code]

to 

[code]RaycastVehicle::~RaycastVehicle()
{
    if (sphShape_)
    {
        delete sphShape_;
        sphShape_ = NULL;
    }
    if (vehicleRaycaster_)
    {
        delete vehicleRaycaster_;
        vehicleRaycaster_ = NULL;
    }
    if (raycastVehicle_)
    {
        btDynamicsWorld *pbtDynWorld = (btDynamicsWorld*)GetPhysicsWorld()->GetWorld();
        pbtDynWorld->removeVehicle(raycastVehicle_);
        delete raycastVehicle_;
        raycastVehicle_ = NULL;
    }
}[/code]

-------------------------

Lumak | 2017-01-02 01:15:48 UTC | #13

Ok, thanks.  This crash doesn't appear in Windows, which os?

edit: this makes sense if the game continues to run after a vehicle is removed.  good find, thx.

-------------------------

Miegamicis | 2017-01-02 01:15:48 UTC | #14

[quote="Lumak"]Ok, thanks.  This crash doesn't appear in Windows, which os?

edit: this makes sense if the game continues to run after a vehicle is removed.  good find, thx.[/quote]

I used Windows. But anyway, great sample! Managed to get this to work without any problems!  :wink:

-------------------------

Virgo | 2018-05-14 20:10:04 UTC | #15

is this for 1.6 only? i tried t do it with 1.7 and failed building the example, it says missing headers

-------------------------

Lumak | 2018-05-15 10:31:40 UTC | #16

I dropped the offroad repo into a fresh 1.7 sandbox, built it, and saw that the last change that I submitted for the **void Vehicle::AutoCorrectPitchRoll()** fn. actually had error using the hullBody_ var. I updated the repo just now with the correction.

Thanks for the feedback on this, as I rarely get any.
Btw, are you aware that 46_RaycastVehicle sample was added to Urho3D in 1.7? It's an adaptation of the raycast demo posted from about three yrs ago, so it should be similar, although, I haven't test it myself.

-------------------------

Virgo | 2018-05-15 10:53:30 UTC | #17

i tried the examples come with official urho3d repo.
but vehicle in both 19_VehicleDemo and 46_RaycastVehicle starts rolling if i accelerate too much

-------------------------

