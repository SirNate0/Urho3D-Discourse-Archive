noals | 2017-01-02 01:10:56 UTC | #1

hi,

well, i have 2 const char* and i try to load a model with it but i don't understand what is needed.

i tryed
[code]
const char* modulePath;
const char* moduleTexturePath;

roomObject->SetModel(cache->GetResource<Model>(modulePath);
roomObject->SetMaterial(cache->GetResource<Material>(moduleTexturePath);
[/code]
or
[code]
String mP(modulePath);
String mTP(moduleTexturePath);

roomObject->SetModel(cache->GetResource<Model>(mP);
roomObject->SetMaterial(cache->GetResource<Material>(mTP);
[/code]

of course, my const char* aren't empty and return the path for the model and for the material file, i verified, but it doesn't compile so i wonder. 

quote from the api :
[quote]Resource * 	GetResource (StringHash type, const String &name, bool sendEventOnFailure=true)
 	Return a resource by type and name. Load if not loaded yet. Return null if not found or if fails, unless SetReturnFailedResources(true) has been called. Can be called only from the main thread. [/quote]

-------------------------

krokodilcapa | 2017-01-02 01:10:56 UTC | #2

You've missed one more bracket from the ends. :slight_smile:

-------------------------

noals | 2017-01-02 01:10:57 UTC | #3

lol, i'm so dumb sometimes. thank you.

-------------------------

krokodilcapa | 2017-01-02 01:10:57 UTC | #4

You're welcomed! I think it happens to every coder sometimes. :smiley: 
[spoiler]Once I forgot to initialize a pointer to null, and I was searching for the crash reason for a whole day... of course the problem started few hours later after I implemented the class :open_mouth:[/spoiler]

-------------------------

Modanung | 2017-01-02 01:11:11 UTC | #5

[quote="noals"]lol, i'm so dumb sometimes. thank you.[/quote]
Seems more like a dumb compiler to me. :wink:
In this case I'd expect an "expected ')' before ';' token" error.

-------------------------

