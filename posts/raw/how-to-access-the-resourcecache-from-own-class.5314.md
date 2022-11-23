wakko | 2019-07-19 17:50:44 UTC | #1

Hello, 
I am still working on this project: [FSDefender](https://discourse.urho3d.io/t/fsdefender-filesystem-flight-mechanics/4240) and before implementing new stuff I would like to clean up some things.
One problem I have is to access the ResourceCache from my own classes.
My original workaround was to have a class member of that type and pass a pointer as a function argument which had to be called after the the constructor.

        // purpose of this class is to change the skybox texture upon entering a new directory
        #include <Urho3D/Graphics/Skybox.h>
        #include <Urho3D/Resource/ResourceCache.h>
        using namespace Urho3D;
        class FSDSkybox
        {
        private:
            ResourceCache*    m_cache;
            Node*             m_parent;
            Node*             m_skyboxNode;
            Skybox*           m_skybox;
            static Material*  m_canyonMaterial;
            static Material*  m_spaceMaterial;
        public:
            FSDSkybox();
            void init(Node* parent_, ResourceCache* cache_);
            void updateMaterial();
        };
However I am sure there must be a better way to do that. I have once tried to inherit from component but it didn't help.

-------------------------

Pencheff | 2019-07-19 18:47:36 UTC | #2

Store Urho3D::Context pointer inside your class, you can access anything Urho3D related from it. If you are just going to use ResourceCache, your approach seems OK. Best way however is to inherit Urho3D::Object.

-------------------------

Modanung | 2019-07-19 21:44:26 UTC | #3

Indeed when inheriting from `Object` you have `GetSubsystem<T>()` at your disposal where `T` would be the `ResourceCache` in this case.

-------------------------

Leith | 2019-07-20 05:35:59 UTC | #4

There are so many reasons to inherit from Urho3D::Object!
One example? Your object can send and receive Urho Events, even if it's not part of any Scene...

I would recommend going a step further, and inheriting from Serializable.
This guy can handle most of the work of loading and saving your object data...

-------------------------

wakko | 2019-07-20 10:22:32 UTC | #5

Thanks everyone. I've figured out how to inherit from Urho3D::Object and I think I can finally get rid of my additional init() function.
I wonder why I didn't try that at first... but it's more than a year that I've actively worked on this project...
I have a lot of fixing to do :slight_smile:

-------------------------

QBkGames | 2019-07-23 04:26:54 UTC | #6

Or you could just get the Context from the parent Node, or any other Node, Material or Skybox, which are member variables of you class and then you don't need to inherit from anything.

-------------------------

