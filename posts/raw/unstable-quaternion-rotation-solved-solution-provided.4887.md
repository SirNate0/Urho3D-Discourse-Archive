Leith | 2019-02-02 15:37:05 UTC | #1


Hey guys, I'm using the following code to rotate an enemy model to face the player model.
It's the humble beginning of a simple steering behaviour.
Generally it's working, but the orientation seems to flicker occasionally, which visually looks like a 90 degree error in orientation. Any ideas what the source of the numerical instability might be?

[code]
        // Get the current facing direction (had to flip sign to suit model)
        Vector3 currentDir = - GetNode()->GetWorldDirection();

        // Get the desired new direction
        Vector3 newDir =  (target_->GetNode()->GetWorldPosition() - GetNode()->GetWorldPosition()).Normalized();

        // Compute the angle between current and new directions
        float angle = currentDir.Angle(newDir);

        // Construct our quaternion to rotate around world up axis by our angle
        Quaternion q(angle, Vector3(0,1,0));

        // Apply rotation
        GetNode()->Rotate(q, TS_WORLD);
[/code]

-------------------------

ab4daa | 2019-02-01 02:12:11 UTC | #2

I don't really know what do you exactly want to do.

But I ran into quaternion rotation problem when trying to rotate toward a target rotation from current rotation with fixed rotation speed/degree per second.
(consider a fighter is chasing its target, it should try to turn to the fleeing target)
This is [my way](https://github.com/ab4daa/vehicle_rotation) to do it.

1. set rotation speed degree per second

> vehicle_rotation.set_speed(spd, spd, spd);

2. initialize current rotation
  >vehicle_rotation.set_rotation(urho3d_quater.PitchAngle(), urho3d_quater.YawAngle(), urho3d_quater.RollAngle());
3. turn toward target each frame
  >Urho3D::Vector3 targetDir = target_location_ - my_position;
  >Urho3D::Quaternion target_q(Urho3D::Vector3::FORWARD, targetDir);
  >vehicle_rotation.turnToward(timeStep, target_q.PitchAngle(), target_q.YawAngle(), target_q.RollAngle());
4. get result and apply to urho3d quaternion each frame
>vehicle_rotation.get_rotation(p, y, r);
>urho3d_quaternion.FromEulerAngles(p, y, r);

By doing this, even target keeps running/zig zag, fighter can smoothly turn toward it.
If just quaternion.nlerp, the turning speed is hard to control and will have some glitch in turning process.

Don't know if it helps.

-------------------------

Leith | 2019-02-01 02:44:07 UTC | #3

Man, you certainly do a lot of angular constraining in your approach :slight_smile:

I still don't yet know what is causing the 'flickering orientation' at certain angles, but I did notice a bug in Node::Rotate, where one of the cases is not normalizing the quaternion it returns:
[code]
    case TS_WORLD:
        if (parent_ == scene_ || !parent_)
            rotation_ = (delta * rotation_).Normalized();
        else
        {
            Quaternion worldRotation = GetWorldRotation();
            rotation_ = rotation_ * worldRotation.Inverse() * delta * worldRotation;
        }
[/code] 
Still, I switched from TS_WORLD to TS_LOCAL, and the flickering still occurs, so that is not the cause of the issue.

EDIT:
I've just noticed that the issue only occurs in one direction.
If the player walks around the enemy in one direction, the enemy tracks the player perfectly - no glitches. But if player walks around enemy in the OTHER direction, glitch city.
This appears to be about the sign of the angle returned by Vector::Angle ... as we know, there is no such thing as a negative angle, we're using a fixed range, 0 to 360 degrees (I checked this). Well guess what, a Quaternion cannot perform a rotation of , say, -10 degrees (eg 350) degrees ... quaternions are limited to 180 degree rotations, but our quaternion class appears not to be smart enough to choose the shortest path of rotation, which causes my orientation to have error of roughly 180 degrees whenever I attempt to rotate in a specific direction. Anyone care to weigh in on this?

-------------------------

Leith | 2019-02-01 10:59:56 UTC | #4

I have solved the issue! The problem? Vector3::Angle( ) returns an UNSIGNED angle between two vectors. I needed a Signed angle.

In order to solve the problem, I poked around in Unity sourcecode for a SignedAngle method, which I've slightly modified for Urho3D math.
I highly recommend that we consider adding this guy to our Vector3 class!

[code]
  float SignedAngle(Vector3 from, Vector3 to, Vector3 axis)
        {
            float unsignedAngle = from.Angle(to);
            float sign = axis.DotProduct(from.CrossProduct(to));
            if(sign<0)
                unsignedAngle = -unsignedAngle;
            return unsignedAngle;
}[/code]

The 'axis' vector is a reference axis of rotation, which is compared (using dot product) against the orthogonal crossproduct of the from and to vectors, though we are only interested in the Sign, which is then applied to the unsigned angle. 
The resulting SIGNED ANGLE is suitable for feeding to Quaternion's angle/axis constructor, no more glitching.

-------------------------

Leith | 2019-02-01 11:00:13 UTC | #5

Here's my implementation for AI steering behaviour, except for having some fixed values for rotation speed limits, that will likely be changed.
Note that I don't drop down to euler angles.

[code]
void Character::UpdateZombie(float timeStep){
    auto* animCtrl = node_->GetComponent<AnimationController>(true);

    if(target_!=nullptr)
    {

        // Get the current facing direction (had to flip sign to suit model)
        Vector3 currentDir = - GetNode()->GetWorldDirection();

        // Get the desired new direction
        Vector3 newDir =  (target_->GetNode()->GetWorldPosition() - GetNode()->GetWorldPosition()).Normalized();

        // Compute the angle between current and new directions
        float angle = SignedAngle(currentDir, newDir, Vector3(0,1,0));

        // Clamp the rate of rotation
        angle *= 5 * timeStep;                  // 5 degrees per second
        angle = Clamp<float>(angle,-30,+30) ;   // But limited to max 30 degrees per frame

        // Construct our quaternion to rotate around world up axis by our angle
        Quaternion q(angle, Vector3(0,1,0));

        // Apply rotation
        GetNode()->Rotate(q, TS_LOCAL);

    }

    // TODO: fix up animations
     animCtrl->PlayExclusive(Animations_[Animations_Zombie::Z_Attack].Name, 0, true, 0.2f);

}
[/code]

-------------------------

guk_alex | 2019-02-01 06:44:26 UTC | #6

Later I also experienced strange behaviour with calculating angles, it gives the range of (-180; 180); when I was working with euler angles as hot fix solution I appended 360 degrees to the result to make it positive and do not change the actual rotation. But this range is definitely not expected (may be in some cases it makes sense), but when calculating direction of rotation the change of the sign in some cases is not desirable effect (-179.9 - 1 = 179.1).

-------------------------

Leith | 2019-02-01 09:23:15 UTC | #7

I have no strange side effects at this point, and shared my code in full, if you have some side cases to talk about i want to know

-------------------------

guk_alex | 2019-02-01 11:00:06 UTC | #8

The only problem was that I thought that EulerAngles function of Quaternion returns values in range [0;360), but it is (-180;180) (I'm not sure does the range include 180 or -180). In this way it makes sense - if you need the [0;180) range and sign to make sure direction of an angle. (In my case I had an issue with dividing this range to get number of sectors of circle)

-------------------------

Leith | 2019-02-01 12:08:59 UTC | #9

I would like your reply twice if i could, but I solved the issue, and am happy to explain it

-------------------------

Leith | 2019-02-01 12:16:39 UTC | #10

our quaternion math concludes that you want to know, or set, degrees of angular change in the counter clockwise direction only

-------------------------

Leith | 2019-02-01 12:18:09 UTC | #11

highly unsafe given a 180 degree freedom

-------------------------

Leith | 2019-02-02 14:43:18 UTC | #12

Guys, we need a signed version of Vector3::Angle, one that tells us about the direction, not just the measure of the angle, its good for steering in games

-------------------------

