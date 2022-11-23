ghidra | 2017-01-02 00:59:54 UTC | #1

I'm trying to move some stuff into classes, using the scriptObject.
If I make a "custom" function, I get Null pointer access for trying to call it from the main script.
for example:

[code]
Character@ _character;

void CreateScene(){
  Node@ character_node = _scene.CreateChild("Character");
  Character@ _character = cast<Character>(character_node.CreateScriptObject(scriptFile, "Character"));
  _character.set_parameters();
}

void MoveCamera(float timeStep){
   _character.push_object();
}
[/code]

That call in MoveCamera is what is giving me the error.
I might be going about this completely the wrong way. I was going to look at approaching this differently, but I still wanted to ask, what might be the right way to try and call a function of a script object like this... if this is at all acceptable?

-------------------------

friesencr | 2017-01-02 00:59:54 UTC | #2

Looks like a scoping issue.  The global variable isn't being assigned.  try this.

[code]
Character@ _character;

void CreateScene(){
  Node@ character_node = _scene.CreateChild("Character");
  _character = cast<Character>(character_node.CreateScriptObject(scriptFile, "Character"));
  _character.set_parameters();
}

void MoveCamera(float timeStep){
   _character.push_object();
}
[/code]

-------------------------

ghidra | 2017-01-02 00:59:54 UTC | #3

silly mistakes.
Just tried it, and now that line is throwing the error. I must have another silly mistake elsewhere.

EDIT:
Just tried it the long form way from the 05_AnimatingScene.as example, and same error.

-------------------------

friesencr | 2017-01-02 00:59:54 UTC | #4

if you post a gist i will check it out.  i am missing the big picture.

-------------------------

ghidra | 2017-01-02 00:59:54 UTC | #5

I appreciate your time.
Basically the gist is the same as the above.

I changed the line from Character@ _character = , to just _character = as you suggested. And then the error moved from the MoveCamera function to that line in CreateScene. It's like it wont let me create the script instance on a global pointer.

The long form that I was mentioning, is using the few lines that 05 example uses, incase there is something lost in translation.

[code]
ScriptInstance@ instance = character_node.CreateComponent("ScriptInstance");
instance.CreateObject(scriptFile,"Character");
_character = cast<Character>(instance.object);
[/code]

But that didnt help anything.

The issue is, that I am trying to be able to have access to a scriptInstance object to call function on it from the main class. Maybe that is bad form?

Ultimately, I am just trying to move some functionality out of the main script into external classes for management. I am trying to move the user input into a class, to be funneled through the main class to the objects that need it. Just trying to get a more class based script setup going. Move the stuff in MoveCamera function into thier own class. Anything dealing with the main character into a class etc.... All the examples happen in a single script file, so there arent a lot of example in the default build that go over, it, except maybe the editor files, which I havent dug into too much so far, maybe I should.

-------------------------

friesencr | 2017-01-02 00:59:54 UTC | #6

I can't quite tell from what you are saying, is the Character class defined inside the same script file you are working in? Does the Character class inherit from ScriptObject?  An invalid cast will result in a nil handle.

Urho will automatically cast based on the type definition whoever that may only apply to urho defined classes. So the cast may not be necessary.  Someone else may know better.

-------------------------

ghidra | 2017-01-02 00:59:54 UTC | #7

Ok, so I think i fixed my issue.
Well, I worked around it.
I think that I am just not using scriptObject right, vs just a basic class. I am/was just confused on when to use them and what for specifically.

My Character class, that I am trying to call from my initial example, is as such:

[code]
class Character:ScriptObject{

  RigidBody@ _body;

  void set_parameters(){

    StaticModel@ coneObject = node.CreateComponent("StaticModel");
    coneObject.model = cache.GetResource("Model", "Models/Cone.mdl");
    coneObject.material = cache.GetResource("Material", "Materials/StoneTiled.xml");
    _body = node.CreateComponent("RigidBody");
    _body.mass = 0.25f;
    _body.friction = 0.75f;
    _body.linearDamping = 0.6f;
    _body.useGravity = false;
    CollisionShape@ shape = node.CreateComponent("CollisionShape");
    shape.SetBox(Vector3(1.0f, 1.0f, 1.0f));
  }

  void push_object(){
    const float OBJECT_VELOCITY = 10.0f;
    _body.linearVelocity = Vector3(0.0f, 0.0f, 1.0f) * OBJECT_VELOCITY;
  }

}
[/code]

It works fine if I am not trying to assign it to a pointer. But then I cant call the push_object method from MoveCamera().

I've got a couple of other working ScriptObject classes that i tried to assign to a pointer like suggested, and they stopped working. So I am assuming that they arent not meant to be used how I was trying to use it. What I did to achieve what I was trying to achive was just make the above a class, like so:

[code]
class Character{

  Node@ _node;
  RigidBody@ _body;

  Character(Scene@ scene){

    _node = scene.CreateChild("Character");

    StaticModel@ coneObject = _node.CreateComponent("StaticModel");
    coneObject.model = cache.GetResource("Model", "Models/Cone.mdl");
    coneObject.material = cache.GetResource("Material", "Materials/StoneTiled.xml");
    _body = _node.CreateComponent("RigidBody");
    _body.mass = 0.25f;
    _body.friction = 0.75f;
    _body.linearDamping = 0.6f;
    _body.useGravity = false;
    CollisionShape@ shape = _node.CreateComponent("CollisionShape");
    shape.SetBox(Vector3(1.0f, 1.0f, 1.0f));
  }

  void push_object(){
    const float OBJECT_VELOCITY = 10.0f;
    _body.linearVelocity = Vector3(0.0f, 0.0f, 1.0f) * OBJECT_VELOCITY;
  }

}
[/code] 

And now it is created and the push_object method is called like this (abridged):

[code]
Character@ _character;

void CreateScene(){
  _scene = Scene();
  _character = Character(_scene);//create the character at the scene level
}
void MoveCamera(float timeStep){
  if (input.mouseButtonPress[MOUSEB_LEFT]){
      _character.push_object();
    }
}
[/code]

And that all works as I would expect.
So i just needed to restructure how I was using classes and thus ScriptObjects.

-------------------------

ghidra | 2017-01-02 00:59:55 UTC | #8

New information has come to light.
I will do my best to explain.
First, I am able to grab a scriptobject if I have the parent node, like so:
[code]CameraLogic@ _camera_logic = cast<CameraLogic>(_cameraNode.GetScriptObject("CameraLogic"));[/code]
That was one part of my problem.
Now in all my hunting I have found some other intersting behaviors of classes.
This would throw an error in the 4th line.
[code]
Character@ _character;

void CreateScene(){
  _character = Character();
}
[/code]
But if in my Character class I have just one argument in the constructor, like this:
[code]
Character@ _character;

void CreateScene(){
  _character = Character(1);
}
[/code]
It works.

Is that by design?

-------------------------

