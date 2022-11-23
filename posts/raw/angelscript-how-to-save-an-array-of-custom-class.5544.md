PsychoCircuitry | 2019-09-01 20:21:14 UTC | #1

Hello, I've been messing around with Urho3D for a little while. I'm a relative novice when it comes to programming. Mostly I've been able to find answers to my queries, but this one really has me stumped.

2 things: I have an array of materials that I need to serialize and deserialize for saving and loading, and the same thing but with an array of custom class objects.

I'm using the angelscript api atm. Any help would be greatly appreciated. Thanks!

-------------------------

Sinoid | 2019-09-01 21:04:41 UTC | #2

You may implement these in your `ScriptObject` class to save/load additional data.

```
void Load(Deserializer&);
void Save(Serializer&);
void ReadNetworkUpdate(Deserializer&);
void WriteNetworkUpdate(Serializer&);
```

Otherwise you basically just write a function to save your things to `Serializer` and read them from `Deserializer` and use those functions in your Load/Save implementations

ie:

```
// reusable function to write an array of DamageInfo to serializer
void SaveDamageInfo(Array<DamageInfo> infos, Serializer&in dest)
{
    dest.WriteUInt(infos.length);
    for (uint i = 0; i < infos.length; ++i)
    {
        dest.WriteUInt(infos[i].damageKind);
        dest.WriteFloat(infos[i].damageModifier);
    }
}

// reusable function to read said info from a deserializer
Array<DamageInfo> LoadDamageInfo(Deserializer& src)
{
    Array<DamageInfo> retList;
    uint ct = src.ReadUInt();
    for (uint i = 0; i < ct; ++i)
    {
        DamageInfo info; 
        info.damageKind = src.ReadUInt();
        info.damageModifier = src.ReadFloat();
        retList.Push(info);
    }
    return retList;
}

// ScriptObject interface implementation

class MyGameObject : ScriptObject
{
    Array<DamageInfo> myDamageInfo;

    // called when our ScriptInstance is read from a file
    void Load(Deserializer& src) { myDamageInfo = LoadDamageInfo(src); }
    // called when our ScriptInstance is written to a file
    void Save(Serializer& dest) { SaveDamageInfo(myDamageInfo, dest); }
}
```

---

Does that make sense?

-------------------------

PsychoCircuitry | 2019-09-02 06:47:26 UTC | #3

Yes that helps. Thank you. Was able to get a solution figured out from your example.

-------------------------

