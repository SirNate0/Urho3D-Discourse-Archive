Leith | 2019-02-10 02:23:41 UTC | #1

When instantiating new object instances, our object factory implementation (see Core/Object.h) does not automatically initialize any Attributes to the default values that we declared via URHO3D_ATTRIBUTE macro. Professional programming standards mandate that we ought to initialize everything ourselves, yet it is a very common mistake to forget to do that, which leads to all kinds of problems that can be difficult to trace, such as the application crashing randomly.
I thought it would be nice if our factory checked for registered attributes, and if found, applied them for us.

I propose the following extension to ObjectFactoryImpl::CreateObject( )
[code]
    /// Create an object of the specific type.
    SharedPtr<Object> CreateObject() override {
        T* rawptr = new T(context_);

        /// Check if the object derives from Serializable
        Serializable* casted = dynamic_cast<Serializable*>(rawptr);
        if(casted!=nullptr)
        {
            /// Initialize local attributes to default values
            const Vector<AttributeInfo>* attribs = context_->GetAttributes(GetType());
            if(attribs!=nullptr){
                for(int i=0;i<attribs->Size();i++)
                {
                    const AttributeInfo& info = attribs->At(i);
                    info.accessor_->Set(casted, info.defaultValue_);
                }
            }
            /// Initialize network attributes to default values
            attribs = context_->GetNetworkAttributes(GetType());
            if(attribs!=nullptr){
                for(int i=0;i<attribs->Size();i++)
                {
                    const AttributeInfo& info = attribs->At(i);
                    info.accessor_->Set(casted, info.defaultValue_);
                }
            }
        }
        return SharedPtr<Object>(rawptr);
    }
[/code]

Note that you'll also need to include Attribute.h at the top of the Object.h file
I've tested this code in my current project, it's stable there, but I have not tested more widely.
You'll still have to initialize any unserialized members yourself, but at least you can rest assured that any serialized attributes will be initialized "automagically".

Oh, and worth mentioning that since this is a templated method, appearing in a header file, the changes can be tested without needing to rebuild the engine.

-------------------------

dertom | 2019-02-10 13:12:31 UTC | #2

I'm not sure what you are doing? Are you writing an object-class without setting the object values to proper values in the constructor? If yes, don't you have a bad feeling about this in the first place? ;)

I'm not that much of an urho3d power user, but I think the usual "method" is to have constants with the default values in your object's .cpp-file that you use to initialize the value in the constructor(!) and(!) to use in the attribute-definition. 
What I think is that the attribute's default-value is mainly to dermine if you need to serialize this value rather than setting it. It is more like, "I'm sure that the default value is exactly this value so I can skip writing this to file when the value is exactly the default value at the moment".  Not 100% sure though....

-------------------------

Sinoid | 2019-02-10 19:37:58 UTC | #3

Would be fine as a debug build exclusive check that raises an error when defaults don't match.

Not a fan of it otherwise.

---

Also, you're not calling `ApplyAttributes`.

-------------------------

Leith | 2019-02-10 23:47:20 UTC | #4

I wasn't aware I needed to call ApplyAttributes, given there are no changes that can't be applied immediately, and given that the object is new, and so not part of any scene yet ;)

-------------------------

Sinoid | 2019-02-11 00:51:11 UTC | #5

You're mass-setting attributes. If you don't call it then you're just setting up the scaffolding for someone's annoying bug to hunt for in the future.

Presently the only place anything *may* (probably doesn't) care about it in this **exact** instance would be stuff in UI.

All bets are off with anyone's custom component attributes (especially those that may interact with Subsystems) having dependency on `ApplyAttributes` which if they're relying on already then they're doing it right.

---

If this sort of init-at-creation thing was done, you'd want to add another attribute flag to exempt a field from being subjected to it.

-------------------------

Leith | 2019-02-11 06:19:00 UTC | #6

I'm still trying to wrap my head around the idea that setting attribute defaults, to the defaults we provided, is a bad idea - I'm struggling with the notion that this is somehow harmful. Generally we can't initialize everything in the constructor, because the object is not part of a scene, and has no connectivity in the scenegraph, so we can only initialize to a certain degree there. Therefore it appears harmless that we should enforce our defaults (I repeat, the ones we declared) just after construction, and just before the new object is returned. What could possibly go wrong? Why would you wish to exempt an attribute from receiving the default value you provided?

-------------------------

johnnycable | 2019-02-11 12:43:48 UTC | #7

Some attributes are mandatory just in some cases. Maybe the problem is telling the difference among them. That's build dependent (with or without networking) and so on. 
So some error check should exist at compile time if some mandatory attribute, dependent on the build features we chose, are missing.
That would require tell apart the Urho data structure, build check a specific setup, for some compile check to go on... I think you got the picture.

-------------------------

Sinoid | 2019-02-12 03:18:29 UTC | #8

- It's a work-around for what is a bug
    - If a type isn't correctly initialized, that's a bug
    - effectively you're patching out bug at runtime
    - thus, report them in debug builds - don't patch them out
- `ApplyAttributes` is how components deal with things that are dependent on more than a single attribute
    - if you don't call it then you're still incompletely initialized, which is the problem you're attempting to patch out
- It creates a lot of extra work during a scene load just for patching-bugs-at-runtime
    - Attribute access isn't free and if you have a scene with 1000 StaticModel's then you'll also be querying for the ResourceCache 2000 times - to do nothing with it
        - obviously, profile and see if it really is meaningful
    - Scene loading is already slow enough as it is due to fat components if you're not using StaticModelGroup, cooking, or have rewritten serialization to have a flat attribute-free route

-------------------------

Leith | 2019-02-12 03:21:22 UTC | #9

I agree it adds work, and counter that we should not be creating new objects often.
I could easily wrap both the original and updated versions in macros, and let the user choose which to use, perhaps based on the presence of a debug define?

-------------------------

Sinoid | 2019-02-12 03:21:33 UTC | #10

It would be more palatable as a build flag to switch between a safety check or forced correction. Which shouldn't be much of an issue since it's not a large block of code to blit attributes like this.

-------------------------

Leith | 2019-02-12 03:22:50 UTC | #11

In debug mode, we expect more than we do in release - we expect some amount of initialization, nothing is random in debug mode

-------------------------

Leith | 2019-02-12 03:24:51 UTC | #12

this is something I am often asked - why does my debug version run fine, but the release version crashes randomly? its ALWAYS uninitialized stuff.

-------------------------

Sinoid | 2019-02-12 03:32:23 UTC | #13

I'm using `debug build` too willy-nilly so you're not tracking, only in the last remark did I specifically state **build flag** as I should have been stating the entire time.

Actual debug build's are pointlessly slow - disable optimization on whatever blocks are in question in a release build, far faster to track down an issue when you aren't impeded.

-------------------------

Leith | 2019-02-12 03:37:34 UTC | #14

If its not a debug build, theres no debug symbols, so debugging/tracing issues is virtually impossible - there is a huge gap between what we get in debug, and what happens in release, but the main thrust of the issue, is what we forgot to initialize.
I second your motion about warnings.

-------------------------

Sinoid | 2019-02-12 03:37:17 UTC | #15

You never ever ship or use a build that isn't w/ symbols. You never ever ship without having your symbol server set up.

I've stated all I have to say on the matter, and since my fork is so greatly diverged that it's a hassle to merge master it really doesn't matter a whole lot to me - so I'm stopping here.

-------------------------

Leith | 2019-02-12 03:39:51 UTC | #16

Perhaps I should not be applying the default value we defined, but emitting a warning when the defined value at runtime was not the same as the one we defined. This lets the constructor do its best, and notifies us when things are not in the state we expected.

-------------------------

Leith | 2019-02-12 03:41:41 UTC | #17

Please don't stop here, and I would rather not create a new fork, I want to contribute to the core. I'm interested in the things that hold us back, the common issues, the ones we can address.

-------------------------

Sinoid | 2019-02-12 04:40:41 UTC | #18

There's no new fork involved, I have a private fork that's from before the ResourceMetaData nonsense (quite a long time ago).

I just have nothing further to add to the discussion and I'm sufficiently diverged that it's a thing I can cherry-pick around.

-------------------------

