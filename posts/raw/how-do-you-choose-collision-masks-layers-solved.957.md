practicing01 | 2017-01-02 01:04:27 UTC | #1

Hello, I need walls to be in one group, players in another (that will collide with walls but not collide with other players) and I need to do a physics raycast that will hit the walls but not the players.  What layer/mask combo do I need to specify for walls and players in the editor?  How do I calculate the unsigned int mask needed by the raycast method?  Thanks for any help. Edit: Thanks, that worked.

-------------------------

jmiller | 2019-11-05 06:44:53 UTC | #2

Because this thread deserved its answers, even if @practicing01 lurks...

```
#include <Urho3D/Container/FlagSet.h>

enum class Flag : unsigned int {
  none = 0
  , env = (1 << 0), obj = (1 << 1), character = (1 << 2), particle = (1 << 3), projectile = (1 << 4)
  , all = Urho3D::M_MAX_UNSIGNED
};
/* bit shift expression to binary (digits presumably corresponding to editor checkboxes)
1 << 0 == 000001 (01) 
1 << 1 == 000010 (02) 
1 << 2 == 000100 (04) 
1 << 3 == 001000 (08) 
1 << 4 == 010000 (16) 
1 << 5 == 100000 (32) 
*/

// Using Urho3D FlagSet without macros.
namespace Urho3D {
  /// Type trait which enables Enum to be used as FlagSet template parameter. Bitwise operators (| & ^ ~) over enabled Enum will result in FlagSet<Enum>.
  template<> struct IsFlagSet<ObjectLayer> {
    inline static constexpr bool value_ = true;
  };
}
using Flags = Urho3D::FlagSet<Flag>;

// ...

// Raycast query for not character or particle or pickup or projectile.
Flags viewMask(~(Flag::character|Flag::particle|Flag::pickup|Flag::projectile));

RayOctreeQuery query(results, revRay, RAY_TRIANGLE, distance, DRAWABLE_GEOMETRY, viewMask);
```

-------------------------

Modanung | 2017-09-18 01:48:24 UTC | #3

You could also add the following constexpr somewhere:
```
constexpr unsigned Layer(unsigned x) { return 1 << (x - 1); }
```
This would allow you to write `Layer(1) + Layer(3)`, for example, to create a layer mask.

-------------------------

Enhex | 2017-09-17 16:54:54 UTC | #4

Note that you can use a constexpr function instead of a macro.

-------------------------

Modanung | 2017-09-17 20:43:11 UTC | #5

Noted and edited. :flight_arrival:

-------------------------

