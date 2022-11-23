vmost | 2020-10-12 04:57:06 UTC | #1

I would like to store logs between runs of the app. Pretty simple and standard directory structure:
```
- bin
    - app.exe
- logs
    - 2020
        - September
           - 2020-09-05T12-00-13_LogIdent.log
        - October
    - 2021
```
And Urho3D has a convenient logging system, I just need to set the log name with directory at runtime.
```
void MyApp::Setup()
{
    engineParameters_[EP_LOG_NAME] = log_name;
}
```

My question is, what's the best (or standard) way to implement this behavior? What do you guys do for your projects? In other words, what basic procedure do you use to define `log_name`? The problem is the user could open the executable from any directory, or move the built bundle around, etc., so the path can't be fixed at compile-time.

-------------------------

SirNate0 | 2020-10-12 14:20:35 UTC | #3

I would discourage storing logs like this for the user, at least for games. The logs will end up with a bunch of log files taking up space on their computer, and presumably users won't care about most of them unless there was a crash. If you still want to save multiple, I would just save the last 10 or so (by naming them Log1.txt through Log10.txt, or something like that, and moving the old ones before the new one is created, and probably compressing the old ones as well). But perhaps you have an app where it would be appropriate (I don't know, server logs maybe) and/or are only doing it for debugging.

That said, good luck with it! I hope the earlier reply helps you figure it out.

-------------------------

vmost | 2020-10-13 00:02:17 UTC | #4

Thanks @vram32 this looks like the right direction! Also, many subsystems (including FileSystem) are created in the Engine constructor, and the engine is created in the Application constructor. So, those subsystems are available from the earliest entry point that we have into runtime (aside from command line arguments), namely `Application::Setup()`. [EDIT: actually, I think they are even available within the initializer list of the `MyApp` constructor, since the `Application` subobject is constructed first]

@SirNate0 you're right and that's what I'll probably end up doing. I also want to persist user settings between sessions, so the settings file needs a robust home in the app bundle. Perhaps in a month or two if things go well I will debut my `SettingsManager` extension for everyone to use :)

-------------------------

Pencheff | 2020-10-13 05:26:44 UTC | #5

I use GetUserDocumentsDir() and append my app name to it, keeping the last 5 logs. That way it is more portable, you usually don't have permissions to write in C:\Program Files\, neither in /usr/bin. Also you'll get the logs in the same directory, no matter where the executable is started from. As SirNate0 said, you could keep your last N logs.
You can easily implement this by doing this before you startup your Urho3D app (assume N is 5):
1. Delete the app.log.N-th log if exists
2. Rename all the app.log.N files to app.log.N+1

-------------------------

Modanung | 2020-10-13 10:28:36 UTC | #6

I use `GetAppPreferencesDir(`...`) + "filename.log"`. Which, on my machine results in:
`/home/frode/.local/share/$org/$app/filename.log`

...and I use the same folder for settings files, which should be semantically obvious. :slightly_smiling_face:

-------------------------

vmost | 2020-10-20 07:20:31 UTC | #7

Hey thanks for your help! I have something working, pasting the code here to show others a possible complete solution. Removing the old log files is noticeably slow (around 0.2s maybe), which is unavoidable I guess.

```
std::string MyApp::InitAppFilePack()
{
    std::string return_message{};

    auto *filesystem = GetSubsystem<FileSystem>();
    auto binary_dir = filesystem->GetProgramDir();

    /// log file
    auto log_dir = binary_dir + MyAppConstants::log_files_directory;

    // create log folder if it doesn't exist
    if (!filesystem->DirExists(log_dir))
    {
        if (!filesystem->CreateDir(log_dir))
        {
            return_message += "Could not create log sub-directory [";
            return_message += MyAppConstants::log_files_directory;
            return_message += "]\n";
        }
    }

    // see if the log folder is full, and remove files if there are too many
    // only gets out files ending in specific '.ext'
    Vector<String> log_dir_contents{};
    filesystem->ScanDir(log_dir_contents, log_dir, String{"*."} + MyAppConstants::log_app_extension, SCAN_FILES, false);

    if (log_dir_contents.Size() >= MyAppConstants::num_log_files)
    {
        // sort the vector
        Sort(log_dir_contents.Begin(), log_dir_contents.End());

        int num_removed{0};

        // remove the oldest logs until there is room to add a new log file
        while (num_removed < (log_dir_contents.Size() - MyAppConstants::num_log_files + 1))
        {
            if (!filesystem->Delete(log_dir + log_dir_contents[num_removed]))
            {
                return_message += "Could not remove old log file [";
                return_message += log_dir_contents[num_removed].CString();
                return_message += "]\n";
            }

            ++num_removed;
        }
    }

    // create a new log file (just the name)
    m_filepack.session_log = log_dir.CString();
    m_filepack.session_log += CreateLogFileName(MyAppConstants::log_app_ident, MyAppConstants::log_app_extension);

    /// settings file
    auto settings_dir = binary_dir + MyAppConstants::settings_file_directory;

    // create settings folder if it doesn't exist
    if (!filesystem->DirExists(settings_dir))
    {
        if (!filesystem->CreateDir(settings_dir))
        {
            return_message += "Could not create setting file sub-directory [";
            return_message += MyAppConstants::settings_file_directory;
            return_message += "]\n";
        }
    }

    // set file name with path
    m_filepack.main_settings = settings_dir.CString();
    m_filepack.main_settings += MyAppConstants::settings_file;

    return return_message;
}

std::string MyApp::CreateLogFileName(const std::string ident, const std::string ext)
{
    // log file name ID in case multiple file names are generated in the same second
    // commented out for now since it isn't useful at this point
    //unsigned short log_id = static_cast<unsigned short>(std::rand());

    // get UTC time
    std::time_t sys_time{std::time(nullptr)};
    std::tm *utc_time = std::gmtime(&sys_time);    //GMT /equiv UTC

    //format year-month-dayThour-minute-second_[ID_]ident.ext
    std::string file_name{};
    if (utc_time && sys_time != (std::time_t)(-1))
    {
        file_name += std::to_string(utc_time->tm_year + 1900) + '-';
        file_name += std::to_string(utc_time->tm_mon + 1) + '-';
        file_name += std::to_string(utc_time->tm_mday) + 'T';
        file_name += std::to_string(utc_time->tm_hour) + '-';
        file_name += std::to_string(utc_time->tm_min) + '-';
        file_name += std::to_string(utc_time->tm_sec) + '_';
    }
    else
    {
        file_name += "TIME_ERROR_";
    }
    //file_name += std::to_string(static_cast<int>(log_id)) + '_';
    file_name += ident + '.';
    file_name += ext;

    return file_name;
}
```

-------------------------

