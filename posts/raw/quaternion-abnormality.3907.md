George1 | 2018-01-02 16:36:04 UTC | #1

I'm trying to draw debug arrow lines between too nodes.
The function FromLookRotation works ok as below.
   	
        Vector3 v = lstOut[j]->GetPosition() - lst[i]->GetPosition();
	Quaternion q;
	Vector3 begin = Vector3(0, 0, v.Length());
	Vector3 pTop = Vector3( 0, (float)0.2*v.Length()*Tan(30.0), 0.9*v.Length()) ;
	Vector3 pBottom = Vector3(0, (float)-0.2*v.Length()*Tan(30.0), 0.9*v.Length()) ;

	q.FromLookRotation(v);
	q.Normalize();
				
	Vector3 p1 = lst[i]->GetPosition() + q* pTop;
	Vector3 p2 = lst[i]->GetPosition() + q* pBottom;
	
	debug->AddLine(p1, lstOut[j]->GetPosition(), Color(1.000, 0.863, 0.000));
	debug->AddLine(lst[i]->GetPosition(), lstOut[j]->GetPosition(), Color(1.000, 0.863, 0.000));
	debug->AddLine(p2, lstOut[j]->GetPosition(), Color(1.000, 0.863, 0.000));


if I replace the q.FromLookRotation(v) with q.FromRotationTo(begin, v), I get error of weird flipping (roll) of the arrow lines at some angles.

-------------------------

