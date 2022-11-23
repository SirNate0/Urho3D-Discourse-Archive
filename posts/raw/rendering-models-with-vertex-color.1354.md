Lumak | 2017-01-02 01:07:06 UTC | #1

I've create a cube in Blender with vertex colors only and verified that there are only MASK_POSITION | MASK_NORMAL | MASK_COLOR masks and data, and it renders a solid white cube with no color.
The material used is:
[code]
<material>
    <technique name="Techniques/NoTextureVCol.xml" />
</material>
[/code]

What am I missing for the vertex colors to show?

edit: added pic
[img]http://i.imgur.com/k4xXLYs.jpg?1[/img]

-------------------------

friesencr | 2017-01-02 01:07:06 UTC | #2

That is what I would do.  My next test would be on the model load to see if the color values were present in the mdl file.

-------------------------

Lumak | 2017-01-02 01:07:06 UTC | #3

Color data looks valid:
[code]
vertex element mask=0x7
======================
Colors:
0xff5ce412,0xff4b8f26,0xff5ad715,0xff5de811,0xffc8133c,0xff2727e4,0xff12e5e0,0xff36c4bc,0xff5ce412,
0xffe81a17,0xffd92a16,0xff4b8f26,0xff37e578,0xff18c7c2,0xff1ee5bf,0xff56e825,0xff11e8e3,0xff12e5e0,
0xff2727e4,0xff2626e7,0xffbf143d,0xff33337a,0xff2626e7,0xff2727e4,
[/code]

At least, they're not all white value.

-------------------------

cadaver | 2017-01-02 01:07:07 UTC | #4

What render API are you using? Are you sure you're applying the material with that technique? Does e.g. the particles fading in NinjaSnowWar work correctly for you? (this uses vertex colors)

-------------------------

ghidra | 2017-01-02 01:07:07 UTC | #5

try this material for lit.

[code]
<material>
    <technique name="Techniques/NoTextureVCol.xml" />
</material>
[/code]

and this for unlit

[code]
<material>
    <technique name="Techniques/NoTextureUnlitVCol.xml" />
</material>
[/code]

also, how did you get that text read out of the values? is that some tool, to see whats in the mdl?

Edit: I just saw that you were using one of these materials....

Anyway, I was just doing this yesterday. And had some trouble, but in the end it was because I did not have correct vertex color values in the MDL. and I didnt have a way to see what values were on there. So it's hard to say what you are missing.. I have a mdl with vertex colors that maybe you can test with.

Here's a download link
[url]http://s000.tinyupload.com/index.php?file_id=00291925156613236624[/url]

-------------------------

Lumak | 2017-01-02 01:07:07 UTC | #6

Resolved. 
Thanks for providing me with your vertex.mdl.  Trouble shooting your model allowed me to find what was wrong - it was just not having the correct path to my material file.
[url=http://imgur.com/btpgPEQ][img]http://i.imgur.com/btpgPEQ.jpg?1[/img][/url]

Test code to dump color info:
[code]
        // test
        {
			unsigned char *pVertexData = (unsigned char*)m_pVertexBuffer->Lock(0, m_pVertexBuffer->GetVertexCount());

            if ( pVertexData )
            {
                unsigned numVertices = m_pVertexBuffer->GetVertexCount();
                unsigned vertexSize = m_pVertexBuffer->GetVertexSize();
               unsigned uElementMask = m_pVertexBuffer->GetElementMask();

                SDL_Log( "vertex element mask=0x%X\n", uElementMask );
                SDL_Log( "======================\n" );
                SDL_Log( "Colors:\n" );

                // copy position and normal
				for (unsigned i = 0; i <numVertices; ++i)
                {
                    unsigned char *pDataAlign = (pVertexData + i * vertexSize);

                    // position
                    if ( uElementMask & MASK_POSITION )
                    {
                        Vector3 &src = *reinterpret_cast<Vector3*>( pDataAlign );
                        //src = print dbg;
                        pDataAlign += sizeof( Vector3 );
                    }

                    // normal
                    if ( uElementMask & MASK_NORMAL )
                    {
                        Vector3 &normal = *reinterpret_cast<Vector3*>( pDataAlign );
                        //normal = print dbg;
                        pDataAlign += sizeof( Vector3 );
                    }

                    // color
                    if ( uElementMask & MASK_COLOR )
                    {
                        unsigned &uColor = *reinterpret_cast<unsigned*>( pDataAlign );
                        uColor = uColor;
                        SDL_Log( "0x%08x,", uColor );
                        pDataAlign += sizeof( unsigned );
                    }

                }
                SDL_Log( "\n" );

                m_pVertexBuffer->Unlock();
            }

[/code]

-------------------------

Lumak | 2017-06-24 04:11:17 UTC | #7

The intent of using vertex color to render an object was to take the vertex buffer information of an object created by btSoftBodyHelpers and convert that data into Urho3D format.

A softbody object created by Bullet looks like this:

https://youtu.be/K29aHBl25HI

-------------------------

Alex-Doc | 2017-06-23 19:02:49 UTC | #8

Sorry for reviving this old post.
I'm having a similar problem.
The link to the colored model looks broken though.

Do anyone have a vertex colored .mdl file?
I am not sure if the problem is in my model, the exporter or the material. Having something to troubleshoot with, would really help. Thanks in advance!

-------------------------

Lumak | 2017-06-23 20:00:46 UTC | #9

prefab models, i.e. box, sphere,  cylinder, etc., in Data/Models/ folder have vcol since last year.

-------------------------

Alex-Doc | 2017-06-23 20:50:27 UTC | #10

Oh, I overlooked them. Thank you very much!

-------------------------

