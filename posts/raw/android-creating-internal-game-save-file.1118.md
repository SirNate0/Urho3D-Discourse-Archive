Lumak | 2017-01-02 01:05:33 UTC | #1

Android how-to create internal game save file.

[b]Part 1 - modifying <urho3d>\Android\src\org\libsdl\app\SDLActivity.java[/b]
Code:
[code]
public class SDLActivity extends Activity {
    
    . . .

    protected void onCreate(Bundle savedInstanceState) {
        Log.v("SDL", "onCreate():" + mSingleton);
        super.onCreate(savedInstanceState);

        SDLActivity.initialize();
        // So we can call stuff from static callbacks
        mSingleton = this;

        // **called after SDLActivity.initialize()
        if ( !hasInternalStoragePrivateFile() )
        {
            createInternalStoragePrivateFile();
        }

        . . .
    }

    protected void createInternalStoragePrivateFile() {
        // Create a path where we will place our private file on external
        // storage.
        File file = new File(((Activity) SDLActivity.getContext()).getFilesDir().getAbsolutePath(), "MyGameSave.dat");


        try {
            // Very simple code to copy a picture from the application's
            // resource into the external file.  Note that this code does
            // no error checking, and assumes the picture is small (does not
            // try to copy it in chunks).  Note that if external storage is
            // not currently mounted this will silently fail.
            OutputStream os = new FileOutputStream(file);
            byte[] data =  "some data".getBytes();
            os.write(data);
            os.close();
            Log.i("FileSystem", "MyGameSave.dat created");

        } catch (IOException e) {
            // Unable to create file, likely because external storage is
            // not currently mounted.
            Log.w("FileSystem", "Error writing " + file, e);
        }

    }
    protected boolean hasInternalStoragePrivateFile() {
        // Get path for the file on external storage.  If external
        // storage is not currently mounted this will fail.
        File file = new File(((Activity) SDLActivity.getContext()).getFilesDir().getAbsolutePath(), "MyGameSave.dat");
        if (file != null) {
            return file.exists();
        }
        return false;
    }
}
[/code]

[b]Part 2 - modifying your App[/b]
Code:
[code]
#include <Urho3D/IO/FileSystem.h> 

void MyApp::Start()
{
    // Execute base class startup
    Sample::Start();

    // file i/o test
    FileSystem *pFileSystem = new FileSystem( context_ );

    if ( pFileSystem )
    {
        String filename = pFileSystem->GetUserDocumentsDir() + "MyGameSave.dat";

        char buff[100];
        SDL_RWops *pFD = SDL_RWFromFile( filename.CString(), "r+" );
        
        // test 1 - read original data
        if ( pFD )
        {
            SDL_Log( "FileSys() SUCCESSFULLY Opened = %s\n", filename.CString() );

            int isizeRead = (int)SDL_RWread( pFD, buff, 1, 100 );
            int iclosed = SDL_RWclose( pFD );

             SDL_Log( "FileSys() data read = %d, closed=%d\n", isizeRead, iclosed  );

             if ( isizeRead > 0 )
             {
                 buff[isizeRead] = '\0';
                 SDL_Log( "FileSys() data = {%s}\n", buff  );
             }
             SDL_FreeRW( pFD );
        }
        else
        {
            SDL_Log( "FileSys() FAILED to open=%s\n", filename.CString() );
        }

        // test 2 - write to file
        pFD = SDL_RWFromFile( filename.CString(), "r+" );

        if ( pFD )
        {
            strcpy( buff, "some data changed and added this" );

            //Sint64 i64Val = SDL_RWseek( pFD, 0, RW_SEEK_SET );
            int iwritelen = SDL_RWwrite( pFD, buff, 1, strlen( buff ) );
            if ( iwritelen <= 0 )
            {
                SDL_Log( "FileSys() RWrite() ERROR = %s\n", SDL_GetError() );
            }
            int iclosed = SDL_RWclose( pFD );

            SDL_Log( "FileSys() wrote data = %d, closed = %d\n", iwritelen, iclosed );

            SDL_FreeRW( pFD );
        }

        // test 3 - re-read what was written
        pFD = SDL_RWFromFile( filename.CString(), "r+" );

        if ( pFD )
        {
            int isizeRead = (int)SDL_RWread( pFD, buff, 1, 100 );
            SDL_Log( "FileSys() re-reading wrote data =%d\n", isizeRead  );

            if ( isizeRead > 0 )
            {
                buff[isizeRead] = '\0';
                SDL_Log( "FileSys() data ={ %s }\n", buff  );
            }

            SDL_RWclose( pFD );
            SDL_FreeRW( pFD );
        }
    }
   . . .
[/code]

Output
[code]
06-13 19:59:24.351    4388-4388/? I/FileSystem? MyGameSave.dat created
06-13 19:59:31.285    4388-4457/? I/SDL/APP? FileSys() SUCCESSFULLY Opened = /data/data/com.github.urho3d/files/MyGameSave.dat
06-13 19:59:31.285    4388-4457/? I/SDL/APP? FileSys() data read = 9, closed=0
06-13 19:59:31.285    4388-4457/? I/SDL/APP? FileSys() data = {some data}
06-13 19:59:31.285    4388-4457/? I/SDL/APP? FileSys() wrote data = 32, closed = 0
06-13 19:59:31.285    4388-4457/? I/SDL/APP? FileSys() re-reading wrote data =32
06-13 19:59:31.285    4388-4457/? I/SDL/APP? FileSys() data ={ some data changed and added this }
[/code]

-------------------------

GoogleBot42 | 2017-01-02 01:05:34 UTC | #2

Neat! Thanks this could be very useful for me.  :slight_smile:

-------------------------

