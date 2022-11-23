codefive | 2019-06-03 00:52:49 UTC | #1

I have finished creating a class that will hold some models, now i want to create a instance of it, but when i do it i break the engine and get a segment fault. For what i know the class has no errors, it inherits from LogicComponent. When i add the class to the main app i do the following.-

1.- In the main app i create a pointer to my class
    
     Myexampleclass* myclass_;

2.- Also create a node pointer for the class Model, etc
    
     SharedPtr<Node> myclassNode_;

So inside a function i just do.-
     
    myclassNode_->CreateComponent<Myexampleclass>();

Or should i use the new keyword? I dont think so, but maybe

    myclass = new Myexampleclass();

Thank you in advance !!! You great ones !!

-------------------------

JTippetts1 | 2019-06-03 03:21:08 UTC | #2

You have to make sure to call Context::RegisterFactory<Myexampleclass>() before you call CreateComponent, or it wont create anything.

-------------------------

Leith | 2019-06-03 07:34:40 UTC | #3

Also, you really should use a WeakPtr to hold the returned component pointer, rather than a SharedPtr, because the object lifetime is already being managed by the scene - components can only exist as part of a scene, and are automatically destroyed when they are removed from the scene.
When this happens, the WeakPtr will contain nullptr, this would not be the case if you used a SharedPtr due to the extra reference being counted.

The way I like to think of it? Generally, if I am ultimately responsible for object destruction, I should use SharedPtr, but if someone else is going to handle the destruction of the object, I should use a WeakPtr. There's no compelling reason I can think of to ever use a naked object pointer, or rawptr, or worse, a voidptr, however I do these things quite often, mostly as a redundant legacy of my low-level programming background.

-------------------------

codefive | 2019-06-03 09:39:57 UTC | #4

Thank you, so RegisterFactory is called somewhere inside my class, i will call that function then, yes i was thinking of using a WeakPtr, but i didnt understood the difference until @Leith mentioned it. Thank you both and happy coding !!!

-------------------------

Leith | 2019-06-03 09:52:58 UTC | #5

NO! RegisterObjectFactory is called from outside your class !! You make a static! method called that or similar, and you call it from your app initialization code to register the class within urho.
You need to call this once, for each custom class, before you ever try to make any instances of them.

-------------------------

Leith | 2019-06-03 09:54:39 UTC | #6

static void RegisterMyDamnClass(Context* ctxt) { stuff }

-------------------------

codefive | 2019-06-03 09:55:49 UTC | #7

Oh theres a flaw in my class design, i will remove it from there and if you allow me i will tell you how it goes all !!

-------------------------

Leith | 2019-06-03 10:14:34 UTC | #8

allow you? haha, its all good! if you need more help, or maybe a proper example, anything you need to help you I will try to provide it - we seem to have somewhat of a society of friends here, which is something I can back up
[code]
        /// Every GameState must implement a static method for registering the class with Urho3D
        /// Note: we can be lazy, and refer to the current class name as 'ClassName' rather than 'GameIntroState'
        void GameIntroState::RegisterObject(Context* context){
            // Register factory for this class
            context->RegisterFactory<ClassName>();
            // Define any Attributes (AKA Properties) that we want to be able to serialize
            URHO3D_ATTRIBUTE("My Value",float,myValue,666.0f,AM_FILE); // note: AM_FILE means 'serialize to disk' - see AM_DEFAULT !!!
        }
[/code]

-------------------------

Modanung | 2019-06-03 23:20:39 UTC | #9

[quote="Leith, post:8, topic:5211"]
context->RegisterFactory<ClassName>();
[/quote]

Although it is indeed conventional to wrap the object registration into a `static` function, this is not a requirement. One _can_ call `RegisterFactory<MeClass>()` directly on the `Context` from anywhere (but in time) provided no attributes require registration, in which case it just becomes convenient to wrap it into a function.

-------------------------

Leith | 2019-06-04 05:19:25 UTC | #10

Absolutely, it's just a pattern that is pervasive in Urho, that each class provides some snippet of code to deal with its registration requirements, which can be called prior to any instantiation of the class. Static method is the obvious choice. There's a bunch of ways we could approach class registration, but I personally like the notion of encapsulating that stuff in an appropriately named static method.

-------------------------

codefive | 2019-06-04 20:48:33 UTC | #11

Well if you ask me both ways seem valid :wink: Thats why it is static, because it is executed/created before anything

-------------------------

codefive | 2019-06-04 22:02:52 UTC | #12

Now i have a "Reference without definition" In my class constructor. Do you know what im doing wrong? Heres a example of my code.-

Myexampleclass* myclass; 

myclass = new Myexampleclass(context_);

classNode->RegisterObject(context_);

classNode->CreateComponent<Myexampleclass>();

I am near thanks to all, but not quite there...

"Reference to collect2 error"

-------------------------

Dave82 | 2019-06-04 23:41:33 UTC | #13

As i see there are a lot of flaw in your code. But the problem is you're missing the point of the overall Urho3d class design. 
 
[quote="codefive, post:12, topic:5211"]
Myexampleclass* myclass;
[/quote]
This is a common c++ mistake. You should NEVER declare a pointer and leave in uninitialized ! Most likely you're getting a warning message of "unitialized local variable" or something similar.

You should : 
[code]
Myexampleclass* myclass = NULL;
myclass = new Myexampleclass(context_);
[/code]
or
[code]
Myexampleclass* myclass =  new Myexampleclass(context_);
[/code]
Also this is wrong. You should never  create components without a node. Some may work but standalone components could crash your app because they may require to be attache to a node (i remember in 1.4 version the StaticModel needed a node otherwise it would crash. however this is not the case in 1.5)
So the correct syntax is : 
[code]
Myexampleclass* myclass = classNode->CreateComponent<Myexampleclass>();
[/code]

this part
[code]
classNode->RegisterObject(context_);
[/code]
doesn't make any sense. I assume classNode is a Urho3D::Node , so RegisterObject(context_); doesn't make any sense. Urho3D::Node is not a component so you can't register it as a component.

you need to register you custom component like Leith suggested with
[code]context->RegisterFactory<Myexampleclass>();[/code]

and then create instances with : 
[code]Myexampleclass* myclass = classNode->CreateComponent<Myexampleclass>();[/code]

-------------------------

codefive | 2019-06-04 23:52:24 UTC | #14

Ok i will tell you how it goes, i think i now got it, thank you !!!

-------------------------

codefive | 2019-06-05 00:00:29 UTC | #15

Yes, @Dave82 i got it running now, feeling a little fool, but thank you everyone !!!

-------------------------

