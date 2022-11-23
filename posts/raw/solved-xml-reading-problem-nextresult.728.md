syjgin | 2017-01-02 01:02:30 UTC | #1

How can I read a XML constructions such as this:
[code]<buildings>
    <building name="building1" count="3"/>
    <building name="building2" count="3"/>
    <building name="building3" count="3"/>
  </buildings>
[/code]

I'm trying to read it in this way:
[code]
XMLElement buildingsElement = rootEl.GetChild("buildings");
    XMLElement currentBuilding = buildingsElement.GetChild("building");
    while(currentBuilding)
    {
        String buildingKey = currentBuilding.GetAttribute("name");
        int buildingCount = currentBuilding.GetInt("count");
        _buildings.insert(std::pair<String,int>(buildingKey, buildingCount));
        currentBuilding = buildingsElement.GetChild("building").NextResult();
    }
[/code]
...but only first "building" line was read. What's may be wrong with NextResult() usage?

-------------------------

Azalrion | 2017-01-02 01:02:31 UTC | #2

nextresult only works for xmlnodes from an xpath query.

-------------------------

syjgin | 2017-01-02 01:02:31 UTC | #3

[quote="Azalrion"]nextresult only works for xmlnodes from an xpath query.[/quote]
Thanks, solved by using XPath:
[code]
XPathQuery query("*/building", "ResultSet");
    XPathResultSet results = query.Evaluate(rootEl);
    for(int i=0; i < results.Size(); i++)
    {
        String buildingKey = results[i].GetAttribute("name");
        int buildingCount = results[i].GetInt("count");
        _buildings.insert(std::pair<String,int>(buildingKey, buildingCount));
    }[/code]

-------------------------

