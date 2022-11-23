Magnetoid | 2017-01-02 01:04:34 UTC | #1

Hello All,

I've been working on a game with Urho3D using the Lua bindings. Recently I added some lua code that removes nodes whose "health" value has hit 0. This crashed the engine (as in segfault) in some other lua code which had stored the node in a table. I would expect the entries to be either nil'd out or have some sort of "invalid" marker that could be checked, but I haven't discovered anything that might work like that. It appears from the C++ code that the node is being deleted (when node:Remove() is called) even though Lua still has pointers to it (hence the segfault later on). Could this be fixed by using sharedptrs for lua references? If not, how can I store nodes in a table safely?

Here's a short standalone script illustrating the problem (you can run it with Urho3DPlayer in headless mode):
[code]

local total = 0
local lastPrintTime = 0
local invalidNodes = {}

function Start()
	scene_ = Scene()

	-- Create scene subsystem components
	scene_:CreateComponent("Octree", LOCAL)
	local phys = scene_:CreateComponent("PhysicsWorld", LOCAL)
	phys.gravity = Vector3(0,-9.8,0)

	SubscribeToEvent("Update", "UpdateStuff")

end

LifeTimer = ScriptObject()

function UpdateStuff()

	local dt = 0.02

	-- Make sure there are 10 alive objects
	while total < 10 do
		print("Creating")
		local newNode = scene_:CreateChild()
		newNode:CreateScriptObject("LifeTimer")
		total = total + 1
		print("Created")
	end

	-- Print out the table every so often
	lastPrintTime = lastPrintTime + dt
	if lastPrintTime > 1 then

		for i,n in ipairs(invalidNodes) do
			-- Problems occur on the next two lines
			print(">>>>> Test:",n.ID,n.position.x)
			n:SendEvent("Junk")
		end

		print("Done test")

		lastPrintTime = lastPrintTime-1
	end

end


function LifeTimer:Start()
	self.life = 1.5
	self.node.position = Vector3(Random(-10,10),Random(-10,10),Random(-10,10))
	print("Start")
end

function LifeTimer:Stop()
	print("Stop")
end

function LifeTimer:FixedUpdate(dt)
	self.life = self.life - dt
	if self.life <= 0 then

		print("Removing")

		-- Add to table before removing
		table.insert(invalidNodes, self.node)
		-- Remove the node
		self.node:Remove()

		print("Removed")
		total = total - 1
	end
end

[/code]
It might not crash for a while (or it might give Lua errors instead), but Valgrind will show you the problems.
I'm using the git master branch on 64-bit Linux.

-------------------------

GoogleBot42 | 2017-01-02 01:04:34 UTC | #2

Hmmm maybe there can be a wrapper class that internally keeps track if a pointer to an object is still valid.  IMO lua/anglescript shouldn't ever be able to cause a segfault.

-------------------------

weitjong | 2017-01-02 01:04:35 UTC | #3

Welcome to our forum. This has been discussed in the last section on this page here. [urho3d.github.io/documentation/H ... Allocation](http://urho3d.github.io/documentation/HEAD/_lua_scripting.html#LuaScripting_Allocation). Our current Lua/C++ binding does not perform reference counting like AngelScript binding does, so for now you will have to take care yourself to manage the life cycle of your objects correctly.

-------------------------

GoogleBot42 | 2017-01-02 01:04:35 UTC | #4

[quote="weitjong"]Our current Lua/C++ binding does not perform reference counting like AngelScript binding does, so for now you will have to take care yourself to manage the life cycle of your objects correctly.[/quote]

:frowning:  That is too bad.  I while it would be nice if Lua integration was finished... I think the other features currently being worked on are much more important though.

So magnetoid I guess you could create a wrapper table that keeps track of if the object is still valid...  You could do this nicely using metatables: [url]http://lua-users.org/wiki/MetamethodsTutorial[/url]

-------------------------

Magnetoid | 2017-01-02 01:04:36 UTC | #5

Thanks for the replies - I think I might be on to a solution! If I store the node's ID instead of a pointer, it cannot be deleted and cause a segfault. Then I can use scene_:GetNode(id) to retreive the pointer back when I need it. Hopefully the lookup performance will be acceptable. The only drawback to this is that the node ID might get reused (what is the probability of that happening? It never happened in the test script). To detect that, I could add some kind of "version" number on the node, e.g.:
[code]
node.version = global_version_number
global_version_number = global_version_number + 1
[/code]
Then when I access it, check for a) the existence of .version, and b) if it matches the value stored with the ID.

GoogleBot, your metatable idea would make a nice way to tidy all this up!

This might work, but it would be nice to do it the "right" way. How hard would it be to change the Node* to a SharedPtr<Node> in the lua bindings? I imagine it's more complicated than simply changing a few pointers. What kind of issues might I run into if I tried this?

-------------------------

thebluefish | 2017-01-02 01:04:36 UTC | #6

Node IDs inherently don't get re-used. When the Node is added to the scene, the scene will assign a new ID if the ID already exists or null (ID = 0).

-------------------------

GoogleBot42 | 2017-01-02 01:04:36 UTC | #7

[quote="Magnetoid"]How hard would it be to change the Node* to a SharedPtr<Node> in the lua bindings? I imagine it's more complicated than simply changing a few pointers. What kind of issues might I run into if I tried this?[/quote]

I thought about doing it that way but it won't work... The SharedPtr class in Urho3D is not the same as this:[url]http://www.cplusplus.com/reference/memory/shared_ptr/[/url]

The reason is because the Node itself holds the reference count number because it is derived from the class "Object"
SharedPtr just calls the respective functions from the templated class on construction, destruction, etc.

So the following code won't compile because those functions don't exist (again these functions that are used for reference counting are defined in the class Object).
[code]class Test
{
  void Foo() {}
};

auto testing = SharedPtr<Test>( new Test() );[/code]

This means that SharedPtr accesses the object itself to determine the ref count number of the object.  If the object is deleted this memory can now have any value...

In other words... it won't work. :frowning:

-------------------------

weitjong | 2017-01-02 01:04:36 UTC | #8

To the OP, I think you are pretty much asking for trouble yourself by trying to use the node object in the later part of your code after you have explicitly call node:Remove() method. If you use node pointer in the table as in your first post and since Lua does not know how to increase the reference count on the object then the pointer becomes bad when the child node is removed. If you use node id in the table then although it is true that it won't cause a segfault by itself when the id becomes bad but for sure scene_:GetNode(id) method would return null in the later part of the code when the node originally associated to that id has already been destroyed. I don't think there is any easier way for you to safely get hold of a child node in this particular case because there is no way you can increase its reference count in Lua at the moment (until someone refactor our current Lua/C++ binding to move away from tolua++). If you really need the node object again after it has been "removed" from the scene then perhaps you can workaround the problem currently by simply not calling node:Remove() method, but instead by calling node:SetParent(deadNodeRoot) where deadNodeRoot is the parent of all dead node. This may or may not suitable for your case because the SetParent() method performs some transformation to try retain its world transform after reparenting. Since now the child node is never destroyed, your node pointer in the table should remain valid forever, well, until you destroy the deadNodeRoot parent node or calling its RemoveAllChildren() method to remove all child nodes or RemoveChild() method to remove a particular dead child node for good this time.

-------------------------

GoogleBot42 | 2017-01-02 01:04:37 UTC | #9

[quote="weitjong"] Lua does not know how to increase the reference count on the object then the pointer becomes bad when the child node is removed.[/quote]

Sorry this really isn't that important but...  :unamused:  Lua doesn't reference count at all for garbage collection it uses a much more advanced method but you point still applies.  :wink:

-------------------------

Magnetoid | 2017-01-02 01:04:37 UTC | #10

[quote="weitjong"]To the OP, I think you are pretty much asking for trouble yourself by trying to use the node object in the later part of your code after you have explicitly call node:Remove() method. ... If you use node id in the table then although it is true that it won't cause a segfault by itself when the id becomes bad but for sure scene_:GetNode(id) method would return null in the later part of the code when the node originally associated to that id has already been destroyed. I don't think there is any easier way for you to safely get hold of a child node in this particular case because there is no way you can increase its reference count in Lua at the moment (until someone refactor our current Lua/C++ binding to move away from tolua++). If you really need the node object again after it has been "removed" from the scene then perhaps you can workaround the problem currently by simply not calling node:Remove() method, but instead by calling node:SetParent(deadNodeRoot) where deadNodeRoot is the parent of all dead node. ... [/quote]

I only want to use the node if it is still valid. The GetNode(id) idea seems to be working - it returns NULL instead of a dangling pointer, which is something that can be checked:
[code]
local node = scene_:GetNode(id)
if node then -- Only do this if not NULL.
    doStuffWithNode(node)
end
[/code]
Otherwise, yes, I would have to do the dead node parent trick as you described (and then implement my own reference counting system so as not to leak them when they are no longer needed).

@GoogleBot, I was referring to Urho3D's SharedPtr. I don't understand why that can't work, since it's the same method used by the rest of the engine. If Lua held a SharedPtr, then the node and its reference count must be valid as long as that is alive. To put it another way - instead of using a SharedPtr, just increment the node's reference value when it gets passed to lua and decrement it when lua calls the __gc metamethod.

-------------------------

GoogleBot42 | 2017-01-02 01:04:38 UTC | #11

[quote="Magnetoid"]@GoogleBot, I was referring to Urho3D's SharedPtr. I don't understand why that can't work, since it's the same method used by the rest of the engine. If Lua held a SharedPtr, then the node and its reference count must be valid as long as that is alive. To put it another way - instead of using a SharedPtr, just increment the node's reference value when it gets passed to lua and decrement it when lua calls the __gc metamethod.[/quote]

Sorry I am bad a communicating clearly...  :confused:   The reason why it won't is because the reference count number is stored in the node itself *not* in the SharedPtr.

All nodes and objects derive from RefCount:
[url]https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Container/RefCounted.h#L47[/url]

-------------------------

Magnetoid | 2017-01-02 01:04:38 UTC | #12

[code]
    /// Reference count. If below zero, the object has been destroyed.
    int refs_;
[/code]

As per the code comment, wouldn't it be sufficient to keep the refcount above zero to keep the node around? Why not increase it with AddRef() when passing it to lua?

-------------------------

weitjong | 2017-01-02 01:04:39 UTC | #13

Like I said before, our current Lua/C++ bindings are generated semi-automatically by using tolua++ tool. This tool does not support the concept of reference counting. If you know the tool well, you could probably write a "hook" so that all the generated binding source files do this AddRef() thing when returning a refcounted object to Lua. However, that is not enough. Considering this code snippet.
[code]local node = scene_:GetNode(id)
local another_ref = node[/code]
Unless the Lua assignment operator and the whole Lua scripting environment also supports this concept, it is rather pointless just fixing the bindings. And unfortunately, last time I check both AddRef() and ReleaseRef() are not being exposed to scripting API, so you cannot get hold of an object and then manually increase/decrease the reference count in Lua.

If you search our forums or our GitHub issues you should be able to find there were numerous previous discussions on how to fix this. However, discussing it is one thing and actually implementing it is another thing.  :wink:

-------------------------

Magnetoid | 2017-01-02 01:04:40 UTC | #14

Ok, I will go poke around some more when I get some free time. One thing I know though is that your code snipped would work fine. In Lua, assignments do not make copies, so they both point to the same thing. Lua's GC will only collect (and thus unreference) the node object when all references are gone. So if you "copy" it to another variable (as in your snippet), nothing changes. Anyway, I'll mess around with it when I get a chance and I'll let you guys know if I make any progress. Thanks for your help!

-------------------------

