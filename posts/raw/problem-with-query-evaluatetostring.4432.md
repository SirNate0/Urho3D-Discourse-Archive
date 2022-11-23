sirop | 2018-08-02 16:17:14 UTC | #1

Hallo,

I have a pretty simple XML file for configuration:
```
<sliders>
    <xyzFactor>0.5</xyzFactor>
    <email>someone_at_mail.com</email>
</sliders>
```
Then when trying to do:
```
        XMLFile* file = cache->GetResource<XMLFile>("Config/sliders.xml");
        //String emailStr;
        if (file)
        {
            XMLElement rootElem = file->GetRoot("sliders");
            XPathQuery    query;

            if( query.SetQuery("email", "String")) {
                String emailStr = query.EvaluateToString(rootElem);
                URHO3D_LOGINFO("emailStr: " + emailStr);

            }

            if( query.SetQuery("xyzFactor", "Float")) {
                float xyzfactor = query.EvaluateToFloat(rootElem);
                URHO3D_LOGINFO("xyzfactor: " + String(xyzfactor));
            }

            query.Clear();
           }
```
I see my log yield:
```
[Thu Aug  2 18:05:17 2018] INFO: emailStr: 
[Thu Aug  2 18:05:17 2018] INFO: xyzfactor: 0.5
```
as if _emailStr_ were empty.

So what's wrong with _query.EvaluateToString_ ?
_query.EvaluateToFloat_ works as one can see above.

Thanks.

-------------------------

sirop | 2018-08-03 09:50:13 UTC | #2

This way it works however:

```
emailStr=rootElem.GetChild("email").GetValue();
URHO3D_LOGINFO("emailStr2: " + emailStr);
```

-------------------------

weitjong | 2018-08-04 10:47:06 UTC | #3

I don't think you have used the XPath query class correctly. Its usage is quite similar to SQL. You perform the select action by using a query. See `XMLElement::Select()`. Normally the select would return a result set. But if you know beforehand that the query would result in a single XMLElement then you can use `XMLElement::SelectSingle()`. When the same query is being used repeatedly then you can consider to prepare the query only once and reuse the prepared query instead. See `XMLElement::SelectPrepeared()` variants. After you get the result from the select then you can call EvaluateToSomething, if you don't want to deal with it as XMLElement directly.

-------------------------

sirop | 2018-08-04 11:09:13 UTC | #4

I do believe your explanations, and this "bug" is not a showstopper for me.
However, it is still strange that
```
 if( query.SetQuery("xyzFactor", "Float")) {
                float xyzfactor = query.EvaluateToFloat(rootElem);
                URHO3D_LOGINFO("xyzfactor: " + String(xyzfactor));
 }
```
works, but
```
if( query.SetQuery("email", "String")) {
                String emailStr = query.EvaluateToString(rootElem);
                URHO3D_LOGINFO("emailStr: " + emailStr);
 }
```
does not yield any string.

-------------------------

weitjong | 2018-08-04 11:28:29 UTC | #5

Try reverse your elements order in the XML and see if your observation remains the same. This part of the code was contributed by me but it was long time ago. So, I could be wrong too. See the sample usage in the UIElement class. In fact I believe that the only place it is being used by the engine directly, not counting the script binding.

-------------------------

sirop | 2018-08-04 11:58:55 UTC | #6

No, reversing the order of elements in the XML file does not change anything.

-------------------------

weitjong | 2018-08-04 14:12:30 UTC | #7

In any case that not how I remember it would work.

-------------------------

