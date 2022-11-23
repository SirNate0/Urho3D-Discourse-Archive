Alex-Doc | 2017-08-17 13:33:20 UTC | #1

I'm making a Component which relies on Component IDs for functioning, serialization and deserialization.
I've just noticed that some IDs are duplicated along the scene, making the whole ID system unreliable for me, as the Scene does not seems to provide recursion in GetComponent().

I know I could manually check the double IDs and eventually use a free ID, but I'd prefer if there's another way to track down a component when serializing/deserializing.

Is there something I'm missing?

-------------------------

Eugene | 2017-08-17 10:59:24 UTC | #2

[quote="Alex-Doc, post:1, topic:3454"]
Is there something I’m missing?
[/quote]

Components must not have duplicate IDs.
Can you share minimal sample with reproducible problem?

-------------------------

Alex-Doc | 2017-08-17 13:31:57 UTC | #3

Sorry, my fault, after further investigation I found out that the problem is the ID will change when I instantiate the xml containing the component, so my way of retrieving the component will not work.

I have to figure out something better.

-------------------------

cadaver | 2017-08-17 13:44:25 UTC | #4

Check what the SceneResolver class does when an xml is instantiated. If your ID's are attributes that have been annotated with AM_NODEID or AM_COMPONENTID, they should get rewritten. Though if your usecase is complex I don't guarantee it will work out of the box.

-------------------------

Alex-Doc | 2017-08-17 15:16:41 UTC | #5

Thanks, I'm now trying with a different approach, based on node names as I could iterate through the children of the node. 

However I'm facing a weird issue, I have probably overlooked something, but it seems the Node cannot find an existing child when loading: 
[code]
void PODAnimationController::SetAnimationControllersAttr( const VariantVector& value )
{
   animationControllers_.Clear();
   for( unsigned i = 0; i < value.Size(); i++ )
   {
      Node* node = node_->GetChild( value[i].GetString() , true );
      if( node )
      {
         AnimationController* controller = node->GetComponent<AnimationController>();
         if( controller )
            animationControllers_.Push( controller );
         else
            URHO3D_LOGERROR( "PODAnimationController::SetAnimationControllersAttr: value is not AnimationController type!" );
      }
      else
      {
         URHO3D_LOGERROR( "PODAnimationController::SetAnimationControllersAttr: Node \"" + value[i].GetString() + "\" not found in children of \"" + node_->GetName() + "\"!" );
         continue;
      }
   }
}
[/code]

[code]
void PODAnimationController::RegisterObject( Context* context )
{
   context->RegisterFactory<PODAnimationController>();

   URHO3D_MIXED_ACCESSOR_ATTRIBUTE( "AnimationControllers", GetAnimationControllersAttr, SetAnimationControllersAttr, VariantVector, Variant::emptyVariantVector, AM_DEFAULT  );
}
[/code]

While it's able to find it through AngelScript:
http://imgur.com/a/49w74

Any help is welcome.

EDIT:

I've just found that [code]node_->GetChildren().Size();[/code] returns 0, considering this, where am I supposed to load my data while making sure that the children are already in there?

EDIT 1:

**Solved:** I just needed to assign the child names in the above function to a [code]Vector<String>[/code] and move the children related part to [code]ApplyAttributes()[/code].

-------------------------

