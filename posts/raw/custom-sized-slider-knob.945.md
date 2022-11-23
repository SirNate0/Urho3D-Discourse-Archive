TikariSakari | 2017-01-02 01:04:19 UTC | #1

I made some simple modifications to have bigger slider knobs. I am using a slider for a zoomer for camera, and the camera is kind 3rd person type camera. I noticed that by default urho wants to automatically adjust the size of the knob and keeps constantly resizing it.

[code]
void Slider::UpdateSlider()
{
    const IntRect& border = knob_->GetBorder();

    if (range_ > 0.0f)
    {
        int sliderLength = 0;
        if (orientation_ == O_HORIZONTAL)
        {
            if( knobAutoSize_ )
               sliderLength = (int)Max((float)GetWidth() / (range_ + 1.0f), (float)(border.left_ + border.right_));
            else
                 sliderLength = knob_->GetWidth();

            float sliderPos = (float)(GetWidth() - sliderLength) * value_ / range_;
            knob_->SetSize(sliderLength, GetHeight());
            knob_->SetPosition(Clamp((int)(sliderPos + 0.5f), 0, GetWidth() - knob_->GetWidth()), 0);
        }
        else
        {
            if( knobAutoSize_ )
                sliderLength = (int)Max((float)GetHeight() / (range_ + 1.0f), (float)(border.top_ + border.bottom_));
            else
                sliderLength = knob_->GetHeight();
            float sliderPos = (float)(GetHeight() - sliderLength) * value_ / range_;
            knob_->SetSize(GetWidth(), sliderLength);
            knob_->SetPosition(0, Clamp((int)(sliderPos + 0.5f), 0, GetHeight() - knob_->GetHeight()));
        }
    }
    else
    {
        knob_->SetSize(GetSize());
        knob_->SetPosition(0, 0);
    }
}
[/code]

As a side note, I noticed that the Page-function keeps sending a lot of messages. Pretty much on every update the cursor is on top of slider, even if there is no chance to sliders. Is this on purpose?

-------------------------

