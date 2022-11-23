miz | 2017-11-03 11:41:05 UTC | #1

When setting alignment of tooltips (for instance to HA_CENTER, VA_CENTER) they show in strange positions... (not relative to parent) 

For some reason in the ToolTip update function there is this:
`SetPosition(screenPosition)`
I suspect this is what is causing this...very strange..

also it is making the root the parent

Is there any reason for this?
I suspect it would work properly if it didn't have this at all

-------------------------

miz | 2017-11-03 11:44:14 UTC | #2

Or it could force top left alignment before setting the position as screen position with root parent then reseting this when not visible?

-------------------------

miz | 2017-11-03 17:33:46 UTC | #3

I propose this solution (works):

add these to ToolTip.h:

`	/// Original horizontal Alignment.`
`	HorizontalAlignment originalHorizontalAlignment_;`
`	/// Original vertical Alignment.`
`	VerticalAlignment originalVerticalAlignment_;`

and Change Update funciton in ToolTip.cpp to:

    void ToolTip::Update(float timeStep)
    {
        // Track the element we are parented to for hovering. When we display, we move ourself to the root element
        // to ensure displaying on top
        UIElement* root = GetRoot();
        if (!root)
            return;
        if (parent_ != root)
            target_ = parent_;

        // If target is removed while we are displaying, we have no choice but to destroy ourself
        if (target_.Expired())
        {
            Remove();
            return;
        }
    	
    	

        if (target_->IsHovering() && target_->IsVisibleEffective())
        {
            float effectiveDelay = delay_ > 0.0f ? delay_ : GetSubsystem<UI>()->GetDefaultToolTipDelay();

            if (!parentHovered_)
            {
                parentHovered_ = true;
                displayAt_.Reset();
            }
            else if (displayAt_.GetMSec(false) >= (unsigned)(effectiveDelay * 1000.0f) && parent_ == target_)
            {
    			originalHorizontalAlignment_ = GetHorizontalAlignment();
    			originalVerticalAlignment_ = GetVerticalAlignment();

                originalPosition_ = GetPosition();
                IntVector2 screenPosition = GetScreenPosition();
                SetParent(root);
    			SetAlignment(HA_LEFT, VA_TOP);
                SetPosition(screenPosition);
                SetVisible(true);
                // BringToFront() is unreliable in this case as it takes into account only input-enabled elements.
                // Rather just force priority to max
                SetPriority(M_MAX_INT);
            }
        }
        else
        {
            if (IsVisible() && parent_ == root)
            {
                SetParent(target_);
                SetPosition(originalPosition_);
    			SetAlignment(originalHorizontalAlignment_, originalVerticalAlignment_);
                SetVisible(false);
            }
            parentHovered_ = false;
            displayAt_.Reset();
        }
    }

-------------------------

