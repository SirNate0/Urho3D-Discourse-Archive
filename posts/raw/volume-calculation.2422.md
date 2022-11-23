leonardo | 2017-01-02 01:15:19 UTC | #1

Hello all,

I have a 3d model in an .obj file that is already remeshed with octree (enclosed, no holes).
Now i can display it in a 3D scene but now i want to calculate its volume.

How can I get triangles of my model (StaticModel instance) in Urho to make some calculations?

Thank you
Leonardo

-------------------------

leonardo | 2017-01-02 01:15:19 UTC | #2

NB: I have found [url]http://stackoverflow.com/questions/1406029/how-to-calculate-the-volume-of-a-3d-mesh-object-the-surface-of-which-is-made-up[/url], now i need a way to get triangles, i have only found VertexBuffer.

-------------------------

Eugene | 2017-01-02 01:15:19 UTC | #3

[quote="leonardo"]NB: I have found [url]http://stackoverflow.com/questions/1406029/how-to-calculate-the-volume-of-a-3d-mesh-object-the-surface-of-which-is-made-up[/url], now i need a way to get triangles, i have only found VertexBuffer.[/quote]
Look at raycast code in StaticModel. It already performs similar thing: raycasting with triangles.
See Geometry::GetHitDistance for details.

-------------------------

leonardo | 2017-01-02 01:15:20 UTC | #4

Thank you very much

I written this code with Xamarin (UrhoSharp, the C# porting of Urho3D):

[code]
        double SignedVolumeOfTriangle(Vector3 p1, Vector3 p2, Vector3 p3)
        {
            return Vector3.Dot(p1, Vector3.Cross(p2, p3));
        }

        unsafe double GetVolume(Geometry geometry)
        {
            double volume = 0.0f;
            var indexBuffer = geometry.IndexBuffer;
            uint indexSize = indexBuffer.IndexSize;
            byte* indexes = (byte*)indexBuffer.ShadowData;

            Vector3[] triangleVertex = new Vector3[3];
            for (int i = 0; i < indexBuffer.IndexCount; i++)
            {
                byte[] bytesArray = MarshalHelper.ToBytesArray(new IntPtr(indexes), (int)indexSize);
                UInt32 currentIndex = 0;
                switch (indexSize)
                {
                    case 1:
                        currentIndex = bytesArray[0];
                        break;
                    case 2:
                        currentIndex = BitConverter.ToUInt16(bytesArray, 0);
                        break;
                    case 4:
                        currentIndex = BitConverter.ToUInt32(bytesArray, 0);
                        break;
                    default:
                        throw new Exception("IndexSize of IndexBuffer not valid");
                }
                int ix = i % 3;
                triangleVertex[ix] = GetVertex(geometry.VertexBuffers[0], currentIndex);

                if (ix == 2)
                {
                    Debug.WriteLine("Triangle: " + triangleVertex[0].ToString() + " " + triangleVertex[1] + " " + triangleVertex[2]);
                    volume += SignedVolumeOfTriangle(triangleVertex[0], triangleVertex[1], triangleVertex[2]);
                }

                indexes += indexSize;
            }
            double res = Math.Abs(volume) / 6.0f;
            Debug.WriteLine("Volume: " + res);
            return res;
        }

        unsafe Vector3 GetVertex(VertexBuffer vertexBuffer, uint index)
        {
            uint vertexSize = vertexBuffer.VertexSize;
            uint startByte = index * vertexSize;
            byte[] verticesBytes = MarshalHelper.ToBytesArray(new IntPtr(vertexBuffer.ShadowData + startByte), (int)vertexSize);
            float v1 = (float)BitConverter.ToSingle(verticesBytes, 0);
            float v2 = (float)BitConverter.ToSingle(verticesBytes, 8);
            float v3 = (float)BitConverter.ToSingle(verticesBytes, 16);
            return new Vector3(v1, v2, v3);
        }
[/code]

[code]var sm = myNode.GetComponent<StaticModel>(true);
GetVolume(sm.GetLodGeometry(0, 0));[/code]

But I get a volume of 0.666 on a Box with volume of 1.

-------------------------

Eugene | 2017-01-02 01:15:20 UTC | #5

I'm unfamiliar with C# and unsure in the magic that you perform in ur function.
Are you sure that you propperly go through triangles and vertices and pick right data?
There is a chance that your model is broken, but if you tried default box, it is impossible...

-------------------------

ghidra | 2017-01-02 01:15:20 UTC | #6

it looks like it might be missing a 
Square Root of 2 in there somewhere..

0.666*sqrt(2)=0.94

-------------------------

leonardo | 2017-01-02 01:15:21 UTC | #7

This  is my debug output:

[code][0:] Triangle: (-0.5, -0.4999999, 0) (-0.5, 0.5, 0) (-0.5, 0.4999999, 0)
[0:] Triangle: (-0.5, 0.4999999, 0) (-0.5, -0.5, 0) (-0.5, -0.4999999, 0)
[0:] Triangle: (0.5, 0.4999999, 5.960464E-08) (-0.5, 0.4999999, 5.960464E-08) (-0.5, 0.5, 5.960464E-08)
[0:] Triangle: (-0.5, 0.5, 5.960464E-08) (0.5, 0.5, 5.960464E-08) (0.5, 0.4999999, 5.960464E-08)
[0:] Triangle: (0.5, -0.5, 0) (0.5, 0.4999999, 0) (0.5, 0.5, 0)
[0:] Triangle: (0.5, 0.5, 0) (0.5, -0.4999999, 0) (0.5, -0.5, 0)
[0:] Triangle: (0.5, -0.4999999, -5.960464E-08) (-0.5, -0.4999999, -5.960464E-08) (-0.5, -0.5, -5.960464E-08)
[0:] Triangle: (-0.5, -0.5, -5.960464E-08) (0.5, -0.5, -5.960464E-08) (0.5, -0.4999999, -5.960464E-08)
[0:] Triangle: (-0.5, 0.5, -0.9999999) (-0.5, -0.4999999, -0.9999999) (0.5, -0.4999999, -0.9999999)
[0:] Triangle: (0.5, -0.4999999, -0.9999999) (0.5, 0.5, -0.9999999) (-0.5, 0.5, -0.9999999)
[0:] Triangle: (0.5, 0.4999999, 0.9999999) (0.5, -0.5, 0.9999999) (-0.5, -0.5, 0.9999999)
[0:] Triangle: (-0.5, -0.5, 0.9999999) (-0.5, 0.4999999, 0.9999999) (0.5, 0.4999999, 0.9999999)
[0:] Volume: 0.666666567325592[/code]

In a box there are 12 triangles and this seem right, but Volume is wrong :frowning:

-------------------------

Eugene | 2017-01-02 01:15:21 UTC | #8

Try to paint your triangles on the paper cause they looks _very_ strange...
How can CUBE have 3 different Z coordinates? I see 1, -1 and 0. Healthy cube shouldn't have such vertices.
Try to debug your code by urself, don't expect that somebody here will do it for you.

-------------------------

