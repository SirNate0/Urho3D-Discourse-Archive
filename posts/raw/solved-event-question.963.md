franck22000 | 2017-01-02 01:04:28 UTC | #1

Hello, 

I am looking to subscribe to an event who is triggered when a node position or rotation is changed. Which is the best event to use for this purpose ? If such event exist in the engine of course :slight_smile: 

Thank you

-------------------------

cadaver | 2017-01-02 01:04:28 UTC | #2

There is no event for this, as events have somewhat high overhead when it's something that would be triggered every frame, for every change.

In scripting, see the TransformChanged() script object method.
In C++, when writing a Component subclass, override the OnMarkedDirty() function. You also need to do node_->AddListener(this); to start getting the dirty notifications.

-------------------------

franck22000 | 2017-01-02 01:04:28 UTC | #3

Thank you ! I have tried the virtual function OnMarkedDirty() before but i have missed to use node_->AddListener(this); ! :slight_smile:

-------------------------

