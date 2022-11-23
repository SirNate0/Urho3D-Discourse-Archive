JTippetts | 2017-01-02 01:06:35 UTC | #1

A recent change to how Variant maps are indexed in Lua required me to go through my entire game and redo how events are sent. A common idiom of mine was to populate a variant map with data, then fire off an event.
[code]
local vm=VariantMap()
vm:SetBool("flag", true)
vm:SetVector3("pos", Vector3(1,1,1))
self.node:SendEvent("Event", vm)
[/code]

The change to Lua variant map indexing broke this idiom, so this morning I went through and made the changes:

[code]
local vm=VariantMap()
vm["flag"]=true
vm["pos"]=Vector3(1,1,1)
self.node:SendEvent("Event", vm)
[/code]

However, something has broken and I am not sure exactly what it is.

I have a component, written in C++, that performs a task of broadcasting an "AreYouReady" type of event, and any objects signed up to receive the event will send back a reply by populating a variant map with their node ID and sending off another event. The scheduler component listens for this event and inserts ready objects into a vector for later processing. Before the change to the variant map indexing, this was functioning as intended, but now it no longer is. The C++ component is essentially structured as so:

[code]
// Turn scheduler
TurnScheduler::TurnScheduler(Context *context) : LogicComponent(context)
{
	SetUpdateEventMask(USE_UPDATE);
	
	SubscribeToEvent(StringHash("RegisterReadyObject"), HANDLER(TurnScheduler, HandleRegisterReadyObject));
}

void TurnScheduler::Update(float dt)
{
	SendEvent(CombatRequestStatus, vm);
}
void TurnScheduler::HandleRegisterReadyObject(StringHash eventType, VariantMap& eventData)
{
	static StringHash ReadyID("ReadyID");
	
	unsigned int id=eventData[ReadyID].GetUInt();
	std::cout << "Ready object: " << id << std::endl;
	// Add object to Ready vector
}
[/code]

Objects then have a LuaScriptObject class that will subscribe to the CombatRequestStatus event, and fire off a RegisterReadyObject event if they are ready:

[code]
CombatCommandQueue=ScriptObject()

function CombatCommandQueue:Start()
	
	self:SubscribeToEvent("CombatRequestStatus", "CombatCommandQueue:HandleRequestStatus")
	self.ready=true
	
end

unction CombatCommandQueue:HandleRequestStatus(eventType, eventData)
	if self.ready then
		print("Sending ready for "..self.node:GetID())
		self.vm["ReadyID"]=self.node:GetID()
		self.node:SendEvent("RegisterReadyObject", self.vm)
	end
end
[/code]

Logging indicates that the HandleRequestStatus event is being received. However, when the RegisterReadyObject event is fired off, it is not being received by the turn scheduler anymore. I've experimented with populating the variant map with string hashes rather than strings:

[code]
self.vm[StringHash("ReadyID")=self.node:GetID()
[/code]

and with sending a string hash of the RegisterReadyObject event instead of a regular string:

[code]
self.node:SendEvent(StringHash("RegisterReadyObject"), self.vm)
[/code]

but to no avail. The events simply are not being received by the C++ component anymore. Anybody have any ideas on what's going wrong?

-------------------------

JTippetts | 2017-01-02 01:06:36 UTC | #2

Further work shows that the event is actually getting through, it's just that when I push a node id like this:

[code]
vm[StringHash("ReadyID")]=node:GetID()
[/code]

In the event handler the node ID is obtained as:

[code]
unsigned int id=eventData[StringHash("ReadyID")].GetUInt();
[/code]

But it always reads it as 0. Pushing the ID as
[code]
vm["ReadyID"]=node:GetID()
[/code]

also does not work.

-------------------------

JTippetts | 2017-01-02 01:06:36 UTC | #3

Okay, I've figured it out.

If you do

[code]
vm["key"]=num
[/code]

the Variant type is set to VAR_DOUBLE by default. So reading it back in C++ as a UInt, Int or Float will not work. It has to be read with GetDouble() then cast to the desired type.

I think I understand why this has to be (Lua only knows about 1 type of number, and the base type of Lua numbers is double) but it's still kind of inconvenient. I'll fill out an issue for further discussion on this.

-------------------------

weitjong | 2017-01-02 01:06:37 UTC | #4

Firstly, sorry to hear that you have to spend time to fix the Lua scripts in your game this way. Secondly, have a read on these links just in case you haven't:
- [topic1228-10.html#p7329](http://discourse.urho3d.io/t/odbcc-database-connectivity/1188/16)
- [github.com/urho3d/Urho3D/issues/820](https://github.com/urho3d/Urho3D/issues/820)
One thing leads to another. Had you joined the discussion earlier or helped me to fix those missing bindings at the beginning, perhaps I would not have touched the LuaScript subsystem at all.  :wink: 

Anyway, I totally agree that the "mismatch" between Lua (at least on version 5.1) and C++ (at least on our Variant class) is an inconvenience and error prone. The idea of removing those setter methods in the VariantMap.pkg is to avoid having duplicate codes (this is one of the thing I can't stand). But in doing so, I have also realized early on that the _newindex metamethod would have problem assigning Lua number to Variant as non-double. I believe you have spotted my code comment and/or code to do special handling for LUA_TNUMBER. But at that time, I thought the problem is not serious enough. I thought code from C++ side could first prep the VariantMap by associating a certain key with a Variant value storing a default integral or floating data type value. Then on the Lua side, the _newindex metamethod would use that initial type as cue to cast the LUA_TNUMBER accordingly preserving the intial integral or floating data type. Obviously this won't work in your case because the event and hence the VariantMap is originated from Lua side, so there is no way for you to prep this.

Incidentally this is also an existing problem for Variant constructors in Lua side. If you do "local test = Variant(100)" then you will always get a Variant storing a double. This happens because the double constructor overload declared later than the integer one in the Variant.pkg and thus it is being considered first. That's how tolua++ works (I just figure out that recently, don't ask me why). Interchange the order won't solve the problem because if integer constructor overload is being considered first then "local test = Variant(100.123)" would always get a Variant storing an integer instead. In other words, these constructor overloads are stepping on each other's toes.
[code]
    Variant(int value);
    Variant(unsigned value);
    Variant(float value);
    Variant(double value);
[/code]
The last one declared wins. I am mentioning this not to shift the focus on the VariantMap problem, but just to strengthen the point that we do have an inherent mismatch problem between Lua/number and C++/Variant.

I propose to solve it this way. Remove those Variant constructors above (or perhaps just keep the double version around). Then bind setter methods to Variant class in Lua side similar to what Variant used to have. Something like: SetInt(i), SetUInt(u), SetFloat(f), SetDouble(d). We can also add a generic Set("typename", i/u/f/d), where typename is one of "int", "unsigned", "float", "double". So, back to your case, you can write something like: vm["ReadyID"]:SetUInt(self.node:GetID())

-------------------------

JTippetts | 2017-01-02 01:06:38 UTC | #5

Don't worry about me having to fix stuff. That's the kind of thing that happens when you pull the repo frequently, rather than using stable.

Looks like I missed that discussion earlier, but had I seen it I probably would have been okay with what you've done. It is closer to the behavior of the C++ and AngelScript branches. I think that with the change done in [url]https://github.com/urho3d/Urho3D/commit/f0b3c8b805174fefa885885c73de5df966e18178[/url] it should be good. It works for me, at any rate.

-------------------------

weitjong | 2017-01-02 01:06:38 UTC | #6

Yes, the new changes just done by Lasse should solve your particular case. The inherent mismatch issue still exists though and may reveal itself in other cases.

-------------------------

