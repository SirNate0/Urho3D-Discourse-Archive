HaeferlKaffee | 2018-09-09 00:37:32 UTC | #1

I'm trying to create a base component to be used as a timer, with a blank function for an action when the timer reaches 0. If being used in a derived function, the derived class' function should be called instead. My problem is that when registering these components to be used as factories, the last derived class is forced, like so:

_base_
|_->_derived1_
|_->_derived2_

    RegisterObject(base);
    RegisterObject(derived1);
    RegisterObject(derived2); 

When trying to attach a _derived1_ to an object, it will instead attach a _derived2_, the inverse if the order of the two is reversed.

Current source:

        ...
    class SelfDestructor : public LogicComponent {
    	URHO3D_OBJECT(SelfDestructor, LogicComponent);

    public:
    	SelfDestructor(Context* context);

    	/// Register object factory and attributes.
    	static void RegisterObject(Context* context);
    	void Start() override;
    	void Update(float timeStep) override;
    	void setTimer(float t);
    	void resetTimer();
    	virtual void Destruct() {}; //Only to be overriden, no base.

    protected:
    	float time = 0.0f;
    	float timeMax = 0.0f;
    	bool complete = false;
    };

    class SelfEmitToggler : public SelfDestructor { //First subclass
    	URHO3D_OBJECT(SelfEmitToggler , SelfDestructor);
    public:
    	SelfEmitToggler(Context* context);
    	static void RegisterObject(Context* context);
    protected:
    	void Destruct() override;
    };

    class SelfNodeRemover : public SelfDestructor { //Second subclass
    	URHO3D_OBJECT(SelfNodeRemover , SelfDestructor);
    public:
    	SelfNodeRemover(Context* context);
    	static void RegisterObject(Context* context);
    protected:
    	void Destruct() override;
    };

Which are registered by:

    Lightning::RegisterObject(context_);
    SelfDestructor::RegisterObject(context_);
    SelfEmitToggler::RegisterObject(context_);

In the above, only SelfEmitToggler can be attached, in that only its version of Destruct(); will be called, rather than SelfDestructor's.

-------------------------

Modanung | 2018-09-09 15:19:54 UTC | #2

This is normal behaviour when overriding. To make sure the parent class's function is used, call it by prepending its namespace:
```
void SelfNodeRemover::Destruct()
{
    //Code before calling parent function

    SelfDestructor::Destruct();

    //Code after calling parent function
}
```
Since `SelfDustructor::Destruct()` is commented with "no base", you may want to make it a _virtual function_ by replacing `{}` by `= 0` like so:
```
    virtual void Destruct() = 0;
```
This will make `SelfDestruct` an _abstract class_, which cannot be instantiated.

-------------------------

