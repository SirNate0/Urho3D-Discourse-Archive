slapin | 2017-05-05 14:04:21 UTC | #1

I have an array of strings representing objects.
I want to construct the objects without too many ifs.

    Array<String> stuff = {
       "bh_node1",
       "bh_node2",
    ...
    }

    Array<TreeElement@> items;

    ....
    for (int i = 0; i < stuff.length; i++) {
        if (stuff[i] == "bh_node1")
            items.Push(ConstructBhNode1());
        else if (stuff[i] == "bh_node2")
            items.Push(ConstructBhNode2());
    ...
    }

I'm not really happy with all this long lines with ifs and hardcoding data in code.
Is there some way to produce lists, line in C or C++ where I could just run respective pointer?
Otherwise it looks very annoying and hard to maintain...

-------------------------

orefkov | 2017-05-05 22:58:36 UTC | #2

You can use funcdefs and creators functions, like this:

    interface SomeIface {
    	void printName();
    };

    class IfaceImpl1 : SomeIface {
    	void printName() {
    		Print("Impl1");
    	}
    };

    class IfaceImpl2 : SomeIface {
    	void printName() {
    		Print("Impl2");
    	}
    };

    funcdef SomeIface@ IfaceCreator();

    SomeIface@ creator1() {
    	return IfaceImpl1();
    }

    SomeIface@ creator2() {
    	return IfaceImpl2();
    }

    Dictionary creators = {{"impl1", creator1},{"impl2", creator2}};

    SomeIface@ createByName(const String& name) {
    	if (creators.Exists(name)) {
    		IfaceCreator@ c = cast<IfaceCreator>(creators[name]);
    		return c();
    	}
    	return null;
    }

    void test() {
    	SomeIface@ iface = createByName("impl1");
    	iface.printName();
    	@iface = createByName("impl2");
    	iface.printName();
    }

Or if your objects links to nodes, you can use ScriptObject - it is created by name.

-------------------------

slapin | 2017-05-05 22:56:21 UTC | #3

Thanks a lot!
The solution is nice!

-------------------------

