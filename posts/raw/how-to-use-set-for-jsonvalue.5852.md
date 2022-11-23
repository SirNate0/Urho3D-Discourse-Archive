Askhento | 2020-01-30 00:58:34 UTC | #1

Didn't find a good explanation on how to use 
void Set(const String&, const JSONValue&);
I have a material which I load from cache and I want to change a parameter.

-------------------------

JTippetts | 2020-02-08 16:54:25 UTC | #2

A JSONValue can hold a Number, Bool, or String as a base type, or an Array or Object(map). So you can do Set("foo", JSONValue(45.0)) which will set the "foo" member of a JSONObject (note that JSONObjects are the only ones that can hold a named parameter like that) to a JSONValue that holds the number 45.0.

This probably isn't what you need, though. After the material is loaded, the JSON it was loaded from can be safely discarded since it isn't used anymore. If you need to change a parameter of an existing, already-loaded material you can do that with Material::SetShaderParameter. If you need to change a texture, use Material::SetTexture.  Note that changing a parameter for a material will change it for all instances of that material, so if you want each object that uses a material to change their parameters independently, you need to clone the material using Material::Clone, and store a separate instance per object.

-------------------------

Askhento | 2020-02-08 18:42:49 UTC | #4

Thanks it works!
I had issue because use Set as 
``` angelscript
matDesc.Get("shaderParameters").Set("MatDiffColor", JSONValue("1 0 1 1"));
``` 
I should not use Get cuz it get value of the field but not the reference to it. Now I use Get in separate variable and then change values and Set it back :smiley:
Maybe you know 2 more things: 
1)How to set Array for value?(I don't know how to create JSONArray)
 2)How can I get reference to the value at specific key?

-------------------------

JTippetts | 2020-02-09 14:47:34 UTC | #5

1) JSONArray is just a typedef of Vector<JSONValue>. So you can do, ie
    JSONArray myarray;
    myarray.Push(JSONValue(42));

    myobject["ArrayField"] = myarray;

2) Use the [] operator instead of Get() to obtain a reference to the value, ie 
    JSONValue &foo = myobject["ArrayField"];
    int firstvalue = foo[0].GetInt();

Note that using [] operator on JSONValue automatically converts the internally stored JSONValue to either JSONArray (if the index parameter is unsigned int) or to a JSONObject (if the parameter is a String), so if you eg. try to index an array using a String it will delete your contained array and convert it to an object instead.

-------------------------

