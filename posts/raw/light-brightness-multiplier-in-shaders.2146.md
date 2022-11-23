dragonCASTjosh | 2017-01-02 01:13:27 UTC | #1

After looking through the shaders i couldnt find the name of the light bright multiplier option within the shader. it would be useful to have as i wish to use it as a luminous power value in PBR.

-------------------------

1vanK | 2017-01-02 01:13:27 UTC | #2

[code]            // Negative lights will use subtract blending, so write absolute RGB values to the shader parameter
            graphics->SetShaderParameter(PSP_LIGHTCOLOR, Color(light->GetEffectiveColor().Abs(),
                light->GetEffectiveSpecularIntensity()) * fade);
[/code]

[code]    /// Return effective color, multiplied by brightness. Do not multiply the alpha so that can compare against the default black color to detect a light with no effect.
    Color GetEffectiveColor() const { return Color(color_ * brightness_, 1.0f); }
[/code]

-------------------------

dragonCASTjosh | 2017-01-02 01:13:27 UTC | #3

Thanks i looks like im going to have to find another solution :slight_smile:

-------------------------

