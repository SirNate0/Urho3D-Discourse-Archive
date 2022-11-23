att | 2017-01-02 00:59:37 UTC | #1

Hi,

I found a memory allocation bug,

[code]// Urho3D: added function
const char* SDL_IOS_GetResourceDir()
{
    if (!resource_dir)
    {
        const char *temp = [[[NSBundle mainBundle] resourcePath] UTF8String];
        resource_dir = malloc(strlen(temp + 1));
        strcpy(resource_dir, temp);
    }
    
    return resource_dir;
}[/code]

[code]resource_dir = malloc(strlen(temp + 1));[/code]
should be
[code]resource_dir = malloc(strlen(temp) + 1);[/code]

 :smiley:

-------------------------

cadaver | 2017-01-02 00:59:37 UTC | #2

Good find, thanks!

-------------------------

