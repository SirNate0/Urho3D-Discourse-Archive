slapin | 2017-05-01 07:24:27 UTC | #1

Is there any JSON loading example in Urho? I know the support is there, but I wonder how to use it.

-------------------------

Mike | 2017-05-01 07:35:52 UTC | #2

https://discourse.urho3d.io/t/2d-physics-editor-loader/2148/4?u=mike

You can also have a look at the Editor's "Localization" feature.

-------------------------

slapin | 2017-05-01 07:47:20 UTC | #3

@Mike please help me fith this:

I have the following JSON file, how can I parse it with Urho?
how can I get keys and values?


    {
            "composites": {
                    "dispname": "Composites",
                    "members": {
                            "sequence": {
                                    "dispname": "Sequence",
                                    "max_children": -1,
                                    "properties": {
                                    }
                            },       
                            "memsequence": {
                                    "dispname": "MemSequence",
                                    "max_children": -1,
                                    "properties": {
                                    }
                            },
                            "selection": {
                                    "dispname": "Selection",
                                    "max_children": -1,
                                    "properties": { 
                                    }
                            },      
                            "memselection": {
                                    "dispname": "MemSelection",
                                    "max_children": -1,
                                    "properties": { 
                                    }       
                            }       
                    }       
            }
    }

-------------------------

slapin | 2017-05-01 07:49:15 UTC | #4

Basically I don't understand how to get these "selection", "memselection", "sequence",... etc. values.

-------------------------

slapin | 2017-05-01 08:00:50 UTC | #5

well, if I do
   JSONFile@ jsonfile = JSONFile();
   jsonfile.Load(path)
  JSONValue root = jsongile.GetRoot();

I see some data and root.size contains sane value,
but I really can't go any farther. is JSON API really implemented or it was done
for some very specific needs?

Thanks!

and yes, I know I can do XML - it works fine, but this time I need JSON as XML is insane for stuff one have to write manually...

-------------------------

slapin | 2017-05-01 08:12:57 UTC | #6

I see the problem. AngelScript have no JSON binding, so it is not possible to use JSON from AngelScript.

Will file a bug about that.

-------------------------

Mike | 2017-05-01 08:15:56 UTC | #7

From what I remember:

- First get the root:
> JSONValue composites = jsonFile.root.Get("composites");

- Each time you have a key that opens a curly brace, you get it as a JSONValue:
> JSONValue members = composites.Get("members");
> JSONValue sequence= members.Get("sequence");

- Then you get each key value nested in the JSONValue:
> String dispname =  sequence.Get("dispname").GetString(); // "dispname" is the key, "Composites" is the value (a string here)

-------------------------

Mike | 2017-05-01 08:17:31 UTC | #8

The example that I provided is in AngelScript...

-------------------------

slapin | 2017-05-01 08:18:45 UTC | #9

But there is no way to know key values.
GetVariantMap() and other methods are not bound. C++ can freely pass files like this
unlike AngelScript.

-------------------------

slapin | 2017-05-01 08:23:48 UTC | #10

Well, using Get is useless to me as I need to add more key values and build list out of them.
Anyway I need to build the list of values and that is not possible.

-------------------------

slapin | 2017-05-01 08:32:37 UTC | #11

Filed a bug about this if anybody interested: 

https://github.com/urho3d/Urho3D/issues/1924

I resume that only XML is supported for value sets now. Which is sad news for me, as it is really booooring
to write XMLs :(

-------------------------

slapin | 2017-05-01 08:32:37 UTC | #12

@Mike thanks for help, but this looks beyond what can be done.

-------------------------

Victor | 2017-05-01 14:54:23 UTC | #13

I could be misunderstanding, but from the issue it looks like you want to know how to iterate through a json file?

I would think that it would work like XML, using JSONValue::IsNull to check if you've reached the end.

https://github.com/urho3d/Urho3D/blob/ee054a1507cb3518c57d4ebc43cfd6dc93de9a27/Source/Urho3D/Resource/JSONValue.h#L177

**Example using xml**

    XMLFile* texturesXML = cache->GetResource<XMLFile>(texturesFilePath_);
    XMLElement child = texturesXML->GetRoot().GetChild();
    while (!child.IsNull()) {
         elem = root.CreateChild("layer");
         elem.SetAttribute("name", child.GetAttribute("name"));
         child = child.GetNext();
    }

Since you're already doing this with XML, it should be easy to convert. I've not used AngelScript for anything in my project, however, creating the necessary bindings shouldn't be too bad if you're missing the IsNull method.

-------------------------

slapin | 2017-05-01 15:38:08 UTC | #14

No, that won't work.

-------------------------

Victor | 2017-05-01 15:49:51 UTC | #15

Creating the bindings, or looping through the objects? Sorry, I'm a bit unfamiliar with AS so I'm not sure :(

-------------------------

Victor | 2017-05-01 16:00:06 UTC | #16

So, just to be sure, I've saved a scene as a JSON file in the editor, and loaded it up. So the answer must be somewhere in the Editor's AS code. At least, I'd suspect you'd find your answer there.

-------------------------

slapin | 2017-05-01 18:18:02 UTC | #17

Well, saving scenes is in C++ code and it is quite specific to that purpose.

-------------------------

Victor | 2017-05-01 19:13:11 UTC | #18

Ah, I see. I didn't realize that was done with C++ :worried:

-------------------------

