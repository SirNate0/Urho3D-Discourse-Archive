gawag | 2017-01-02 01:03:34 UTC | #1

Edit: There are Clone() functions inside the Material and Model classes. Could be better to also have copy constructors to follow typical C++ style. I assumed not having copy constructor meant "is not copyable", but they are.
Edit2: This was a bad idea. I've used to much Qt... ITT: me complaining about Urho not being like Qt but being better...

It would be nice if Urho had directly copyable materials (like with copy constructors). For example to give the same model different shader parameters (like for custom team colors or whatever).
I wrote an (incomplete) function that copies a material by creating a new one and copying the attributes from the original to the new one:
[code]
Material* copy_material(Material* mat)
{
    Material* ret=new Material(mat->GetContext());
    for(int i=0;i<14;i++)  // there are 14 entries in the TextureUnit enum in GraphicsDefs.h
    {
        Texture* t=mat->GetTexture((TextureUnit)i);
        ret->SetTexture((TextureUnit)i,t);
    }
    for(int i=0;i<mat->GetNumTechniques();i++)
        ret->SetTechnique(i,mat->GetTechnique(i));
    return ret;
}
[/code]
Example usage: giving each material (aka each of the 400 cubes) a different MatDiffColor:
[code]
for(int x=-10;x<10;x++)
    for(int y=-10;y<10;y++)
    {
        Node* boxNode_=scene_->CreateChild("Box");
        boxNode_->SetPosition(Vector3(x,-3,y));
        StaticModel* boxObject=boxNode_->CreateComponent<StaticModel>();
        boxObject->SetModel(cache->GetResource<Model>("Models/Box.mdl"));

        Material* mat1=cache->GetResource<Material>("Materials/Stone.xml");
        Material* mat2=copy_material(mat1);
        mat2->SetShaderParameter("MatDiffColor",Color((x+10)/20.0f,(y+10)/20.0f,.5));  // the diffuse colors are between (0, 0, 0.5) and (1, 1, 0.5)
        boxObject->SetMaterial(mat2);
        boxObject->SetCastShadows(true);
        boxNode_->SetScale(.9);
    }
[/code]
[img]http://i.imgur.com/fsmYGPO.jpg[/img]
There may be also other classes where it may be useful to have a copy option (which doesn't exist yet).
Is it a good idea to copy materials like that? Are textures & techniques shared?

-------------------------

thebluefish | 2017-01-02 01:03:34 UTC | #2

One way to do it is to Load() the Material:

[code]
Urho3D::XMLFile* file = GetSubsystem<Urho3D::ResourceCache>()->GetResource<Urho3D::XMLFile>("Materials/RocketDocument.xml");
batchInfo.batch->material_ = new Urho3D::Material(context_);
batchInfo.batch->material_->Load(file->GetRoot());		
batchInfo.batch->material_->SetTexture(TU_DIFFUSE, batchInfo.texture);
[/code]

However I do agree it would be nice to be able to Copy a material.

-------------------------

hdunderscore | 2017-01-02 01:03:34 UTC | #3

Did you see Material::Clone(): [urho3d.github.io/documentation/1 ... 017bc5e274](http://urho3d.github.io/documentation/1.32/class_urho3_d_1_1_material.html#af4a270694b5e998e19ff6e017bc5e274)

-------------------------

gawag | 2017-01-02 01:03:34 UTC | #4

[quote]One way to do it is to Load() the Material:[/quote]
The material is not copied with already made changes. Which could be nice.
Is the material, or are files in general, reloaded when reloading something from a file or are they shared/cached in some way?

[quote]Did you see Material::Clone(): [urho3d.github.io/documentation/1](http://urho3d.github.io/documentation/1) ... 017bc5e274[/quote]
Oh didn't see that one.
Didn't see any copy constructor so thought it would not be possible.
Just tested Clone() and it seems to work, nice.

Would still be a good idea to add a copy constructor that uses Clone() (with the default argument).

-------------------------

cadaver | 2017-01-02 01:03:34 UTC | #5

The copy constructor is intentionally left out of Object / RefCounted subclasses to make it harder to accidentally allocate them on the stack, which would result in a serious error as soon as you assigned them into an object, but the stack-scope would destroy them. Furthermore the Clone() function already returns the clone wrapped in a shared pointer, to direct toward the proper use and prevent memory leaks if you forgot to either assign it somewhere or delete the clone.

-------------------------

gawag | 2017-01-02 01:03:35 UTC | #6

Ah, that makes sense. I'm so used to Qt's model of managing widgets by himself and me using barely any pointer at all (stack&RAII ftw).
Then I got no better idea on how to do it. Changing topic title again.  :wink: 

The RessourceCache does optimize multiple calls like cache->GetResource<Model>("Models/Box.mdl") so that the file is touched just once or is the file still checked for changed or newer versions and reloaded? Is there a behavior difference for different file types like Model/Texture?

-------------------------

cadaver | 2017-01-02 01:03:36 UTC | #7

When a resource has been already loaded into memory, GetResource() will just perform a map lookup and should be very fast. No file access is performed in that case, and all resource types perform similarly. Resource live reload is not on by default but can be activated with ResourceCache::SetAutoReloadResources().

-------------------------

