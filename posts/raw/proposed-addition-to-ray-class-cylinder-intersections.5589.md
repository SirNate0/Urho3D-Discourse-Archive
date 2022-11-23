Leith | 2019-09-17 05:15:05 UTC | #1

Hey guys, I've been working on a solution for detecting nearest point of intersection of a ray and a cylinder, if anyone feels inclined to do some third party testing, and/or offer suggestions for improving the implementation, I would be most grateful. 

I return the hit point and the distance, but I can also provide a surface normal, so it's a good fit with the usual suspect intersection tests of the Ray class.

The entrypoint to this code is the third function provided - it takes a ray and a cylinder defined in world space, thus it deals with oriented and translated cylinders. Scale is not addressed in this implementation - but there's no mention of node transforms, so it's not relevant.

[code]
// Calculate the normal of a point on the surface of a cylinder
// The cylinder is assumed to have the center of its lower cap coinciding with the origin,
// and to be oriented along the world UP (Y+) axis...
// We assume we are working in the "local space" of the cylinder...
Vector3 GetCylinderNormal (const Vector3& p, float radius, float height)
{
	// Point is on one of the bases
	if (p.x_<radius && p.x_>-radius && p.z_<radius && p.z_>-radius)
	{
        /// Check if point is on the upper cap
		double epsilon = 0.00000001;
		if (p.y_ < height+epsilon && p.y_>height-epsilon){
			return Vector3::UP;
		}
		/// Check if point is on the lower cap
		if (p.y_ < epsilon && p.y_>-epsilon){
			return Vector3::DOWN;
		}
	}

	// Point is on lateral surface
 	Vector3 c0 (0, p.y_, 0);
 	Vector3 v = (p-c0).Normalized();
 	return v;
}

// Calculate intersection with cylinder base having center c = either <0,0,0> or <0,height,0>
// We do this by calculating the intersection with the Y plane,
// and then checking if the intersection is within the 2D circle (XZ).
// Again, we assume we are working in "cylinder local space".
bool intersectCylinderBase (const Ray& ray, float radius, float height, const Vector3& c, double& dist, Vector3& hitPoint)
{
	Vector3 normal = GetCylinderNormal (c, radius, height);

	double D =  -normal.DotProduct(c);
	double phi = normal.DotProduct(ray.direction_);

	if (phi==0)
		return false;

	dist = - (normal.DotProduct(ray.origin_)+D) / phi;

	const double epsilon = 0.00000001;
	if (dist < epsilon)
		return false;

	Vector3 p  = ray.origin_+dist*ray.direction_;
	if (p.x_*p.x_+p.z_*p.z_-radius*radius > epsilon)
		return false;

	hitPoint=p;
	return true;
}

/// Compute intersection of cylinder and ray in world space!
// First, find intersection with infinite vertical cylinder....
// In order to do that, transform the ray so that the center of the bottom base
// is at the origin and the cylinder's length axis coincides with the Y axis,
// then calculate intersection with the canonical infinite cylinder,
// and check if the ray intersects the lateral surface of the cylinder within our
// bases, and if not, check if ray intersects the bases and if not, there's NO intersection!
float intersectCylinder (const Ray& inray, const Vector3& center, const Vector3& normal, float radius, float height, Vector3& hitPoint)
{

    /// Compute a suitable rotation from a base vector to the desired direction
    Quaternion q;
    q.FromRotationTo(Vector3::UP, normal);

    /// Compute transform from cylinder local space to world space
    Matrix3x4 mat(center, q, Vector3::ONE);

    /// Compute transform from world space to cylinder local space
    Matrix3x4 inv=mat.Inverse();

    /// Transform ray from world space to cylinder local space
    Ray ray = inray.Transformed(inv);

    /// We wish to compute a positive value for t
    float t;

	// Note the ray origin (transformed into cylinder's local space)
	Vector3 p0 = ray.origin_;

	// coefficients for the intersection equation
	// got them mathematically intersecting the line equation with the cylinder equation
	double a = ray.direction_.x_*ray.direction_.x_+ray.direction_.z_*ray.direction_.z_;
	double b = ray.direction_.x_*p0.x_ +ray.direction_.z_*p0.z_;
	double c = p0.x_*p0.x_+p0.z_*p0.z_-radius*radius;

	double delta = b*b - a*c;

	//use epsilon because of computation errors between doubles
	const double epsilon = 0.00000001;

	// delta < 0 means no intersections
	if (delta < epsilon)
		return M_INFINITY;

	// nearest intersection
	t = (-b - sqrt (delta))/a;

	// t<0 means the intersection is behind the ray origin
	// which we don't want
	if (t<=epsilon)
		return M_INFINITY;

	hitPoint = p0 + t * ray.direction_;


	/// check if we intersect one of the cylinder caps (aka bases)
	if (hitPoint.y_ > height+epsilon || hitPoint.y_ < -epsilon) {
		double dist;
		Vector3 hp1, hp2;

        /// Check for intersection with upper cap
		bool b1 = intersectCylinderBase(ray, radius, height, Vector3(0, height, 0), dist, hp1);
		if(b1) { t=dist; hitPoint=hp1; }

		/// Check for intersection with lower cap
		bool b2 = intersectCylinderBase (ray, radius, height, Vector3::ZERO, dist, hp2);
		if(b2 && dist>epsilon && t>=dist) { t=dist; hitPoint=hp2; }

        /// If there's NO intersection...
		if(! (b1||b2) )
            t=M_INFINITY;
	}

    /// If t is valid, then transform the hitpoint from cylinder space to worldspace
    if(t!=M_INFINITY)
        hitPoint = mat * hitPoint;

	return t;

}
[/code]

-------------------------

Leith | 2019-09-19 05:03:29 UTC | #2

I was wondering how everyone feels about changing the existing AddCylinder (wireframe) method to support orientation? In my ideal world, it would be a breaking change, because I would not like to merely "tack on" optional arguments in an arbitrary order... what I propose would break backward compatibility, for drawing cylinders in wireframe, but would allow us to orient them. Current code does not.. vertical cylinder only.

-------------------------

SirNate0 | 2019-09-19 16:18:56 UTC | #3

I am in favor of it - it would make it consistent with some of the other shapes like a cone, right? I doubt many people have AddCylinder calls more than once or twice in their code, if at all. As long as it doesn't break the debug rendering for other existing things (like bullet) my vote would be go for it. Just please specify what the orientation is rotating from (I assume a cylinder along the y axis) in the documentation so that users down the line don't have to guess and proceed through trial-and-error.

-------------------------

Leith | 2019-09-20 06:53:45 UTC | #4

Yes, I've retained our convention for the definition of cylinders (origin coincides with center of lower cap, and lateral axis is Y+)... for orienting cylinders, I was happy to provide just a desired direction normal and extrapolate a suitable orientation from that alone, but for oriented boundingboxes, I opted to provide a quaternion. Would it break bullet debug drawing to modify our debugrenderer? I'll have to look closer at the Bullet side to make sure, and would be happy to remedy and rectify any such unintended side-effects.

-------------------------

Modanung | 2019-09-20 10:04:19 UTC | #5

[quote="Leith, post:4, topic:5589"]
I’ve retained our convention for the definition of cylinders (origin coincides with center of lower cap, and lateral axis is Y+)
[/quote]
Cylinder colliders in Bullet as well as Cylinder.mdl *do* have centered origins.

-------------------------

Leith | 2019-09-20 10:30:45 UTC | #6

I am familiar with Bullet, I know Erwin, happy to adapt, as I mentioned

-------------------------

Leith | 2019-09-20 10:34:01 UTC | #7

i disagree with Erwin on some things, if that makes me more relatable, then its true, but genuinely, how many people do i argue with about inertia tensors? ;)

-------------------------

Leith | 2019-09-20 10:35:43 UTC | #8

we agree to disagree, and i agree i can teach a variant

-------------------------

Leith | 2019-09-20 10:36:53 UTC | #9

Erwin and me disagree, on at least two points, and thats fine with me

-------------------------

Leith | 2019-09-20 10:38:55 UTC | #10

Did you test my code? It works... I filled a hole, I do not want praise, just a nod will be fine.

-------------------------

Leith | 2019-09-20 10:43:33 UTC | #11

(I am tipping, he did not bother to test my shit, but let this serve as a warning, if you wish to call me out, be all well armed)

-------------------------

Leith | 2019-09-20 10:49:41 UTC | #12

Erwin does not truly understand tensors, he thinks all tensors can be reduced to a vec3, and thats not actually true, I have tried to talk to him about it, sigh

-------------------------

Modanung | 2019-09-20 10:55:31 UTC | #13

Are you aware of Discource's edit functionality? It would save half the space in this case.

-------------------------

Leith | 2019-09-20 11:27:09 UTC | #14

Possibly, but I am not against people seeing my train of thought and the lead up to a possible solution, its a good thing, in my opinion anyway

-------------------------

Leith | 2019-09-20 11:28:31 UTC | #15

I don't have a lot of time, to sit around and evaluate my own stuff, that should not even be a thing for me, I have a place to publish, or if you consider I am out of place, I will make one, and do it there, starting with 60+ changes I didnt post here

-------------------------

Leith | 2019-09-20 11:30:25 UTC | #16

Believe me, I can do that, in well less than one day, and be online, sharing Yet Another Version, but in C++, and superior to the master branch, I have nothing to lose :)

-------------------------

Leith | 2019-09-20 11:32:10 UTC | #17

I would rather contribute, but the system is not really geared for it, come in as an outsider and look again at it

-------------------------

