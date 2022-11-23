1vanK | 2017-01-02 01:05:57 UTC | #1

I have found that the engine supports JSON.  Why not use JSON instead XML for resources (UI, scenes, etc.)? After all JSON is more human-accessible. What are the advantages of XML?

[code]
<element>
    <attribute name="Min Size" value="0 16" />
    <attribute name="Max Size" value="2147483647 16" />
    <attribute name="Layout Mode" value="Horizontal" />
    <element type="Text">
        <attribute name="Text" value="Editor settings" />
    </element>
    <element type="Button" style="CloseButton">
        <attribute name="Name" value="CloseButton" />
    </element>
</element>
[/code]

[code]
{
    "Min Size": "0 16",
    "Max Size": "2147483647 16",
    "Layout Mode": "Horizontal",
    {
        "type": "Text",
        "Text": "Editor settings"
    }
    {
        "type": "Button",
        "style": "CloseButton",
        "Name": "CloseButton"
    }
}
[/code]

or

[code]
{
    "Min Size": {0, 16},
    "Max Size": {2147483647, 16},
    "Layout Mode": "Horizontal",
    Text: {
        "Text": "Editor settings"
    },
    Button: {
        "style": "CloseButton",
        "Name": "CloseButton"
    }
}
[/code]

-------------------------

codingmonkey | 2017-01-02 01:05:57 UTC | #2

the best practice use the binary files :slight_smile:  minimum size, fast loading, no parsing

why are using the XML? i guess that because all around in engine and tools based on it

-------------------------

cadaver | 2017-01-02 01:05:57 UTC | #3

It's mostly a matter of preference and tradition; Urho started using XML.

The JSON API in Urho is a bit cumbersome and should ideally be refactored to just use composition (either array or object) of the supported JSON data types. Compare

[github.com/urho3d/Urho3D/blob/m ... SONValue.h](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Resource/JSONValue.h)
with
[github.com/cadaver/turso3d/blob ... SONValue.h](https://github.com/cadaver/turso3d/blob/master/Turso3D/IO/JSONValue.h)

And codingmonkey is right, for performance binary is the optimal. In my measurements the performance hotspot in both JSON and XML reading has been the parsing of floating-point values from text, not the overhead from the XML/JSON structure or memory allocation.

-------------------------

globus | 2017-01-02 01:05:58 UTC | #4

I do not like XML, too.

Alternatives:

[b]TOML[/b] - Tom's Obvious, Minimal Language
[url]https://github.com/toml-lang/toml[/url]

[b]JSMN[/b] - is a minimalistic JSON parser in C. It can be easily integrated into the resource-limited projects or embedded systems.
[url]http://zserge.com/jsmn.html[/url]

Or [b]INI[/b] reader - writer for use with not Big Data settings
For example - MIT licensed [url]http://ndevilla.free.fr/iniparser/index.html[/url]

================================
And, yes, for final product need own binary format.

-------------------------

weitjong | 2017-01-02 01:05:59 UTC | #5

I beg to differ. I admit I also hate to close each end tag manually, but that is why there are many tools to author XML file out there. There are other standards surrounding XML usage too. XPath for querying and XSLT for transforming, just to name a few. I am not saying the other format does not have tools to perform the equivalent but my key point here is the standardization. I have added some XPath query in Urho3D code base some time ago and I don't have to worry about only myself could understand it and maintain it in the future, for example.

I agree that XML is not suitable as the final format to ship the product with, but IMHO there is no problem with XML as an intermediate format for data exchange. Sure XML is "heavier" than JSON. In the context of Client/Server where data is being pushed via the cloud, JSON format is a sure winner because it is lightweight and can be directly 'eval'-ed by Javascript (long ago I used a similar approach where I have *.pl configuration files that I could "source" into my PERL script to get the data in the configuration files without actually parsing them but too bad none of the PERL gurus/monks give it a fancy name then). Outside of Client/Server context though, JSON is just as good as any other data exchange format currently available in the market. Personally, I would pick one format that I know it will stay around in foreseeable future and that I don't need to re-learn or train other peoples on how to use it or its tools.

-------------------------

sabotage3d | 2017-01-02 01:05:59 UTC | #6

If it is for readability one can be converted to the other. Do we have support for binary XML and binary JSON ?

-------------------------

cadaver | 2017-01-02 01:05:59 UTC | #7

No. There's support for Urho's custom binary format for scene load/save, which is just a binary dump of the attributes.

-------------------------

