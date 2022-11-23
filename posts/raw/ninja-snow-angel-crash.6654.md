Modanung | 2021-01-08 14:13:18 UTC | #1

Am I the only one who can't play Ninja Snow War with the latest master?

```
[Fri Jan  8 14:58:38 2021] INFO: Compiled script module Scripts/NinjaSnowWar.as
[Fri Jan  8 14:58:38 2021] ERROR: bin/Data/Scripts/NinjaSnowWar.as:335,5 - Exception 'Null pointer access' in 'void SpawnPlayer(Connection@)'
AngelScript callstack:
	bin/Data/Scripts/NinjaSnowWar.as:void SpawnPlayer(Connection@):335,5
	bin/Data/Scripts/NinjaSnowWar.as:void StartGame(Connection@):302,5
	bin/Data/Scripts/NinjaSnowWar.as:void Start():90,9
```

Most scripts seem to throw several of these warnings:
```
[...] WARNING: Scripts/Utilities/Sample.as:184,13 Signed/Unsigned mismatch
```

-------------------------

1vanK | 2021-01-09 00:29:41 UTC | #2

Works on Win 10. With what options did you compile the engine?

-------------------------

Modanung | 2021-01-09 03:24:33 UTC | #3

Must've been build leftovers, works again.

-------------------------

