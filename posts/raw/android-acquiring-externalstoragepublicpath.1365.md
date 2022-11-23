Lumak | 2017-01-02 01:07:13 UTC | #1

A routine to acquire ExternalStoragePublicPath in Android, returns the root of the main "MyFolder" or "Folder" path depending on your device.  This path is guaranteed to exist in every Android device.

Edit: This function does not require you to check the storage state before being called.

ThirdParty\SDL\src\core\android\SDL_android.c, below SDL_AndroidGetExternalStoragePath() function.
[code]
const char * SDL_AndroidGetExternalStoragePublicPath()
{
    static char *s_AndroidExternalStoragePublicPath = NULL;

    if (!s_AndroidExternalStoragePublicPath) {
        struct LocalReferenceHolder refs = LocalReferenceHolder_Setup(__FUNCTION__);
        jmethodID mid;
        jclass cls;
        jobject fileObject;
        jstring pathString;
        const char *path;

        JNIEnv *env = Android_JNI_GetEnv();
        if (!LocalReferenceHolder_Init(&refs, env)) {
            LocalReferenceHolder_Cleanup(&refs);
            return NULL;
        }

        /* fileObject = Environment.getExternalStoragePublicDirectory( "" ); */
        cls = (*env)->FindClass(env, "android/os/Environment");
        mid = (*env)->GetStaticMethodID(env, cls,
                "getExternalStoragePublicDirectory", "(Ljava/lang/String;)Ljava/io/File;");

        jstring jpath = (jstring)((*env)->NewStringUTF(env, ""));
        fileObject = (*env)->CallStaticObjectMethod(env, cls, mid, jpath);
        (*env)->DeleteLocalRef(env, jpath);
        if (!fileObject) {
            SDL_SetError("Couldn't get external StoragePublicDirectory");
            LocalReferenceHolder_Cleanup(&refs);
            return NULL;
        }

        /* path = fileObject.getAbsolutePath(); */
        mid = (*env)->GetMethodID(env, (*env)->GetObjectClass(env, fileObject),
                "getAbsolutePath", "()Ljava/lang/String;");
        pathString = (jstring)(*env)->CallObjectMethod(env, fileObject, mid);

        path = (*env)->GetStringUTFChars(env, pathString, NULL);
        s_AndroidExternalStoragePublicPath = SDL_strdup(path);
        (*env)->ReleaseStringUTFChars(env, pathString, path);

        LocalReferenceHolder_Cleanup(&refs);
    }
    return s_AndroidExternalStoragePublicPath;
}
[/code]

ThirdParty\SDL\src\dynapi\SDL_dynapi_overrides.h, below #define SDL_AndroidGetExternalStoragePath SDL_AndroidGetExternalStoragePath_REAL
[code]
#define SDL_AndroidGetExternalStoragePublicPath SDL_AndroidGetExternalStoragePublicPath_REAL
[/code]

ThirdParty\SDL\src\dynapi\SDL_dynapi_procs.h, below SDL_DYNAPI_PROC(const char*,SDL_AndroidGetExternalStoragePath,(void),(),return)
[code]
SDL_DYNAPI_PROC(const char*,SDL_AndroidGetExternalStoragePublicPath,(void),(),return)

[/code]
ThirdParty\SDL\include\SDL_system.h, after extern DECLSPEC const char * SDLCALL SDL_AndroidGetExternalStoragePath();
[code]
extern DECLSPEC const char * SDLCALL SDL_AndroidGetExternalStoragePublicPath();

[/code]

-------------------------

Lumak | 2017-01-02 01:07:13 UTC | #2

Use case example - creating your public "MyGame" folder.

[code]
    FileSystem *pFileSystem = GetSubsystem<FileSystem>();
    String strPublicRootPath = SDL_AndroidGetExternalStoragePublicPath();
    String strDir = strPublicRootPath + "/MyGame/";
    bool bDirExists = false;

    if ( !pFileSystem->DirExists( strDir ) )
    {
        bDirExists = pFileSystem->CreateDir( strDir );
    }
    else
    {
        bDirExists = true;
    }

[/code]

-------------------------

rasteron | 2017-01-02 01:07:14 UTC | #3

Nice one! :slight_smile:

-------------------------

Lumak | 2017-01-02 01:07:16 UTC | #4

I'd like to note that the public folder usage, for my game, was used to store player generated content.  A game-save file should be stored in a more private folder, such as what you get from calling ProgramDir() function.

-------------------------

