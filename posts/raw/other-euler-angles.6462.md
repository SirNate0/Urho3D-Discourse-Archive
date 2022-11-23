SirNate0 | 2020-10-26 22:52:21 UTC | #1

As you may know, Euler angles are one way to represent a rotation, by specifying rotation angles around the X, Y, and Z axes, and then applying all 3 of those rotations. As rotations are not commutative, the different order of you X, Y, and Z rotations form different sets of Euler angles for the same rotation. Urho3D implements one such ordering, but because of how I was forming some rotations in a project of mine, I needed a different decomposition. As such, I wrote some code to give you all 6 possible Euler angles (the permutations of [X,Y,Z]). Though rotations can also be given as a rotation around X, then around Y, then around X again, for example, this latter form I did not handle (however, I include the python code used to generate the C++ code, so those could be added if you had a use for it - just install the cogapp with PIP to use the code generation).

As you can see, I don't specially handle the Gimble-lock sort of cases as the normal code does except for the one ordering that I needed. That said, here's the actual code:

```cpp
// QuaternionRotation.h

#pragma once

#include <Urho3D/Math/Quaternion.h>
#include <array>

std::array<Urho3D::Vector3,6> AllEulerAngles(const Urho3D::Quaternion& q);

Urho3D::Vector3 EulerAnglesYXZ(const Urho3D::Quaternion& q);
```

```cpp
// QuaternionRotation.cpp
#include "QuaternionRotation.h"

using namespace Urho3D;

std::array<Urho3D::Vector3,6> AllEulerAngles(const Urho3D::Quaternion& q)
{
    return {

/*[[[cog
#!/bin/python3

from numpy import *
from sympy import *
#q = [q0, iq1, jq2, kq3]

q0,q1,q2,q3 = symbols('q0 q1 q2 q3')
q0,q1,q2,q3 = symbols('q.w_ q.x_ q.y_ q.z_')
init_printing()

q = [q0,q1,q2,q3]
qi = q[1:]

R = diag(*(q0**2+sum([qx**2 * (1 if i == j else -1) for i,qx in enumerate(qi)]) for j in range(3)))

for i in range(3):
    for j in range(3):
        if i==j:
            continue
        k = [0,1,2]
        k.remove(i)
        k.remove(j)
        k = k[0]
        sgn = 1 if (i+j)%2 == 0 else -1
        sgn *= -1 if i > j else 1
        var = 2*(qi[i]*qi[j] + sgn*q0*qi[k])
        R[i,j] = var

pprint(R)

# that was the homogeneous R
# for inhomogeneous R
R = R + eye(3) * (1 - sum(dot(q,q)))

a,b,c = symbols('a b c')

Rx,Ry,Rz = [rot_axis1(-a),rot_axis2(-b),rot_axis3(-c)]

euler = [Rx,Ry,Rz]

for r in [Rx,Ry,Rz]:
    pprint(r)
    
from itertools import permutations

order = list(range(3))
triples = list(permutations(order))
doubles = list(permutations(order,2))

print(triples)

sines = {s*sin(ang):(ang,s,angidx) for angidx,ang in enumerate([a,b,c]) for s in [-1,1]}
def findSine(mat):
    for i,m in enumerate(mat):
        if m in sines:
            return unravel_index(i,mat.shape),sines[m]

toEulerWithOrder = {}
toEulerWithOrderCpp = {}

for o in triples:
    xyz = ''.join('xyz'[i] for i in o)
    print(xyz)
    Rorder = [euler[i] for i in o]
    Re = prod(Rorder) # prod([A,B,C]) = A*B*C and not C*B*A
    pprint(Re)
    fs = findSine(Re)
    sineRowCol,(angle,signOfSine, angIdx) = fs
    print(fs)
    pprint(R[sineRowCol])
    
    # We have found the sine(angle_i)
    # Now we grab the row and column of the matrix excluding that element to calculate the angles _j and _k
    # angle_j is from the side with no j index and angle_k is from the side with no _k idx. I.e. angle_i would come from the matrix column if C==i
    # the cosine is from the diagonal, and the sine is the other element. Both are multiplied by cos(angle_i).
    allI = {0,1,2} # a set
    Row,C = sineRowCol
    #Rcs = allI - {C}
    #Crs = allI - {R}
    offDiag = (allI - {Row,C}).pop()
    
    # Column
    Cdiag = (C,C)
    CoffDiag = (offDiag,C)
    Cangle = [a,b,c][Row]
    Cangle_i = Row
    Ccos = R[Cdiag]
    Csin = R[CoffDiag]
    
    print(Cangle,Cangle_i)
    pprint(Csin)
    pprint(Ccos)
    
    # Row
    Rdiag = (Row,Row)
    RoffDiag = (Row,offDiag)
    Rangle = [a,b,c][C]
    Rangle_i = C
    Rcos = R[Rdiag]
    Rsin = R[RoffDiag]
    
    print(Rangle,Rangle_i)
    pprint(Rsin)
    pprint(Rcos)
    
    # Construct vector of euler angles
    ea = [0]*3
    ea[angIdx] = signOfSine * asin(R[sineRowCol])
    ea[Rangle_i] = atan2(Rsin,Rcos)#*signOfSine
    ea[Cangle_i] = atan2(Csin,Ccos)#*signOfSine
    
    pprint(ea)
    print(python(ea))
    print(ccode(ea))
    
    def urho(vec):
        import re
        out = []
        for v in vec:
            c = ccode(v)
            cpp=re.sub(r'pow\(([^,]+), 2\)',r'\1*\1',c)
            cpp = cpp.replace('atan2','Atan2').replace('asin','Asin')
            #cpp = re.sub(r'q(\d)','q[\d]')
            out.append(cpp)
        return out
    print(urho(ea))
    
    toEulerWithOrder[xyz] = ea
    toEulerWithOrderCpp[xyz] = urho(ea)
    
    print('')
    
    print('')

pprint(R)

print(toEulerWithOrder)


# confirm ordering
#print(prod([diag(1,0),Matrix([[0,1],[1,0]]),Matrix([[1,2],[3,4]])][::-1]))
#print(prod([diag(1,0),Matrix([[0,1],[1,0]]),Matrix([[1,2],[3,4]])]))
#print(diag(1,0)*Matrix([[0,1],[1,0]])*Matrix([[1,2],[3,4]]))

#print(findSine(Re))
#pprint(Re)

for order in toEulerWithOrderCpp:
    cog.outl(f'//{order}')
    val = ', '.join(toEulerWithOrderCpp[order])
    cog.outl(f'Vector3({val}),')
]]]*/
//xyz
Vector3(Atan2(-2*q.w_*q.x_ + 2*q.y_*q.z_, -2*q.x_*q.x_ - 2*q.y_*q.y_ + 1), Asin(2*q.w_*q.y_ + 2*q.x_*q.z_), Atan2(-2*q.w_*q.z_ + 2*q.x_*q.y_, -2*q.y_*q.y_ - 2*q.z_*q.z_ + 1)),
//xzy
Vector3(Atan2(2*q.w_*q.x_ + 2*q.y_*q.z_, -2*q.x_*q.x_ - 2*q.z_*q.z_ + 1), Atan2(2*q.w_*q.y_ + 2*q.x_*q.z_, -2*q.y_*q.y_ - 2*q.z_*q.z_ + 1), Asin(2*q.w_*q.z_ - 2*q.x_*q.y_)),
//yxz
Vector3(Asin(2*q.w_*q.x_ - 2*q.y_*q.z_), Atan2(2*q.w_*q.y_ + 2*q.x_*q.z_, -2*q.x_*q.x_ - 2*q.y_*q.y_ + 1), Atan2(2*q.w_*q.z_ + 2*q.x_*q.y_, -2*q.x_*q.x_ - 2*q.z_*q.z_ + 1)),
//yzx
Vector3(Atan2(-2*q.w_*q.x_ + 2*q.y_*q.z_, -2*q.x_*q.x_ - 2*q.z_*q.z_ + 1), Atan2(-2*q.w_*q.y_ + 2*q.x_*q.z_, -2*q.y_*q.y_ - 2*q.z_*q.z_ + 1), Asin(2*q.w_*q.z_ + 2*q.x_*q.y_)),
//zxy
Vector3(Asin(2*q.w_*q.x_ + 2*q.y_*q.z_), Atan2(-2*q.w_*q.y_ + 2*q.x_*q.z_, -2*q.x_*q.x_ - 2*q.y_*q.y_ + 1), Atan2(-2*q.w_*q.z_ + 2*q.x_*q.y_, -2*q.x_*q.x_ - 2*q.z_*q.z_ + 1)),
//zyx
Vector3(Atan2(2*q.w_*q.x_ + 2*q.y_*q.z_, -2*q.x_*q.x_ - 2*q.y_*q.y_ + 1), Asin(2*q.w_*q.y_ - 2*q.x_*q.z_), Atan2(2*q.w_*q.z_ + 2*q.x_*q.y_, -2*q.y_*q.y_ - 2*q.z_*q.z_ + 1)),
//[[[end]]]
    };
}

Vector3 EulerAnglesYXZ(const Quaternion &q)
{
    float sine = 2*q.w_*q.x_ - 2*q.y_*q.z_;
    if (sine > 0.9995f)
        return Vector3(90,
                       0,
                       Atan2(2*q.w_*q.z_ + 2*q.x_*q.y_, -2*q.x_*q.x_ - 2*q.z_*q.z_ + 1)
                    );
    else if (sine < -0.9995f)
        return Vector3(-90,
                       0,
                       -Atan2(2*q.w_*q.z_ + 2*q.x_*q.y_, -2*q.x_*q.x_ - 2*q.z_*q.z_ + 1)
                    );
    return Vector3(Asin(sine),
                   Atan2(2*q.w_*q.y_ + 2*q.x_*q.z_, -2*q.x_*q.x_ - 2*q.y_*q.y_ + 1),
                   Atan2(2*q.w_*q.z_ + 2*q.x_*q.y_, -2*q.x_*q.x_ - 2*q.z_*q.z_ + 1));
}
```

-------------------------

