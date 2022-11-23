itisscan | 2017-01-02 01:14:55 UTC | #1

A couple of days I try to understand why It does not to work. So i have class two simple classes : PlanetInfo and StarSystem, which i want to use in AS scripts. 

[b]There is PlanetInfo class declaration.[/b]
[code]
class PlanetInfo 
{
public:
	PlanetInfo();
	PlanetInfo(const PlanetInfo& info);
	~PlanetInfo() { }
	PlanetInfo operator=(const PlanetInfo& info) { return PlanetInfo(info); }

	bool Initialize(const XMLElement& planetNode);

	static void RegisterScript(asIScriptEngine* engine);
private:
	int m_Id;
	float m_DistanceFromPrimaryStar;
	float m_Mass;
}
[/code]

[b]There is PlanetInfo class implementation:[/b]
[code]
PlanetInfo::PlanetInfo() :
	m_DistanceFromPrimaryStar(0.0f),
	m_Mass(0.0f)
{ }

PlanetInfo::PlanetInfo(const PlanetInfo& info) :
	m_DistanceFromPrimaryStar(info.m_DistanceFromPrimaryStar),
	m_Mass(info.m_Mass)
{ }

bool PlanetInfo::Initialize(const XMLElement& planetNode)
{
	m_DistanceFromPrimaryStar = planetCharacteristics.GetFloat("DistanceFPS");
	m_Mass = planetCharacteristics.GetFloat("Mass");
	return true;
}

void PlanetInfo::RegisterScript(asIScriptEngine* engine)
{
	engine->RegisterObjectType("PlanetInfo", sizeof(PlanetInfo), asOBJ_VALUE | asOBJ_APP_CLASS_CDAK);
	engine->RegisterObjectBehaviour("PlanetInfo", asBEHAVE_CONSTRUCT, "void f()", asFUNCTION(ConstructPlanetInfo), asCALL_CDECL_OBJLAST);
	engine->RegisterObjectBehaviour("PlanetInfo", asBEHAVE_CONSTRUCT, "void f(const PlanetInfo&in)", asFUNCTION(ConstructPlanetInfoCopy), asCALL_CDECL_OBJLAST);
	engine->RegisterObjectBehaviour("PlanetInfo", asBEHAVE_DESTRUCT, "void f()", asFUNCTION(DestructPlanetInfo), asCALL_CDECL_OBJLAST);
	engine->RegisterObjectMethod("PlanetInfo", "PlanetInfo opAssign(const PlanetInfo&in)", asMETHODPR(PlanetInfo, operator =, (const PlanetInfo&), PlanetInfo), asCALL_THISCALL);
	engine->RegisterObjectProperty("PlanetInfo", "int id", offsetof(PlanetInfo, m_Id));
	engine->RegisterObjectProperty("PlanetInfo", "float m_DistanceFromPrimaryStar", offsetof(PlanetInfo, m_DistanceFromPrimaryStar));
	engine->RegisterObjectProperty("PlanetInfo", "float m_Mass", offsetof(PlanetInfo, m_Mass));
}

static void ConstructPlanetInfo(PlanetInfo* ptr)
{
	new(ptr) PlanetInfo();
}

static void DestructPlanetInfo(PlanetInfo* ptr)
{
	ptr->~PlanetInfo();
}

static void ConstructPlanetInfoCopy(const PlanetInfo& planetInfo, PlanetInfo* ptr)
{
	new(ptr)PlanetInfo(planetInfo);
}

[/code] 


[b]There is StarSystem class declaration.[/b]
[code]
class StarSystem : public Serializable
{
	URHO3D_OBJECT(StarSystem, Serializable)

public:
	StarSystem(Context* context);
	~StarSystem();
	virtual bool LoadXML(const XMLElement& source, bool setInstanceDefault = false);

	const Vector<PlanetInfo>& GetPlanets() const { return m_Planets; }

	static void RegisterScript(asIScriptEngine* engine);
private:
	Vector<PlanetInfo> m_Planets;
};
[/code]

[b]There is StarSystem class implementation.[/b]
[code]StarSystem::StarSystem(Context* context) : Serializable(context)
{
	Script* pScriptSystem = GetSubsystem<Script>();
	if (pScriptSystem)
	{
		RegisterScript(pScriptSystem->GetScriptEngine());
	}
}

StarSystem::~StarSystem()
{

}

bool StarSystem::LoadXML(const XMLElement& source, bool setInstanceDefault)
{
	XMLElement systemCharacteristics = root.GetChild("SystemCharacteristics");	
	XMLElement planets = systemCharacteristics.GetChild("Planets");
	for (XMLElement it = planets.GetChild(); it; it = it.GetNext())
	{
		PlanetInfo newPlanet = PlanetInfo();
		if (newPlanet.Initialize(it))
		{
			m_Planets.Push(newPlanet);
		}
	}
	return true;
}

void StarSystem::RegisterScript(asIScriptEngine* engine)
{
	PlanetInfo::RegisterScript(engine);

	RegisterSerializable<StarSystem>(engine, "StarSystem");
	engine->RegisterObjectMethod("StarSystem", "Array<PlanetInfo>@ GetPlanets() const", asFUNCTION(StarSystemGetPlanets), asCALL_CDECL_OBJLAST);
	engine->RegisterGlobalFunction("StarSystem@+ GetStarSystem()", asFUNCTION(GetStarSystem), asCALL_CDECL);
}

static StarSystem* GetStarSystem()
{
	return GetScriptContext()->GetSubsystem<StarSystem>();
}

static CScriptArray* StarSystemGetPlanets(StarSystem* ptr)
{
	Vector<PlanetInfo> planets = ptr->GetPlanets();

	for (int i = 0; i != planets.Size(); i++)
	{
		URHO3D_LOGINFO("m_Mass = " + String(planets[i].m_Mass));
	}

	return VectorToArray<PlanetInfo>(planets, "Array<PlanetInfo>");
}
[/code]

Generally StarSystem holds info about all planets in Vector structure.
I create StarSystem::RegisterScript(asIScriptEngine* engine) and PlanetInfo::RegisterScript(asIScriptEngine* engine) functions based on Urho3D AS bindings. 

The problem is the following - 
when in script i try to get all planets as [b]Array<PlanetInfo> planets[/b], then in each PlanetInfo object all member variables are not initialized. (i just loop for each planet and print each object member values in order to see value). But when is called method [code]static CScriptArray* StarSystemGetPlanets(StarSystem* ptr) {
 ... 
	for (int i = 0; i != planets.Size(); i++)
	{
		URHO3D_LOGINFO("m_Mass = " + String(planets[i].m_Mass));
....
	}[/code] 

then i have noticed that in Vector<PlanetInfo> planets all values are initialized correctly. Therefore there is mistake in my AS bindings or somewhere else.

There is script file where i print each PlanetInfo's member values.

[code]class StarSystemController : ScriptObject
{
	void DelayedStart()
	{
		XMLFile@ starSystemXML = cache.GetResource("XMLFile", "StarSystem.xml");
		if(starSystem.LoadXML(starSystemXML.GetRoot()))
		{
			// GET ALL PLANETS
			Array<PlanetInfo> planets = starSystem.GetPlanets();
			for(uint i = 0; i < planets.length; i++)
			{
                                // IN CONSOLE I GET ZERO FOR EACH VARIABLE, WHAT IS ABSOLUTELY WRONG
				Print("m_Id= " + String(planets[i].m_Id));
				Print("m_Mass= " + String(planets[i].m_Mass));
				Print("m_DistanceFromPrimaryStar= " + String(planets[i].m_DistanceFromPrimaryStar)); 
			}
         }
	}
}[/code]

Someone can explain why in scripts i get incorrect values ?

Thanks.

-------------------------

itisscan | 2017-01-02 01:14:55 UTC | #2

I have solved it. 

In the code i have [code] PlanetInfo operator=(const PlanetInfo& info) { return PlanetInfo(info); }[/code], but what i really need is next 

[code]
PlanetInfo& operator=(const PlanetInfo& info)
{
	m_Id = info.m_Id;
	m_DistanceFromPrimaryStar = info.m_DistanceFromPrimaryStar;
	m_Mass = info.m_Mass;
	return *this;
}
[/code]

Never dealt with operator overloading before. It was good lesson for me.  :slight_smile:

-------------------------

