ghidra | 2017-01-02 01:00:13 UTC | #1

So, I cam trying to call a function on a script object from not inside that script object. Anglescript.

Basically, I have come across 2 scenarios where this is something i have failed on so far. 

Once, When I wanted to kind of make a controller. I was trying to put the functions to move the node inside the script object, but I couldnt find a way to call those function from a controller class I made. I ended up using a second class to move the node, instead of using the script object to move it.

Second, now I am trying to assign a enemy target. Currently have two layers of classes. One that holds data like this, and one that is the script object just to handle the update calls, and collision detection, but then it refers to the class that created it. I pass it that class when created, and just refer to it in the scriptobject, and grab any data I want. So if I want to set a target, I set it on that parent class, then look for it from my script object..

Does that make sense? Is that acceptable? What would be cool, If I could just say something like:

[code]
Pawn@ pawn = cast<Pawn>(some_node.scriptObject);
pawn.set_enemy(someother_node);
[/code]

-------------------------

friesencr | 2017-01-02 01:00:13 UTC | #2

For your first scenario I use a little trick.  the node method is actually a kind of odd.  it is a global method that automatically binds to the caller but is not a member of the script object.  to get around this i make a method on the script object Node();

[code]
class Pawn {
  Node@ Node() { return node; }
}
[/code]

For your second scenario the concept does work.  There are some possible problems.  If the objects are not pare of the same scriptfile this will result in an error.  the pawn variable would be null from a bad cast or a compile error from the constant not being found.  The angelscript compiler is pretty good but its error messages aren't always the most helpful.  If you have multiple scriptfiles Urho will only report errors on the main entry scriptfile.  You would have to check the logfile to get the errors for subsequent scriptfiles.  

Another posibility is that the receiver needs store using the handle.

[code]

pawn.set_enemy(@someother_node);

class Pawn {
Node@ _enemyNode;
set_enemy(Node@ enemyNode_)
{
_enemyNode = @enemyNode_;
}
}
[/code]

Urho does something kind of out of the ordinary where it will always pass Urho defined objects by reference/handle, so my advice might be not helpful.   Its' worth a shot if you are stuck though :slight_smile:

-------------------------

ghidra | 2017-01-02 01:00:14 UTC | #3

You've mentioned that first trick to me before. I went ahead and put it in my base class just incase i find myself scrathcing my head about  a related issue.
My fix was actually exactly what I was trying before, I must have just had a syntax problem. So to set on my controller I give it what script object I want to control i do something like this:
[code]
class InputPlayer{

     Node@ node_;

     void set_control(Node@ control_node){
          Pawn@ pawn = cast<Pawn>(control_node.scriptObject);
          if (pawn !is null)
               node_ = control_node;
     }
     void move( Vector3 direction, float timeStep){
          if(node_ !is null){
               Pawn@ pawn = cast<Pawn>(node_.scriptObject);
               pawn.move( direction, timeStep);
          }
     }

}
[/code]

-------------------------

