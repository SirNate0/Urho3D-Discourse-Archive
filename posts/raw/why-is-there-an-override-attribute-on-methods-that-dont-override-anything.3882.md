S.L.C | 2017-12-25 23:30:51 UTC | #1

With the migration to C++11, I've noticed that the `override` keyword was added to various methods in the engine (github.com/urho3d/Urho3D/pull/2108). Even for methods that don't override anything. Which is weird, because the engine compiles just fine within its own the build system. But as soon as you try the same thing outside of that, you get compile-time errors like `error: 'virtual bool Urho3D::Example::Dummy(...)' marked 'override', but does not override`.

The simplest one I would encounter:
```c++
struct btVector3;

class Component {
public:
    virtual ~Component();
};

class PhysicsWorld : public Component {
public:

    virtual ~PhysicsWorld() override;

    virtual bool isVisible(const btVector3& aabbMin, const btVector3& aabbMax) override;
};
```

Seen in action here: https://godbolt.org/g/rTNmb4

Is there a particular flag applied to the compiler that I'm not aware of? I wasn't able to find anything about this.

-------------------------

artgolf1000 | 2017-12-26 00:28:39 UTC | #2

In c++11, if you use keyword of 'override', you must implement the method.
So the method of isVisible(...) must be implemented.

-------------------------

S.L.C | 2017-12-26 00:30:57 UTC | #3

The error is still there: https://godbolt.org/g/CKkVCd

```c++
struct btVector3;

class Component {
public:
    virtual ~Component();
};

class PhysicsWorld : public Component {
public:

    virtual ~PhysicsWorld() override;

    virtual bool isVisible(const btVector3&, const btVector3&) override
    {
        return false;
    }
};
```

-------------------------

SirNate0 | 2017-12-26 02:33:40 UTC | #4

It's not an error because PhysicsWorld also inherits from class btIDebugDraw which declares isVisible.

-------------------------

artgolf1000 | 2017-12-26 03:00:23 UTC | #5

Two ways:

struct btVector3;
  
class Component {
public:
    virtual ~Component();
    virtual bool isVisible(const btVector3&, const btVector3&);
};

class PhysicsWorld : public Component {
public:

    virtual ~PhysicsWorld() override;

    virtual bool isVisible(const btVector3&, const btVector3&) override
    {
        return false;
    }
};

or

struct btVector3;
  
class Component {
public:
    virtual ~Component();
};

class PhysicsWorld : public Component {
public:

    virtual ~PhysicsWorld() override;

    virtual bool isVisible(const btVector3&, const btVector3&)
    {
        return false;
    }
};

-------------------------

S.L.C | 2017-12-26 03:22:59 UTC | #6

Oh now I see. I didn't notice this because I updated the Bulled library which did not have that method. And I couldn't figure out what it was trying to overload. Should've known it was something like this. Thank you.

```c++
	// Urho3D: added function to test visibility of an AABB
	virtual bool    isVisible(const btVector3& aabbMin,const btVector3& aabbMax)=0;
```

-------------------------

Modanung | 2017-12-27 11:28:27 UTC | #7

As I understand the `virtual` and `override` keywords:
- only the base function _needs_ the `virtual` keyword
- `override` should be used on all functions that override it
- **If both keywords are used on a single method, either is redundant**


Also this class...
```
class Component {
public:
    virtual ~Component();
};
```
...has no `isVisible` function that could be overridden. Can't argue with the compiler on that one. ;)

-------------------------

