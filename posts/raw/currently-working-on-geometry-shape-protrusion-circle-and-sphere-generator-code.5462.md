codexhound | 2019-08-14 03:43:45 UTC | #1

Needed some of it for my project and I thought it would be good to have some easy functions to create simple geometry.

Heres a sample of protruding a circle and making a cone:
![DebugUniversalis%202019-08-13%2007-59-36-77|690x388](upload://b0VbtVQP4vfXtrILXHucJgxQZbv.jpeg) 

And an example of a sphere:
![DebugUniversalis%202019-08-13%2007-59-15-90|690x388](upload://jEhaCrBrhg8yRmr9XQPBdS4CKzb.jpeg) 

               Some Example Code:
                       void CustomGeometry::ProtrudeShape(const std::vector<Vector3>& mShapeList, const                std::vector<Vector3>& mPointList)
           {
    Vector3 centerPoint = Urho3D::Average<Urho3D::Vector3>(mShapeList);
    Vector3 pointCurrent;
    Vector3 shapeCurrent;
    Vector3 shapePointVec;
    Vector3 shapePointDir;
    Vector3 pointLast;
    std::vector<Vector3> mPointBuffer(mShapeList.size()*mPointList.size()+mShapeList.size());

    std::vector<Vector3> mLastShapePos = mShapeList;
    auto pointIter = mPointList.begin();
    auto shapeIter = mLastShapePos.begin();

    int bufferCount = 0;
    while (shapeIter != mLastShapePos.end()) {
        mPointBuffer.at(bufferCount) = (*shapeIter);
        shapeIter++;
        bufferCount++;
    }

    
    int count = 0;
    while (pointIter != mPointList.end()) {
        shapeIter = mLastShapePos.begin();
        pointCurrent = (*pointIter);
        count = 0;
        while (shapeIter != mLastShapePos.end()) {
            shapeCurrent = (*shapeIter);
            if (shapeIter == mLastShapePos.begin()) { //protrude from first point of the shape and create dir Vector to point
                shapePointVec = pointCurrent - centerPoint;
                centerPoint = pointCurrent;
            }
            // protrude from the rest of the points on the shape to the next point given a dir and length vector
            shapePointDir = shapePointVec;
            shapePointDir.Normalize();
            mLastShapePos[count] = mLastShapePos[count] + shapePointDir * shapePointVec.Length();
            mPointBuffer.at(bufferCount) = mLastShapePos[count];

            bufferCount++;
            shapeIter++;
            count++;
        }
        pointIter++;
    }
    CreateQuadsFromBuffer(mPointBuffer, mShapeList.size(), mPointList.size()+1);

![DebugUniversalis%202019-08-13%2015-32-12-50|690x388](upload://um3aHOYFH8LNc2v3Cl9JSPftDQA.jpeg) ![DebugUniversalis%202019-08-13%2015-29-22-20|690x388](upload://2Nxu5RR4vD28TRGIeMxrFEcUzCt.jpeg)

-------------------------

