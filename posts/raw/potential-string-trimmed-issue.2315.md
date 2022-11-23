Victor | 2017-01-02 01:14:41 UTC | #1

So I've been trying to figure out why my SQLite queries haven't been returning any row counts, and I've tracked it down to what's going on when String::Trimmed is performed. Here's the Urho3D code I'm assuming is causing the issue:
[github.com/urho3d/Urho3D/blob/m ... on.cpp#L67](https://github.com/urho3d/Urho3D/blob/master/Source/Urho3D/Database/SQLite/SQLiteConnection.cpp#L67)

When using Trimmed the error: "Could not execute: only one SQL statement is allowed" will occur. The current workaround is to use the sqlite3 functions directly, however it'd be nice if I could continue using the Urho methods :slight_smile:

[b]Using String::Trimmed[/b]
[img]http://i.imgur.com/m10Aykx.png[/img]

[b]Not using String::Trimmed[/b]
[img]http://i.imgur.com/CMy85Uo.png[/img]

-------------------------

cadaver | 2017-01-02 01:14:41 UTC | #2

Note that Trimmed() returns a String object by value. If you execute CString() on a string that is a temporary, the buffer contents are no longer valid after the statement in question is over.

Try storing the trimmed string in a non-temporary variable.

-------------------------

Victor | 2017-01-02 01:14:41 UTC | #3

[quote="cadaver"]Note that Trimmed() returns a String object by value. If you execute CString() on a string that is a temporary, the buffer contents are no longer valid after the statement in question is over.

Try storing the trimmed string in a non-temporary variable.[/quote]

You're absolutely correct. Since Trimmed is being called in the Urho base code I've gone ahead and created a PR: [github.com/urho3d/Urho3D/pull/1639](https://github.com/urho3d/Urho3D/pull/1639) This only fixes SQLite queries however. I haven't tested ODBC queries... :slight_smile:

-------------------------

cadaver | 2017-01-02 01:14:41 UTC | #4

Thanks! ODBC code should already be safe, since nanodbc's execute() operates on string objects and does not return a string buffer pointer for inspection, like sqlite.

-------------------------

