freegodsoul | 2017-01-02 01:08:29 UTC | #1

Hello, Devs!

I think math library of Urho3D really needs in some improvements.
Here is my proposal draft about some useful additions to the lib.
The proposal consists of three parts which may refer to each other.

[size=150][b]1. Subscript [] operator[/b][/size]

Ability to access to elements of Vectors and Matrices by subscript [] operator. Vectors must return float reference and Matrices - major-vector reference. Usage example:
[code]Matrix3x3 m; 	// create matrix
... 			// fill matrix with some initial values
m[2][1] = 1.0f;	// element at [row:3, col:2] will be modified,
m[0].z = 5.0f;	// element at [row:1, col:3] will be modified ("z" was used instead of "z_" since Part 2)
// cross product will be accomplished between first and second rows of matrix
Vector3 cross = m[0].Cross( m[1] ); // "Cross" instead of "CrossProduct" since Part 3[/code]
	
e.g implementation for Vector3:
[code]const float& operator [] ( int i ) const
{
	return ( &x_ )[ i ];
}
float& operator [] ( int i )
{
	return ( &x_ )[ i ];
}[/code]
	
e.g. implementation for Matrix3x3:
[code]const Vector3& operator [] ( int i ) const
{
	return ( ( const Vector3* ) &m00_ )[ i ];
}
Vector4& operator [] ( int i )
{
	return ( ( Vector3* ) &m00_ )[ i ];
}[/code]

Full list of classes, which should support subscript [] operator:
[code]Vector2
Vector3
Vector4
IntVector2
Matrix3
Matrix3x4
Matrix4
Color
Quaternion (Under doubt, because I've never used quaternions directly through member variables, but only via methods and Euler-values)[/code]

[size=150][b]2. Shorthands for useful member variables[/b][/size]

Ability to access to public fields of high-usage classes through short notation, e.g. "x", "y" and "z" for Vector3 instead of "x_", "y_", "z_".
This part can be considered as continuation of thread, that i've created earlier: [url]http://discourse.urho3d.io/t/math-shorter-aliases-for-public-fields-of-core-classes/1546/1[/url]

I offer to introduce an additional rule into coding conventions ([url]http://urho3d.github.io/documentation/HEAD/_coding_conventions.html[/url]), because it seems to be reasonable:
[i]If class considered as POD and *high-usage*, if it has only public member fields (examples: Vector3, Color, Ray), then there must be *Shorthands* or *Properties* or *Aliases* (call as you want) for standard member variables in notation: lower-camelcase, have [b]NOT[/b] an underscore appended.[/i]
		
For example, that how could be declared and documented member variables of Vector2:
[code]union
{
	/// X coordinate.
	float x_;
	/// [Shorthand] X coordinate.
	float x;
};
union
{
	/// Y coordinate.
	float y_;
	/// [Shorthand] Y coordinate.
	float y;
};[/code]

or Ray:
[code]union
{
	/// Ray origin.
	Vector3 origin_;
	/// Same as origin_
	Vector3 o;
};
union
{
	/// Ray direction.
	Vector3 direction_;
	/// Same as direction_
	Vector3 d;
};[/code]
		
With [b]union [/b]statements there is no conflict or conformance exception with fifth rule in Coding conventions:
[quote]Variables are in lower-camelcase. Member variables have an underscore appended. For example numContacts, randomSeed_.[/quote]
What I'm offering is just an [b]addition[/b] to already existed rules.
		
List of classes (in my opinion) which should have shorthands by default:
[code]Vector2
Vector3
Vector4
IntVector2
IntRect
Color
Rect
Ray
Plane
Sphere
BoundingBox
[/code]
Under doubt:
[code]Quaternion[/code]
Unnecessary since Part 1:
(as matrices usually considered as (two-dimensional) arrays and it is more logically to access to their elements through index)
[code]
Matrix3
Matrix3x4
Matrix4[/code]

[size=150][b]Part 3. Shorter methods[/b][/size]

Also it is may be useful to use shorter names for classic methods like
[code]v1.Dot( v2 );
v1.Cross( v2 );[/code]
instead of
[code]v1.DotProduct( v2 );
v2.CrossProduct( v2 );[/code]
Because they can't be confused with something else.

[size=150][b]Conclusion[/b][/size]

My current modification of the math library which I'm using: [url]http://gdurl.com/148O[/url]
It's not a final proposal, but an opening point for discussion and suggestions. I really like the Urho3D and want it to be even better.
I thought about making a pull request as guy with nick [b]franck22000[/b] advised me, but I've never did make it before. So in order to not spend time for reading git help I've decided just to create this thread, as I think every day Urho3D have new user and we can save him from PITA :smiley:

-------------------------

codingmonkey | 2017-01-02 01:08:30 UTC | #2

I guess this extremely short names produce code's low informativity then you see code first time

[code]   union
    {
        /// Ray origin.
        Vector3 origin_;
        /// [Shorthand] Ray origin.
        Vector3 o;
    };
    union
    {
        /// Ray direction.
        Vector3 direction_;
        /// [Shorthand] Ray direction.
        Vector3 d;
    };
};[/code]

Why not just?

Vector3 dir
Vector3 orig

at last just omit this underscore at the end will be also nice

Vector3 direction
Vector3 origin

i want mention what only underscores as the end are my "pain" and not lenth of names.

-------------------------

freegodsoul | 2017-01-02 01:08:30 UTC | #3

[quote="codingmonkey"]I guess this extremely short names produce code's low normativity then you see code first time

[code]   union
    {
        /// Ray origin.
        Vector3 origin_;
        /// [Shorthand] Ray origin.
        Vector3 o;
    };
    union
    {
        /// Ray direction.
        Vector3 direction_;
        /// [Shorthand] Ray direction.
        Vector3 d;
    };
};[/code]

Why not just?

Vector3 dir
Vector3 orig

at last just omit this underscore at the end will be also nice

Vector3 direction
Vector3 origin

i want mention what only underscores as the end are my "pain" and not lenth of names.[/quote]

Simply omitting underscore will be OK too. Here I just wanted to show more variants than one and see what people think about it. Because of ray has so simple structure, and due to a fact that people who using 3D game engine have at least school math background, why not to use mathematically-conventional concepts as names like "O" for origin or "D" for direction vector, but in lowercase. It's hard to confuse it with something else.

-------------------------

thebluefish | 2017-01-02 01:08:31 UTC | #4

[quote="freegodsoul"]due to a fact that people who using 3D game engine have at least school math background[/quote]

You're presuming a lot with that line. Truth be told, a lot of people getting into game dev do NOT have high mathematics education. Sure there's a lot of devs who are math geniuses, but not all. For example, I barely cleared Algebra.

-------------------------

billyquith | 2017-01-02 01:09:54 UTC | #5

I think the math library is fine as it is. Longer, explanatory variables are good practice, they make code more readable. There are other suggestions to rename the math library, but they generally aim at changing the names to a users individual preference. Soon, someone else will suggest changes that they like, but you don't. Also, most editors have code completion these days so this can save a lot of typing.

You should be careful with C/reinterpret casting like that in C++ as it tends to inhibit the compiler from making certain optimisations. It confuses the aliasing. Always use a union where possible.

-------------------------

