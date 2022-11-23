SeeSoftware | 2017-12-01 23:40:06 UTC | #1

Is there a way to pass aditional parameters into custom c++ Components eg i have this component:
    
    class MyComponent : public LogicComponent // or Component whatever
    {
    	URHO3D_OBJECT(MyComponent , LogicComponent)
        
        public:
            MyComponent(Context* context,int foo,int bar)
        ...
        ...
        ...
    }

is there a way i could create the component in a node with some additional parameters like this:

    	node->CreateComponent<MyComponent>(CreateMode::REPLICATED, 0, 123, 456); //last 2 are the additional parameters

i know i could create the component with 

`MyComponent* comp = new MyComponent(context_,123,456)` 

and then add it to the node like this 

`node->AddComponent(comp, 0, CreateMode::REPLICATED);`

but its kinda ugly and i would prefere variadic templates
like its done in std::make_shared

-------------------------

SirNate0 | 2017-12-02 23:23:37 UTC | #2

As far as I know there is not a way presently to do that. Since I think we're now using C++11 by default, perhaps this will (or has already) changed.

I think, though, that these functions will let you do more of what you want to do:
```
template<class C, typename... Types>
C* FullCreateComponent(Node* n, unsigned id, CreateMode cm, Context* context, Types... args)
{
    C* comp = new C(context,args...);
    n->AddComponent(comp, id, cm);
    return comp;
}

template<class C, typename... Types>
C* FullCreateComponent(Node* n, unsigned id, Context* context, Types... args)
{
    C* comp = new C(context,args...);
    n->AddComponent(comp, id, REPLICATED);
    return comp;
}

template<class C, typename... Types>
C* FullCreateComponent(Node* n, Context* context, Types... args)
{
    C* comp = new C(context,args...);
    n->AddComponent(comp, 0, REPLICATED);
    return comp;
}
```
Called like:
```
Battler* b = FullCreateComponent<Battler>(node,context_,filename);
```

-------------------------

Eugene | 2017-12-03 08:08:26 UTC | #3

As @SirNate0 said, there is no way.

Once you step away from "default" constructors, the big part of Scene features gets broken (e.g. serialization and replication).
So, every component should have properly working "default" ctor anyway.
So, there is no much sence in supporting custom ctors.

Please fix me if I'm wrong.

-------------------------

SeeSoftware | 2017-12-03 14:28:57 UTC | #4

The problem for me is that i need some variables to exist in the constructor and by having a seperate Initialize function leaves the object in an invalid state if i dont call Initialize. Ofc you could have the constructor use good known values and then if you want you can change those with another function but it just doesnt feel right doing it like that.

-------------------------

