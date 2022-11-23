Rolf | 2018-05-23 02:56:04 UTC | #1

Hello,

I have a question about how Urho deals with rotation through Quaternions and Matrices. I just don't understand it anymore after looking at it for a long time.

So given the conventions: https://urho3d.github.io/documentation/1.7/_conventions.html

It says 'positive rotation is clockwise'. I think this means if you look from the origin in the direction of the axis.

So I put 90 degrees on X:

Urho3D::Quaternion test;
test.FromEulerAngles(90.f, 0.f, 0.f);

Now I convert it to a Rotation matrix:
Urho3D::Matrix4 test_mat = test.RotationMatrix();

Now, I want to convert a vector that's aiming UP, so: 0, 1, 0.

Urho3D::Vector3 test_vec(0,1,0);

Now I'm gonna rotate that vector 90 degrees over the X axis. You'd expect it to be -1 on Z right? wrong, it becomes +1 on Z.

Urho3D::Vector3 result2 = test_mat * test_vec;

What's happening? It makes no sense.

Thanks for reading.

edit: I've just come to the conclusion that the convention is just lying, and it is actually following DirectX convention where rotation is negative angles (so looking from the axis towards the origin).

Furthermore, you guys should probably add in the conventions that matrices are stored in memory in column-major order. It's specified nowhere but it's kind of crucial to know. Also, the operator* on matrix4 class that takes vector3/vector4 are treating the vector as row-major vector, but mathematical convention is that M*v means that the vector is a column vector. Again, this crucial info is specified nowhere in your documents.

-------------------------

SirNate0 | 2018-05-23 03:42:39 UTC | #2

You have a point that the direction we consider (counter)clockwise should probably be specified in the docs for additional clarity, but I'm pretty sure usual convention would be to look from the positive direction of the axis towards the origin. My understanding is usually we use a right handed coordinate system and counterclockwise angles, where if you look down at the xy plane positive goes from +x to +y (for a +90 degree angle), and in this z would be out. In any case I find it much easier to use the left-hand rules to remember how things should be. In my case (though this may deviate from normal), thumb is x, index finger is y, points up, and middle finger is z. For angles, thumb goes in the + direction along the vector, fingers curl in the positive angular direction around it.

As to the ordering of the matrices, I may be wrong, as I don't really work with them for what I do, but I'm pretty sure they are stored in memory in row-major ordering. Take the Matrix3x4 class - this would be a matrix with 3 rows and 4 columns, right? The elements are stored in the order (based on a quick glance at the header file) "m00_, m01_, m02_, m03_, m10_,...", which I read as "m[row][col]_". I'm pretty sure this would be a row-major ordering for the matrices, and thus treats the vector as a column vector like normal.

I hope that helps, and do correct me if I'm wrong!

-------------------------

Rolf | 2018-05-23 13:01:31 UTC | #3

Hello,

The m03, m13 and m23 of matrix4 stores the translation. In a row-major left handed system it would be m30, m31, m32. So that’s why I am saying it must be column-major. However I am confused about the rotation part.

If I look at Quaternion::RotationMatrix() cpp file I can see that it’s storing the data like so:
https://math.stackexchange.com/questions/1631807/rotation-to-quaternion-matrix-handeness

So that’s like as if the Matrix4 contains row-major rotation data but column-major translation data for a left handed system. (memory layout)

If I look at D3DXMatrixRotationQuaternion it’s building a transposed matrix compared to the Urho3D one.
https://doxygen.reactos.org/de/d57/dll_2directx_2wine_2d3dx9__36_2math_8c_source.html

So I’m totally confused regarding who is right and who is wrong. Because dx says its left handed system, rowmajor. Urho says its left handed, but stores the rotation matrix transposed compared to the dx one, however according to wikipedia its the correct way for a left handed system (what the?).

Finally, I was saying that the matrix operator* acts like its a row vector because the memory layout of the matrix is column-major. So even though mathematically the operator method is treating the input like a column vector, its still computed finally as a row vector because the memory layout of the matrix is column-major (at least the translation part is). For a left handed system.

Hope someone can clarify what’s going on with the rotation...

-------------------------

Eugene | 2018-05-23 13:43:10 UTC | #4

[quote="Rolf, post:3, topic:4255"]
In a row-major left handed system it would be m30, m31, m32. So that’s why I am saying it must be column-major
[/quote]

Matrices layout is sometimes tricky question.
There are two different but very similar things.

**Row/column vectors** is the question of math.
In few words, you shoud either write `vector(x, y, z) * makeTranslation(a, b, c)` or `makeTranslation(a, b, c) * vector(x, y, z)` while using some specific library. Urho has **column vectors**.

**Row/column majority** is the question of matrix memory layout. It has nothing to do with math, and the user of the library may be even not aware if he use row-major and column-major matrices. Urho has **row-major matrices**.

For example, there's a formula for vector translation for **column vectors** (I hope you know how this formula would look like for row vectors)
```
[ 1, 0, 0, a ]   [x]   [x + a]
[ 0, 1, 0, b ]   [y]   [y + b]
[ 0, 0, 1, c ]   [z]   [z + c]
[ 0, 0, 0, 1 ] * [1] = [  1  ]
```

Now, you could store this specific matrix as either row major
`[1, 0, 0, a; 0, 1, 0, b; 0, 0, 1, c; 0, 0, 0, 1]`
or column major
`[1, 0, 0, 0; 0, 1, 0, 0; 0, 0, 1, 0; a, b, c, 1]`

Some people highly distingush these two conventions.
Other people mix them and call matrix math with row vectors "row major" and with column vectors "column major". This may be simpler, but isn't really correct.

When you read any matrix-related docs you should be aware what exactly the author means and how he writes his formulas.

-------------------------

Rolf | 2018-05-23 15:21:55 UTC | #5

Urho3D stores is matrixes in memory like this:

> [1, 0, 0, a; 0, 1, 0, b; 0, 0, 1, c; 0, 0, 0, 1]

(abc = translation)

So basicly transposed compared to the DirectX way (and OpenGL way also afaik).

Now, in Urho3D, the matrix4 operator* that takes a vector3 or vector4, computes correctly.

> [ 1, 0, 0, a ]   [x]   [x + a]
> [ 0, 1, 0, b ]   [y]   [y + b]
> [ 0, 0, 1, c ]   [z]   [z + c]
> [ 0, 0, 0, 1 ] * [1] = [  1  ]

In DirectX, you can't do
v_transformed = M * v

In DirectX, you have to do D3DXVec3TransformCoord which is basicly
v_transformed = v * M

However, in Urho3D, you can do M * v because Urho3D stores the matrix layout in transposed way compared to DirectX (like specified above).

So basicly
Urho3D M * v == DirectX v * M

Which is not specified anywhere in Urho3D docs. Shouldn't it be mentioned somewhere??
https://urho3d.github.io/documentation/1.7/_conventions.html

Finally in my opinion the conventions should also be clearly specifying that angles are measured as looking from the axis towards the origin. The Urho3D convention states "positive rotation is clockwise" which sounds like it means looking from the origin in the direction of the axis and then going clockwise, but that's not at all how Urho3D works.

-------------------------

Eugene | 2018-05-23 16:14:49 UTC | #6

[quote="Rolf, post:5, topic:4255"]
Which is not specified anywhere in Urho3D docs. Shouldn’t it be mentioned somewhere??
[/quote]

This is default math notation. Probably it's better to be mentioned somewhere tho.

-------------------------

Rolf | 2018-05-23 16:56:43 UTC | #7

In Urho3D are matrices calculated like this?
1. m_mvp = m_proj * m_view * m_world

or DirectX way:
2. m_mvp = m_world * m_view * m_proj

I'm guessing the first way because the matrices are transposed in Urho3D compared to the DirectX way.

So a vector is translated like this in Urho3D:
v_transformed = m_proj * m_view * m_world * v

DirectX:
v_transformed = v * m_world * m_view * m_proj

However inside hlsl shaders both use the same convention:
mul(vector, matrix)

-------------------------

