Taqer | 2019-06-24 15:44:55 UTC | #1

Hi, I want to save/load some custom data not stored in nodes to/from xml/json, how to do that?

-------------------------

jmiller | 2019-06-24 18:31:58 UTC | #2

Hello,
Nodes have a freeform VariantMap for persistent user variables; cf. [class Node](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_node.html), SetVar/GetVar/GetVars methods.

Some examples of node vars usage can be found in the forum and samples 03,14, 24, 37.

@cadaver explains some about the VariantMap.
https://discourse.urho3d.io/t/material-override-inside-xml-scene/1270/4

-------------------------

SirNate0 | 2019-06-25 04:12:56 UTC | #3

If you just want to create a custom xml/json file rather than storing data in the scene you can store the data in an [XMLElement](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_x_m_l_element.html) or [JSONValue](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_j_s_o_n_value.html) and then write it to an [XMLFile](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_x_m_l_file.html) or [JSONFile](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_j_s_o_n_file.html).

-------------------------

Modanung | 2019-06-25 11:13:49 UTC | #4

Depending on your case you may also use a custom class that inherits from `Serializable` and register attributes to it. By default these attributes will be saved and loaded with the `SaveXML` and `LoadXML` functions, which can be overridden for more control.

Check out the [documentation on serialization](https://urho3d.github.io/documentation/HEAD/_serialization.html) for more information.

-------------------------

Taqer | 2019-06-25 15:05:13 UTC | #5

Thanks guys for replies, I think, the most related one is from @SirNate0, I wanted to do this, but I dont know how to append XMLElement to file:

	//container for all items
	XMLElement container = XMLElement();

	//now suppose I want to add some thing
	container.CreateChild("PI").SetFloat("value", 3.14f);

	XMLFile * file = new XMLFile(context_);
	
	//how to append container to file???

	file->SaveFile("save.xml");

-------------------------

SirNate0 | 2019-06-25 15:38:51 UTC | #6

I don't have a computer right now to check that this works, but I think what you want is XMLFile::[
CreateRoot](https://urho3d.github.io/documentation/HEAD/class_urho3_d_1_1_x_m_l_file.html#a749db4388da1420917188fda2e01cec8) (const String &name)
Something like:
```
XMLFile * file = new XMLFile(context_);

//container for all items - the root element of the file
XMLElement container = file->CreateRoot("tagName");

//now suppose I want to add some thing
container.CreateChild("PI").SetFloat("value", 3.14f);

// Assuming I'm correct, the XMLFile should already have everything at this point and you just need to save it to the disk now

file->SaveFile("save.xml");
```

-------------------------

Taqer | 2019-06-25 15:39:44 UTC | #7

Thanks, works like a charm. :smiley:

-------------------------

