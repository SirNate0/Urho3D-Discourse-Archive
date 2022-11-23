itisscan | 2017-01-02 01:14:52 UTC | #1

We develop custom editor for game, where we need to override component's virtual LoadXML/SaveXML methods in order to create custom data serialization into/from XML file. Before everything was good, but with ScriptInstance became problem. So we created new class with name ScriptComponent that inherits from ScriptInstance. After ScriptComponent was attached to the node, we called ScriptComponent's method CreateObject(), which simply call base class ("ScrriptInstance") method [b]CreateObject[/b] with necessary parameters. Look,

[code]void ScriptComponent::CreateScriptObjects()
{
	const String& className = this->GetClassName();
	if (className != m_ClassName)
	{
		if (!m_ScriptFilePath.Empty())
		{
			ScriptFile* scriptFile = g_pApp->GetConstantResCache()->GetResource<ScriptFile>(m_ScriptFilePath);
			if (scriptFile)
			{
				this->CreateObject(scriptFile, m_ClassName);
			}
		}
	}
}[/code]

And there is ScriptComponent class declaration 
[code]class ScriptComponent : public ScriptInstance
{
	URHO3D_OBJECT(ScriptComponent, ScriptInstance)

public:
	ScriptComponent(Context* context);
	virtual ~ScriptComponent();
	static void RegisterObject(Context* context);

	/// Save as XML data. Return true if successful.
	virtual bool SaveXML(XMLElement& dest) const;

	/// Load from XML data. When setInstanceDefault is set to true, after setting the attribute value, store the value as instance's default value. Return true if successful.
	virtual bool LoadXML(const XMLElement& source, bool setInstanceDefault = false);

	void CreateScriptObjects();

protected:
	String m_ScriptFilePath;
	String m_ClassName;
};[/code]

In the result i get the memory leak, when exit from the program. 
The dump about memory leak - [url]http://pastebin.com/TpJ7n6tz[/url]. There you can see that in asCScriptObject::SetUserData() (457 line) was allocated memory and was not released then. 
Here is image, which show the place, where happens memory allocation (457 line) [url]http://imgur.com/a/xz0ar[/url]
In other words this code raises the memory leak. 
[code]if( !extra )
extra = asNEW(SExtra);[/code]

I suppose another 4 leaks were raised by the same code.

At once want to ask, is it safely to override ScriptInstance's LoadXML/SaveXML method ? 

Someone has idea why the memory leak happens and how can fix it ? 

We use urho3d 1.5 release version.

Thanks.

-------------------------

itisscan | 2017-01-02 01:14:53 UTC | #2

It seems that i have solved the memory leek problem, but i do not know is it good solution.

In ScriptComponent's destructor i have added following lines - 

[code]ScriptComponent::~ScriptComponent()
{
	asIScriptObject* pScriptObject = this->GetScriptObject();
	if (pScriptObject)
	{
		pScriptObject->Release();
	}
}[/code]

May someone explain why i need to call also Release() in ScriptComponent destructor, while ScriptInstance's destructor already does scriptObject_ releasing ?
[code]
ScriptInstance::~ScriptInstance()
{
    ReleaseObject();
}

void ScriptInstance::ReleaseObject()
{
        ...
        scriptObject_->SetUserData(0);
        scriptObject_->Release();
        scriptObject_ = 0;
}
[/code]

-------------------------

cadaver | 2017-01-02 01:14:53 UTC | #3

This looks like somewhere an extra ref is being added to the asIScriptObject, and by releasing twice you ensure correct release. Do you ever see this happening by using just ScriptInstance? If yes, it's an Urho bug. If not, then it's likely the culprit is your code.

-------------------------

itisscan | 2017-01-02 01:14:53 UTC | #4

[quote="cadaver"]This looks like somewhere an extra ref is being added to the asIScriptObject, and by releasing twice you ensure correct release. Do you ever see this happening by using just ScriptInstance? If yes, it's an Urho bug. If not, then it's likely the culprit is your code.[/quote]

No, i have never seen this by using just ScriptInstance. Moreover, i have tested AngelScriptIntegration sample project for memory leak. It works without any memory leak. So i suppose the culprit is our code, but it looks very strange that somewhere can be added extra ref. I have no idea where it can be added, because there is one place (it is ScriptComponent class), where we directly deal with ScriptInstance.

-------------------------

cadaver | 2017-01-02 01:14:53 UTC | #5

Double-check any AS bindings that you've added; auto handles ( @+ ) mean the script engine handles refcounts automatically when a raw pointer is passed to/from C++. Normal handles ( @ ) assume you will manage the refcount manually in the bound code, as necessary. If you get these wrong there could either be extra refs added, or too early release. I never remember the rules, see [angelcode.com/angelscript/sd ... andle.html](http://www.angelcode.com/angelscript/sdk/docs/manual/doc_obj_handle.html) for reference.

-------------------------

itisscan | 2017-01-02 01:14:53 UTC | #6

[quote="cadaver"]Double-check any AS bindings that you've added; auto handles ( @+ ) mean the script engine handles refcounts automatically when a raw pointer is passed to/from C++. Normal handles ( @ ) assume you will manage the refcount manually in the bound code, as necessary. If you get these wrong there could either be extra refs added, or too early release. I never remember the rules, see [angelcode.com/angelscript/sd ... andle.html](http://www.angelcode.com/angelscript/sdk/docs/manual/doc_obj_handle.html) for reference.[/quote]

We did not add any new AS bindings in our code. And if scene is with only one node and i try to add ScriptComponent (inherited from ScriptInstance) to the node with following script
[code]class Planet : ScriptObject
{
    void Start()
    {
	Print("Hello!");
    }
	
    // Update is called during the variable timestep scene update
    void Update(float timeStep)
    {
		
    }
}
[/code]

Then i still get the memory leak. (In case if i do not call Release() method in ScriptComponent's destructor). 
If you look in the [url]http://pastebin.com/iQjBNHYy[/url] dump, where now there are 3 memory leaks. 

First memory leaks happens in as_scriptobject.cpp (457).
1)MSVCR120D.dll!malloc() 
b:\programming\protocolseven\source\github\source\thirdparty\angelscript\source\as_scriptobject.cpp (457): 
Second,
2)MSVCR120D.dll!malloc() b:\programming\protocolseven\source\github\source\thirdparty\angelscript\source\as_builder.cpp
(It seems that memory is not released for ScriptFile, which resource cache loads)
Third,
3)In the same place as first.

-------------------------

