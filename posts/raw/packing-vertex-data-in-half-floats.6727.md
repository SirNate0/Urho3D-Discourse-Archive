townforge | 2021-02-23 23:39:16 UTC | #1

In my game (https://discourse.urho3d.io/t/townforge-a-blockchain-multiplayer-economic-game-with-voxel-world/6722), building geometry is made up of voxels, so grid aligned squres. Each vertex is made of 32 bytes (3 floats for position, 2 floats for textures coordinates, 3 floats for normal). My understanding is that the size of the data itself is a major consideration for performance, so I was looking at how much this could do down, and in theory I could have:

position: 3 coordinates, for 4096 range and grid aligned, 13 bits each
uv: 3 bits each
normal: 6 vectors to choose from, so 3 bits

So I was thinking of making the vertex data be 3 half floats, so 6 bytes, more than 5 times better. The contents would be:
data[0]: x on the top bits, u on the bottom 3 bits
data[1]: y on the top bits, v on the bottom 3 bits
data[2]: z on the top bits, normal on the bottom 3 bits

Now that'd require  custom a vertex program to mask and regenerate the data. It would also requite adding support for half float for position, since it seems Urho3D does not support it (this is really not my area of expertise so I might be wrong though).

Is this possible in theory, or is there a showstopper here ?

For reference, using the half conversion code from Urho3D, this gets me the range I need (it'd limit view distance, but to an acceptable maximum):
```
int main()
{
  for (float x = -2048; x <= 2048 + 1; x += 1.0f)
  {
    unsigned short y = FloatToHalf(x * 8);
    float z = HalfToFloat(y) / 8;
    if (x != z) printf("oops at %f: %f\n", x, z);
  }
  return 0;
}
```

-------------------------

JSandusky | 2021-02-24 00:01:24 UTC | #2

The vertex data fetch is still in multiples of 32 bytes AFAIK.

There shouldn't be anything preventing you from adding half support to the vertex-declarations. However, it will make different functions that work with vertex-buffers (like WriteDrawablesToOBJ, mesh triangle raycasts, etc) unusable (will crash) unless modified to support the added half types as they all assume we can safely access float types from the shadow copies of those buffers.

The generated patching that handles mapping a vertex-declaration/input-layout to a vertex-shader will include the costs to convert those halfs into floats (let's just pretend mobiles with half support don't exist to avoid muddiness).

So really the question you're going to have to find the answer to is if saving on VBO size is going to cost you less than the conversion to float.

Situations like "*I'm constantly updating these buffers as I stream*" change that value.

-------------------------

