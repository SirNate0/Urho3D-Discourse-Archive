ChunFengTsin | 2022-07-15 17:46:35 UTC | #1

Hi,  every one, 
I am reading the source code of Urho3D,

When I read this at View.cpp :

```
void View::GetLitBatches(Drawable* drawable, LightBatchQueue& lightQueue, BatchQueue* alphaQueue)
{
    Light* light = lightQueue.light_;
    Zone* zone = GetZone(drawable);
    const Vector<SourceBatch>& batches = drawable->GetBatches();

    bool allowLitBase =
        useLitBase_ && !lightQueue.negative_ && light == drawable->GetFirstLight() && drawable->GetVertexLights().Empty() &&
        !zone->GetAmbientGradient();

```
I don't know what's the means about `allowLitBase`,  what is the purpose of it ?

-------------------------

Eugene | 2022-07-15 17:53:59 UTC | #2

Urho uses (as one of the options) classic forward rendering with separate light passes, so you normally get object rendered N+1 times: ambient only, first light, second light, etc.

"lit base" is the name of optimization where first two passes are merged into one, so the object is rendered only N times: ambient plus first light, second light, etc.

-------------------------

ChunFengTsin | 2022-07-15 18:00:02 UTC | #3

Thanks for such a clear reply！

-------------------------

