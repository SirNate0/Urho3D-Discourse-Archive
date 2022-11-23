TheComet | 2017-01-02 01:14:46 UTC | #1

I have this situation in my code where I've subclassed UIElement and am maintaining a child UIElement that gets loaded from XML (a pattern I learned from Qt now that I think about it).

What I'd like to be able to write is this:
[code]void MenuScreen::ReloadUI()
{
    ResourceCache* cache = GetSubsystem<ResourceCache>();

    if(ui_)
        RemoveChild(ui_);
    ui_ = LoadChildXML(
        xml_->GetRoot(),
        cache->GetResource<XMLFile>("UI/DefaultStyle.xml")
    );
}[/code]

Where:
[code]SharedPtr<XMLFile> xml_;
SharedPtr<UIElement> ui_;[/code]

Except that I can't, because [b]LoadChildXML()[/b] returns a bool and not a pointer to the child that was created. There seems to be no easy way to fish out the created child afterwards, because I can't rely on the name nor can I rely on ui_ being the only child of MenuScreen.

I propose the function be changed to return the child pointer. No functionality is lost, since you can still check if creation failed by comparing to NULL:
[code]UIElement* UIElement::LoadChildXML(const XMLElement& childElem, XMLFile* styleFile, bool setInstanceDefault)
{
    bool internalElem = childElem.GetBool("internal");
    if (internalElem)
    {
        URHO3D_LOGERROR("Loading internal child element is not supported");
        return NULL;
    }

    String typeName = childElem.GetAttribute("type");
    if (typeName.Empty())
        typeName = "UIElement";
    unsigned index = childElem.HasAttribute("index") ? childElem.GetUInt("index") : M_MAX_UNSIGNED;
    UIElement* child = CreateChild(typeName, String::EMPTY, index);

    if (child)
    {
        if (!styleFile)
            styleFile = GetDefaultStyle();
        if (!child->LoadXML(childElem, styleFile, setInstanceDefault))
            return NULL;
    }

    return child;
}[/code]

This would require changes to the angelscript bindings:

[b]APITemplates.h:953[/b]
[code]static UIElement* UIElementLoadChildXML(XMLFile* file, XMLFile* styleFile, UIElement* ptr)
{
    if (file == NULL)
        return NULL;

    XMLElement rootElem = file->GetRoot("element");
    if (rootElem)
        return ptr->LoadChildXML(rootElem, styleFile);
}[/code]

[b]APITemplates.h:1055[/b]
[code]    engine->RegisterObjectMethod(className, "UIElement@+ LoadChildXML(const XMLElement&in, XMLFile@+ arg1 = null, bool arg2 = false)", asMETHOD(T, LoadChildXML), asCALL_THISCALL);
    engine->RegisterObjectMethod(className, "UIElement@+ LoadChildXML(XMLFile@+, XMLFile@+ arg1 = null)", asFUNCTION(UIElementLoadChildXML), asCALL_CDECL_OBJLAST);[/code]

As well as in the editor script [b]EditorUIElement.as:319[/b]
[code]if (editUIElement.LoadChildXML(xmlFile, uiElementDefaultStyle !is null ? uiElementDefaultStyle : uiStyle) !is null)[/code]

I can make a PR if you want.

-------------------------

cadaver | 2017-01-02 01:14:46 UTC | #2

I believe this would make sense. If you want, you can make a PR (it's not a large change)

One thing to consider is what to do when the child has been created but load fails. Should the child be destroyed then? Presently it isn't, but false would be returned regardless in the current implementation.

-------------------------

TheComet | 2017-01-02 01:14:46 UTC | #3

Good point. I'd argue it would make sense to destroy the child if loading fails. It makes little sense to keep an empty child around. If the child isn't destroyed, it would be kind of deceitful to return NULL.

Returning the empty child would be the other option, however, that makes it harder to check if loading fails.

-------------------------

cadaver | 2017-01-02 01:14:46 UTC | #4

If you make the PR, you can make it so that the child is destroyed. We can correct later if it turns out other behavior is needed. This error case shouldn't happen in normal editor use; only in the case of malformed handwritten UI XML, but in that case I don't think it would even get as far as creating the child.

-------------------------

TheComet | 2017-01-02 01:14:47 UTC | #5

Here you go: [url]https://github.com/urho3d/Urho3D/pull/1649[/url]

I made sure the editor works and I tested the behaviour of the function in my own code.

There appear to be no lua bindings for this function. I didn't create any because I don't understand it enough.

-------------------------

