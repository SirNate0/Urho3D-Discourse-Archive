HaeferlKaffee | 2018-09-03 00:16:28 UTC | #1

I'm trying to create an effect that requires the world position, or at least position relative to node, of a random vertex on a mesh's surface

I'm currently using this:

    		Geometry* geom = ((AnimatedModel*)adjNode->GetComponent<AnimatedModel>())->GetLodGeometry(0, 0);

			const unsigned char* vertexData;
			const unsigned char* indexData;
			unsigned vertexSize;
			unsigned indexSize;
			const PODVector<VertexElement>* elements;

			geom->GetRawData(vertexData, vertexSize, indexData, indexSize, elements);

			// If data is bad:
			if (!vertexData || !elements || VertexBuffer::GetElementOffset(*elements, TYPE_VECTOR3, SEM_POSITION) != 0) {
				return;
			}
			const auto* vertices = (const unsigned char*)vertexData;

			// 16-bit indices ; short
			if (vertexSize == sizeof(unsigned short)) {
				surfacePoint = *(Vector3*)(&vertices[(short)Random(0, (int)vertexSize)]);

				// Rotate
				surfacePoint = adjNode->GetWorldRotation() * surfacePoint;
				// Scale
				surfacePoint *= adjNode->GetWorldScale();
				// Position
				surfacePoint = surfacePoint + adjNode->GetWorldPosition();

			}

Currently, the position of the vertex seems to be totally wrong. When I tried to create small spheres at each random location, they would group together at a point not on the mesh, and when enough spheres were created, they didn't form the mesh they were supposed to be placed upon

Ideally, it should get the skinned position, i.e. use the animated model not the static mesh

-------------------------

SFrost | 2018-09-03 14:07:17 UTC | #2

change:
[code]
surfacePoint = *(Vector3*)(&vertices[(short)Random(0, (int)vertexSize)]); 
// Rotate 
surfacePoint = adjNode->GetWorldRotation() * surfacePoint; 
// Scale 
surfacePoint *= adjNode->GetWorldScale(); 
// Position 
surfacePoint = surfacePoint + adjNode->GetWorldPosition();
[/code]

to
[code]
surfacePoint = *(Vector3*)(&vertices[(short)Random(0, (int)vertexSize)]); 

// local to world
surfacePoint = adjNode->GetWorldTransform() * surfacePoint;
[/code]

-------------------------

Modanung | 2018-09-03 14:13:17 UTC | #3

Nodes even have a function for that: `Node::LocalToWorld(const Vector3&)`

-------------------------

SFrost | 2018-09-03 14:30:59 UTC | #4

That's a really helpful function for someone who's not familiar with linear algebra.

-------------------------

HaeferlKaffee | 2018-09-03 17:01:07 UTC | #5

Using the single world transform doesn't help. I think it's the way vertex positions are found, which I've mirrored from the Geometry GetHit function

-------------------------

Modanung | 2018-09-03 17:06:29 UTC | #6

@SFrost Welcome to the forums, btw! :confetti_ball: :slight_smile:

-------------------------

SFrost | 2018-09-03 23:04:37 UTC | #7

I didn't realize that *(Vector3*) surfacePoint assignment was also incorrect. 
Change it to:
[code]
surfacePoint = *(Vector3*)(&vertices[(short)Random(0, (int)geom->GetVertexCount()) * vertexSize]);

[/code]

Thank you, Modanung.

-------------------------

Dave82 | 2018-09-03 19:30:01 UTC | #8

[code]
surfacePoint = *(Vector3*)(&vertices[(short)Random(0, (int)vertexSize)]);
[/code]

This part doesnt seem right !

EDIT : Oh you just realised it too !

-------------------------

HaeferlKaffee | 2018-09-03 23:05:10 UTC | #9

This is what I was looking for, thanks

I must've misunderstood how the GetHit function worked. Now to figure out how to get the skinned mesh...

-------------------------

