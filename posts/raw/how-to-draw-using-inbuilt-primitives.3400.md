senstatic | 2017-07-31 11:09:28 UTC | #1

Hello everyone, 

I have recently started developing with Urho3d and am amazed at how powerful yet simple it is to use. After a quick test, I have come to a point where I need to draw a path (line/spline/curve), but I cannot find any good resource to do so. 

Upon further investigation, I came across  the folder - **LinePrimitives** under **CoreData.Models** which contains some model files named Basis.mdl and CubicBezier.mdl etc. I'm hoping that these will somehow be used to draw a path. 

Can someone point me in the right direction on how to use these ?

Thanks!

-------------------------

Victor | 2017-07-31 11:22:20 UTC | #2

I've used them in the following manner to create a grid:

        Node* gridNode_ = scene->CreateChild("Grid");
        gridNode_->SetPosition(Vector3::ZERO);

        int gridSize = 32;
        float blockScale = 1.0f; // size of each cell in the grid.

        // Use instancing to draw the lines to display tiles.
        Node* lineTileGroupNode = gridNode_->CreateChild("GridLineTileGroup");
        StaticModelGroup* lineTileGroup = lineTileGroupNode->CreateComponent<StaticModelGroup>();
        lineTileGroup->SetModel(cache->GetResource<Model>("Models/LinePrimitives/UnitX.mdl"));

        // Set your material
        lineTileGroup->SetMaterial(mat);

        // Iterate creating both the vertical and horizontal lines.
        for (int i = 0; i <= gridSize; i++) {
            Node* hNode = gridNode_->CreateChild("GridTileLineH");
            hNode->SetPosition(Vector3(0, 0, i * blockScale));
            hNode->SetScale(Vector3(blockScale * gridSize, 0.0f, 0.0f));
            lineTileGroup->AddInstanceNode(hNode);

            // You could use the UnitY.mdl model, or just rotate the one you already have.
            Node* vNode = gridNode_->CreateChild(fmt::format("GridTileLineV", i).c_str());
            Quaternion rot = Quaternion::IDENTITY;
            rot.FromEulerAngles(0.0f, -90.0f, 0.0f);
            vNode->SetPosition(Vector3(i * blockScale, 0, 0));
            vNode->SetRotation(rot);
            vNode->SetScale(Vector3(blockScale * gridSize, 0.0f, 0.0f));
            lineTileGroup->AddInstanceNode(tNode);
        }

-------------------------

johnnycable | 2017-07-31 12:27:17 UTC | #3

Or you can use DebugDraw utilities for that...

-------------------------

senstatic | 2017-08-01 09:33:19 UTC | #4

Thanks for the code Victor. However,  I could  not get the bezier models (CubicBezier,LinearBezier, QuadraticBezier) to work. The others did work though; but that's not what I am looking for.

@johnnycable : Thanks for the tip. I tried using the debug draw to draw lines , circles and quads, but the renderings are really basic and primitive looking and good for exactly that - debugging. 

What I have in mind is more on the lines of - <iframe src="https://giphy.com/embed/3o6Ztah2Jo4BQReDIs" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/loop-crash-after-effects-3o6Ztah2Jo4BQReDIs">via GIPHY</a></p>

or 

<iframe src="https://giphy.com/embed/3o6ZtdI8hZ2nc5H4UE" width="480" height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a href="https://giphy.com/gifs/after-effects-tao-trapcodetao-3o6ZtdI8hZ2nc5H4UE">via GIPHY</a></p>  

Any help would be greatly appreciated! Thanks!

-------------------------

johnnycable | 2017-08-01 11:15:26 UTC | #5

I've searched for that too. None found. You have to create your own line drawing with noise functions (drawing geometry) and coat them fluo design. You could use st like @Lumak  https://discourse.urho3d.io/t/basic-material-effects-for-rendering/2953/37.

UrhoSharp ported Skia library into for that.

-------------------------

