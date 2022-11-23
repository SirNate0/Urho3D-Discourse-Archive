Bananaft | 2017-01-02 01:14:56 UTC | #1

I'm doing volumetric light scattering for deferred lighting (GLSL). Taking from this tutorial: [blog.mmacklin.com/2010/05/29/in-scattering-demo/](http://blog.mmacklin.com/2010/05/29/in-scattering-demo/)

I've got everything sort of working for point lights and almost for spotlights with default rotation and fov. Thing is,  for spotlights I need transformation matrix(position and rotation) and aperture (spot FOV), to draw a proper volumetric cone.
I tried to use [b]cLightMatricesPS[0][/b], but as I understand it is not a proper transform matrix, but some special one, that also has fov transformation in it. I also tried inversed [b]iModelMatrix[/b], but also with no luck.

While poking randomly, I was able to create a matrix that works with Miles Macklin's code, but only for spotlights with default rotation. Here it is:
[code]
mat4 mymat = mat4(vec4( 1. , 0. , 0. , 0. ),
                  vec4( 0. , 1. , 0. , 0. ),
                  vec4( 0. , 0. , -1. , 0. ),
                  vec4( -cLightPosPS.x ,-cLightPosPS.y , cLightPosPS.z , 1. ));[/code]

I will appreciate any hints and suggestions on how to get proper transform matrix. Should iModelMatrix work? Or does it also have additional information (like scale as range) in it?
As for fov, I have no idea where to get it. I thought, there should be an uniform for it, but there is not.

-------------------------

Bananaft | 2017-01-02 01:14:56 UTC | #2

Just in case, here is the function I need to feed with said parameters. It calculates intersection of ray and a cone.

[spoiler][code]void IntersectCone(vec3 rayOrigin, vec3 rayDir, mat4 invConeTransform, float aperture, float height, out float minT, out float maxT)
{
	vec4 localOrigin = invConeTransform * vec4(rayOrigin, 1.0);
	vec4 localDir = invConeTransform * vec4(rayDir, 0.0);
	// could perform this on the cpu
	float tanTheta = tan(aperture);
	tanTheta *= tanTheta;

	float a = localDir.x*localDir.x + localDir.y*localDir.y - localDir.z*localDir.z*tanTheta;
	float b = 2.0*(localOrigin.x*localDir.x + localOrigin.y*localDir.y - localOrigin.z*localDir.z*tanTheta);
	float c = localOrigin.x*localOrigin.x + localOrigin.y*localOrigin.y - localOrigin.z*localOrigin.z*tanTheta;

	SolveQuadratic(a, b, c, minT, maxT);

	float y1 = localOrigin.z + localDir.z*minT;
	float y2 = localOrigin.z + localDir.z*maxT;

	// should be possible to simplify these branches if the compiler isn't already doing it

	if (y1 > 0.0 && y2 > 0.0)
	{
		// both intersections are in the reflected cone so return degenerate value
		minT = 0.0;
		maxT = -1.0;
	}
	else if (y1 > 0.0 && y2 < 0.0)
	{
		// closest t on the wrong side, furthest on the right side => ray enters volume but doesn't leave it (so set maxT arbitrarily large)
		minT = maxT;
		maxT = 10000.0;
	}
	else if (y1 < 0.0 && y2 > 0.0)
	{
		// closest t on the right side, largest on the wrong side => ray starts in volume and exits once
		maxT = minT;
		minT = 0.0;
	}
}[/code][/spoiler]

-------------------------

Bananaft | 2017-01-02 01:14:56 UTC | #3

And yes, it appears that iModelMatrix is affected by fov.

-------------------------

cadaver | 2017-01-02 01:14:56 UTC | #4

Spotlight attenuation in Urho is based on a projector texture, the texture transform matrix (in case of deferred rendering) is cLightMatricesPS[0] and should transform world space position to the projector coordinates. Otherwise the cone angle isn't being transmitted as a uniform.

-------------------------

Bananaft | 2017-01-02 01:14:57 UTC | #5

Thank you for reply.

So I guess, I need to dive into C++, to add this as uniforms.

-------------------------

