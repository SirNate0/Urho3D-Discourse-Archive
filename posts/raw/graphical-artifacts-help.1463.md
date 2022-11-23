Lumak | 2017-01-02 01:07:53 UTC | #1

Integrating TurboBadger to Urho3D-master shows some weird graphical artifacts, e.g. lines above fonts, lines inside boxes and radial buttons, shown below.  
Same code and data in 1.4 didn't show any of this.

Where should I look to debug this problem? I'm thinking batch process or shader routine.

Both code base can be found here:
[url]https://github.com/Lumak/Urho3D-1.4-TurboBadger[/url]
[url]https://github.com/Lumak/Urho3D[/url]

[img]http://i.imgur.com/ou2Jc88.jpg?1[/img]

-------------------------

Lumak | 2017-01-02 01:07:54 UTC | #2

Using the same code and data in 1.4 didn't show this, a pic from 1.4 below.  It's a screenshot that I took of my implementation and not a pic from Turbo Badger's github.

I haven't started digging into this yet, as I have no idea where to look, but I can start with diff'ing the UIBatch render process.

[img]http://i.imgur.com/gA2z5qi.jpg?1[/img]

-------------------------

Enhex | 2017-01-02 01:07:56 UTC | #3

Looks like texture bleeding to me too.
Notice how it mostly happen above upper case letters and special characters.
Maybe texture filtering changed somewhere? I'd try to test with no filtering.
Maybe adding 1 pixel padding around glyphs if nothing else works.

-------------------------

friesencr | 2017-01-02 01:07:56 UTC | #4

I got those kinds of artifacts from enabling multisampling a while ago.

-------------------------

Lumak | 2017-01-02 01:07:59 UTC | #5

Thanks for your input.

I looked at the graphics settings for 1.4 and 1.5 and they both have multisample set to 1.  I diff'd the UI code and didn't see anything different that would caused this problem. Still no resolution.

-------------------------

Enhex | 2017-01-02 01:08:00 UTC | #6

[quote="Lumak"]Thanks for your input.

I looked at the graphics settings for 1.4 and 1.5 and they both have multisample set to 1.  I diff'd the UI code and didn't see anything different that would caused this problem. Still no resolution.[/quote]
Try to disable filtering (completely) regardless of changes.

-------------------------

Lumak | 2017-01-02 01:08:00 UTC | #7

Setting multisample = 0 had no effect - still see the same artifacts.

I built OpenGL version of 1.5 and there is no graphical artifacts.  It's clean as what's seen in 1.4.

Just don't use DirectX, ha.  

But seriously, I diff'd DirectX9Texture and Graphics files and didn't see changes that would cause this.  There's something else I'm not seeing.

-------------------------

Lumak | 2017-01-02 01:08:00 UTC | #8

Ok, I'll look into that next.

Here's the recap:
[ul]
[li] 1.4 OpenGL - no issue[/li]
[li] 1.4 DirectX9 - no issue[/li]
[li] 1.5 OpenGL - no issue[/li]
[li][b][color=#FF0000]1.5 DirectX9 - artifacts[/color][/li][/ul][/b]

edit: DirectX9

-------------------------

Enhex | 2017-01-02 01:08:00 UTC | #9

[quote="Lumak"]Setting multisample = 0 had no effect - still see the same artifacts.[/quote]

If you mean engine MSAA than that's not what I meant.
I meant texture filtering, disabling it by using FILTER_NEAREST.

Though just sticking with OpenGL is a valid solution.

-------------------------

Lumak | 2017-01-02 01:08:00 UTC | #10

@Sinoid, 
In the RenderBatch() func, all incoming batch are padded to the end of the vertexbuffer:
[code]
        unsigned begin = batch.vertexData_->Size();
        batch.vertexData_->Resize(begin + _pb->vertex_count * UI_VERTEX_SIZE);
        float* dest = &(batch.vertexData_->At(begin));
[/code]

It's similar to how UIBatch class constructs the batch data.  Here is a sniplet from UIBatch::AddQuad() func:
[code]
    unsigned begin = vertexData_->Size();
    vertexData_->Resize(begin + 6 * UI_VERTEX_SIZE);
    float* dest = &(vertexData_->At(begin));
    vertexEnd_ = vertexData_->Size();

    dest[0] = left;
    dest[1] = top;
    dest[2] = 0.0f;
    ((unsigned&)dest[3]) = topLeftColor;
    dest[4] = leftUV;
    dest[5] = topUV;
[/code]

Except my code is in a for loop.  If I wasn't accounting for offset then I imagine I would not get anything to render except for garbage.

edit: added uibatch::addquad() code sniplet.

again, below is a pic from 1.4 DX9

[img]http://i.imgur.com/gA2z5qi.jpg?1[/img]


@Enhex

I thought you could've meant that, so also did that test but forgot to mentioned it.  Using the FILTER_NEAREST filter initially showed like it would work.  The very 1st window in the TB demo looked like there were no artifacts but the remaining windows had it.

-------------------------

Enhex | 2017-01-02 01:08:00 UTC | #11

[quote="Lumak"]I thought you could've meant that, so also did that test but forgot to mentioned it.  Using the FILTER_NEAREST filter initially showed like it would work.  The very 1st window in the TB demo looked like there were no artifacts but the remaining windows had it.[/quote]

I don't know the implementation details, but maybe each window uses it's own texture and you only disabled filtering on a single window?

-------------------------

Lumak | 2017-01-02 01:08:01 UTC | #12

All TBTextures are created by a overriden Texture ctor and where the filter was set.  So, every TB demo window and textures went through the same ctor.

-------------------------

Enhex | 2017-01-02 01:08:01 UTC | #13

[quote="Lumak"]All TBTextures are created by a overriden Texture ctor and where the filter was set.  So, every TB demo window and textures went through the same ctor.[/quote]
Sounds like a "should". Did you confirm that the windows with the artifacts have unfiltered texture?
Maybe something changes it later?
Maybe only the first window uses that constructor?

-------------------------

Lumak | 2017-01-02 01:08:01 UTC | #14

Now I understand what you mean. And I stand corrected in regards to my claim that the pic was from DX9, I looked at my build again and it was OpenGL.

All fixed!  Thanks for your help!

[RESOLVED]

-------------------------

Lumak | 2017-01-02 01:08:03 UTC | #15

[quote]

Re: graphical artifacts help

PostPosted by Sinoid ? 08 Nov 2015, 21:09
I did your work for you.

------------------------------------------------

I said this:

    I'd look at texture coordinates and check 'border' colors and texture border modes. Looking at the lines around the colored text portion it appears that the lines are areas of "off glyph" texture that's bleeding through.

    If you can get a dump of the rasterized font I'd look at that and compare it to the offending characters to see if there's any stand out indicators (ie. maybe the font rasterize only writes alpha where it thinks it needs to instead of everywhere).

    Then I'd look at whoever/where-ever the font is rendered into an image (as in turning a TTF into a bitmap).



And then you said this:

    I haven't started digging into this yet, as I have no idea where to look, but I can start with diff'ing the UIBatch render process.



What is that: "I have no idea where to look" ... I gave you a detailed list of exactly where I'd look. You're implementing a third party library but incapable of looking into that library? You're implementing a third party library without even thoroughly reading the documentation available?

I can tell you exactly how to adjust Recast/Detour/DetourCrowd to account for multiple agent sizes in exchange for speed - because I implemented that stuff and understood the library I was working with before I picked up the work before me.

You've expressed nothing but "terror" at the thought of investigating TurboBadger.

The 0.5,0.5 offset IS IN THE DOCUMENTATION! RTFM! There is no good reason for anyone to believe that your implementation of TurboBadger is worth using. You're clearly afraid of TurboBadger, and you very clearly are lacking in ability.

So tubobadger isn't filling my view horizontally, what's wrong?

Find an answer.[/quote]
LOL, I don't know what to make of this, but AWESOME JOB in doing all the work! You are the best!

And maybe you should get back on your meds! LOL

-------------------------

weitjong | 2017-01-02 01:08:04 UTC | #16

Since the OP issue is already resolved, I lock this thread for now so it does not go off topic.

-------------------------

