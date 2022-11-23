George | 2017-01-02 01:06:36 UTC | #1

Hi I want to sort the Vector of structs T.

The struct contains 
double time
String Value
Enum event

I want to sort based on time order, is there equivalent to std::sort?

Thanks
George

-------------------------

friesencr | 2017-01-02 01:06:36 UTC | #2

There is a sort header and Sort method in the Urho3D/Containers folder.  You have to write a compare function

#include "Container/Sort.h"
bool CompareThing(const Thing& a, const Thing&b)  
{
return a.time > b.time;
}

Sort(thingList.Begin(), thingList.End(), CompareThing);

-------------------------

George | 2017-01-02 01:06:36 UTC | #3

Awsome, Thanks Mate,

I wish there is a search interface for the documentation.

Regards
George

-------------------------

weitjong | 2017-01-02 01:06:36 UTC | #4

[quote="George"]Awsome, Thanks Mate,

I wish there is a search interface for the documentation.

Regards
George[/quote]
Me too. The problem is, our website is a static website generated using Jekyll. There is no backend app server to process any request query parameter. We could try to add some more JavaScript to perform search action on the client side, probably with the help of Google search API. Alternatively, you can search using Google directly with additional "site:urho3d.github.io" keyword to limit your search result to our website.

-------------------------

jmiller | 2017-01-02 01:06:38 UTC | #5

[google.com/search?q=site%3A ... tion/HEAD/](https://www.google.com/search?q=site%3Aurho3d.github.io/documentation/HEAD/)

Similarly for this forum (prophpbb.com seems to cripple search)
[google.com/search?q=search+ ... ophpbb.com](https://www.google.com/search?q=search+site%3Aurho3d.prophpbb.com)

If you add such to your browser as search engines, it's actually convenient.

-------------------------

