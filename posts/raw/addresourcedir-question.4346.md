capelenglish | 2018-06-22 19:04:24 UTC | #1

I have several games. Each game has different model (.mdl) files associated with it. In order to keep the projects organized, I want to create a folder under the source folder called Models and put all my .mdl files there. However, the following doesn't work:

    ResourceCache* cache = GetSubsystem<ResourceCache>();
    cache->AddResourceDir("/home/user/projectname/source/Models");
    tableObject->SetModel(cache->GetResource<Model>("Models/post2.mdl"));

I tried using a relative path (./Models) and that didn't work either. What am I doing wrong?

-------------------------

Eugene | 2018-06-25 11:24:10 UTC | #2

[quote="capelenglish, post:1, topic:4346"]
What am I doing wrong?
[/quote]

Path passed into `GetResource` shall be "relative" to path passed to `AddResourceDir`.
`..`-parenting in path is not alowed.

-------------------------

capelenglish | 2018-06-25 11:24:10 UTC | #3

Ok, I figured it out. I was putting the Models folder under the source dir. It worked when I put it under the build dir.

-------------------------

