Alex.B | 2017-01-02 01:10:51 UTC | #1

I'm using "Run script.." command in the editor to change my scene. It is works fine, but I can't define any functions or classes inside such script - only plane code. Can anybody explain me - is it known limitation or somethilg else?
My script loks like:
[code]
void processNode(Node@ node)
{
	// do something
}

for (uint i = 0; i < scene.numChildren; ++i)
{
	Node@ childNode = scene.children[i];

	processNode(childNode);
}


[/code]
Console show ERROR: 1,6 expected ';'


Thanks.

-------------------------

cadaver | 2017-01-02 01:10:51 UTC | #2

This is a limitation of the AngelScript immediate execution. It already encloses your code in a dummy function, so it should just contain isolated statements, not define more functions.

-------------------------

Alex.B | 2017-01-02 01:10:51 UTC | #3

Clear now.

Thanks.

-------------------------

