zerokol | 2017-01-02 01:06:34 UTC | #1

Hello, I'm trying to load a content from a XML file (It is my game score database), update some content then save it in archive again.

All is almost right.

First of all I set these two global variables:

[code]XMLFile@ baseXMLFile;
XMLElement baseXMLElement;[/code]

then initialize it:

[code]baseXMLFile = cache.GetResource("XMLFile", "base.xml");
baseXMLElement = baseXMLFile.root;[/code]

I use the XMLElement methods to modify the content, all right, but only not SetValue(const String&)

when a try to save:

[code]File file;
file.Open("base.xml", FILE_READWRITE);
baseXMLElement.file.Save(file);[/code]

My initial file was (base.xml)

[code]<?xml version="1.0"?>
<base>
	<position hits="10" place="1" time="10">Charles Xavier</position>
	<position hits="5" place="2" time="6">Thor</position>
</base>
[/code]

After save:

[code]<?xml version="1.0"?>
<base>
	<position hits="10" place="1" time="10">Charles Xavier</position>
	<position hits="7" place="2" time="8">	
		Thor
		aj alves
	</position>
        <position hits="5" place="3" time="6">Thor</position>
</base>
[/code]

What is  going wrong, why can not I change the XMLElement value?
Is there a best approach to open/update/save files?

-------------------------

cadaver | 2017-01-02 01:06:34 UTC | #2

This is a legitimate bug in XMLElement. It's always appending a new value instead of rewriting the old, if one already exists. Should be fixed in the near future.

EDIT: fix is in the master branch.

-------------------------

zerokol | 2017-01-02 01:06:34 UTC | #3

Works like a glove! Thanks!

-------------------------

