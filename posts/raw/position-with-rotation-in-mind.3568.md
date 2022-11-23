nergal | 2017-09-15 14:25:55 UTC | #1

This is a pretty basic 3D question I guess. But I have objects that rotate since they are rigid-bodies and when I raycast towards them I want to create new objects relative to their rotations.

More specific; It's a voxel-object that I want to explode and all debris should be created relative to the objects rotation. Otherwise they are placed in the same structure as the object in it's non-rotated state.

Example:
Vector3 body_pos = body->GetPosition(); 
Quaternion body_rot = body->GetRotation();
int voxel_pos_x = X;
int voxel_pos_y = Y;
int voxel_pos_z = Z;
Vector3 new_relative_pos = body_rot * Vector3(body_pos.x_+voxel_pos_x, body_pos.y_+voxel_pos_y, body_pos.z_+voxel_pos_x);
CreateMyNewObject(new_relative_pos);

But this calculation seems way wrong. Hints please? :slight_smile:

-------------------------

Eugene | 2017-09-16 06:42:59 UTC | #2

The simplest way is to create new objects as children of "reference" objects using relative position&rotation and then re-parent them to detach from the object.

-------------------------

nergal | 2017-09-16 06:42:54 UTC | #3

Thanks Eugene, that was an easy way of doing it! Worked perfect!

-------------------------

