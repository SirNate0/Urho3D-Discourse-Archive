SirNate0 | 2017-01-05 01:16:10 UTC | #1

Is there a way to Execute() an angelscript function with a basic type (bool, int, etc.) as a reference, e.g. 
----------
//CPP
Variant boolean = true;
v.Push(cont);
scriptFile_->Execute("void Test(bool &out test)",v);
----------
//Angelscript file
void Reenter(bool &out test)
{
	test = false;
	return;
}

-------------------------

cadaver | 2017-01-05 08:24:54 UTC | #2

Not right now, but looks possible to add, using the SetArgAddress function.

-------------------------

