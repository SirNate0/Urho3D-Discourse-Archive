TheComet | 2019-07-03 04:51:37 UTC | #1

What is the correct way to join paths in Urho3D? I'd like to write a config file to ```GetSubsystem<FileSystem>()->GetAppPreferencesDir()```

-------------------------

jmiller | 2019-07-03 18:17:16 UTC | #2

Hi,

You have a lot of choices for joining paths.. Here it is done in Samples.
https://github.com/urho3d/Urho3D/blob/a476f0c40114b92c2637145c24f50ccef6de5d3c/Source/Samples/Sample.inl#L61

-------------------------

