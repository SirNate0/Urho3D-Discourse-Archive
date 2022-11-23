godan | 2017-01-02 01:11:52 UTC | #1

I'm building an app that allows the user to load Script files (in my case, Angelscript) during runtime. This works fine, however, I've noticed that if the user changes the file on disk and reloads it, the system still uses a cached verison. My logic for loading the script file is pretty basic, so I'm probably missing something:

[code]//run the script if one is present
	Script* script_engine = GetContext()->GetSubsystem<Script>();

	ResourceCache* cache = GetContext()->GetSubsystem<ResourceCache>();
	FileSystem* fs = GetContext()->GetSubsystem<FileSystem>();
	ScriptFile* script_file = cache->GetResource<ScriptFile>(path);
	if(script_file)
	{
		bool res = script_file->Execute("void CS_SCRIPT_START()");
		if(!res)
			script_file->Execute("void Start()");
		if(!res)
			URHO3D_LOGINFO("Could not start script file");
	}[/code]

I know that there is a method that checks if the script is compiled or not, but I'm not sure how to force the compile to happen.

-------------------------

jmiller | 2017-01-02 01:11:52 UTC | #2

You might try a version of ResourceCache::ReleaseResource()
[github.com/urho3d/Urho3D/blob/m ... che.h#L105](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Resource/ResourceCache.h#L105)

This seems to work for me:
[code]
void ExecuteScript(const String& fn) {
  ResourceCache* cache(GetSubsystem<ResourceCache>());
  cache->ReleaseResource(ScriptFile::GetTypeStatic(), fn, true);
  ScriptFile* scriptFile(cache->GetResource<ScriptFile>(fn));
  if (scriptFile) {
    scriptFile->Execute("void Start()");
  }
}
[/code]

-------------------------

cadaver | 2017-01-02 01:11:52 UTC | #3

Additional ways to achieve reloading:

- Like the editor, enable hot reload by ResourceCache::SetAutoReloadResources(true). Reload / recompile will then happen automatically as part of the frame update once a change is detected, which may not be convenient for your case.
- Call ResourceCache::ReloadResource() when you already have a pointer to the script.
- Disallow caching of the script by using ResourceCache::GetTempResource() to load it, and store it in a shared ptr yourself. Then simply let go of the old pointer and repeat loading when needed.

-------------------------

godan | 2017-01-02 01:11:52 UTC | #4

Thanks! ReloadResource() worked a treat.

-------------------------

