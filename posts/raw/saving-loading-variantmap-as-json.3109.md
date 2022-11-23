JTippetts | 2017-05-07 21:48:41 UTC | #1

I'm trying to figure out how to save and load a standalone VariantMap as JSON.

Currently, I implement the functions:

```
void SaveVariantMapJSON(String &fname, VariantMap &vm)
{
	JSONFile jf(GetScriptContext());
	File f(GetScriptContext());
	f.Open(fname, FILE_WRITE);
	
	JSONValue &root=jf.GetRoot();
	root.SetVariantMap(vm);
	jf.Save(f);
}

VariantMap LoadVariantMapJSON(String &fname)
{
	JSONFile jf(GetScriptContext());
	File f(GetScriptContext());
	f.Open(fname, FILE_READ);
	
	jf.BeginLoad(f);
	JSONValue &root=jf.GetRoot();
	
	return root.GetVariantMap();
}
```

Then I bind these functions to global functions in AngelScript. It seems to work on the face of it:

```
VariantMap vm;
vm["test"]="test";
vm["testmap"]=VariantMap();
SaveVariantMapJSON("testvm.json", vm);
```

This results in saving the json file:
```
{
	"4745D132": {
		"type": "String",
		"value": "test"
	},
	"9949668A": {
		"type": "VariantMap",
		"value": {}
	}
}
```
However, if I then try to load it in:

```
VariantMap nvm=LoadVariantMapJSON("testvm.json");
```

It doesn't seem to work. It loads the file, it populates the VariantMap, and the values of the entries seem to be correct. I can iterate the values of the map and it shows two values, of type String and type Variant map, in the structure. However, the keys are not correct. Attempt to acess nvm["test"] results in an empty Variant. Iterating the loaded variant map shows the following for key/valuetype:

```
00001289 : String
0097D1E4 : VariantMap
```
As you can see the hash keys are different from what was saved to the JSON file. It looks to me like it's probably re-hashing the already hashed key or something to that effect.

Is there something I'm missing here? Is there a better way of doing this? I'm trying to store a sort of ad-hoc settings/configurations type of file which typically I would just save as a Lua table, but I'm trying to learn AngelScript which is requiring some different methods.

Edit: It seems like it might be a confusing of bases. In JSONValue::SetVariantMap, the VariantMap key is converted to a string via StringHash::ToString, which converts the hashed value to hexadecimal format. In JSONValue::GetVariantMap, the hash string is read and converted using GetUInt() using the default base (Base 10).

Edit2: Looks like that's what is going on. By writing a helper function:


```
VariantMap GetVariantMap(JSONValue &v)
{
    VariantMap variantMap;
    if (!v.IsObject())
    {
        URHO3D_LOGERROR("JSONValue is not a object");
        return variantMap;
    }

    for (ConstJSONObjectIterator i = v.Begin(); i != v.End(); ++i)
    {
        StringHash key(ToUInt(i->first_, 16));
        Variant variant = i->second_.GetVariant();
        variantMap[key] = variant;
    }

    return variantMap;
}
```

which converts the hash string from base 16 instead, it works as expected. Of course, any nested maps will still use the built-in GetVariantMap function, so the full solution in this way would need to be writing external helpers for all the various GetVariant* functions.

-------------------------

cadaver | 2017-05-08 07:50:03 UTC | #2

Should be fixed in the engine to at least include your base16 fix. Ideally it should work with any keys in the JSON map, but that's a hash reverse mapping problem.

-------------------------

cadaver | 2017-05-08 10:34:18 UTC | #3

Base16 fix is in master branch.

-------------------------

