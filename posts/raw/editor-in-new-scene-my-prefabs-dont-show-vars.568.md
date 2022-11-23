codingmonkey | 2017-01-02 01:01:25 UTC | #1

hi folks, I create a prefab with variables: fx(int) = 1 and type(string) = "boom" . 
[url=http://savepic.org/6546695.htm][img]http://savepic.org/6546695m.png[/img][/url]
and I save it in a folder data\objects\


Then I create a new blank scene and inserts there Prefab. but variables does not indicated in atribute inspector, [url=http://savepic.ru/6332670.htm][img]http://savepic.ru/6332670m.png[/img][/url]

but i just know that variables in the file exist.
[code]
<?xml version="1.0"?>
<node id="3">
	<attribute name="Is Enabled" value="true" />
	<attribute name="Name" value="boom" />
	<attribute name="Position" value="13.3563 -2.07224 0.489285" />
	<attribute name="Rotation" value="1 0 0 0" />
	<attribute name="Scale" value="1 1 1" />
	<attribute name="Variables">
		<variant hash="1360791162" type="String" value="boom" />
		<variant hash="6691218" type="Int" value="1" />
	</attribute>
	<component type="StaticModel" id="16777249">
		<attribute name="Model" value="Model;Models/Icosphere.mdl" />
		<attribute name="Material" value="Material;Materials/MT_Boom.xml" />
	</component>
	<component type="Light" id="16777250">
		<attribute name="Color" value="1 0.5 0 1" />
		<attribute name="Specular Intensity" value="0" />
		<attribute name="Brightness Multiplier" value="3" />
		<attribute name="Light Shape Texture" value="TextureCube;" />
	</component>
	<node id="16777234">
		<attribute name="Is Enabled" value="true" />
		<attribute name="Name" value="boomRing" />
		<attribute name="Position" value="0 0 0" />
		<attribute name="Rotation" value="1 0 0 0" />
		<attribute name="Scale" value="1 1 1" />
		<attribute name="Variables">
			<variant hash="6691218" type="Int" value="1" />
		</attribute>
		<component type="StaticModel" id="16777251">
			<attribute name="Model" value="Model;Models/BoomMesh.mdl" />
			<attribute name="Material" value="Material;Materials/MT_BoomRing.xml" />
		</component>
	</node>
</node>
[/code]

Why is this happening? How to make so that the variables of prefab were visible in the new scenes?

-------------------------

cadaver | 2017-01-02 01:01:26 UTC | #2

It's a somewhat ill-construed system where the variable hash->name reverse mappings are only stored in the scene where the node was originally constructed. Nodes themselves, or prefab files, do not store the mapping.

I committed a change in the editor which shows a fallback hexadecimal value of the hash if the mapping is not available. This way editing the values should be possible.

-------------------------

codingmonkey | 2017-01-02 01:01:26 UTC | #3

ok, now i see some numbers )
also i inspect scene.xml file and see this:

[code]
	<attribute name="Variables" />
	<attribute name="Variable Names" value="type;fx;ai" />
[/code]

mb this lines needed to add in prefab too?

ps. in this last version that i download & compile - the editor's camera is crazy in rotation, have you seen this ?) 
i fix camara rotation by change 344 line of EditorView.as set to "bool orbiting = true;"

-------------------------

hdunderscore | 2017-01-02 01:01:26 UTC | #4

[quote="codingmonkey"]ok, now i see some numbers )
ps. in this last version that i download & compile - the editor's camera is crazy in rotation, have you seen this ?) 
i fix camara rotation by change 344 line of EditorView.as set to "bool orbiting = true;"[/quote]

A change I submitted could have caused this, but I haven't been able to reproduce this with a clean build from master.

Does this happen every time you start up the editor ? What about other samples / ninja war when you toggle the console?

Did you build clean from master ?

-------------------------

codingmonkey | 2017-01-02 01:01:27 UTC | #5

>Did you build clean from master ?
yes, i'm delete all old files and copy new files to clean folder then run cmake gui and compile with vs2008.

>Does this happen every time you start up the editor ? What about other samples / ninja war when you toggle the console?

ok, there is:
in new scene add few yours simple prefabs, and try rotate, camera - is crazy ) (with bool orbiting = false) 
then go to file EditorView.as and fix:  bool orbiting = true
close editor, and run it again.
now add few prefabs in new scene - now camera rotation is ok

-------------------------

cadaver | 2017-01-02 01:01:27 UTC | #6

If you add the var names to the prefab xml, it won't have effect (It's not an attribute of Node.) But you can copy them to a scene xml.

I don't think I've seen weird camera behavior with the latest changes.

-------------------------

codingmonkey | 2017-01-02 01:01:27 UTC | #7

>But you can copy them to a scene xml.
this way is not for cross-scene or cross-project prefab ))
i mean, why prefab can not be something self-contained and easily move from project to project or from scene to scene without any additional edits in it or scene? )

>I don't think I've seen weird camera behavior with the latest changes.
i experiment again, tried a few times and got only once this issue, but basically is okay. This problem is not regular cause and I do not understand what it was.

-------------------------

codingmonkey | 2017-01-02 01:01:27 UTC | #8

i don't know somehow but this time it happened again - rotation bug
editor was minimized in the system tray for a while, then I just maximized it

[video]http://youtu.be/mMO5cOjtPCA[/video]

-------------------------

cadaver | 2017-01-02 01:01:27 UTC | #9

[quote="codingmonkey"]this way is not for cross-scene or cross-project prefab ))
i mean, why prefab can not be something self-contained and easily move from project to project or from scene to scene without any additional edits in it or scene? )
[/quote]

I never said the current system is perfect or could not be improved. However you need to understand that the same attribute structure (where vars are referred to with hashes) is used for all use cases: net replication, load/save, and editing, so making prefabs (which are just serialized Nodes) behave differently is not easy. When you use the vars in code you don't need the human-readable names, only when editing.

-------------------------

codingmonkey | 2017-01-02 01:01:27 UTC | #10

>When you use the vars in code you don't need the human-readable names, only when editing.
but i use human-readable names in code )
for example: 
i'm check if hit object has FX tag, then "follow" variable of the camera is no clip, else clip.
[code]
if (results.Size())
	{
		RayQueryResult& result = results[0];

		Variant v = result.node_->GetVar("fx");
		if (v.GetInt() == 1) // if this some fx not clip follow 
		{
	
		}
[/code]

i know that my - "fx" var has been converted to hash in compile time, but now - in edit time, this is simple string of text.

>I never said the current system is perfect or could not be improved
No, everything is fine Urho great engine with the set of possibilities.

You did not understand me.
Look there's an object.xml, let it consists of
1. Standart information for the engine about this object
2. Additional(Extra) information for the editor (and only for him, engine ignores it). 

This extra part through manipulations in editor influent to first standart part of object.
with this second part object will be more cross-scene and cross-project

-------------------------

codingmonkey | 2017-01-02 01:01:28 UTC | #11

Okay, I understand your point of view.
Let's hope for the best solution.

[quote]Personally, I completely removed the node variables editing from the builds I gave to a few artists. They have no business messing with them.[/quote]
poor [size=50]lemo[/size] artists :slight_smile:

-------------------------

hdunderscore | 2017-01-02 01:01:28 UTC | #12

[quote="codingmonkey"]i don't know somehow but this time it happened again - rotation bug
editor was minimized in the system tray for a while, then I just maximized it

[video]http://youtu.be/mMO5cOjtPCA[/video][/quote]
Interesting. Somethings I noticed:
[ul][li]Is that how your cursor always looks?[/li]
[li]Were you middle mouse rotating? It didn't seem to be centering on some of the nodes you selected[/li]
[li]Just to confirm, were you using the relative mouse mode in the settings?[/li][/ul]

-------------------------

codingmonkey | 2017-01-02 01:01:28 UTC | #13

>?Is that how your cursor always looks?
No, it's looks usual, this is somekind video stretching

>?Were you middle mouse rotating? It didn't seem to be centering on some of the nodes you selected
yes, this is middle mouse button rotation 

>?Just to confirm, were you using the relative mouse mode in the settings
i'am using std editor settings except fix what i made in 344 line of script. whats' all.

I realized that my correction code does not affect the appearance of the bug.
He appears, even if the return everything in defaul.

-------------------------

