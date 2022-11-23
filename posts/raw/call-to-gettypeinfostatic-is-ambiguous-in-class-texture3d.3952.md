haolly | 2018-01-18 09:06:42 UTC | #1

The macro `URHO3D_OBJECT` in class `Texture3D` complains **Call to GetTypeInfoStatic is ambiguous** when I open the project in Clion, but it compiles well on VS2017.

So I find the generated preprocessed file use the method described on [SO here](https://stackoverflow.com/questions/1389838/how-to-debug-macros-efficiently-in-vs) and replace the macro,


    public:
    		using ClassName = Texture3D;
    		using BaseClassName = Texture;
    		virtual Urho3D::StringHash GetType() const override { return GetTypeInfoStatic()->GetType(); }
    		virtual const Urho3D::String& GetTypeName() const override { return GetTypeInfoStatic()->GetTypeName(); }
    		virtual const Urho3D::TypeInfo* GetTypeInfo() const override { return GetTypeInfoStatic(); }
    		static Urho3D::StringHash GetTypeStatic() { return GetTypeInfoStatic()->GetType(); }
    		static const Urho3D::String& GetTypeNameStatic() { return GetTypeInfoStatic()->GetTypeName(); }
    		static const Urho3D::TypeInfo* GetTypeInfoStatic()
    		{
    			static const Urho3D::TypeInfo typeInfoStatic("Texture3D",BaseClassName::GetTypeInfoStatic());
    			return &typeInfoStatic;
    		};

It turned out  the code `BaseClassName::GetTypeInfoStatic()` cause this. 

seems like Texture class does not define it's owne GetTypeInfoStatic function, but inherit from Object/Resource/ResourceWithMetadata class, so it is ambigusou ??

It's weird that VS does not report this issue
The same happens in class Texture2D

-------------------------

Eugene | 2018-01-18 09:01:54 UTC | #2

[quote="haolly, post:1, topic:3952"]
URHO3D_OBJECT
[/quote]
Does it fix the problem if you add `URHO3D_OBJECT` to `Texture`?

-------------------------

haolly | 2018-01-18 09:10:30 UTC | #3

`URHO3D_OBJECT(Texture, ResourceWithMetadata);` 
yes, it does

-------------------------

haolly | 2018-01-22 12:42:10 UTC | #4

May I ask one more question?
https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Graphics/Direct3D11/D3D11Texture2D.cpp#L416

Does the line 416 use `CreateTexture2D(&textureDesc, nullptr, (ID3D11Texture2D**)&object_);`  not `CreateTexture2D(&textureDesc, nullptr, (ID3D11Texture2D**)&object_.ptr_);` for a particular purpose ? 
I see the latter was used in class `Texture3D` and `TextureCube`

-------------------------

Eugene | 2018-01-22 13:16:10 UTC | #5

Non-functional typo, I think

-------------------------

haolly | 2018-01-23 00:26:55 UTC | #6

[quote="Eugene, post:5, topic:3952, full:true"]
Non-functional typo, I think
[/quote]

Because `object_` is an union,  all share the same address memory :thinking:

-------------------------

