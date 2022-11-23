archwind | 2017-10-10 05:52:00 UTC | #1

I stopped development of my project back in February and just picked it back up after I retired from work in September. I decided to take on a new project again to keep me active. I chose to go with the defunct Multiverse since it is MIT and I can republish it once it is a bit more polished up.

If you don't know about Multiverse here is a bit of background:

Multiverse server is a high scalable MMO framework using TCP/RDP and multi threading infrastructures. It is capable of running on anything since the code base is Java. It can run on one machine or a thousand plus machines and communicate via RDP/TCP. It uses MySQL as its database and with enterprise level Mariadb it is fully capable of handling 1000s of concurrent connections.

Multiverse was first released as a commercial engine. At the time it was released in 2004 it was considered the state of the art MMO framework engine. It has similar functionality as BigWorlds and the open source Massiv engine which use the same type of infrastructure but are not as portable since they are written in C++)  It was free to develop under through multiverse.net. In 2010 the developers took the proprietary code and made it MIT license for the few developers that were left. I stopped my project in 2007 but I was still interested in it. The code was released and worked on by several others but the projects seem to have died back in 2013 or so.

Anyway, I Got it completely compiled (java server and C# client) and functional (was lots of script and code changes). I have the server running on a remote VM machine and I am now looking to replace Axiom engine in the client before I put it back up on GitHub.

My goal was to make the current system work FIRST before mentioning it which was a real nightmare without any documentation except the internal code documentation, bits and pieces scattered around the web and mostly broken code in the scripts due to 64 bit system.

Now that this step is completed, I need to start looking at engines. Since Urho3d is MIT it would make sense to go with it BUT it means a complete rewrite of the Multiverse client since the client is originally done in C#. It won't be to difficult but very time consuming.

I'm trying to decide the best course of action. I need to stay with the current setup which means it has to have its own editors and interface. It is a project of epic proportions. It is not for the weak and requires considerable amount of skills to use but this is lack of tools kind of thing. 

So I need some feedback on the next step here. What should I do?

-------------------------

Eugene | 2017-10-10 09:44:20 UTC | #2

If you are tied to C# and want to use Urho, you could try UrhoSharp or AtomicEngine. They both has Urho core. UrhoSharp is more straightforward and Atomic is more distinctive.

-------------------------

archwind | 2017-10-10 14:07:27 UTC | #3

OH, I forgot about Urhosharp. I will check it out.

Thanks

-------------------------

