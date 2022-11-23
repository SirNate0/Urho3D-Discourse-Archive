smellymumbler | 2018-01-10 00:12:42 UTC | #1

I've always been a big fan of the Quake CVARs. They allow you to quickly experiment and prototype with values until you find the sweet spot, right there within the game. So, now that my game is going further in Urho, i was trying to find a good way to handle them.

Right now i have a global std::unordered_map<string, float> that i call from everywhere. I'm pretty sure that globals are evil and so on, but I have no idea how to do this properly. Any suggestions or is this good enough?

-------------------------

Modanung | 2018-01-10 03:20:56 UTC | #2

Would using [attributes](https://urho3d.github.io/documentation/HEAD/_serialization.html) do the trick? That would allow you to modify variables by name.
Most classes that inherit from `Serializable` have code samples of how to register attributes in their `RegisterObject` method.

-------------------------

kostik1337 | 2018-01-10 08:31:29 UTC | #3

What's wrong with unordered_map?

One another thing you can do - when you obtain CVAR somewhere in your code, instead of returning value, you can return a pointer to that value, so when that value changes, your pointer will be pointing to already changed value with no overhead. AFAIK, CVARs in Quake are working the same way

-------------------------

smellymumbler | 2018-01-10 15:46:15 UTC | #4

[quote="Modanung, post:2, topic:3930, full:true"]
Would using attributes do the trick? That would allow you to modify variables by name.

Most classes that inherit from Serializable have code samples of how to register attributes in their RegisterObject method.
[/quote]


Yes, but attributes are entity-specific, right? CVARs are global, which can be read by entities.

[quote="kostik1337, post:3, topic:3930, full:true"]
What’s wrong with unordered_map?

One another thing you can do - when you obtain CVAR somewhere in your code, instead of returning value, you can return a pointer to that value, so when that value changes, your pointer will be pointing to already changed value with no overhead. AFAIK, CVARs in Quake are working the same way
[/quote]

I'm not sure if i follow... you mean a `map<string, *cvar_t>`? Having:

    union {
      int i;
      float f;
      std::string s;
    } cvar_t;

-------------------------

kostik1337 | 2018-01-10 17:20:17 UTC | #5

Can you really have such union? I cannot compile it because of string's non-trivial constructor or something like that.

Not necessarily you need map with pointer values, you can have it like `map<string, *cvar_t>`, and obtain values like
    auto iterator = cvars.find("qwe");
    cvar_t* var = &iterator->second;
So, when cvar in map changes later, pointer `var` will be pointing to that changed value.

-------------------------

smellymumbler | 2018-01-10 20:03:22 UTC | #6

Nah, that was just pseudo-code in my head. I'm using only int now, but i will need a union in the future. But hey, cross that bridge when you get there, right? :stuck_out_tongue: 

Why the iterator though? Is it faster than cvars["qwe"]?

-------------------------

kostik1337 | 2018-01-10 20:55:01 UTC | #7

[quote="smellymumbler, post:6, topic:3930"]
Why the iterator though? Is it faster than cvars[“qwe”]?
[/quote]
Pretty sure it's not, just the matter of style. I usually check if map contains entry with such key, you can't do this with just operator[]

-------------------------

Pencheff | 2018-02-25 01:55:09 UTC | #8

I have implemented my devconsole like this (I don't have the code around)
[code]
class CVar {
public:
// getters and setter
String GetName() const;
String GetDescription() const;
String GetValue() const;
String GetDefaultValue() const;
int GetInt() const;
float GetFloat() const;
private:
  String name_;
  String value_;
  String default_value_;
  String description_;
  int flags_;

  CvarManager* manager_;

  CVar (const String& name,
      const String& value, 
      int flags, 
      const String& description, 
      float valueMin, 
      float valueMax,
      CvarManager* owner);
}

// in the cvar manager:

class CVarManager {
public:
...
// Register a Cvar with the manager.
  CvarPtr AddCvar(const std::string& name, const std::string& value,
                  const std::string& description, int flags = CVAR_ARCHIVE,
                  bool has_min = false, bool has_max = false,
                  float valueMin = 0.0f, float valueMax = 0.0f);

  const std::string& GetString(const std::string& name);
  int GetInt(const std::string& name);
  float GetFloat(const std::string& name);
  bool GetBool(const std::string& name);
    
  void SetString(const std::string& name, const std::string& value, int flags = 0);
  void SetBool(const std::string& name, const bool& value, int flags = 0);
  void SetInt(const std::string& name, const int& value, int flags = 0);
  void SetFloat(const std::string& name, const float& value, int flags = 0);
}
[/code]

Anywhere in the code:
[code]
cvarMaxFps = cvar()->AddCvar("r_maxfps", "60", 
    "Frame rate limit", CVAR_ARCHIVE, true, false, -1.0f);
[/code]

The cvars themselves don't do much, they just store the data and have getters and setters, but the setters actually call the parent cvar manager's code. That way you can track changing cvars at a single place and save them as config file on change.

Using code from Urho3D it can be done much easier using Variant and VariantMap.

-------------------------

Pencheff | 2018-02-25 13:13:15 UTC | #9

[quote="kostik1337, post:3, topic:3930, full:true"]
What’s wrong with unordered_map?

One another thing you can do - when you obtain CVAR somewhere in your code, instead of returning value, you can return a pointer to that value, so when that value changes, your pointer will be pointing to already changed value with no overhead. AFAIK, CVARs in Quake are working the same way
[/quote]
This is exactly how it works. You register (or declare) a cvar once, then use the resulting pointer to the cvar to read the value from the cvar, so you don't have to do lookups in the unordered_map everytime. I got so used to that quake style console, I use it in almost every of my projects, even those not having to do anything with graphics :D

Screenshot from my engine:
![quake_style_cvar|690x388](upload://etZbFrw9RRzYawBvhTDweVUgwAE.jpg)

-------------------------

