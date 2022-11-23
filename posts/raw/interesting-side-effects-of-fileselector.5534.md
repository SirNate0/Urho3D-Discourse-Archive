Leith | 2019-08-31 05:21:41 UTC | #1

If we create a FileSelector, we are responsible for its lifetime, unlike MessageBox (afaik).
If we choose to simply HIDE our FileSelector, input will be disabled on ALL LineEdit elements (other than those owned by our hidden FileSelector)
All other elements will continue to operate perfectly - selection inside disabled LineEdits still works, but there's no cursor, and you can't type into them.
FileSelector apparently causes MODAL effects to occur with respect ONLY to LineEdits.
It's unusual.

-------------------------

