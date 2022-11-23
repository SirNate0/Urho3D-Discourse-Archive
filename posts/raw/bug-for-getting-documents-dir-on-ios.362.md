att | 2017-01-02 00:59:52 UTC | #1

Hi, I think the function FileSystem::GetUserDocumentsDir() should return the Documents dir on iOS, but it just return the app dir as the FileSystem::GetProgramDir().
So I checked the code and found, the two functions just both call the SDL_IOS_GetResourceDir() function which return the app dir which can not write file to.

Following code should return the correct Documents dir.
[code]        NSArray *paths = NSSearchPathForDirectoriesInDomains(NSDocumentDirectory, NSUserDomainMask, YES);
        NSString *basePath = ([paths count] > 0) ? [paths objectAtIndex:0] : nil;
        
        const char *temp = [basePath UTF8String];
        resource_dir = malloc(strlen(temp) + 1);
        strcpy(resource_dir, temp);[/code]

-------------------------

weitjong | 2017-01-02 00:59:53 UTC | #2

em.. there are no corresponding free() in the new code and the existing SDL_IOS_GetResourceDir(). I think NSString provides other way to return a c-string in a buffer. Otherwise I also think it is good to return a user writable directory.
[stackoverflow.com/questions/1567 ... the-iphone](http://stackoverflow.com/questions/1567134/how-can-i-get-a-writable-path-on-the-iphone)

-------------------------

cadaver | 2017-01-02 00:59:54 UTC | #3

Thanks. This change is now in.

Yes, there is a memory leak at exit due to never freeing the copies that we make of those path strings. Those could be freed when destroying the app delegate, but in any case it's a smallish leak that happens only once.

-------------------------

