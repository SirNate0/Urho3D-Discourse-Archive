mostafa901 | 2019-11-07 15:42:31 UTC | #1

Well as i am getting my feet wet, Ideas keeps popping, so any Idea how to animate CameraNode.LookAt(position);
I tried the below snippet
 
            var delta = Quaternion.FromRotationTo(CameraNode.Position, Targetposition);
			await CameraNode.RunActionsAsync(new EaseInOut(new RotateBy( 3, delta.PitchAngle,delta.YawAngle,delta.RollAngle), 5f));

but the result is extremely weird!!!

-------------------------

Modanung | 2019-11-07 19:32:39 UTC | #2

Answered on Gitter. For posterity:

https://urho3d.github.io/documentation/HEAD/_attribute_animation.html

-------------------------

