SirNate0 | 2017-03-04 14:52:17 UTC | #1

I was wondering if anyone had made a Debugging Helper for QtCreator for the Urho container classes, and if so would you be willing to share?
Thanks

-------------------------

Eugene | 2017-03-04 15:00:53 UTC | #2

I have one for Visual Studio, but it unlikely would be helpful.

It'd be nice to gather such stuff somewhere.

-------------------------

SirNate0 | 2017-03-07 03:42:23 UTC | #3

I've made fair progress with QtCreator's Debugging Helpers -- Vector and HashMap are working, and I'm in the middle of Variant. I'll probably finish it sometime, but if anyone wants what I have so far here:

Note: I'm using QtCreator 5.5.1 with gdb 7.11.1

you can check your gdb version by running (inside gdb):
```
py import sys; print(sys.version)
```
I have the following, so it might break on yours

```
3.5.2 (default, Nov 17 2016, 17:05:23) 
[GCC 5.4.0 20160609]
```

```python
#!/usr/bin/python

#this line is VERY IMPORTANT! And not mentioned in the examples/docs, I'm pretty sure. It is what was causing most of my problems...
from dumper import *
#Thank you Stack Overflow: http://stackoverflow.com/questions/34354573/how-to-write-a-debugging-helper-for-qtcreator

def qdump__Urho3D__Vector(d, value):
    array = value["buffer_"]
    size = value["size_"]
    maxDisplayItems = 100
    innerType = d.templateArgument(value.type, 0)
    p = array.cast(innerType.pointer())
    d.putValue('[{0}] @{1}'.format(size,str(array)))
    d.putItemCount(size)
    if d.isExpanded():
        d.putPlotData(p, size, innerType)
        
def qdump__Urho3D__Variant(d, value):
    t = value["type_"]
    d.putNumChild(0)
    d.putValue("{} int({})".format(str(t),int(t)))
    i = int(t)
    type_str = str(t)
    if type_str == "Urho3D::VAR_NONE":
        d.putValue("NONE")
    elif type_str == "Urho3D::VAR_INT":
        d.putValue("int {}".format(value["value_"]["int_"]))
    elif type_str == "Urho3D::VAR_BOOL":
        if value["value_"]["bool_"]:
            d.putValue("(bool) true")
        else:
            d.putValue("(bool) false")
    elif type_str == "Urho3D::VAR_FLOAT":
        d.putValue("float {}".format(value["value_"]["float_"]))
    return
    #TODO: finish
    if type_str == "Urho3D::VAR_VECTOR2":
        d.putValue("<{},{}>".format(value["value_"]["VECTOR2"]))
    if type_str == "Urho3D::VAR_VECTOR3":
        d.putValue("VECTOR3".format(value["value_"]["VECTOR3"]))
    if type_str == "Urho3D::VAR_VECTOR4":
        d.putValue("VECTOR4".format(value["value_"]["VECTOR4"]))
    if type_str == "Urho3D::VAR_QUATERNION":
        d.putValue("QUATERNION".format(value["value_"]["QUATERNION"]))
    if type_str == "Urho3D::VAR_COLOR":
        d.putValue("COLOR".format(value["value_"]["COLOR"]))
    if type_str == "Urho3D::VAR_STRING":
        d.putValue("STRING".format(value["value_"]["STRING"]))
    if type_str == "Urho3D::VAR_BUFFER":
        d.putValue("BUFFER".format(value["value_"]["BUFFER"]))
    if type_str == "Urho3D::VAR_VOIDPTR":
        d.putValue("VOIDPTR".format(value["value_"]["VOIDPTR"]))
    if type_str == "Urho3D::VAR_RESOURCEREF":
        d.putValue("RESOURCEREF".format(value["value_"]["RESOURCEREF"]))
    if type_str == "Urho3D::VAR_RESOURCEREFLIST":
        d.putValue("RESOURCEREFLIST".format(value["value_"]["RESOURCEREFLIST"]))
    if type_str == "Urho3D::VAR_VARIANTVECTOR":
        d.putValue("VARIANTVECTOR".format(value["value_"]["VARIANTVECTOR"]))
    if type_str == "Urho3D::VAR_VARIANTMAP":
        d.putValue("VARIANTMAP".format(value["value_"]["VARIANTMAP"]))
    if type_str == "Urho3D::VAR_INTRECT":
        d.putValue("INTRECT".format(value["value_"]["INTRECT"]))
    if type_str == "Urho3D::VAR_INTVECTOR2":
        d.putValue("INTVECTOR2".format(value["value_"]["INTVECTOR2"]))
    if type_str == "Urho3D::VAR_PTR":
        d.putValue("PTR".format(value["value_"]["PTR"]))
    if type_str == "Urho3D::VAR_MATRIX3":
        d.putValue("MATRIX3".format(value["value_"]["MATRIX3"]))
    if type_str == "Urho3D::VAR_MATRIX3X4":
        d.putValue("MATRIX3X4".format(value["value_"]["MATRIX3X4"]))
    if type_str == "Urho3D::VAR_MATRIX4":
        d.putValue("MATRIX4".format(value["value_"]["MATRIX4"]))
    if type_str == "Urho3D::VAR_DOUBLE":
        d.putValue("DOUBLE".format(value["value_"]["DOUBLE"]))
    if type_str == "Urho3D::VAR_STRINGVECTOR":
        d.putValue("STRINGVECTOR".format(value["value_"]["STRINGVECTOR"]))

#    for s in dir(value["value_"]):
#        d.put('nanavar="%s"'%s)


def qdump__Urho3D__SharedPtr(d, value):
#based on qdump__std__shared_ptr(d, value):
    i = value["ptr_"]
    if not i:
        d.putValue("(null)")
        d.putNumChild(0)
        return

#    if d.isSimpleType(d.templateArgument(value.type, 0)):
#        d.putValue("{} @0x{:h}".format(d.simpleValue(i.dereference()), d.pointerValue(i)))
#    else:
#        d.putValue("@0x{:h}" % d.pointerValue(i))
    #d.putValue("@0x{0:h}".format(int(i)))
    #d.putAddress(i.dereference().address)
    d.putValue("@x{0:x}".format(int(i)))
    d.putItem(i)
    d.putNumChild(3)
    if d.isExpanded():
        with Children(d, 3):
#            d.putSubItem("data", i)
            refcount = i["refCount_"]
            d.putSubItem("refs_", refcount["refs_"])
            d.putSubItem("weakRefs_", refcount["weakRefs_"])

def qdump__Urho3D__HashMap(d,value):
    keyType = d.templateArgument(value.type, 0)
    valueType = d.templateArgument(value.type, 1)
    ptrs = value["ptrs_"]
    szTypeP = d.lookupType("unsigned*")
    size = 0
    numBuckets = 0
    d.putAddress(value.address)
    if ptrs:
        size = ptrs.cast(szTypeP).dereference()
        numBuckets = (ptrs.cast(szTypeP) + 1).dereference()
    if ptrs:
        d.putValue('[{0}] in {1} @{2}'.format(size,numBuckets,str(ptrs)))
    else:
        d.putValue('empty @{2}'.format(size,numBuckets,str(ptrs)))
        
    p = value["head_"]
    end = value["tail_"]
    d.putItemCount(size)
    
    
    innerType = d.templateArgument(value.type, 0)
    n = int(size)
    p = value["head_"]
    innerType = d.lookupType(value.type.name + "::Node")
    if d.isExpanded():
        with Children(d, n):
            p = value["head_"]
            for i in range(n):
                d.putSubItem("%s" % i, d.createValue(d.pointerValue(p), innerType)["pair_"])
                p = p["next_"]
```

-------------------------

SirNate0 | 2019-08-20 15:04:16 UTC | #4

Added support for a few additional types, like (Int)Vector2/3/4
```
#!/usr/bin/python

#this line is VERY IMPORTANT! And not mentioned in the examples/docs, I'm pretty sure. It is what was causing most of my problems...
from dumper import *
#Thank you Stack Overflow: http://stackoverflow.com/questions/34354573/how-to-write-a-debugging-helper-for-qtcreator

def qdump__Urho3D__Vector(d, value):
    array = value["buffer_"]
    size = value["size_"]
    maxDisplayItems = 100
    innerType = d.templateArgument(value.type, 0)
    p = array.cast(innerType.pointer())
    d.putValue('[{0}] @{1}'.format(size,str(array)))
    d.putItemCount(size)
    if d.isExpanded():
        d.putPlotData(p, size, innerType)
        
qdump__Urho3D__PODVector = qdump__Urho3D__Vector
        
def qdump__Urho3D__Variant(d, value):
    t = value["type_"]
    d.putNumChild(0)
    d.putValue("{} int({})".format(str(t),int(t)))
    i = int(t)
    type_str = str(t)
    if type_str == "Urho3D::VAR_NONE":
        d.putValue("NONE")
    elif type_str == "Urho3D::VAR_INT":
        d.putValue("int {}".format(value["value_"]["int_"]))
    elif type_str == "Urho3D::VAR_BOOL":
        if value["value_"]["bool_"]:
            d.putValue("(bool) true")
        else:
            d.putValue("(bool) false")
    elif type_str == "Urho3D::VAR_FLOAT":
        d.putValue("float {}".format(value["value_"]["float_"]))
    return
    #TODO: finish
    if type_str == "Urho3D::VAR_VECTOR2":
        d.putValue("<{},{}>".format(value["value_"]["VECTOR2"]))
    if type_str == "Urho3D::VAR_VECTOR3":
        d.putValue("VECTOR3".format(value["value_"]["VECTOR3"]))
    if type_str == "Urho3D::VAR_VECTOR4":
        d.putValue("VECTOR4".format(value["value_"]["VECTOR4"]))
    if type_str == "Urho3D::VAR_QUATERNION":
        d.putValue("QUATERNION".format(value["value_"]["QUATERNION"]))
    if type_str == "Urho3D::VAR_COLOR":
        d.putValue("COLOR".format(value["value_"]["COLOR"]))
    if type_str == "Urho3D::VAR_STRING":
        d.putValue("STRING".format(value["value_"]["STRING"]))
    if type_str == "Urho3D::VAR_BUFFER":
        d.putValue("BUFFER".format(value["value_"]["BUFFER"]))
    if type_str == "Urho3D::VAR_VOIDPTR":
        d.putValue("VOIDPTR".format(value["value_"]["VOIDPTR"]))
    if type_str == "Urho3D::VAR_RESOURCEREF":
        d.putValue("RESOURCEREF".format(value["value_"]["RESOURCEREF"]))
    if type_str == "Urho3D::VAR_RESOURCEREFLIST":
        d.putValue("RESOURCEREFLIST".format(value["value_"]["RESOURCEREFLIST"]))
    if type_str == "Urho3D::VAR_VARIANTVECTOR":
        d.putValue("VARIANTVECTOR".format(value["value_"]["VARIANTVECTOR"]))
    if type_str == "Urho3D::VAR_VARIANTMAP":
        d.putValue("VARIANTMAP".format(value["value_"]["VARIANTMAP"]))
    if type_str == "Urho3D::VAR_INTRECT":
        d.putValue("INTRECT".format(value["value_"]["INTRECT"]))
    if type_str == "Urho3D::VAR_INTVECTOR2":
        d.putValue("INTVECTOR2".format(value["value_"]["INTVECTOR2"]))
    if type_str == "Urho3D::VAR_PTR":
        d.putValue("PTR".format(value["value_"]["PTR"]))
    if type_str == "Urho3D::VAR_MATRIX3":
        d.putValue("MATRIX3".format(value["value_"]["MATRIX3"]))
    if type_str == "Urho3D::VAR_MATRIX3X4":
        d.putValue("MATRIX3X4".format(value["value_"]["MATRIX3X4"]))
    if type_str == "Urho3D::VAR_MATRIX4":
        d.putValue("MATRIX4".format(value["value_"]["MATRIX4"]))
    if type_str == "Urho3D::VAR_DOUBLE":
        d.putValue("DOUBLE".format(value["value_"]["DOUBLE"]))
    if type_str == "Urho3D::VAR_STRINGVECTOR":
        d.putValue("STRINGVECTOR".format(value["value_"]["STRINGVECTOR"]))

#    for s in dir(value["value_"]):
#        d.put('nanavar="%s"'%s)


def qdump__Urho3D__SharedPtr(d, value):
#based on qdump__std__shared_ptr(d, value):
    i = value["ptr_"]
    if not i:
        d.putValue("(null)")
        d.putNumChild(0)
        return

#    if d.isSimpleType(d.templateArgument(value.type, 0)):
#        d.putValue("{} @0x{:h}".format(d.simpleValue(i.dereference()), d.pointerValue(i)))
#    else:
#        d.putValue("@0x{:h}" % d.pointerValue(i))
    #d.putValue("@0x{0:h}".format(int(i)))
    #d.putAddress(i.dereference().address)
    d.putValue("@x{0:x}".format(int(i)))
    d.putItem(i)
    d.putNumChild(3)
    if d.isExpanded():
        with Children(d, 3):
#            d.putSubItem("data", i)
            refcount = i["refCount_"]
            d.putSubItem("refs_", refcount["refs_"])
            d.putSubItem("weakRefs_", refcount["weakRefs_"])

def qdump__Urho3D__HashMap(d,value):
    keyType = d.templateArgument(value.type, 0)
    valueType = d.templateArgument(value.type, 1)
    ptrs = value["ptrs_"]
    szTypeP = d.lookupType("unsigned*")
    size = 0
    numBuckets = 0
    d.putAddress(value.address)
    if ptrs:
        size = ptrs.cast(szTypeP).dereference()
        numBuckets = (ptrs.cast(szTypeP) + 1).dereference()
    if ptrs:
        d.putValue('[{0}] in {1} @{2}'.format(size,numBuckets,str(ptrs)))
    else:
        d.putValue('empty @{2}'.format(size,numBuckets,str(ptrs)))
        
    p = value["head_"]
    end = value["tail_"]
    d.putItemCount(size)
    
    
    innerType = d.templateArgument(value.type, 0)
    n = int(size)
    p = value["head_"]
    innerType = d.lookupType(value.type.name + "::Node")
    if d.isExpanded():
        with Children(d, n):
            p = value["head_"]
            for i in range(n):
                d.putSubItem("%s" % i, d.createValue(d.pointerValue(p), innerType)["pair_"])
                p = p["next_"]
                

# https://doc.qt.io/qtcreator/creator-debugging-helpers.html
# def qdump__MapNode(d, value):
#    d.putValue("This is the value column contents")
#    d.putNumChild(2)
#    if d.isExpanded():
#        with Children(d):
#            # Compact simple case.
#            d.putSubItem("key", value["key"])
#            # Same effect, with more customization possibilities.
#            with SubItem(d, "data")
#                d.putItem("data", value["data"])

def generic_numeric_vector(d, value, dirs, bounds_fmt='<{}>', number_fmt='{}'):
    names = ["%s_"%x for x in dirs]
    vals = [number_fmt.format(value[n]) for n in names]
    d.putValue(bounds_fmt.format(', '.join(vals)))
    d.putNumChild(len(names))
    if d.isExpanded():
        with Children(d):
            for n in names:
                d.putSubItem(n,value[n])
    #TODO: maybe add a length faked child member or such
    
def qdump__Urho3D__IntVector2(d, value):
    generic_numeric_vector(d,value,'xy')
    
def qdump__Urho3D__Vector2(d, value):
    generic_numeric_vector(d,value,'xy')
    
def qdump__Urho3D__IntVector3(d, value):
    generic_numeric_vector(d,value,'xyz')
    
def qdump__Urho3D__Vector3(d, value):
    generic_numeric_vector(d,value,'xyz')

def qdump__Urho3D__Vector4(d, value):
    generic_numeric_vector(d,value,'xyzw')
    
def qdump__Urho3D__Quaternion(d, value):
    generic_numeric_vector(d,value,'wxyz','({})')
    

def qdump__Urho3D__Color(d, value):
    generic_numeric_vector(d,value,'rgba','rgba({})')

```

-------------------------

Modanung | 2019-08-20 17:23:15 UTC | #5

:confused:

![NotHelping|690x32](upload://cKHHHF9H4bWDOovrUr0VCaBeOR6.png)

I copied your code into a `.py` file and set it as Extra Debugging Helpers in QtCreator, btw.

If I paste the same code into the _Customization_ field of the debugger options, the debugger fails to start.

-------------------------

SirNate0 | 2019-08-20 18:58:48 UTC | #6

That's how I have it working, saved as a `.py` and pointed to by the Options > Debugger > GDB > Extra Debugging Helpers field. It works for you when saved as a python script, right? I don't see why it wouldn't work pasted in the Debugging Helper Customization field, but I haven't tried it. Based on the tooltip the block (I'm not certain what defines a block) the code would have to be surrounded by a `python` and an `end` (and as a guess maybe the import statement would need to be removed?)...

It's a very different display than mine, however. My guess is this is from a different version of QtCreator and/or GDB. With my setup I get values displayed like this ![gdbVisualizerResults|443x186](upload://96cG8o46wQFlf5uGieJhTd8OIYV.png) 
This is using
```
Qt Creator 3.5.1 (opensource)
Based on Qt 5.5.1 (GCC 4.9.1 20140922 (Red Hat 4.9.1-10), 64 bit)
Built on Oct 15 2015 01:56:01
From revision b4c52505ca
```
with 
```
GNU gdb (Ubuntu 7.11.1-0ubuntu1~16.5) 7.11.1
```

I'll make a repository for this, and then if anyone figures out how to make improvements pull requests can be made there.

Edit: didn't notice the formatting hid the version of Qt Creator, fixed it now.

-------------------------

Modanung | 2019-08-20 19:14:00 UTC | #7

[quote="SirNate0, post:6, topic:2849"]
It works for you when saved as a python script, right?
[/quote]

Neither works (properly) for me, and *here* the Extra Debugging Helpers field is under the Locals & Expressions tab. Version information is as follows:

> Qt Creator 4.5.2
Based on Qt 5.9.5 (GCC 7.3.0, 64 bit)

>GNU gdb (Ubuntu 8.1-0ubuntu3) 8.1.0.20180409-git

-------------------------

SirNate0 | 2020-07-08 20:38:10 UTC | #8

I switched to a newer version of Qt Creator for my desktop and got the debugging helpers working with that. I did initial see (and corrected) the same sort of improper output (`Value(name='x_'...)`) sort of output, so hopefully these will work better.

I have not finished all of them (e.g. Variant is still broken), but I believe Vector and HashMap are working correctly, which are probably the most useful ones. If you want to disable one of them you can just comment it out or change the name of the function so it doesn't match the class any more (like I did with the "old" ones).

At some point I'll probably finish at least Variant and come back and edit this and/or throw it on Github, but for now hopefully it's useful to someone.

```py
#!/usr/bin/python

#this line is VERY IMPORTANT! And not mentioned in the examples/docs, I'm pretty sure. It is what was causing most of my problems...
from dumper import *
#Thank you Stack Overflow: http://stackoverflow.com/questions/34354573/how-to-write-a-debugging-helper-for-qtcreator

# also helpful https://github.com/qt-creator/qt-creator/blob/master/share/qtcreator/debugger/dumper.py

# very very helpful: https://doc.qt.io/qtcreator/creator-debugging-helpers.html

def old_qdump__Urho3D__Vector(d, value):
    array = value["buffer_"]
    size = value["size_"]
    maxDisplayItems = 100
    innerType = d.templateArgument(value.type, 0)
    p = array.cast(innerType.pointer())
    #d.putValue('[{0}] @{1}'.format(size,str(array)))
    #d.putItemCount(size)
    #d.putNumChild(size)
    #d.putNumChild(size)
    d.putNumChild(10)
    if d.isExpanded():
        #d.putPlotData(p, size, innerType)
        with Children(d):
            try:
                d.putSubItem("{!s}".format((p.pointer(),size.integer())).replace("'","$").replace('"','|'),size)
                with SubItem(d, "data"):
                    d.putValue('<{}> items @0x{:x}'.format(size.integer(),p.pointer()))
                    d.putArrayData(p.pointer(), size.integer(), innerType)
            except Exception as e:
                #d.put('value="<invalid>",type="<unknown>",numchild="0",')
                d.putSubItem("EXCEPTION! {!s}".format(e).replace("'","$").replace('"','|'),size)

            d.putSubItem("size", size)
            #with SubItem(d):
                #d.putName("test-with-sub")
                #d.putItem("buffer",size)
            d.putSubItem("{!s}".format(size).replace("'","$").replace('"','|'),size)
            d.putSubItem("{!s}".format(array),size)
            d.putSubItem("{!s}".format(value.type).replace("'","$").replace('"','|'),size)
            d.putSubItem("{!s}".format(innerType).replace("'","$").replace('"','|'),size)
            d.putSubItem("{!s}".format(p).replace("'","$").replace('"','|'),size)
            #with SubItem(d, "buffer") as sub:
                #sub.putNumChild(size)
                #if sub.isExpanded():
                    #with Children(sub):
                        #sub.putArrayData(array, size, value.type[0])
        
def qdump__Urho3D__Vector(d, value):
    array = value["buffer_"]
    size = value["size_"]
    maxDisplayItems = 100
    innerType = d.templateArgument(value.type, 0)
    p = array.cast(innerType.pointer())
    d.putNumChild(size.integer())
    if d.isExpanded():
        with Children(d):
            try:
                with SubItem(d, "data"):
                    d.putValue('<{}> items @0x{:x}'.format(size.integer(),p.pointer()))
                    d.putArrayData(p.pointer(), size.integer(), innerType)
            except Exception as e:
                #d.put('value="<invalid>",type="<unknown>",numchild="0",')
                d.putSubItem("EXCEPTION! {!s}".format(e).replace("'","$").replace('"','|'),size)

qdump__Urho3D__PODVector = qdump__Urho3D__Vector
        
def qdump__Urho3D__Variant(d, value):
    t = value["type_"]
    d.putNumChild(0)
    d.putValue("{} int({})".format(str(t),int(t)))
    i = int(t)
    type_str = str(t)
    if type_str == "Urho3D::VAR_NONE":
        d.putValue("NONE")
    elif type_str == "Urho3D::VAR_INT":
        d.putValue("int {}".format(value["value_"]["int_"]))
    elif type_str == "Urho3D::VAR_BOOL":
        if value["value_"]["bool_"]:
            d.putValue("(bool) true")
        else:
            d.putValue("(bool) false")
    elif type_str == "Urho3D::VAR_FLOAT":
        d.putValue("float {}".format(value["value_"]["float_"]))
    return
    #TODO: finish
    if type_str == "Urho3D::VAR_VECTOR2":
        d.putValue("<{},{}>".format(value["value_"]["VECTOR2"]))
    if type_str == "Urho3D::VAR_VECTOR3":
        d.putValue("VECTOR3".format(value["value_"]["VECTOR3"]))
    if type_str == "Urho3D::VAR_VECTOR4":
        d.putValue("VECTOR4".format(value["value_"]["VECTOR4"]))
    if type_str == "Urho3D::VAR_QUATERNION":
        d.putValue("QUATERNION".format(value["value_"]["QUATERNION"]))
    if type_str == "Urho3D::VAR_COLOR":
        d.putValue("COLOR".format(value["value_"]["COLOR"]))
    if type_str == "Urho3D::VAR_STRING":
        d.putValue("STRING".format(value["value_"]["STRING"]))
    if type_str == "Urho3D::VAR_BUFFER":
        d.putValue("BUFFER".format(value["value_"]["BUFFER"]))
    if type_str == "Urho3D::VAR_VOIDPTR":
        d.putValue("VOIDPTR".format(value["value_"]["VOIDPTR"]))
    if type_str == "Urho3D::VAR_RESOURCEREF":
        d.putValue("RESOURCEREF".format(value["value_"]["RESOURCEREF"]))
    if type_str == "Urho3D::VAR_RESOURCEREFLIST":
        d.putValue("RESOURCEREFLIST".format(value["value_"]["RESOURCEREFLIST"]))
    if type_str == "Urho3D::VAR_VARIANTVECTOR":
        d.putValue("VARIANTVECTOR".format(value["value_"]["VARIANTVECTOR"]))
    if type_str == "Urho3D::VAR_VARIANTMAP":
        d.putValue("VARIANTMAP".format(value["value_"]["VARIANTMAP"]))
    if type_str == "Urho3D::VAR_INTRECT":
        d.putValue("INTRECT".format(value["value_"]["INTRECT"]))
    if type_str == "Urho3D::VAR_INTVECTOR2":
        d.putValue("INTVECTOR2".format(value["value_"]["INTVECTOR2"]))
    if type_str == "Urho3D::VAR_PTR":
        d.putValue("PTR".format(value["value_"]["PTR"]))
    if type_str == "Urho3D::VAR_MATRIX3":
        d.putValue("MATRIX3".format(value["value_"]["MATRIX3"]))
    if type_str == "Urho3D::VAR_MATRIX3X4":
        d.putValue("MATRIX3X4".format(value["value_"]["MATRIX3X4"]))
    if type_str == "Urho3D::VAR_MATRIX4":
        d.putValue("MATRIX4".format(value["value_"]["MATRIX4"]))
    if type_str == "Urho3D::VAR_DOUBLE":
        d.putValue("DOUBLE".format(value["value_"]["DOUBLE"]))
    if type_str == "Urho3D::VAR_STRINGVECTOR":
        d.putValue("STRINGVECTOR".format(value["value_"]["STRINGVECTOR"]))

#    for s in dir(value["value_"]):
#        d.put('nanavar="%s"'%s)


def qdump__Urho3D__SharedPtr(d, value):
#based on qdump__std__shared_ptr(d, value):
    i = value["ptr_"]
    if not i:
        d.putValue("(null)")
        d.putNumChild(0)
        return

#    if d.isSimpleType(d.templateArgument(value.type, 0)):
#        d.putValue("{} @0x{:h}".format(d.simpleValue(i.dereference()), d.pointerValue(i)))
#    else:
#        d.putValue("@0x{:h}" % d.pointerValue(i))
    #d.putValue("@0x{0:h}".format(int(i)))
    #d.putAddress(i.dereference().address)
    d.putValue("@x{0:x}".format(int(i)))
    d.putItem(i)
    d.putNumChild(3)
    if d.isExpanded():
        with Children(d, 3):
#            d.putSubItem("data", i)
            refcount = i["refCount_"]
            d.putSubItem("refs_", refcount["refs_"])
            d.putSubItem("weakRefs_", refcount["weakRefs_"])


def qdump__Urho3D__HashMap(d, value):
    keyType = d.templateArgument(value.type, 0)
    valueType = d.templateArgument(value.type, 1)
    ptrs = value["ptrs_"]
    ptrsVal = ptrs.pointer()
    szTypeP = d.lookupType("unsigned*")
    size = 0
    numBuckets = 0
    #d.putAddress(value.address())
    #innerType = d.templateArgument(value.type, 0)
    #p = array.cast(innerType.pointer())
    #d.putNumChild(size.integer())
    
    if ptrsVal:
        sizeValue = ptrs.cast(szTypeP).dereference()
        size = sizeValue.integer()
        numBuckets = (ptrs.cast(szTypeP) + 1).dereference().integer()
        d.putValue('<{0}> in {1} buckets @{2:x}'.format(size,numBuckets,ptrsVal))
    else:
        d.putValue('empty @{:x}'.format(ptrsVal))
    
    d.putNumChild(size)
    if d.isExpanded():
        with Children(d):
            try:
                #with SubItem(d, "data"):
                    #d.putValue('<{!s}> items @0x{!s}'.format(ptrs, szTypeP).replace("'","$").replace('"','|'))
                #with SubItem(d, "address?"):
                    #d.putValue('@0x{:x}'.format(ptrsVal))
                #d.putSubItem("{!s}".format(ptrsVal).replace("'","$").replace('"','|'),ptrs)
                innerType = d.templateArgument(value.type, 0)
                n = int(size)
                p = value["head_"]
                innerType = d.lookupType(value.type.name + "::Node")
                for i in range(n):
                    pair = d.createValue(p.pointer(), innerType)["pair_"]
                    #d.putSubItem("{!s}".format(pair).replace("'","$").replace('"','|'),sizeValue)
                    d.putSubItem("[{}]".format(i),pair)
                    #with SubItem(d, str(i)):
                        #d.putType(innerType.name)
                        #d.putType('double')
                        #d.putValue("{!s}".format(pair).replace("'","$").replace('"','|'))
                        #d.putValue(d.hexencode(str(innerType.name)).format(pair).replace("'","$").replace('"','|'))
                        #d.putNumChild(0)
                    #with SubItem(d, str(i-10)):
                        #d.putType('double')
                        #d.putValue("{!s}".format(innerType).replace("'","$").replace('"','|'))
                        #d.putNumChild(1)
                    #with SubItem(d, str(i-100)):
                        #d.putType('double')
                        #d.putValue("{!s}".format(innerType.name).replace("'","$").replace('"','|'))
                        #d.putNumChild(1)
                    #d.putSubItem("{!s}".format(ptrsVal).replace("'","$").replace('"','|'),ptrs)
                    #d.putSubItem("[%s]" % i, )
                    p = p["next_"]
            except Exception as e:
                #d.put('value="<invalid>",type="<unknown>",numchild="0",')
                d.putSubItem("EXCEPTION! {!s}".format(e).replace("'","$").replace('"','|'),ptrs)

def qdump_old__Urho3D__HashMap(d,value):
    try:
        keyType = d.templateArgument(value.type, 0)
        valueType = d.templateArgument(value.type, 1)
        ptrs = value["ptrs_"]
        szTypeP = d.lookupType("unsigned*")
        size = 0
        numBuckets = 0
        d.putAddress(value.address)
        if ptrs:
            size = ptrs.cast(szTypeP).dereference()
            numBuckets = (ptrs.cast(szTypeP) + 1).dereference()
        if ptrs:
            d.putValue('[{0}] in {1} @{2}'.format(size,numBuckets,str(ptrs)))
        else:
            d.putValue('empty @{2}'.format(size,numBuckets,str(ptrs)))
            
        p = value["head_"]
        end = value["tail_"]
        d.putItemCount(size.integer())
        
        
        innerType = d.templateArgument(value.type, 0)
        n = int(size)
        p = value["head_"]
        innerType = d.lookupType(value.type.name + "::Node")
        if d.isExpanded():
            with Children(d, n):
                p = value["head_"]
                for i in range(n):
                    d.putSubItem("%s" % i, d.createValue(d.pointerValue(p), innerType)["pair_"])
                    p = p["next_"]
    
    except Exception as e:
        d.putNumChild(10)
        if d.isExpanded():
            #d.putPlotData(p, size, innerType)
            with Children(d):
                #d.put('value="<invalid>",type="<unknown>",numchild="0",')
                with SubItem(d,'exception'):
                    d.putField("EXCEPTION! {!s}".format(e).replace("'","$").replace('"','|'))
                    d.putType('unsigned')
                    d.putValue('error')

                

# https://doc.qt.io/qtcreator/creator-debugging-helpers.html
# def qdump__MapNode(d, value):
#    d.putValue("This is the value column contents")
#    d.putNumChild(2)
#    if d.isExpanded():
#        with Children(d):
#            # Compact simple case.
#            d.putSubItem("key", value["key"])
#            # Same effect, with more customization possibilities.
#            with SubItem(d, "data")
#                d.putItem("data", value["data"])

def generic_numeric_vector(d, value, dirs, bounds_fmt='<{}>', number_fmt='{}'):
    names = ["%s_"%x for x in dirs]
    vals = [number_fmt.format(value[n].value()) for n in names]
    d.putValue(bounds_fmt.format(', '.join(vals)))
    d.putNumChild(len(names))
    if d.isExpanded():
        with Children(d):
            for n in names:
                d.putSubItem(n,value[n])
#    x,y,z = [value["%s_"%x] for x in 'xyz']
#    d.putValue('<{},{},{}>'.format(x,y,z))
#    d.putNumChild(3)
#    if d.isExpanded():
#        with Children(d):
#            for x in 'xyz':
#                d.putSubItem("%s_"%x,value['%s_'%x])
    #TODO: maybe add a length faked child member or such
    
def qdump__Urho3D__IntVector2(d, value):
    generic_numeric_vector(d,value,'xy')
    
def qdump__Urho3D__Vector2(d, value):
    generic_numeric_vector(d,value,'xy')
    
def qdump__Urho3D__IntVector3(d, value):
    generic_numeric_vector(d,value,'xyz')
    
def qdump__Urho3D__Vector3(d, value):
    generic_numeric_vector(d,value,'xyz')

def qdump__Urho3D__Vector4(d, value):
    generic_numeric_vector(d,value,'xyzw')
    
def qdump__Urho3D__Quaternion(d, value):
    generic_numeric_vector(d,value,'wxyz','({})')
    

def qdump__Urho3D__Color(d, value):
    generic_numeric_vector(d,value,'rgba','rgba({})')

```

For reference, I am using 
```
Qt Creator 4.11.0
Based on Qt 5.12.8 (GCC 9.3.0, 64 bit)

GNU gdb (Ubuntu 9.1-0ubuntu1) 9.1
```

**Edit**: Got a half-way finished dumper for Urho3D::Variant finished:
```py 
def qdump__Urho3D__Variant(d, value):
    
    types = [
        'VAR_NONE',
        'VAR_INT',
        'VAR_BOOL',
        'VAR_FLOAT',
        'VAR_VECTOR2',
        'VAR_VECTOR3',
        'VAR_VECTOR4',
        'VAR_QUATERNION',
        'VAR_COLOR',
        'VAR_STRING',
        'VAR_BUFFER',
        'VAR_VOIDPTR',
        'VAR_RESOURCEREF',
        'VAR_RESOURCEREFLIST',
        'VAR_VARIANTVECTOR',
        'VAR_VARIANTMAP',
        'VAR_INTRECT',
        'VAR_INTVECTOR2',
        'VAR_PTR',
        'VAR_MATRIX3',
        'VAR_MATRIX3X4',
        'VAR_MATRIX4',
        'VAR_DOUBLE',
        'VAR_STRINGVECTOR',
        'VAR_RECT',
        'VAR_INTVECTOR3',
        'VAR_INT64',
        'VAR_CUSTOM_HEAP',
        'VAR_CUSTOM_STACK',
        'MAX_VAR_TYPES'
    ]
    
    try:
        import struct
        
        t = value["type_"]
        i = int(t)
        #type_str = str(t)
        type_str = 'Urho3D::' + types[t.integer()]
        if type_str == "Urho3D::VAR_NONE":
            d.putNumChild(0)
            d.putValue("NONE")
        elif type_str == "Urho3D::VAR_INT":
            d.putNumChild(0)
            d.putValue("int {}".format(value["value_"]["int_"].integer()))
        elif type_str == "Urho3D::VAR_BOOL":
            d.putNumChild(0)
            if value["value_"]["bool_"].integer():
                d.putValue("(bool) true")
            else:
                d.putValue("(bool) false")
        elif type_str == "Urho3D::VAR_FLOAT":
            d.putNumChild(0)
            data = value["value_"]["float_"].data()
            #sz = data.tobytes() # data.format
            #d.putValue("float {} tp {} sz {}".format(type(data),sz,data))
            (val,) = struct.unpack('f',data)
            d.putValue("float {:g}".format(val))
        elif type_str == "Urho3D::VAR_DOUBLE":
            #d.putNumChild(0)
            #data = value["value_"]["double_"].data()
            #(val,) = struct.unpack('d',data)
            #d.putValue("double {:g}".format(val))
            d.putItem(value["value_"]["double_"])
            d.putBetterType('Variant:double')
        elif type_str == "Urho3D::VAR_VECTOR2":
            d.putItem(value["value_"]["vector2_"])
            d.putType("Variant:Vector2")
        elif type_str == "Urho3D::VAR_VECTOR3":
            d.putItem(value["value_"]["vector3_"])
            d.putType("Variant:Vector3")
        elif type_str == "Urho3D::VAR_VECTOR4":
            d.putItem(value["value_"]["vector4_"])
            d.putType("Variant:Vector4")
        elif type_str == "Urho3D::VAR_QUATERNION":
            d.putItem(value["value_"]["quaternion_"])
            d.putType("Variant:Quaternion")
        elif type_str == "Urho3D::VAR_INTVECTOR2":
            d.putItem(value["value_"]["intVector2_"])
            d.putType("Variant:IntVector2")
        elif type_str == "Urho3D::VAR_INTVECTOR3":
            d.putItem(value["value_"]["intVector3_"])
            d.putType("Variant:IntVector3")
        elif type_str == "Urho3D::VAR_COLOR":
            d.putItem(value["value_"]["color_"])
            d.putType("Variant:Color")
        elif type_str == "Urho3D::VAR_STRING":
            d.putItem(value["value_"]["string_"])
            d.putType("Variant:String")
        elif type_str == "Urho3D::VAR_MATRIX3":
            d.putItem(value["value_"]["matrix3_"])
            d.putType("Variant:Matrix3")
        elif type_str == "Urho3D::VAR_MATRIX3X4":
            val = value["value_"]["matrix3x4_"]
            d.putItem(val)
            d.putBetterType(val.type.name.replace('Urho3D:','Variant'))
        elif type_str == "Urho3D::VAR_MATRIX4":
            val = value["value_"]["matrix4_"]
            d.putItem(val)
            d.putBetterType(val.type.name.replace('Urho3D:','Variant'))
        else:
            d.putValue("{} int({})".format(type_str,t.integer()))
    except Exception as e:
        d.putValue("EXCEPTION! {!s}".format(e).replace("'","$").replace('"','|'))
        
    return
```

-------------------------

