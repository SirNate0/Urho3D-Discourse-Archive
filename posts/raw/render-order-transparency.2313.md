Lumak | 2017-01-02 01:14:40 UTC | #1

Ok, I'm a novice graphics programmer and don't understand what's going on with what's shown in the pic nor what it's called.

The problem is when looking at a wave in a way which will overlap some waves behind it, I see some triangle become transparent and renders what's behind it making it look like there's a hole there.

How to fix this?  This occurs in DX9 and OpenGL, the transparency setting is 0.94, freznel env map.

Edit: the red circle is a vertex reference to give some perspective from one pic to the other.

[img]http://i.imgur.com/6rnCGZP.jpg[/img]

-------------------------

TheComet | 2017-01-02 01:14:40 UTC | #2

[EDIT] Disregard this post, it turns out I was wrong and I'm having the same issue.

You could try enabling depth write (which is the default setting).
[code]<technique>
    <pass name="litalpha" depthwrite="true" blend="addalpha" />
</technique>[/code]

Disclaimer: This turned out to work for me, but I am by no means an expert myself either.

-------------------------

cadaver | 2017-01-02 01:14:40 UTC | #3

Having depth write on is likely fine if your material is "mostly opaque". It can cause missing blending of the far-away triangles, in case the front triangles get drawn first.

To properly solve the issue, you would need to rewrite the model's index buffer each frame based on the camera position, so that back-to-front order is guaranteed. But that could be a nasty performance drain.

That's sort of what billboardset does, it sorts the billboards back-to-front when the sorting is enabled.

-------------------------

Lumak | 2017-01-02 01:14:40 UTC | #4

[quote="TheComet"][EDIT] Disregard this post, it turns out I was wrong and I'm having the same issue.
[/quote]

Yeah, it's difficult to know what's going.

[b]Some helpful debugging code:[/b]
Remove 	
<cull value="none" /> 
from MatOcean.xml

In Ocean.hpp/.c
[code]
    void SetPause(bool bset)            { pauseProcessing_ = bset; }
    bool GetPause() const               { return pauseProcessing_; }

    // dbg
    bool                pauseProcessing_;


void Ocean::HandleUpdate(StringHash eventType, VariantMap& eventData)
{
    if ( !pauseProcessing_ && !IsProcessPending() )
    {
        UpdateVertexBuffer();

        SetProcessPending(true);
    }
}

[/code]

Edit: I had my SetPause() in .cpp but moved it in .h for this.

In Water.cpp
[code]
void Water::MoveCamera(float timeStep)
{
. . .

    if (input->GetKeyDown(' ') && m_pOcean)
    {
        bool setpause = !m_pOcean->GetPause();
        m_pOcean->SetPause(setpause);
    }
}
[/code]

-------------------------

Lumak | 2017-01-02 01:14:41 UTC | #5

[quote="cadaver"]Having depth write on is likely fine if your material is "mostly opaque". It can cause missing blending of the far-away triangles, in case the front triangles get drawn first.

To properly solve the issue, you would need to rewrite the model's index buffer each frame based on the camera position, so that back-to-front order is guaranteed. But that could be a nasty performance drain.

That's sort of what billboardset does, it sorts the billboards back-to-front when the sorting is enabled.[/quote]

That does sound nasty.

-------------------------

Lumak | 2017-01-02 01:14:41 UTC | #6

@TheComet,
Setting the depthwrite="true" looks much better. At least it gets rid of holes.  I can live with this. Thx.

-------------------------

TheComet | 2017-01-02 01:14:41 UTC | #7

It will look good from certain angles, but as cadavar pointed out, if fragments behind other fragments happen to be rendered first, you'll still get those "holes" you speak of.

I'm just thinking out loud here, but it should be possible to completely solve this issue by using two passes. In the first pass you render all transparent objects to a depth buffer. In the second pass you do the actual alpha shading, and discard any pixels with a depth value not equal to what you sample from the depth buffer.

-------------------------

Lumak | 2017-01-02 01:14:41 UTC | #8

[quote="TheComet"]It will look good from certain angles, but as cadavar pointed out, if fragments behind other fragments happen to be rendered first, you'll still get those "holes" you speak of.
[/quote]

I made more tweaks in the shader progs just minutes ago.  Check out the latest repo, and you'll see that it's fixed.

-------------------------

