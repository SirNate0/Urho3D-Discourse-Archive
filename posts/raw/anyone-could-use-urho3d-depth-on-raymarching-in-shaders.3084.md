rbnpontes | 2017-05-01 02:28:24 UTC | #1

Hello Guys, a while ago i was trying to implement raymarching technique on Urho3D shaders,
but i have problem while using Urho3D Depth, the objects appeared normaly but, raymarching always stay on top of Models.
I use this code to implement Urho3D Depth on Raymarch:
<code>// Raymarch along given ray
// ro: ray originThis text will be hidden
// rd: ray direction
// s: Urho3D depth buffer
float4 raymarch(float3 ro, float3 rd, float s) {
float4 ed4 ret = float4 (0,0,0,0);

const int maxstep = 64;
float t = 0; // current distance traveled along ray
	for (int i = 0; i < maxstep; ++i) {
// If we run past the depth buffer, or if we exceed the max draw distance,
// stop and return nothing (transparent pixel).
// this way raymarched objects and traditional meshes can coexist.
	if (t >= s || t > cDrawDistance) { // Depth is Okay, but doesn't work here
	ret = fixed4(0, 0, 0, 0);
	break;
	}

	float3 p = ro + rd * t; // World space position of sample
	float2 d = map(p);		// Sample of distance field (see map())

	// If the sample <= 0, we have hit something (see map()).
	if (d.x < 0.001) {
	// Draw Object
	break;
	}

	// If the sample > 0, we haven't hit anything yet so we should march forward
	// We step forward by distance d, because d is the minimum distance possible to intersect
	// an object (see map()).
	t += d;
	}
</code>
i have followed this tutorial to implement DepthBuffer, but in unity: [http://flafla2.github.io/2016/10/01/raymarching.html](http://flafla2.github.io/2016/10/01/raymarching.html)

-------------------------

artgolf1000 | 2017-05-02 02:14:16 UTC | #2

Hi, you may look into my post: https://discourse.urho3d.io/t/volumetric-lighting/2373

-------------------------

rbnpontes | 2017-05-02 14:08:08 UTC | #3

Yes I see, this is a excellent post, but it still did not solve my problem

-------------------------

