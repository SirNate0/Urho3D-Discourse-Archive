slapin | 2017-01-02 01:15:05 UTC | #1

Hi, all!

could anybody help me make this work?
Currently it doesn't work at all (produce zero effect on bones).
No visual difference, feet still penetrate terrain.
Any ideas on what I miss? any alternative solutions?

[code]
// Used article:
// http://discourse.urho3d.io/t/solved-ik-foot-placement/1010/1

class LegIK {
    Node@ root_bone, left_foot, right_foot;
    Vector3 leg_axis;
    Node@ char_node;
    float left_leg_length, right_leg_length,
       original_root_height;
    Scene@ scene;
    float uneven_threshold = 0.05;
    bool do_ik = false;
    void solve_ik(Node@ effector, Vector3 target_pos)
    {
        Vector3 start_joint_pos = effector.parent.parent.worldPosition; // thigh pos (hip joint)
        Vector3 mid_joint_pos = effector.parent.worldPosition; // Calf pos (knee joint)
        Vector3 effector_pos = effector.worldPosition; // Foot pos (ankle joint)
        Vector3 thigh_dir = mid_joint_pos - start_joint_pos; // thigh direction
        Vector3 calf_dir = effector_pos - mid_joint_pos; // calf direction
        Vector3 target_dir = target_pos - start_joint_pos; // leg direction
        float length1 = thigh_dir.length;
        float length2 = calf_dir.length;
        float limb_length = length1 + length2;
        float lengthH = target_dir.length;
        if (lengthH > limb_length) {
            target_dir = target_dir * (limb_length / lengthH) * 0.999; // Do not overshoot if target unreachable
            lengthH = target_dir.length;
        }
        float lengthHsquared = target_dir.lengthSquared;

        // current knee angle (from animation keyframe)
        float knee_angle = thigh_dir.Angle(calf_dir);

        // new knee angle
        float cos_theta = (lengthHsquared - thigh_dir.lengthSquared - calf_dir.lengthSquared) / (2 * length1 * length2);
        if (cos_theta > 1.0)
            cos_theta = 1.0;
        else if (cos_theta < -1.0)
            cos_theta = -1.0;
        float theta = Acos(cos_theta);
        if (Abs(theta - knee_angle) > 0.01) {
            Quaternion new_knee_angle((theta - knee_angle), leg_axis);
            Quaternion new_hip_angle(-(theta - knee_angle) * 0.5, leg_axis);

            // Apply rotations
            effector.parent.rotation = effector.parent.rotation * new_knee_angle;
            effector.parent.parent.rotation = effector.parent.parent.rotation * new_hip_angle;
        }
    }
    void solve_leg_ik()
    {
        AnimationController@ anim = char_node.GetComponent("AnimationController");
        if (!anim.IsPlaying("Models/girl/Models/Run.ani")) {
            root_bone.worldPosition = Vector3(root_bone.worldPosition.x, char_node.position.y + original_root_height, root_bone.worldPosition.z);
        }
        float root_height = root_bone.worldPosition.y - char_node.position.y;
        float foot_height_l = left_foot.worldPosition.y - char_node.position.y;
        float foot_height_r = right_foot.worldPosition.y - char_node.position.y;
        Vector3 left_ground(left_foot.worldPosition), right_ground(left_foot.worldPosition);
        bool left_down = false, right_down = false;
        if (left_ground.y < right_ground.y - uneven_threshold)
            left_down = true;
        else if (right_ground.y < left_ground.y - uneven_threshold)
            right_down = true;
        PhysicsRaycastResult result = scene.physicsWorld.RaycastSingle(Ray(left_ground + Vector3(0, left_leg_length, 0), Vector3(0, -1, 0)), 10, 2);
        left_ground = result.position;
        // Distance from foot to ground
        float left_dist = left_foot.worldPosition.y - (left_ground.y + foot_height_l);
        Vector3 left_normal = result.normal;

        result = scene.physicsWorld.RaycastSingle(Ray(right_ground + Vector3(0, right_leg_length, 0), Vector3(0, -1, 0)), 10, 2);
        right_ground = result.position;
        // Distance from foot to ground
        float right_dist = left_foot.worldPosition.y - (left_ground.y + foot_height_l);
        Vector3 right_normal = result.normal;

        float height_diff = 0.0f;
        if (left_down || left_ground.y <= right_ground.y) {
            height_diff = left_dist;
            if (Abs(height_diff) > 0.001)
                right_ground = right_ground + Vector3(0.0, height_diff, 0.0);
        } else if (right_down || right_ground.y < left_ground.y) {
            height_diff = right_dist;
            if (Abs(height_diff) > 0.001)
                left_ground = left_ground + Vector3(0.0, height_diff, 0.0);
        }
        if (Abs(height_diff) < 0.001)
            return;
        root_bone.worldPosition = root_bone.worldPosition - Vector3(0.0, height_diff, 0.0);
        if (!left_down) {
            left_ground.x = 0.0;
            left_ground.z = 0.0;
            solve_ik(left_foot, left_ground);
        }
        if (!right_down)
            right_ground.x = 0.0;
            right_ground.z = 0.0;
            solve_ik(right_foot, right_ground);
    }
    void handle_scene_drawable_update_finished(StringHash eventType, VariantMap& eventData)
    {
        if (do_ik)
            solve_leg_ik();
    }
    LegIK(Node@ char_node, Scene@ scene)
    {
        left_foot = char_node.GetChild("foot.L", true);
        right_foot = char_node.GetChild("foot.L", true);
        leg_axis = Vector3(0, 0, -1);
        AnimatedModel@ model = char_node.GetComponent("AnimatedModel");
        Skeleton@ skel = model.skeleton;
        // Get root bone of the skeleton as we will move it to match IK targets
        root_bone = char_node.GetChild(skel.rootBone.name, true);
        // left thigh length + left calf length
        left_leg_length = skel.GetBone(left_foot.parent.parent.name).boundingBox.size.y + skel.GetBone(left_foot.parent.name).boundingBox.size.y;
        right_leg_length = skel.GetBone(right_foot.parent.parent.name).boundingBox.size.y + skel.GetBone(right_foot.parent.name).boundingBox.size.y;
        // Used when no animation is playing
        original_root_height = root_bone.worldPosition.y - char_node.position.y;
        this.char_node = char_node;
        this.scene = scene;
        SubscribeToEvent("SceneDrawableUpdateFinished", "handle_scene_drawable_update_finished");
    }
}
[/code]

-------------------------

Mike | 2017-01-02 01:15:05 UTC | #2

Did you set do_ik to true ?

-------------------------

slapin | 2017-01-02 01:15:05 UTC | #3

Yep, that part works.

As I understand, no bone modification works at all
with animation enabled. I tried to just modify bone rotations and it doesn't work
in the same way.

-------------------------

slapin | 2017-01-02 01:15:05 UTC | #4

As I dug deeply, I found the culprit, but I don't know what to do about it.

In all my exports from Blender all bone bounding boxes are set to infinite, so IK can't calculate sizes.
I don't know how to do export so that bounding boxes are there.

-------------------------

Mike | 2017-01-02 01:15:06 UTC | #5

The script doesn't use bone bounding box, it uses bone node position, so maybe your skeleton is weirdly authored.

-------------------------

slapin | 2017-01-02 01:15:06 UTC | #6

[quote]The script doesn't use bone bounding box, it uses bone node position, so maybe your skeleton is weirdly authored.[/quote]

[code]
        left_leg_length = skel.GetBone(left_foot.parent.parent.name).boundingBox.size.y + skel.GetBone(left_foot.parent.name).boundingBox.size.y;
        right_leg_length = skel.GetBone(right_foot.parent.parent.name).boundingBox.size.y + skel.GetBone(right_foot.parent.name).boundingBox.size.y;
[/code]

These (both) result to infinity (-inf)

-------------------------

slapin | 2017-01-02 01:15:06 UTC | #7

Also I tested that at export stage all bone bounding boxes are fine.
Which looks like AngelScript-specific issue.

-------------------------

Mike | 2017-01-02 01:15:06 UTC | #8

Sorry, I forgot that I was using bone bounding box in the first place.
If I would do it now, I would no longer rely on bone bounding box anymore, as it cannot give accurate results all the time, due to the fact that it is computed from nearest vertices. I'd rather use bone node positions instead, which will give perfect results and will never fail.

-------------------------

slapin | 2017-01-02 01:15:06 UTC | #9

How would you overcome tail bone problem?

-------------------------

Mike | 2017-01-02 01:15:06 UTC | #10

It's certainly time to add a new export option to the Blender exporter, so that we can safely rely on bone bounding box when accuracy is mandatory (IK, ragdoll...)
I'll contact Reattiva to check if he is OK with this proposition.

[color=red]EDIT:[/color] New option added (Skeletons > Clamp bones bounding box).

-------------------------

slapin | 2017-01-02 01:15:07 UTC | #11

Thanks a lot! That would be great feature indeed.

-------------------------

