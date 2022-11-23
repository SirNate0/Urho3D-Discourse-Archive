vivienneanthony | 2017-01-02 01:03:06 UTC | #1

Hi

How hard would it be to add a additional Vector type? Intended for space scenes minus physics for now.

Vector6D(float x_, float y_, float z_, long int xmulti_, long int ymulti_, long int zmulti_)

Region=size X axismultipler

Im thinking the axismultipler is defaulted at 0. Also there can be a enable or disable multiplier flag.

As more functions are coded they can account for the vector type and it at least steer the code for procedual systems either ground or space, in infinte space.

Just saying.

-------------------------

cadaver | 2017-01-02 01:03:06 UTC | #2

In the end scene nodes have to store transform data in a fixed format, as anything else would cause major inefficiency across the engine. This sounds very app-specific, so if the application wants to do calculations using this vector type, it should do that on its own, then transform those results to ordinary Vector3's and apply them to Urho scene nodes.

A compile flag to enable double precision in Vectors and matrices might be more feasible, but those would still have to be transformed into float precision for stuffing into GPU shader constants.

-------------------------

