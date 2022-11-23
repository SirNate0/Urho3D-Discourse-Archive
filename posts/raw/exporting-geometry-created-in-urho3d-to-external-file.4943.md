Angramme | 2019-02-20 01:55:53 UTC | #1

So basically I created this little tree generation program using some space colonization algorithm, and it works pretty well, BUT!
For now I can only view the results in the engine itself:
![Przechwytywanie|347x500](upload://qBufujVaQm0x1DcZU88h59xtRdL.png) 
I'm creating the model inside Urho3D in this way:

    struct tVertex {
    	Tree::vec3f position, normal;
    };
    std::vector<tVertex> vertexData;
    std::vector<Tree::vec3us> indexData;

    //some magic filling in the data...

    SharedPtr<VertexBuffer> vb(new VertexBuffer(context_));
    vb->SetShadowed(true); // Shadowed buffer needed for raycasts to work, and so that data can be 
    automatically restored on device loss
    PODVector<VertexElement> elements;
    elements.Push(VertexElement(TYPE_VECTOR3, SEM_POSITION));
    elements.Push(VertexElement(TYPE_VECTOR3, SEM_NORMAL));
    vb->SetSize(vertexData.size(), elements);
    vb->SetData(static_cast<void*>(vertexData.data()));


    SharedPtr<IndexBuffer> ib(new IndexBuffer(context_));
    ib->SetShadowed(true);
    ib->SetSize(indexData.size() * 3, false);
    ib->SetData(static_cast<void*>(indexData.data()));

    SharedPtr<Geometry> geom(new Geometry(context_));
    geom->SetVertexBuffer(0, vb);
    geom->SetIndexBuffer(ib);
    geom->SetDrawRange(TRIANGLE_LIST, 0, indexData.size() * 3);

    return geom;

So please if someone knows how a way to export the geometry could you explain it to a Urho3D newbie? I know there is Assimp integration in the engine, thus theoretically exporting is possible out of the box?
Thanks for help in advance!

-------------------------

Sinoid | 2019-02-20 02:33:15 UTC | #2

There is a function in the engine for exporting to OBJ format:

```
URHO3D_API bool WriteDrawablesToOBJ(PODVector<Drawable*> drawables, File* outputFile, bool asZUp, bool asRightHanded, bool writeLightmapUV = false);
```

If you need a different format or more data than OBJ supports you can refer to those as a bit of a guide.

---

Unless it has been stripped out there's a menu to do this through the editor, I did the initial work and the use-cases were focused on merge-batching or dumping geometry to use for modeling *pefect fit* geometry against (load the exported scene so you can model those tree roots to be in the right place, etc).

I don't believe it is bound to Lua though, just C++ and Angelscript.

-------------------------

Angramme | 2019-02-20 02:49:41 UTC | #3

thanks for the reply, will try it out tomorrow!

-------------------------

Angramme | 2019-02-20 11:33:38 UTC | #4

[quote="Sinoid, post:2, topic:4943"]
PODVector&lt;Drawable*&gt; drawables
[/quote]

Yeah soo, how can I convert my geometry to a Drawable? I thought that I can just take my StaticModel I used to render and make a cast to Drawable because it is it's base class...
But nope:
![Przechwytywanie|690x27](upload://ti2lrdxb8OrCpumQ9G6WWGacnBd.png) 

And I don't know why because my variables aren't const...
Could you please show a snippet of code converting from geometry to a Drawable in a way that I can use it with WriteDrawablesToOBJ?

Sorry if this is basic but I'm new to Urho3D and C++

//#EDIT:

I'm taking geometry created before and using it to make a StaticModel like this

    SharedPtr<Urho3D::Model> TreeModel(new Urho3D::Model(context_));
	TreeModel->SetNumGeometries(1);
	TreeModel->SetGeometry(0, 0, geom);
	TreeModel->SetBoundingBox(BoundingBox(
		Vector3( BBsize.x * -0.5f, 0.0f, BBsize.z * -0.5f ),
		Vector3( BBsize.x * 0.5f, BBsize.y, BBsize.z * 0.5f )
	));
	
	// Though not necessary to render, the vertex & index buffers must be listed in the model so that it can be saved properly
	Vector<SharedPtr<VertexBuffer> > vertexBuffers;
	Vector<SharedPtr<IndexBuffer> > indexBuffers;
	vertexBuffers.Push(SharedPtr<VertexBuffer>(geom->GetVertexBuffer(0)));
	indexBuffers.Push(SharedPtr<IndexBuffer>(geom->GetIndexBuffer()));
	// Morph ranges could also be not defined. Here we simply define a zero range (no morphing) for the vertex buffer
	PODVector<unsigned> morphRangeStarts;
	PODVector<unsigned> morphRangeCounts;
	morphRangeStarts.Push(0);
	morphRangeCounts.Push(0);
	TreeModel->SetVertexBuffers(vertexBuffers, morphRangeStarts, morphRangeCounts);
	TreeModel->SetIndexBuffers(indexBuffers);
	
	return TreeModel;

then I try to use it like that:

    PODVector<Drawable*> pod;
    pod.Push(SharedPtr<Drawable>(TreeModel));
    String filename = "output.obj";
    SharedPtr<File>file = SharedPtr<File>(new File(context_, filename, FILE_WRITE));
    WriteDrawablesToOBJ(pod, file, false, false);

and it gives the compile-time errors I've listed above...

-------------------------

elix22 | 2019-02-20 12:18:58 UTC | #5

pod.Push(dynamic_cast<Drawable*>(TreeModel.Get()));

-------------------------

Angramme | 2019-02-20 12:46:44 UTC | #6

Thanks for the reply elix22! It works but I have a different problem now:
![Zrzut%20ekranu%20(6)|690x388](upload://hDBxaNmyHaMuvl3btGoZ9yjDW64.png) 
Why is that? Am I doing something wrong with SharedPtr<File> file?

-------------------------

elix22 | 2019-02-20 13:32:06 UTC | #7

Try 
pod.Push((Drawable*)(TreeModel.Get()));

It is still fails , you will have to step into WriteDrawablesToOBJ()  (F11)
And debug it

-------------------------

lezak | 2019-02-20 15:27:40 UTC | #8

Model class is not derived from Drawable (it's a resource) but StaticModel is, You should put 'treeobj' instead of 'treemodel' in the vector.

-------------------------

elix22 | 2019-02-20 15:50:50 UTC | #9

[quote="lezak, post:8, topic:4943, full:true"]
Model class is not derived from Drawable (it’s a resource) but StaticModel is, You should put ‘treeobj’ instead of ‘treemodel’ in the vector.
[/quote]

Ouch , you are right , my bad , sorry for misleading

-------------------------

elix22 | 2019-02-20 19:38:11 UTC | #10

Feeling bad for misleading 

This one should work :slight_smile:

> #include <Urho3D/Graphics/Model.h>
#include <Urho3D/Graphics/StaticModel.h>
...
...


> 	// if you already created a scene , disregard this line
	scene_ = new Scene(context_);

	Node* treeNode = scene_->CreateChild("treeNode");
	StaticModel* staticTreeModel = treeNode->CreateComponent<StaticModel>();
	staticTreeModel->SetModel(TreeModel);

	PODVector<Drawable*> pod;
	pod.Push(staticTreeModel);
	String filename = "output.obj";
	SharedPtr<File>file = SharedPtr<File>(new File(context_, filename, FILE_WRITE));
	WriteDrawablesToOBJ(pod, file, false, false);
	file->Close();

-------------------------

lezak | 2019-02-20 19:14:11 UTC | #12

Code provided by @elix22 creates file in root folder of You program and even if it fail to create .obj, empty file still should be created in the same folder as executable. 
Are You running it directly from VS? I think that, in this case file will be created in the folder that is set as "working directory" in project's properties, have You checked it?

-------------------------

Angramme | 2019-02-20 22:12:22 UTC | #13

You are right! I forget about that so many times!
Really, a stupid error, sorry for bothering...

-------------------------

Sinoid | 2019-02-22 00:57:22 UTC | #14

I take it you got it all worked out?

-------------------------

Angramme | 2019-02-23 00:28:51 UTC | #15

Yeah no worries. 
It works now I can get .obj no problem
Thanks for help btw

-------------------------

