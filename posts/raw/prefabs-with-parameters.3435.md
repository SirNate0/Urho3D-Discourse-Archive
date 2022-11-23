JTippetts | 2017-08-09 04:50:26 UTC | #1

I'm doing some refactoring on my game, and in the process I'm running up against a question that has cropped up for me a few times before: the question of how to implement prefab objects with parameters.

My game makes heavy use of object templates that describe the overall structure of a node, but the individual script components require parameters that are specific for a particular instance of the object. Currently, I am making use of a system where a node and component hierarchy can be instanced from a template provided as a Lua table. I create the table, seed it with the various parameters, then pass it off to a Lua function that traverses a table and instances the node and component hierarchy. So I might have an object template for a fireball spell that looks like this:

    local desc=
			{
				Components=
				{
					{Type="ParticleEmitter", Material="Effects/flame.xml", UpdateInvisible=false, NumParticles=500,
						Sorted=false, Relative=false, MinRotationSpeed=-60, MaxRotationSpeed=60, MinDirection=Vector3(-0.25,-1,-0.25), MaxDirection=Vector3(0.25,-1,0.25),
						MinVelocity=0.5, MaxVelocity=1, MinParticleSize=Vector2(0.5, 0.5), MaxParticleSize=Vector2(0.75,0.75), MinEmissionRate=90, MaxEmissionRate=105,
						ConstantForce=Vector3(0,1,0), SizeMul=Rect(0.5,0.5), FaceCamera=true, MinTimeToLive=0.5, MaxTimeToLive=1,
						Color=Color(0.1,0.045,0.35),
					},
					{Type="Light", LightType=LIGHT_POINT, Color={r=1.5,g=0.75,b=0.45}, Range=4, CastShadows=true},
					{Type="ScriptObject", Classname="SpawnedAction", Parameters={ownernode=args.caster}},
					{Type="ScriptObject", Classname="Projectile", Parameters={startpos={x=myx,y=myy+0.25,z=myz}, endpos={x=targetpos.x,y=targety,z=targetpos.y}, speed=8, archeight=2}},
					{Type="ScriptObject", Classname="ObjectSpawnerPayload", Parameters={desc=fireballexplosion}},
					{Type="ScriptObject", Classname="DamageSingleTargetPayload",
						Parameters=
						{
							target=args.hexmap:getObjectOrAuxID(args.targetx, args.targetz),
							attacker=args.caster,
							attack="test fireball",
							damage=dmg
						}
					},
					{Type="ScriptObject", Classname="DoTPayload", Parameters={dot={ttl=10, counter=0, attack="Fiery Corruption", 
						damage=dmg, ownerid=args.caster:GetID()}}},
					{Type="CombatCameraControllerTemporary"},
				}
			}

Then I can instance the object from that description. The table is generated local to (in this example) a Spell:Execute function, which passes parameters (skill level, spell caster attack and damage modifiers, etc....) to those script objects that require them. Some of the parameters can be other object description tables (such as the ObjectSpawnerPayload script object, which spawns its designated object upon receipt of the TriggerPayload event, to make the fireball explode in a flash of particles). Since the table is built as a local when Execute is called, it is easy to seed the parameters to it upon table construction, so that the proper data is in place and available when the components are created.

However, this method is highly reliant upon Lua and doesn't work as well in the statically-typed languages of C++ and AngelScript.

What I'm looking for is ideas on how to implement a similar system that isn't tied to Lua. I have thought about using Scene::InstantiateJSON to instance from a JSON template, but I still have the issue of seeding the various parameters to the components. (Many of the parameters might be a struct or class type, such as DamageSingleTargetPayload which takes a DamageRecord structure.) If I try to construct the JSON description in-place like I do with the tables, then I have the problem of seeding these non-JSON-value type parameters throughout. I could generate the components without parameters, then iterate the instanced node hierarchy and all components, and set parameters manually after the template is instantiated, but this seems clunky and inelegant to me.

Anyone have any ideas? How do you guys handle prefab instancing with parameters?

-------------------------

Victor | 2017-08-09 13:28:17 UTC | #2

Honestly, my approach has been that if I couldn't describe it in JSON, then I created a C++ object for the case. This doesn't work for everyone, but that's just how I have tackled it so far.

-------------------------

SirNate0 | 2017-08-09 19:14:24 UTC | #3

I've done a few things - in some cases, I've just used the node's user variables to store parameters, in other cases I've made a new resource type (it may actually be a serializable, derived from the component class, I'm not sure right now - either way it ends up being about the same - requesting that it be loaded) that I use to construct the node hierarchy accordingly. One trick I've also done for parametrizing (AngelScript) scripts is to declare all the parameters in one file, and then include the template script after that that uses all the parameters.

-------------------------

JTippetts | 2017-08-10 00:29:18 UTC | #4

I'm thinking the way I might go is to build the node hierarchy using InstantiateJSON, then pass in custom data and instance-specific data using events. Most of my custom data structures (DamageRecord, SpellCastingContext, TargetList, etc...) can be broken down into a VariantMap representation, passed via event, and reconstituted on the other side. Works for AngelScript and LuaScript components as well.

-------------------------

