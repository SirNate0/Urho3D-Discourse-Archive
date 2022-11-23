dev4fun | 2019-12-29 00:29:17 UTC | #1

Hello everyone,
I am trying to implement crowd navigation on my project, but the function OnCrowdUpdate isn't be called, this way, I haven't the event E_CROWD_AGENT_REPOSITION handler.

I don't know why Im getting troubles about it, in-game I can see the NavigationMesh and the CrowdAgent, but when I call **SetCrowdTarget**, Im getting a code failure on library function:

![image|690x419](upload://igGClCGU6Fjq1XqmS4Gi02Bq0W1.png) 

Debbugging, I see this ref is zero retrieved from queryPolygons function:
![image|690x447](upload://6Ci707xzpG6TMDzJjzGTqLX7rhj.png) 

Someone knows what is happening?
Thanks.

![image|587x500](upload://zTfMORb5H7VONWbTAZ8V7AwvlH0.jpeg)

-------------------------

