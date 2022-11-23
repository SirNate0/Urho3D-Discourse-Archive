artgolf1000 | 2017-01-02 01:14:25 UTC | #1

Hi,

I have written a lip sync logic component for my 3d character, though it is messy, it is useful for me.

First, make some blend shapes for your 3d character, here are the shapes: [url]https://github.com/meshonline/rhubarb-lip-sync[/url], if you like Papagayo's shapes, refer to 'Readme.txt' in the 'src-patch' subdirectory.

Make a 'blink' blend shape to control eyes blink.
 
Then, use the above rhubarb-lip-sync utility to generated a text file for your voice.
For example:
./rhubarb voice.wav > voice.txt

Here is the LipSync Class:

LipSync.h
[code]#pragma once

#include <Urho3D/Urho3DAll.h>

/// Custom logic component for moving the animated model and rotating at area edges.
class LipSync : public LogicComponent
{
    URHO3D_OBJECT(LipSync, LogicComponent);
    
public:
    /// Construct.
    LipSync(Context* context) :
    LogicComponent(context)
    {
        EaseWeights[0] = 0.0f;
        EaseWeights[1] = 0.1925f;
        EaseWeights[2] = 0.605f;
        EaseWeights[3] = 0.8f;
        EaseWeights[4] = 0.605f;
        EaseWeights[5] = 0.1925f;
        EaseWeights[6] = 0.0f;

        blinking = false;
        currentStep = 0;
        accuTime = 0.0f;
        blinkEyes = StringHash("blink");
        
        lipSyncing = false;
        currentStep2 = 0;
        prior_lipIndex = -1;
        current_lipIndex = -1;
        
        priorSyncTime_ = FLT_MAX;
        
        ResourceCache* cache = GetSubsystem<ResourceCache>();
        SharedPtr<File> file = cache->GetFile("Sounds/voice.txt");
        while (!file->IsEof()) {
            String line = file->ReadLine();
            if (line.Length()) {
                Vector<String> items = line.Split('\t');
                if (items.Size() == 2) {
                    MY_MORPH_KEY one_key;
                    one_key.time = atof(items[0].CString());
                    one_key.key = StringHash(items[1]);
                    morphKeys_.Push(one_key);
                }
            }
        }
        
        // Only the scene update event is needed: unsubscribe from the rest for optimization
        SetUpdateEventMask(USE_UPDATE);
    }
    
    /// Handle scene update. Called by LogicComponent base class.
    virtual void Update(float timeStep)
    {
        // Get the model's first (only) animation state and advance its time. Note the convenience accessor to other components
        // in the same scene node
        AnimatedModel* model = GetComponent<AnimatedModel>();
        if (model->GetNumAnimationStates())
        {
            AnimationState* state = model->GetAnimationStates()[0];
            state->AddTime(timeStep);
            
            // blink eyes every two seconds
            accuTime += timeStep;
            if (accuTime >= 2.0f) {
                accuTime = 0.0f;
                blinking = true;
            }
            // deal with blink
            if (blinking) {
                model->SetMorphWeight(blinkEyes, EaseWeights[currentStep]);
                currentStep++;
                if (currentStep == 7) {
                    currentStep = 0;
                    blinking = false;
                }
            }
            
            // search next lip sync point
            if (!lipSyncing) {
                float syncTime = state->GetTime();
                // Animation loop back
                if (syncTime < priorSyncTime_) {
                    // Rewind voice
                    SoundSource* voicecSource = node_->GetChild("Voice")->GetComponent<SoundSource>();
                    voiceSource->SetPositionAttr(0);
                }
                priorSyncTime_ = syncTime;
                // search from back to front
                for (int i=morphKeys_.Size()-1; i>=0; i--) {
                    // find a lip sync point
                    if (morphKeys_[i].time <= syncTime) {
                        // trigger lip sync when new sync point appeared
                        if (i != current_lipIndex) {
                            prior_lipIndex = current_lipIndex;
                            current_lipIndex = i;
                            lipSyncing = true;
                        }
                        break;
                    }
                }
            }
            // deal with lip sync
            if (lipSyncing) {
                // Ease out
                if (prior_lipIndex != -1) {
                    model->SetMorphWeight(morphKeys_[prior_lipIndex].key, EaseWeights[currentStep2 + 3]);
                }
                // Ease in
                if (current_lipIndex != -1) {
                    model->SetMorphWeight(morphKeys_[current_lipIndex].key, EaseWeights[currentStep2]);
                }
                currentStep2++;
                if (currentStep2 == 4) {
                    currentStep2 = 0;
                    lipSyncing = false;
                }
            }
        }
    }
    
private:
    float EaseWeights[7];
    bool blinking;
    int currentStep;
    float accuTime;
    StringHash blinkEyes;

    bool lipSyncing;
    int currentStep2;
    int prior_lipIndex;
    int current_lipIndex;
    float priorSyncTime_;

    struct MY_MORPH_KEY {
        float time;
        StringHash key;
    };

    Vector<MY_MORPH_KEY> morphKeys_;
};
[/code]

Here is the demo: [url]https://youtu.be/zIpupeSpXl4[/url]

-------------------------

1vanK | 2017-01-02 01:14:25 UTC | #2

Nice!

-------------------------

