theak472009 | 2017-01-02 01:09:50 UTC | #1

Hello!
I dont know if this is the right place but there is a bug in Drawable.cpp:
Function: WriteDrawablesToOBJ
Buggy Line number: 530 -> Vector3 vertexNormal = *((const Vector3*)(&vertexData[(vertexStart + j) * elementSize + positionOffset]));
Correct Line -> Vector3 vertexNormal = *((const Vector3*)(&vertexData[(vertexStart + j) * elementSize + normalOffset]));

positionOffset should be replaced by normalOffset. (one of the evils of ctrl-c + ctrl-v  :stuck_out_tongue:)

Also, I dont know if this is right but multiplying the worldTransform with the normal is not required.

-------------------------

rasteron | 2017-01-02 01:09:50 UTC | #2

Yes, probably post this issue on GitHub as well. :slight_smile:

-------------------------

codingmonkey | 2017-01-02 01:09:53 UTC | #3

actually this is not all, There is another bug with normal orientation, if you trying save scene and import into blender.

this code solve this bug for blender import  
Drawable.cpp (line 468)
[code]        Node* node = drawable->GetNode();
        Matrix3x4 transMat = drawable->GetNode()->GetWorldTransform();
        Matrix3x4 n = transMat.Inverse();
        Matrix3 normalMat = Matrix3(n.m00_, n.m01_, n.m02_, n.m10_, n.m11_, n.m12_, n.m20_, n.m21_, n.m22_);
        normalMat = normalMat.Transpose();[/code]

line(535)
[code]                        vertexNormal = normalMat * vertexNormal;[/code]

after this fix meshes are not have inside oriented normal (black faces)

[url=http://savepic.net/7670130.htm][img]http://savepic.net/7670130m.png[/img][/url]

-------------------------

weitjong | 2017-01-02 01:09:54 UTC | #4

Can someone send a PR for this. Thanks.

-------------------------

