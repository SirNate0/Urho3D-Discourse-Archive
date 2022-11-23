rku | 2018-11-13 14:30:25 UTC | #1

I just cant wrap my head around anchors. I know how they work. `min anchor-pivot` is coordinate of top-left corner of `UIElement` and `max anchor+pivot` is coordinate of bottom-right corner. However that is now how we think about UI elements and that is whats extremely confusing. Natural way of thinking is position and size and we already have that when setting absolute coordinates. Is there any advantage to having anchors as opposed to "normalized size" and "normalized position"? They both achieve exactly same thing, except dealing with one is way more intuitive than with the other.

-------------------------

Sinoid | 2018-11-14 02:23:28 UTC | #2

I feel like that stuff needs a bit of a rework.

As soon as I started adding rotation to more UI elements than just sprite, the pivot/anchor stuff just fell apart into not making any sense - it really doesn't help that the pivot has nothing in common with the pivots in other software (at least that I've used).

![Blocks_2018-11-11_14-59-54|165x61](upload://gr3GU2a1JLCQCcSClsFm3DucqbN.png)

-------------------------

rku | 2018-11-14 10:00:19 UTC | #3

My understanding of pivot is that its a center point in normalized widget coordinates. That made sense to me. `0.5, 0.5` pivot should be great for rotations, no?

What kind of rework do you have in mind? Replacing anchors with normalized pos/size or something better?

-------------------------

Sinoid | 2018-11-15 01:26:45 UTC | #4

In Free mode the pivots certainly work exactly as one would expect, however when horizontal/vertical get involved the pivots + anchors start to behave weirdly enough that it's a pain to setup UI elements such that they align nicely under changing circumstances.

Though I think some of the severity there is just the absence of rich-text requiring `Text` gymnastics to get the desired results.

> What kind of rework do you have in mind? Replacing anchors with normalized pos/size or something better?

I still don't know, I've been trying to articulate it myself just so I understand what/why before I do much of anything in the UI.

The only thing I've really managed to pin down about how I feel about the UI, is that it's far too unwilling to resize an element smaller (such as when a Text element changes from "500" to "5"), though again - that's really only severe because there's no rich-text.

-------------------------

rku | 2018-11-21 13:56:33 UTC | #5

Im thinking this:

* Keep pivot as it is - a modification of UIElement's origin, 0;0 = top-left corner, 0.5;0.5 = center, 1;1 - bottom-left corner.
* Replace `minAnchor_` with `anchorPosition_`.
* Replace `maxAnchor_` with `anchorSize_`.
* Replace `minOffset_` and `maxOffset_` with just `IntVector2 anchorOffset_`.

When anchoring enabled do following:

Element size would be `anchorSize_ * parentSize` and clamped to min/max size.

Element position would be `anchorPosition_ * parentSize - pivot * elementSize + anchorOffset`.

"Size" and "Position" attribute becomes auto-managed, layouting would adjust it based on anchoring parameters. Modifying them should be prevented when anchoring is enabled. At the moment it is actually possible to use "Position" attribute as sort of offset when anchoring is enabled, but that probably is not intended and should not be used.

Most notable change is loosing ability to specify anchor offset from the bottom-right corner. I have no idea when it would be needed though. We still can use offsets to tweak positioning, moving UIElement to all directions anyway. It is actually an offset, where in current system it seems to affect size as well.

How does this sound? Did i miss anything important?

-------------------------

Modanung | 2018-11-21 15:49:56 UTC | #6

I'm thinking maybe anchors that use pixel coordinates allow for easier aligning of elements and avoid blurring the elements (on 90 degree rotations and flips)? But I have no experience in their use.

-------------------------

rku | 2018-11-23 08:14:59 UTC | #7

@Modanung point of anchors is to not use pixel coordinates. Position/Size already use pixel coordinates. It is fine, element sizes are still rounded to pixel size so there should be no blur.

-------------------------

rku | 2018-11-27 14:28:50 UTC | #8

I have a preliminary patch implementing my ideas. It does appear to work with `LM_FREE`, but cant say i trust it very much just yet. My understanding is that anchors are not supposed to be honored with other layout modes.

```patch
diff --git a/Source/Urho3D/UI/UIElement.cpp b/Source/Urho3D/UI/UIElement.cpp
index 94e4dbda5..76317e704 100644
--- a/Source/Urho3D/UI/UIElement.cpp
+++ b/Source/Urho3D/UI/UIElement.cpp
@@ -93,8 +93,7 @@ static bool CompareUIElements(const UIElement* lhs, const UIElement* rhs)
 XPathQuery UIElement::styleXPathQuery_("/elements/element[@type=$typeName]", "typeName:String");
 
 UIElement::UIElement(Context* context) :
-    Animatable(context),
-    pivot_(std::numeric_limits<float>::max(), std::numeric_limits<float>::max())
+    Animatable(context)
 {
     SetEnabled(false);
 }
@@ -122,11 +121,11 @@ void UIElement::RegisterObject(Context* context)
         horizontalAlignments, HA_LEFT, AM_FILEREADONLY);
     URHO3D_ENUM_ACCESSOR_ATTRIBUTE("Vert Alignment", GetVerticalAlignment, SetVerticalAlignment, VerticalAlignment, verticalAlignments,
         VA_TOP, AM_FILEREADONLY);
-    URHO3D_ACCESSOR_ATTRIBUTE("Min Anchor", GetMinAnchor, SetMinAnchor, Vector2, Vector2::ZERO, AM_FILE);
-    URHO3D_ACCESSOR_ATTRIBUTE("Max Anchor", GetMaxAnchor, SetMaxAnchor, Vector2, Vector2::ZERO, AM_FILE);
-    URHO3D_ACCESSOR_ATTRIBUTE("Min Offset", GetMinOffset, SetMinOffset, IntVector2, IntVector2::ZERO, AM_FILE);
-    URHO3D_ACCESSOR_ATTRIBUTE("Max Offset", GetMaxOffset, SetMaxOffset, IntVector2, IntVector2::ZERO, AM_FILE);
-    URHO3D_ACCESSOR_ATTRIBUTE("Pivot", GetPivot, SetPivot, Vector2, Vector2(std::numeric_limits<float>::max(), std::numeric_limits<float>::max()), AM_FILE);
+    URHO3D_ACCESSOR_ATTRIBUTE("Anchor Position", GetAnchorPosition, SetAnchorPosition, Vector2, Vector2::ZERO, AM_FILE);
+    URHO3D_ACCESSOR_ATTRIBUTE("Anchor Size", GetAnchorSize, SetAnchorSize, Vector2, Vector2::ZERO, AM_FILE);
+    URHO3D_ACCESSOR_ATTRIBUTE("Anchor Position Offset", GetAnchorPositionOffset, SetAnchorPositionOffset, IntVector2, IntVector2::ZERO, AM_FILE);
+    URHO3D_ACCESSOR_ATTRIBUTE("Anchor Size Offset", GetAnchorSizeOffset, SetAnchorSizeOffset, IntVector2, IntVector2::ZERO, AM_FILE);
+    URHO3D_ACCESSOR_ATTRIBUTE("Pivot", GetPivot, SetPivot, Vector2, Vector2(0, 0), AM_FILE);
     URHO3D_ACCESSOR_ATTRIBUTE("Enable Anchor", GetEnableAnchor, SetEnableAnchor, bool, false, AM_FILE);
     URHO3D_ACCESSOR_ATTRIBUTE("Clip Border", GetClipBorder, SetClipBorder, IntRect, IntRect::ZERO, AM_FILE);
     URHO3D_ACCESSOR_ATTRIBUTE("Priority", GetPriority, SetPriority, int, 0, AM_FILE);
@@ -428,8 +427,8 @@ const IntVector2& UIElement::GetScreenPosition() const
         {
             const IntVector2& parentScreenPos = parent->GetScreenPosition();
 
-            pos.x_ += parentScreenPos.x_ + (int)Lerp(0.0f, (float)parent->size_.x_, anchorMin_.x_);
-            pos.y_ += parentScreenPos.y_ + (int)Lerp(0.0f, (float)parent->size_.y_, anchorMin_.y_);
+            pos.x_ += parentScreenPos.x_ + (int)Lerp(0.0f, (float)parent->size_.x_, anchorPosition_.x_);
+            pos.y_ += parentScreenPos.y_ + (int)Lerp(0.0f, (float)parent->size_.y_, anchorPosition_.y_);
             pos.x_ -= (int)(size_.x_ * pivot_.x_);
             pos.y_ -= (int)(size_.y_ * pivot_.y_);
 
@@ -706,24 +705,19 @@ void UIElement::SetHorizontalAlignment(HorizontalAlignment align)
         align = HA_LEFT;
     }
 
-    Vector2 min = anchorMin_;
-    Vector2 max = anchorMax_;
+    Vector2 pos = anchorPosition_;
     float pivot = pivot_.x_;
-    float anchorSize = max.x_ - min.x_;
 
     if (align == HA_CENTER)
-        min.x_ = pivot = 0.5f;
+        pos.x_ = pivot = 0.5f;
     else if (align == HA_LEFT)
-        min.x_ = pivot = 0.0f;
+        pos.x_ = pivot = 0.0f;
     else if (align == HA_RIGHT)
-        min.x_ = pivot = 1.0f;
+        pos.x_ = pivot = 1.0f;
 
-    max.x_ = enableAnchor_ ? (min.x_ + anchorSize) : min.x_;
-
-    if (min.x_ != anchorMin_.x_ || max.x_ != anchorMax_.x_ || pivot != pivot_.x_)
+    if (pos.x_ != anchorPosition_.x_ || pivot != pivot_.x_)
     {
-        anchorMin_.x_ = min.x_;
-        anchorMax_.x_ = max.x_;
+        anchorPosition_.x_ = pos.x_;
         pivot_.x_ = pivot;
         if (enableAnchor_)
             UpdateAnchoring();
@@ -739,24 +733,19 @@ void UIElement::SetVerticalAlignment(VerticalAlignment align)
         align = VA_TOP;
     }
 
-    Vector2 min = anchorMin_;
-    Vector2 max = anchorMax_;
+    Vector2 pos = anchorPosition_;
     float pivot = pivot_.y_;
-    float anchorSize = max.y_ - min.y_;
 
     if (align == VA_CENTER)
-        min.y_ = pivot = 0.5f;
+        pos.y_ = pivot = 0.5f;
     else if (align == VA_TOP)
-        min.y_ = pivot = 0.0f;
+        pos.y_ = pivot = 0.0f;
     else if (align == VA_BOTTOM)
-        min.y_ = pivot = 1.0f;
-
-    max.y_ = enableAnchor_ ? (min.y_ + anchorSize) : min.y_;
+        pos.y_ = pivot = 1.0f;
 
-    if (min.y_ != anchorMin_.y_ || max.y_ != anchorMax_.y_ || pivot != pivot_.y_)
+    if (pos.y_ != anchorPosition_.y_ || pivot != pivot_.y_)
     {
-        anchorMin_.y_ = min.y_;
-        anchorMax_.y_ = max.y_;
+        anchorPosition_.y_ = pos.y_;
         pivot_.y_ = pivot;
         if (enableAnchor_)
             UpdateAnchoring();
@@ -771,54 +760,54 @@ void UIElement::SetEnableAnchor(bool enable)
         UpdateAnchoring();
 }
 
-void UIElement::SetMinOffset(const IntVector2& offset)
+void UIElement::SetAnchorPositionOffset(const IntVector2& offset)
 {
-    if (offset != minOffset_)
+    if (offset != anchorPosOffset_)
     {
-        minOffset_ = offset;
+        anchorPosOffset_ = offset;
         if (enableAnchor_)
             UpdateAnchoring();
     }
 }
 
-void UIElement::SetMaxOffset(const IntVector2& offset)
+void UIElement::SetAnchorSizeOffset(const IntVector2& offset)
 {
-    if (offset != maxOffset_)
+    if (offset != anchorSizeOffset_)
     {
-        maxOffset_ = offset;
+        anchorSizeOffset_ = offset;
         if (enableAnchor_)
             UpdateAnchoring();
     }
 }
 
-void UIElement::SetMinAnchor(const Vector2& anchor)
+void UIElement::SetAnchorPosition(const Vector2& position)
 {
-    if (anchor != anchorMin_)
+    if (position != anchorPosition_)
     {
-        anchorMin_ = anchor;
+        anchorPosition_ = position;
         if (enableAnchor_)
             UpdateAnchoring();
     }
 }
 
-void UIElement::SetMinAnchor(float x, float y)
+void UIElement::SetAnchorPosition(float x, float y)
 {
-    SetMinAnchor(Vector2(x, y));
+    SetAnchorPosition(Vector2(x, y));
 }
 
-void UIElement::SetMaxAnchor(const Vector2& anchor)
+void UIElement::SetAnchorSize(const Vector2& size)
 {
-    if (anchor != anchorMax_)
+    if (size != anchorSize_)
     {
-        anchorMax_ = anchor;
+        anchorSize_ = size;
         if (enableAnchor_)
             UpdateAnchoring();
     }
 }
 
-void UIElement::SetMaxAnchor(float x, float y)
+void UIElement::SetAnchorSize(float x, float y)
 {
-    SetMaxAnchor(Vector2(x, y));
+    SetAnchorSize(Vector2(x, y));
 }
 
 void UIElement::SetPivot(const Vector2& pivot)
@@ -1519,11 +1508,11 @@ void UIElement::RemoveAllTags()
 
 HorizontalAlignment UIElement::GetHorizontalAlignment() const
 {
-    if (anchorMin_.x_ == 0.0f && anchorMax_.x_ == 0.0f && (!pivotSet_ || pivot_.x_ == 0.0f))
+    if (anchorPosition_.x_ == 0.0f && (!pivotSet_ || pivot_.x_ == 0.0f))
         return HA_LEFT;
-    else if (anchorMin_.x_ == 0.5f && anchorMax_.x_ == 0.5f && (!pivotSet_ || pivot_.x_ == 0.5f))
+    else if (anchorPosition_.x_ == 0.5f && (!pivotSet_ || pivot_.x_ == 0.5f))
         return HA_CENTER;
-    else if (anchorMin_.x_ == 1.0f && anchorMax_.x_ == 1.0f && (!pivotSet_ || pivot_.x_ == 1.0f))
+    else if (anchorPosition_.x_ == 1.0f && (!pivotSet_ || pivot_.x_ == 1.0f))
         return HA_RIGHT;
 
     return HA_CUSTOM;
@@ -1531,11 +1520,11 @@ HorizontalAlignment UIElement::GetHorizontalAlignment() const
 
 VerticalAlignment UIElement::GetVerticalAlignment() const
 {
-    if (anchorMin_.y_ == 0.0f && anchorMax_.y_ == 0.0f && (!pivotSet_ || pivot_.y_ == 0.0f))
+    if (anchorPosition_.y_ == 0.0f && (!pivotSet_ || pivot_.y_ == 0.0f))
         return VA_TOP;
-    else if (anchorMin_.y_ == 0.5f && anchorMax_.y_ == 0.5f && (!pivotSet_ || pivot_.y_ == 0.5f))
+    else if (anchorPosition_.y_ == 0.5f && (!pivotSet_ || pivot_.y_ == 0.5f))
         return VA_CENTER;
-    else if (anchorMin_.y_ == 1.0f && anchorMax_.y_ == 1.0f && (!pivotSet_ || pivot_.y_ == 1.0f))
+    else if (anchorPosition_.y_ == 1.0f && (!pivotSet_ || pivot_.y_ == 1.0f))
         return VA_BOTTOM;
 
     return VA_CUSTOM;
@@ -2059,12 +2048,16 @@ void UIElement::UpdateAnchoring()
 {
     if (parent_ && enableAnchor_)
     {
+        IntVector2 newPosition;
+        newPosition.x_ = (int)(parent_->size_.x_ * Clamp(anchorPosition_.x_, 0.0f, 1.0f) - size_.x_ * (1.0f - pivot_.x_)) + anchorPosOffset_.x_;
+        newPosition.y_ = (int)(parent_->size_.y_ * Clamp(anchorPosition_.y_, 0.0f, 1.0f) - size_.y_ * (1.0f - pivot_.y_)) + anchorPosOffset_.y_;
+
         IntVector2 newSize;
-        newSize.x_ = (int)(parent_->size_.x_ * Clamp(anchorMax_.x_ - anchorMin_.x_, 0.0f, 1.0f)) + maxOffset_.x_ - minOffset_.x_;
-        newSize.y_ = (int)(parent_->size_.y_ * Clamp(anchorMax_.y_ - anchorMin_.y_, 0.0f, 1.0f)) + maxOffset_.y_ - minOffset_.y_;
+        newSize.x_ = (int)(parent_->size_.x_ * Clamp(anchorSize_.x_, 0.0f, 1.0f)) + anchorSizeOffset_.x_;
+        newSize.y_ = (int)(parent_->size_.y_ * Clamp(anchorSize_.y_, 0.0f, 1.0f)) + anchorSizeOffset_.y_;
 
-        if (position_ != minOffset_)
-            SetPosition(minOffset_);
+        if (position_ != newPosition)
+            SetPosition(newPosition);
         if (size_ != newSize)
             SetSize(newSize);
     }
diff --git a/Source/Urho3D/UI/UIElement.h b/Source/Urho3D/UI/UIElement.h
index f004ac330..61b90654a 100644
--- a/Source/Urho3D/UI/UIElement.h
+++ b/Source/Urho3D/UI/UIElement.h
@@ -259,18 +259,18 @@ public:
     void SetVerticalAlignment(VerticalAlignment align);
     /// Enable automatic positioning & sizing of the element relative to its parent using min/max anchor and min/max offset. Default false.
     void SetEnableAnchor(bool enable);
-    /// Set minimum (top left) anchor in relation to the parent element (from 0 to 1.) No effect when anchor is not enabled.
-    void SetMinAnchor(const Vector2& anchor);
-    /// Set minimum anchor.
-    void SetMinAnchor(float x, float y);
-    /// Set maximum (bottom right) anchor in relation to the parent element (from 0 to 1.) No effect when anchor is not enabled.
-    void SetMaxAnchor(const Vector2& anchor);
-    /// Set maximum anchor.
-    void SetMaxAnchor(float x, float y);
-    /// Set offset of element's top left from the minimum anchor in pixels. No effect when anchor is not enabled.
-    void SetMinOffset(const IntVector2& offset);
-    /// Set offset of element's bottom right from the maximum anchor in pixels. No effect when anchor is not enabled.
-    void SetMaxOffset(const IntVector2& offset);
+    /// Set normalized position relative to element's parent.
+    void SetAnchorPosition(const Vector2& position);
+    /// Set normalized position relative to element's parent.
+    void SetAnchorPosition(float x, float y);
+    /// Set normalized size relative to element's parent.
+    void SetAnchorSize(const Vector2& size);
+    /// Set normalized size relative to element's parent.
+    void SetAnchorSize(float x, float y);
+    /// Set position offset in pixels which is added to normalized position. Has no effect when anchoring is disabled.
+    void SetAnchorPositionOffset(const IntVector2& offset);
+    /// Set size offset in pixels which is added to normalized size. Has no effect when anchoring is disabled.
+    void SetAnchorSizeOffset(const IntVector2& offset);
     /// Set pivot relative to element's size (from 0 to 1, where 0.5 is center.) Overrides horizontal & vertical alignment.
     void SetPivot(const Vector2& pivot);
     /// Set pivot relative to element's size (from 0 to 1, where 0.5 is center.) Overrides horizontal & vertical alignment.
@@ -454,17 +454,17 @@ public:
     /// Return whether anchor positioning & sizing is enabled.
     bool GetEnableAnchor() const { return enableAnchor_; }
 
-    /// Return minimum anchor.
-    const Vector2& GetMinAnchor() const { return anchorMin_; }
+    /// Return anchor position.
+    const Vector2& GetAnchorPosition() const { return anchorPosition_; }
 
-    /// Return maximum anchor.
-    const Vector2& GetMaxAnchor() const { return anchorMax_; }
+    /// Return anchor size.
+    const Vector2& GetAnchorSize() const { return anchorSize_; }
 
-    // Return minimum offset.
-    const IntVector2& GetMinOffset() const { return minOffset_; }
+    // Return anchor position offset.
+    const IntVector2& GetAnchorPositionOffset() const { return anchorPosOffset_; }
 
-    // Return maximum offset.
-    const IntVector2& GetMaxOffset() const { return maxOffset_; }
+    // Return anchor size offset.
+    const IntVector2& GetAnchorSizeOffset() const { return anchorSizeOffset_; }
 
     /// Return pivot.
     const Vector2& GetPivot() const { return pivot_; }
@@ -771,20 +771,20 @@ private:
     IntVector2 childOffset_;
     /// Parent's minimum size calculated by layout. Used internally.
     IntVector2 layoutMinSize_;
-    /// Minimum offset.
-    IntVector2 minOffset_;
-    /// Maximum offset.
-    IntVector2 maxOffset_;
-    /// Use min/max anchor & min/max offset for position & size instead of setting explicitly.
+    /// Anchor position offset.
+    IntVector2 anchorPosOffset_;
+    /// Anchor size offset.
+    IntVector2 anchorSizeOffset_;
+    /// Use position/size anchor & position/size offset for position & size instead of setting explicitly.
     bool enableAnchor_{};
     /// Has pivot changed manually.
     bool pivotSet_{};
-    /// Anchor minimum position.
-    Vector2 anchorMin_;
-    /// Anchor maximum position.
-    Vector2 anchorMax_;
+    /// Anchor position.
+    Vector2 anchorPosition_;
+    /// Anchor size.
+    Vector2 anchorSize_;
     /// Pivot Position
-    Vector2 pivot_;
+    Vector2 pivot_{0.0f, 0.0f};
     /// Opacity.
     float opacity_{1.0f};
     /// Derived opacity.
```

P.S. forum wont allow uploading `*.patch` files.

-------------------------

