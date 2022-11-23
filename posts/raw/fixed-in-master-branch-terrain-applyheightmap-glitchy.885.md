gawag | 2017-01-02 01:03:48 UTC | #1

Sometimes ApplyHeightMap() doesn't update the terrain at all or just some of the affected chunks:

[img]http://i.imgur.com/vupmRNG.jpg[/img]

Sometimes it updates them after doing more changes, other times it keeps stuck in that half-updated-state.

This is my code:
[code]
IntVector2 v=terrain->WorldToHeightMap(cameraNode_->GetWorldPosition());
Image* i=terrain->GetHeightMap();
for(int x=-10;x<10;x++)
    for(int y=-10;y<10;y++)
        i->SetPixel(v.x_+x,v.y_+y,i->GetPixel(v.x_+x,v.y_+y)+Color(0.1,0.1,0.1));
terrain->ApplyHeightMap();
[/code]
I'm using Urho 1.32. Is that an issue with Urho or am I doing something wrong?

-------------------------

cadaver | 2017-01-02 01:03:48 UTC | #2

The algorithm for determining update region expands it only 1 pixel, so it seems possible the coarser LODs of neighbor patches may not get updated. This should be possible to fix in the master branch.

EDIT: when I change the whole heightmap with smoothing enabled, I see the update taking rather long (longer than it should) and it will glitch in a diagonal line.

-------------------------

cadaver | 2017-01-02 01:03:48 UTC | #3

Should be fixed now in the master branch. The worst-case partial update performance was quite atrocious (a stall of several seconds for a 1025x1025 heightmap), now it should be much faster.

-------------------------

gawag | 2017-01-02 01:03:49 UTC | #4

So my code should work with the newest version? Going to check that later and post the result here.
Thanks for the quick fix!

I had smoothing enabled and the update had no noticeable lag.

-------------------------

gawag | 2017-01-02 01:03:49 UTC | #5

I'm getting an error and a warning while generating build files with CMake-GUI (freshly cloned Urho).
Update:
Whoops my mistake. I had selected the "Source" folder as the source code location inside CMake-GUI. That made really weird stuff. Urho is building now.

-------------------------

gawag | 2017-01-02 01:03:52 UTC | #6

Wow that was a lot of work...
Building the newest Urho from Git wasn't that difficult, but building my project with that... Wow!
Had to change my CMake file because the path to this CMake common file has changed and had to change every include path (the old one were weird but worked somehow). Also had to set more paths manually in CMake-GUI.
I also had to add a line to the top of Urho3D/Container/LinkedList.h:
[code]
#pragma once
#define URHO3D_API            // <- added (yeah dirty fix)
namespace Urho3D
{
/// Singly-linked list node base class.
struct URHO3D_API LinkedListNode
{
    /// Construct.
    LinkedListNode() :
        next_(0)
    {
    }

    /// Pointer to next node.
    LinkedListNode* next_;
};
...
[/code]
Seems like URHO3D_API wasn't defined and I got several errors because of that:
[code]
In file included from S:/dev/git_urho3d/Build/include/Urho3D/Core/../Core/Object.h:25:0,
                 from S:/dev/git_urho3d/Build/include/Urho3D/Core/CoreEvents.h:25,
                 from S:\dev\git_sh_urho3d\Source\main.cpp:20:
S:/dev/git_urho3d/Build/include/Urho3D/Core/../Core/../Container/LinkedList.h:28:19: error: variable 'Urho3D::URHO3D_API Urho3D::LinkedListNode' has initializer but incomplete type
 struct URHO3D_API LinkedListNode
                   ^
S:/dev/git_urho3d/Build/include/Urho3D/Core/../Core/../Container/LinkedList.h:31:22: error: expected '}' before ':' token
     LinkedListNode() :
                      ^
S:/dev/git_urho3d/Build/include/Urho3D/Core/../Core/../Container/LinkedList.h:31:22: error: expected ',' or ';' before ':' token
S:/dev/git_urho3d/Build/include/Urho3D/Core/../Core/../Container/LinkedList.h:37:5: error: 'LinkedListNode' does not name a type
     LinkedListNode* next_;
     ^
S:/dev/git_urho3d/Build/include/Urho3D/Core/../Core/../Container/LinkedList.h:170:1: error: expected declaration before '}' token
 }
 ^
[/code]
(I'm using Urho as a static lib so I think it's defined to empty anyway, if it's defined)

But now my project is building and running again.
The terrain issues are all gone!
No more forgotten or half updates!

-------------------------

weitjong | 2017-01-02 01:03:52 UTC | #7

That's the common pitfall when migrating old codes to the master branch with new build system. See the updated documentation on how the new include statement should look like here. [urho3d.github.io/documentation/H ... nFramework](http://urho3d.github.io/documentation/HEAD/_main_loop.html#MainLoop_ApplicationFramework). The first include "#include <Urho3D/Urho3D.h>" is the one responsible for defining the URHO3D_API preprocessor macro.

-------------------------

