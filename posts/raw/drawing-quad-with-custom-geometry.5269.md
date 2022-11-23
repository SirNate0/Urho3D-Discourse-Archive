Taqer | 2019-06-30 18:40:32 UTC | #1

Hi I wanted to draw a simple bordered quad (no fill) with custom geometry, but I can't get it to look right, I got some weird line that goes down to negative infinity I guess:
![obraz|323x285](upload://c8E1DYp57ojONcG1AKphwI91WVk.png) 
My code:
		quad = scene->CreateChild();

		CustomGeometry* cg = quad ->CreateComponent<CustomGeometry>();

		cg->Clear();
		cg->SetNumGeometries(1);
		cg->BeginGeometry(0, PrimitiveType::LINE_STRIP);

		cg->DefineGeometry(0, PrimitiveType::LINE_STRIP, 4, false, true, false, false);

		cg->DefineVertex(Vector3(0, 0.1f, 0));
		cg->DefineColor(Color::BLUE);
		cg->DefineVertex(Vector3(1, 0.1f, 0));
		cg->DefineColor(Color::BLUE);
		cg->DefineVertex(Vector3(1, 0.1f, 1));
		cg->DefineColor(Color::BLUE);
		cg->DefineVertex(Vector3(0, 0.1f, 1));
		cg->DefineColor(Color::BLUE);

		Material* mat = new Material(context_);
		auto teq = cache->GetResource<Technique>("Techniques/NoTextureUnlitVCol.xml");
		mat->SetTechnique(0, teq);
		cg->SetMaterial(mat);

		cg->Commit();
I tried changing LINE_STRIP to LINE_LIST, and adding 5. vertex same as first vertex, I got a quad but still there is a line that goes down.

-------------------------

WangKai | 2019-07-01 03:30:54 UTC | #2


I think you should try use either `DefineGeometry` or `BeginGeometry`.

-------------------------

Taqer | 2019-07-01 08:27:40 UTC | #3

Good to know but that still didn't work.
But I made it work with that:

		cg->DefineVertex(Vector3(0, 0.1f, 0));
		cg->DefineColor(Color::BLUE);
		cg->DefineVertex(Vector3(1, 0.1f, 0));
		cg->DefineColor(Color::BLUE);

		cg->DefineVertex(Vector3(1, 0.1f, 0));
		cg->DefineColor(Color::BLUE);
		cg->DefineVertex(Vector3(1, 0.1f, 1));
		cg->DefineColor(Color::BLUE);

		cg->DefineVertex(Vector3(1, 0.1f, 1));
		cg->DefineColor(Color::BLUE);
		cg->DefineVertex(Vector3(0, 0.1f, 1));
		cg->DefineColor(Color::BLUE);

		cg->DefineVertex(Vector3(0, 0.1f, 1));
		cg->DefineColor(Color::BLUE);
		cg->DefineVertex(Vector3(0, 0.1f, 0));
		cg->DefineColor(Color::BLUE);

-------------------------

SirNate0 | 2019-07-01 09:10:37 UTC | #4

I think your original code should work if you removed the `cg->DefineGeometry()` line and added another blue vertex with position 0, .1, 0 (I'm not certain the last vertex is needed, though).

-------------------------

Taqer | 2019-07-01 09:10:31 UTC | #5

Thanks, it works, I think I was trying that before but because of using also DefineGeometry() it gave me that line going to bottom.

-------------------------

