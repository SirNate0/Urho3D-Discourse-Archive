nickwebha | 2021-08-21 06:30:57 UTC | #1

I am working on an Urho3D boilerplate template for a blog post and something is confusing me: What are the units of measurement in Urho3D?

Some questions:
1. How big is `Urho3D::Node::SetScale( Urho3D::Vector3::ONE )`? One meter in all directions? One foot in all directions? How about `Urho3D::Terrain::SetSpacing( Urho3D::Vector3::ONE )`?
2. How far is `Urho3D::Camera::SetFarClip( 1 )`? How far is `Urho3D::Camera::SetFarClip( 100 )`? What about `Urho3D::Zone::SetFogStart( 175.0f )`/`Urho3D::Zone::SetFogEnd( 250.0f )`? `Urho3D::Zone::SetBoundingBox( Urho3D::BoundingBox( Urho3D::Sphere( Urho3D::Vector3::ZERO, 200 ) ) )`?
3. How can I tell when something is relative (like `Urho3D::RigidBody::SetFriction()`) as opposed to absolute (like `Urho3D::Node::SetScale()`)? What is the rhyme and reason here?
4. How do the absolute and relative relate to each other?
5. Is it the same in the scripting languages?

To give an example, imagine I wanted to create a map of the real world out of tiles. What `Urho3D::Node::SetScale()` or `Urho3D::Terrain::SetSpacing()` would I use to make sure one meter in the real world is equal to one meter in the game? I assume the answer to that one is based on the number of pixels/width/height in each tile but how does that match up to the numbers input into the above? What is the math there?

It is pretty late here so I hope I was able to phrase this in a way that made sense.

-------------------------

SirNate0 | 2021-08-22 16:48:25 UTC | #2

Urho's vectors don't have units, it's your application that defines them. For a typical project with physics and roughly human sized entities 1=1m is a reasonable choice. This is what the PhysicsWorld uses as it's default gravity unit - Earth gravity in m/s^2. But you could easily change that and make your whole game in feet if you wanted, or even inches, etc. As long as you keep all the values consistent you can use whatever scaling you want. Though you may run into precision issues if you go too small or too large, though I at least couldn't tell you where that will be. My rule of thumb is trying to keep physics objects between about 0.5 and 50, and for my projects meters works well to give me that.

I'm terms of relative vs absolute, you probably just need to read documentation and know a bit of physics. The friction coefficient is a unitless number, for example, relating the normal force to the frictional force. `Node::Scale` is actually relative as well to whatever the parent scale is, unless it's a top level node, which has Scale=World Scale. The World Scale is relative to whatever your unit choice is, though you also have to know what your model's scale is too say how that corresponds to what you'll see on the screen.

-------------------------

