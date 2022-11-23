Enhex | 2017-04-26 18:27:22 UTC | #1

Currently the direction billboards only have world direction.
I tried updating their direction via AngelScript to be relative to their node, but it has frame(s) delay.

I suggest adding a new billboard facing mode for relative direction, which is relative to the BillboardSet's node's direction.

Implementation example, modifying BillboardSet::UpdateVertexBuffer()'s FC_DIRECTION code to be relative:

    else // something like FC_RELATIVE_DIRECTION
    {
		const auto node_rotation = node_->GetWorldRotation();

        for (unsigned i = 0; i < enabledBillboards; ++i)
        {
            Billboard& billboard = *sortedBillboards_[i];
			auto direction = node_rotation * billboard.direction_;

            Vector2 size(billboard.size_.x_ * billboardScale.x_, billboard.size_.y_ * billboardScale.y_);
            unsigned color = billboard.color_.ToUInt();
            if (fixedScreenSize_)
                size *= billboard.screenScaleFactor_;

            float rot2D[2][2];
            SinCos(billboard.rotation_, rot2D[0][1], rot2D[0][0]);
            rot2D[1][0] = -rot2D[0][1];
            rot2D[1][1] = rot2D[0][0];

            dest[0] = billboard.position_.x_;
            dest[1] = billboard.position_.y_;
            dest[2] = billboard.position_.z_;
            dest[3] = direction.x_;
            dest[4] = direction.y_;
            dest[5] = direction.z_;
            ((unsigned&)dest[6]) = color;
            dest[7] = billboard.uv_.min_.x_;
            dest[8] = billboard.uv_.min_.y_;
            dest[9] = -size.x_ * rot2D[0][0] + size.y_ * rot2D[0][1];
            dest[10] = -size.x_ * rot2D[1][0] + size.y_ * rot2D[1][1];

            dest[11] = billboard.position_.x_;
            dest[12] = billboard.position_.y_;
            dest[13] = billboard.position_.z_;
            dest[14] = direction.x_;
            dest[15] = direction.y_;
            dest[16] = direction.z_;
            ((unsigned&)dest[17]) = color;
            dest[18] = billboard.uv_.max_.x_;
            dest[19] = billboard.uv_.min_.y_;
            dest[20] = size.x_ * rot2D[0][0] + size.y_ * rot2D[0][1];
            dest[21] = size.x_ * rot2D[1][0] + size.y_ * rot2D[1][1];

            dest[22] = billboard.position_.x_;
            dest[23] = billboard.position_.y_;
            dest[24] = billboard.position_.z_;
            dest[25] = direction.x_;
            dest[26] = direction.y_;
            dest[27] = direction.z_;
            ((unsigned&)dest[28]) = color;
            dest[29] = billboard.uv_.max_.x_;
            dest[30] = billboard.uv_.max_.y_;
            dest[31] = size.x_ * rot2D[0][0] - size.y_ * rot2D[0][1];
            dest[32] = size.x_ * rot2D[1][0] - size.y_ * rot2D[1][1];

            dest[33] = billboard.position_.x_;
            dest[34] = billboard.position_.y_;
            dest[35] = billboard.position_.z_;
            dest[36] = direction.x_;
            dest[37] = direction.y_;
            dest[38] = direction.z_;
            ((unsigned&)dest[39]) = color;
            dest[40] = billboard.uv_.min_.x_;
            dest[41] = billboard.uv_.max_.y_;
            dest[42] = -size.x_ * rot2D[0][0] - size.y_ * rot2D[0][1];
            dest[43] = -size.x_ * rot2D[1][0] - size.y_ * rot2D[1][1];

            dest += 44;
        }

I think it's quite obvious that it has use cases - prefabs, any direction billboard which is attached to a rotated node, ...

-------------------------

