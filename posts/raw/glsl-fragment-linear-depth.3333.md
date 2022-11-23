sabotage3d | 2017-07-09 14:47:20 UTC | #1

I have been trying for a while to get Linear Depth without using a texture. I am trying to compute it in the vertex shader and use it in the fragment shader. I have tried three different approaches below. I also tried to linearlize based on far and near clip planes. So far 3 game me the most accurate result but it still not perfect. In my technique I have: `depthtest="always" depthwrite="false"` 

    // 1
    // VS
    vWorldPos = vec4(worldPos, GetDepth(gl_Position));
    // PS
    float depth = vWorldPos.z/vWorldPos.w;

    // 2
    // PS
    float depth = gl_FragCoord.z;

    // 3
    varying float v_depth;
    // VS
    v_depth = -(inverse(cViewInv * cViewProj) * gl_Position).z;
    // PS
    depth = v_depth;

-------------------------

