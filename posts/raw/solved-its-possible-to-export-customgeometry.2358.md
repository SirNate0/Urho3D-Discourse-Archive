rbnpontes | 2017-01-02 01:14:57 UTC | #1

Hello guys again, in my last post i asked how to invert faces in CustomGeometry, i got it to solve the problem, but i need to export my Generated mesh in CustomGeometry to MDL file or something,
i tried several ways to export my mesh but it's doesn't work, now i modified the CustomGeometry Code to export, but every time i'm import, the engine give-me this error: [b][color=#FF0000]Index out of Bounds[/color][/b],
above is a piece of my code
/* Sorry Again for my English */
[code]
// Export Code, used to handle my road 
Model* model = new Model(context_);
			model->SetNumGeometries(1);
			model->SetIndexBuffers(model->GetIndexBuffers());
			model->SetGeometry(0, 0, _customGeom->GetLodGeometry(0,0));
			model->SetNumGeometryLodLevels(0, 1);
			File file(context_, path, FILE_WRITE);
			if (file.IsOpen())
				model->Save(file);
[/code]
[code]
// This is a CustomGeometry Save function created by me, but not working
void CustomGeometry::SaveGeometry(int index, const String& path)
{
	if (index >= geometries_.Size())
		return;
		File file(context_, path, FILE_WRITE);
		Model* model = new Model(context_);
		model->SetNumGeometries(1);
		model->SetGeometry(0, 0, geometries_[index]);
		if (file.IsOpen())
			model->Save(file);
}
[/code]

-------------------------

Eugene | 2017-01-02 01:14:58 UTC | #2

Where do you set vertex buffer of the model?

-------------------------

rbnpontes | 2017-01-02 01:14:58 UTC | #3

I get vertexbuffer from CustomGeometry, i have modified source and createa function called GetVertexBuffer

-------------------------

weitjong | 2017-01-02 01:14:58 UTC | #4

If you are using master branch, you may want to check this commit [github.com/urho3d/Urho3D/commit ... 90b824da42](https://github.com/urho3d/Urho3D/commit/20af1aa85fde8a74bec44667470c9990b824da42).

-------------------------

rbnpontes | 2017-01-02 01:14:58 UTC | #5

Thank's Bro, its really working :smiley:

-------------------------

