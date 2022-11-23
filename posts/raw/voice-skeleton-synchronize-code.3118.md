artgolf1000 | 2017-05-13 03:20:28 UTC | #1

Hi,

If you want to synchronize the voice and the skeleton animation, you may adjust the skeleton animation time manually according to the voice.

I have tested it on my very slow iPhone 5s, it works.
[code]/// Handle scene update. Called by LogicComponent base class.
virtual void Update(float timeStep)
{
    AnimatedModel* model = GetComponent<AnimatedModel>();
    AnimationState* state = model->GetAnimationStates()[0];
    state->AddTime(timeStep);

    SoundSource* musicSource = node_->GetChild("Music")->GetComponent<SoundSource>();
        float audioTime = musicSource->GetTimePosition() * musicSource->GetSound()->GetFrequency() / musicSource->GetFrequency();

        // fix bug of ogg sound
        if (musicSource->GetSound()->IsCompressed()) {
            float audioLength = musicSource->GetSound()->GetLength();
            while (audioTime >= audioLength) {
                audioTime -= audioLength;
            }
        }
            
        // adjust time
        if (fabsf(audioTime - state->GetTime()) > 0.25f) {
            state->SetTime(audioTime);
        }
}[/code]

-------------------------

