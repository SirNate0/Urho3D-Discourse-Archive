dev4fun | 2018-05-01 21:07:20 UTC | #1

Hey, Im trying to make an animation on my text to looks a scaling, bringing up the text to scene (like coordinate z).

First of all I implemented a new interpolation method (elastic ease out, http://easings.net):

	float a = value1.GetFloat();
	float b = value2.GetFloat();

	const float c = b - a;

	if( t == 0.0f ) 
		return a; 

	if( t == 1.0f ) 
		return a + c;

	float p = 0.3f;
	float d = c;
	float s = p / 4;

	return (d * pow( 2, -10 * t ) * sin( (t - s)*(2 * M_PI) / p ) + c + a);

The animation looks right, but I dont know why this dont looks smooth, check:
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/8/8d5590e74595da42751a912a6d3b45a6066616c2.gif'>

I've already tried to use the IM_LINEAR interpolation method, but the same problem happens.
My code to apply valueanimation on the text it's:

	SharedPtr<ValueAnimation> textAnimation( new ValueAnimation( context_ ) );
	textAnimation->SetInterpolationMethod( IM_LINEAR );
	textAnimation->SetKeyFrame( 0.0f, 0.0f );
	textAnimation->SetKeyFrame( 1.0f, 18.0f );
	instructionText_->SetAttributeAnimation( "Font Size", textAnimation );

I don't understand why this happens, is something with Font Size attribute?
Thanks.

-------------------------

dev4fun | 2018-05-01 21:21:34 UTC | #2

Sure, I understood the problem, probably I will need to use Text3D and use this animation on scale. :tired_face:

@The problem its bcoz when I change Font Size, engine always will create a new font. What I need its just change the size on render.
@Anyway to change the size of texture 2d from font on render?

-------------------------

dev4fun | 2018-05-02 05:29:13 UTC | #3

To scale the font render, I used the function **Text::ConstructBatch**

    const float scale = 2.0f;

    for (unsigned i = 0; i < pageGlyphLocation.Size(); ++i)
    {
		const GlyphLocation& glyphLocation = pageGlyphLocation[i];
		const FontGlyph& glyph = *glyphLocation.glyph_;

        pageBatch.AddQuad((dx + glyphLocation.x_ + glyph.offsetX_) * scale, (dy + glyphLocation.y_ + glyph.offsetY_) * scale, glyph.width_ * scale,
            glyph.height_ * scale, glyph.x_, glyph.y_, glyph.texWidth_, glyph.texHeight_);
    }

I hope that its the best way for what I want. I plan make some updates on UI:Text of Urho3D, like formatting tags and now the scaling function.

If someone have a better way to do it, tell me haha.

@ Just fix the text alignment now. It works if I used out of valueanimation, so I need to check later what is happening.
<img src='//cdck-file-uploads-global.s3.dualstack.us-west-2.amazonaws.com/standard17/uploads/urho3d/original/2X/1/1e3b6d80c0f0518a0adca6ef65b5c6e8a7155d62.gif'>

-------------------------

Pencheff | 2018-05-04 13:09:23 UTC | #4

https://discourse.urho3d.io/t/3d-rich-text-view/2969/21

There's some formatting done and ready to use.

-------------------------

dev4fun | 2018-05-04 22:45:05 UTC | #5

Aaah I didnt know that was possible to use on Text2D :tired_face:
But now I already doing my own version for this, will be interesting to learn Urho UI.

Im using bbcode instead of html tags (something like that http://cegui.org.uk/wiki/Formatting_Tags_in_CEGUI):

` +200 Test[color=red]ing eas[/color]ing`

-------------------------

