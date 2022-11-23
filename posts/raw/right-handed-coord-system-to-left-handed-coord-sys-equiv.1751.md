atai | 2017-01-02 01:09:52 UTC | #1

Urho3D uses a left handed coordinate system as a convention.  If I am using it to implement higher level APIs that take right handed coordinate system parameters for matrices, vectors, quaternion, etc., what is the proper way to transform them to the left handed equivalents?  For example, for simple points I will negate the z coordinate values.

More details: both coordinate systems I am referring to here are, x pointing to the right, y pointing to the top, and z point away from the default eye position (left hand) and towards or behinds the eye (right hand).

Thanks for info on this

-------------------------

thebluefish | 2017-01-02 01:09:52 UTC | #2

You will most likely need to write helper functions for each type data that you are attempting to convert. Since you will be converting from Urho3D's data structures to each system (ie Urho3D::Vector3 <> btVector3), it can be done on-the-fly during this process. Just Google each data type that you are converting.

-------------------------

atai | 2017-01-02 01:09:52 UTC | #3

[quote="thebluefish"]You will most likely need to write helper functions for each type data that you are attempting to convert. Since you will be converting from Urho3D's data structures to each system (ie Urho3D::Vector3 <> btVector3), it can be done on-the-fly during this process. Just Google each data type that you are converting.[/quote]
Hi, thanks.  I tried to Google the relevant ways of doing the conversion but am not sure what is the correct way of converting between the two coordinate systems which have the same x and y directions but opposing z directions.  Some Google results point to the way to convert by swapping y and z which seems to be for converting models from Blender or other tools and I don't think applies here.

Can you give more more pointers on this... thanks

-------------------------

thebluefish | 2017-01-02 01:09:52 UTC | #4

I think you should look up what right and left handed coordinate systems are and how they apply to things like your 3rd party libs or Blender. I have a hunch that your 3rd party libs aren't using a standard coordinate system, or you aren't converting coordinates to it properly.

-------------------------

