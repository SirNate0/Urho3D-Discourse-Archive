hualin | 2017-01-02 00:59:05 UTC | #1

Hi,
I don't know how to use class FileWatcher, currently, I defined an obj, and call fw_->StartWatching(programDir_ + "/Data/", false), and then I subscribe the FileChanged event in Application, but when I changed the file contents, there is nothing happend. The file is under the Data/ directory.

Would you tell me the right way to use this class?

Thank you!

Edit:
Thank you, cadaver.
I see now.

-------------------------

cadaver | 2017-01-02 00:59:05 UTC | #2

FileWatcher itself doesn't send the event, it's ResourceCache that does, if it has its own change tracking / resource live reloading enabled (which is enabled by ResourceCache::SetAutoReloadResources(true))

If you use FileWatcher directly, you need to poll changes from it by calling its GetNextChange() function until it returns false.

-------------------------

