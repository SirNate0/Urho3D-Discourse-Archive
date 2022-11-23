setzer22 | 2017-01-02 01:02:10 UTC | #1

Hello everyone!  :smiley: 

The title should be self explanatory, even though let me give some background:

I had a working accessor attribute for an XML resource file and now with the changed macros I'm not able to set it right.

Before I had:

[code]ACCESSOR_ATTRIBUTE(MapProperties, VAR_RESOURCEREF, "Map data", GetXmlAttr, SetXmlAttr, ResourceRef, ResourceRef(XMLFile::GetTypeStatic()), AM_DEFAULT);[/code]

Now I've changed it to:

[code]ACCESSOR_ATTRIBUTE("Map data", GetXmlAttr, SetXmlAttr, ResourceRef, ResourceRef(XMLFile::GetTypeStatic()), AM_DEFAULT);[/code]

But that isn't compiling, and gcc is not being helpful at all to point out the error:

[code]

.../Urho3D/Source/Engine/Scene/Serializable.h:262:316: error: no matching function for call to ?Urho3D::AttributeAccessorImpl<MapProperties, Urho3D::ResourceRef, Urho3D::AttributeTrait<Urho3D::ResourceRef> >::AttributeAccessorImpl(Urho3D::ResourceRef (MapProperties::*)() const, void (MapProperties::*)(Urho3D::ResourceRef))?
 #define ACCESSOR_ATTRIBUTE(name, getFunction, setFunction, typeName, defaultValue, mode) context->RegisterAttribute<ClassName>(Urho3D::AttributeInfo(GetVariantType<typeName >(), name, new Urho3D::AttributeAccessorImpl<ClassName, typeName, AttributeTrait<typeName > >(&ClassName::getFunction, &ClassName::setFunction), defaultValue, mode))
                                                                                                                                                                                                                                                                                                                            ^
.../Source/Components/Map/Properties/MapProperties.cpp:14:5: note: in expansion of macro ?ACCESSOR_ATTRIBUTE?
     ACCESSOR_ATTRIBUTE("Map data", GetXmlAttr, SetXmlAttr, ResourceRef, ResourceRef(XMLFile::GetTypeStatic()), AM_DEFAULT);
     ^
.../Source/Engine/Scene/Serializable.h:262:316: note: candidate is:
 #define ACCESSOR_ATTRIBUTE(name, getFunction, setFunction, typeName, defaultValue, mode) context->RegisterAttribute<ClassName>(Urho3D::AttributeInfo(GetVariantType<typeName >(), name, new Urho3D::AttributeAccessorImpl<ClassName, typeName, AttributeTrait<typeName > >(&ClassName::getFunction, &ClassName::setFunction), defaultValue, mode))

[/code]

There's more of it if it's really relevant to solve the issue... (I'm not a huge fan of g++).

Thank you very much!

EDIT:

I've found this line searching the sources (Light.cpp):

[code]MIXED_ACCESSOR_ATTRIBUTE("Attenuation Texture", GetRampTextureAttr, SetR    ampTextureAttr, ResourceRef, ResourceRef(Texture2D::GetTypeStatic()), AM_DEFAULT);
[/code]

I don't know what a MIXED_ACCESSOR_ATTRIBUTE is but changing it doesn't seem to solve the question. Anyway, what's a mixed accessor attribute?

-------------------------

thebluefish | 2017-01-02 01:02:24 UTC | #2

The answer to your second question is in Serializable.h:

[code]
/// Define an attribute that uses get and set functions.
#define ACCESSOR_ATTRIBUTE(name, getFunction, setFunction, typeName, defaultValue, mode)
/// Define an attribute that uses get and set functions, where the get function returns by value, but the set function uses a reference.
#define MIXED_ACCESSOR_ATTRIBUTE(name, getFunction, setFunction, typeName, defaultValue, mode)
[/code]

Also make sure to follow the specific notes found in Serializable.h:

[code]// The following macros need to be used within a class member function such as ClassName::RegisterObject().
// A variable called "context" needs to exist in the current scope and point to a valid Context object.[/code]

-------------------------

