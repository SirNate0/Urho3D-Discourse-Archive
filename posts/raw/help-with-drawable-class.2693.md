dakilla | 2017-01-11 12:57:44 UTC | #1


I created a class based on Drawable to render particles geometries from an external library.

In my Drawable class I recompute all the geometries at each frame using the library data that compute all. I'd like to know if a drawable class can be use as follow.

It works fine but as I never seen example like that, I would like to know if this can rise some problems later. I do that because the library I use is non thread safe, and as HandleUpdate event is called by the main frame it fix all my threading problems.


in sumarry I do that :



    void ParticleEmitter::OnNodeSet(Node* node)
    {
        ...
        SubscribeToEvent(E_UPDATE, URHO3D_HANDLER(MagicParticleEmitter, HandleUpdate));
    }

    void ParticleEmitter::UpdateBatches(const FrameInfo& frame)
    {    
        distance_ = frame.camera_->GetDistance(GetWorldBoundingBox().Center());
    }

    void MagicParticleEmitter::UpdateGeometry(const FrameInfo& frame)
    {
        // nothing here
    }

    UpdateGeometryType ParticleEmitter::GetUpdateGeometryType()
    {
        return UPDATE_NONE;
    }

    void ParticleEmitter::HandleUpdate(StringHash eventType,VariantMap& eventData)
    {
        using namespace Update;
        float timeStep = eventData[P_TIMESTEP].GetFloat();

        // All is done here :
     
        // call to library to update particles
        // set indices buffer
        // set vertices buffer
        // set geometries and batches
    }

thanks.

-------------------------

cadaver | 2017-01-11 15:26:14 UTC | #2

Looks OK. The main gotcha with Drawable is that UpdateBatches could be called from worker threads, and there is practically no way to prevent that, but your code avoids that by having it be a no-op.

-------------------------

dakilla | 2017-01-11 18:49:42 UTC | #3

good, thanks.
and Happy good year (to complete 20 char min) ;)

-------------------------

