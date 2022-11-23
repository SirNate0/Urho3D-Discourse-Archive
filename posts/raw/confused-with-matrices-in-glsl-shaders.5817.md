restless | 2020-01-15 04:38:36 UTC | #1

I tried to read all of the https://urho3d.github.io/documentation/HEAD/pages.html but couldn't quite understand well enough how do the transformation matrices work in Urho3D.

Specifically, when I set shader parameter like this:

    SetShaderParameter("MyRot", node_->GetWorldRotation().RotationMatrix());

I can access that data in vertex shader by `cMyRot`.

But if I try to get the rotation already supplied shader variables, like this:

    mat4 modelMatrix = iModelMatrix;
    mat3 my_rot = mat3(modelMatrix);

I get totally different kind of data, expecting to just get the world transform matrix as in the previous code block.

I don't know lot about glsl and Urho3D approach on it, so any pointers or ideas would be appreciated

-------------------------

restless | 2020-01-16 12:28:14 UTC | #2

Solution that worked for me:

    mat3 get_rot_from_mat4 (mat4 m) {
        mat3 m3 = transpose(mat3(m));

        // extract the scaling factors
        float scaling_x = length(m3[0]);
        float scaling_y = length(m3[1]);
        float scaling_z = length(m3[2]);

        // and remove all scaling from the matrix
        m3[0] /= scaling_x;
        m3[1] /= scaling_y;
        m3[2] /= scaling_z;
        return m3;
    }

-------------------------

