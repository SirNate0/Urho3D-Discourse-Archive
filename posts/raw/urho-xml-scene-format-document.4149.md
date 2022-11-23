johnnycable | 2018-04-05 13:16:39 UTC | #1

Hello, where can I find a good description of Urho xml scene format? I mean, if there's some doc out there which shows scene/nodes/etc structure and attributes... for loading scenes in code...

-------------------------

weitjong | 2018-04-06 00:33:57 UTC | #2

I am afraid there is none. Done a quick grep in the Doc subdir and found nothing as well. However, since Urho3D is open source, the best documentation is the code for save/load itself.

-------------------------

johnnycable | 2018-04-06 07:41:15 UTC | #4

That's a start, thank you

-------------------------

weitjong | 2018-04-06 09:21:46 UTC | #5

I was referring to XML scene structure earlier. For attribute list, we do have a generated page (https://urho3d.github.io/documentation/HEAD/_attribute_list.html), if that is what you are looking for.

-------------------------

johnnycable | 2018-04-06 12:51:27 UTC | #6

Yes, I'll be using that too. Checking attributes in code to double check. Still trying to get the big picture...

-------------------------

Sinoid | 2018-04-07 03:41:36 UTC | #7

It's all done through attributes / Serializable - so you really just have to look at how Variant serializes to XML as far as what the format is going to be.

It gets a little odd with the *structure* stuff, but thankfully that *stuff* is barely used. Most everything else is pretty basic.

The rest of it is just **node** element contains an ID xml-attribute and **component** elements contain xml-attributes for ID and type (using the string name). You can tell whether something is local or replicated based on the value of the ID (anything >= 16777216 is local, anything else is replicated).

Edit: Except the serialized attribute/object animation. I forgot about that.

-------------------------

