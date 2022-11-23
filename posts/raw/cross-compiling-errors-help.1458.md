vivienneanthony | 2017-01-02 01:07:51 UTC | #1

Hello

Do anyone know why the line fails to compile under MiniGW but not GCC?

[quote]       serverConnection->SendMessage((unsigned int)NetMessageAuthenticateSend, true, true, msg, 0);[/quote]

Error 
[code][ 96%] Building CXX object Source/GameEconomic/GameEconomicGameClient/CMakeFiles/GameEconomicGameClient.dir/GameEconomicGameClientNetworking.cpp.obj
/media/home2/vivienne/Urho3D-gameeconomic/Source/GameEconomic/GameEconomicGameClient/GameEconomicGameClientNetworking.cpp: In member function ?void GameEconomicGameClient::SendNetworkMessage(NetworkMessageTypes, Urho3D::String)?:
/media/home2/vivienne/Urho3D-gameeconomic/Source/GameEconomic/GameEconomicGameClient/GameEconomicGameClientNetworking.cpp:337:1: error: ?class Urho3D::Connection? has no member named ?SendMessageA?
make[2]: *** [Source/GameEconomic/GameEconomicGameClient/CMakeFiles/GameEconomicGameClient.dir/GameEconomicGameClientNetworking.cpp.obj] Error 1
make[1]: *** [Source/GameEconomic/GameEconomicGameClient/CMakeFiles/GameEconomicGameClient.dir/all] Error 2
make: *** [all] Error 2
[/code]

In code
[code]
/// Send a network message
void GameEconomicGameClient::SendNetworkMessage(NetworkMessageTypes MessageType, String Message)
{
    /// If sending message is empty
    if (Message.Empty())
    {
        return; // Do not send an empty message
    }

    /// Get connection
    Network* network = GetSubsystem<Network>();
    Connection* serverConnection = network->GetServerConnection();

    /// this is the message to send the password
    if(MessageType == NetMessageAuthenticateSend)
    {
        /// create a new message
        VectorBuffer msg;
        msg.WriteString(Message);

        ///cout << "Sending NetMessageAuthenticateSend (" << Message.CString() << ")." <<endl;

        serverConnection->SendMessage((unsigned int)NetMessageAuthenticateSend, true, true, msg, 0);
    }

    return;
}
[/code]

I'm not sure whats going on when trying to cross-compile. It shows no error and compiles fine  but fails when I try to do it under MiniGW file cmake_minigw.sh

Vivienne

-------------------------

cadaver | 2017-01-02 01:07:51 UTC | #2

The SendMessageA error is related to macros in Windows headers. You could try doing #undef SendMessage

-------------------------

vivienneanthony | 2017-01-02 01:07:51 UTC | #3

[quote="cadaver"]The SendMessageA error is related to macros in Windows headers. You could try doing #undef SendMessage[/quote]

I put in the Networking Header

[code]#ifdef WIN32
#undef SendMessage
#endif[/code]

-------------------------

vivienneanthony | 2017-01-02 01:07:51 UTC | #4

Hi

The last problem is with . I'm trying to get the WIN32 to detect the MySQL include and library. I tried the find_library in the WIN32 part which it does not detect the library. I also tried hard coding the ROOT_DIR  which fails also.

The Linux side compiles but now the Win32 finds the includes if I hard code the include path but it does not add the libraries. Additional in the header

#include "mysql_connectionh" for example shows file not detected.

Vivienne


[code]# - Try to find Mysql-Connector-C++
# Once done, this will define
#
#  MYSQLCONNECTORCPP_FOUND - system has Mysql-Connector-C++ installed
#  MYSQLCONNECTORCPP_INCLUDE_DIRS - the Mysql-Connector-C++ include directories
#  MYSQLCONNECTORCPP_LIBRARIES - link these to use Mysql-Connector-C++
#
# The user may wish to set, in the CMake GUI or otherwise, this variable:
#  MYSQLCONNECTORCPP_ROOT_DIR - path to start searching for the module

set(MYSQLCONNECTORCPP_ROOT_DIR
        "${MYSQLCONNECTORCPP_ROOT_DIR}"
        CACHE
        PATHS
        "path goes here")

if(WIN32)
	set(MYSQLCONNECTORCPP_INCLUDE_DIR "/usr/local/include")
	set(MYSQLCONNECTORCPP_ROOT_DIR "/usr/local/include")
	set(MYSQLCONNECTORCPP_LIBRARY "/usr/local/lib")

     
else()
        find_path(MYSQLCONNECTORCPP_INCLUDE_DIR
                mysql_connection.h
                HINTS
                ${MYSQLCONNECTORCPP_ROOT_DIR}
                PATH_SUFFIXES
                include)
               
        find_library(MYSQLCONNECTORCPP_LIBRARY
                NAMES
                mysqlcppconn
                mysqlcppconn-static
                HINTS
                ${MYSQLCONNECTORCPP_ROOT_DIR}
                PATH_SUFFIXES
                lib64
                lib)

endif()

mark_as_advanced(MYSQLCONNECTORCPP_INCLUDE_DIR MYSQLCONNECTORCPP_LIBRARY)

include(FindPackageHandleStandardArgs)

find_package_handle_standard_args(MysqlConnectorCpp
        DEFAULT_MSG
        MYSQLCONNECTORCPP_INCLUDE_DIR
        MYSQLCONNECTORCPP_LIBRARY)

if(MYSQLCONNECTORCPP_FOUND)
        set(MYSQLCONNECTORCPP_INCLUDE_DIRS "${MYSQLCONNECTORCPP_INCLUDE_DIR}") # Add any dependencies here
        set(MYSQLCONNECTORCPP_LIBRARIES "${MYSQLCONNECTORCPP_LIBRARY}") # Add any dependencies here
        mark_as_advanced(MYSQLCONNECTORCPP_ROOT_DIR)
endif()  
[/code]

CMake Build
[code]vivienne@vivienne-System-Product-Name:/media/home2/vivienne/Urho3D-gameeconomic$ ./cmake_mingw.sh /media/home2/vivienne/GameEconomicUrhoWin  -DURHO3D_64BIT=0 -DURHO3D_GAMEECONOMICSERVER=0 -DURHO3D_GAMEECONOMICSERVERCLIENT=0 -DURHO3D_GAMEECONOMICGAMECLIENT=1  -DWIN32=0 -DCMAKE_BUILD_TYPE=RelWithDebInfo -DWIN32=0 -DURHO3D_SSE=0
-- DirectX SDK search skipped for MinGW. It is assumed that MinGW itself comes with the necessary headers & libraries
-- Configuring done
WARNING: Target "GameEconomicGameClient" requests linking to directory "/usr/local/lib".  Targets may link only to libraries.  CMake is dropping the item.
-- Generating done
-- Build files have been written to: /media/home2/vivienne/GameEconomicUrhoWin[/code]

Compile Results

[code]-- Generating done
-- Build files have been written to: /media/home2/vivienne/GameEconomicUrhoWin
[  5%] Built target FreeType
[  5%] Built target JO
[  5%] Built target LZ4
[  5%] Built target PugiXml
[  5%] Built target rapidjson
[ 17%] Built target SDL
[ 17%] Built target StanHull
[ 17%] Built target STB
[ 21%] Built target AngelScript
[ 21%] Built target Civetweb
[ 24%] Built target kNet
[ 25%] Built target Detour
[ 26%] Built target DetourCrowd
[ 26%] Built target DetourTileCache
[ 27%] Built target Recast
[ 32%] Built target Box2D
[ 48%] Built target Bullet
[ 48%] Built target GLEW
[ 49%] Built target LibCpuId
[ 76%] Built target Urho3D
[ 76%] Built target Urho3DPlayer
[ 95%] Built target Assimp
[ 95%] Built target AssetImporter
[ 95%] Built target OgreImporter
[ 95%] Built target PackageTool
[ 95%] Built target RampGenerator
[ 95%] Built target SpritePacker
[ 96%] Built target ScriptCompiler
[ 96%] Building CXX object Source/GameEconomic/GameEconomicGameClient/CMakeFiles/GameEconomicGameClient.dir/__/GameEconomicComponents/connectorDB.cpp.obj
/media/home2/vivienne/Urho3D-gameeconomic/Source/GameEconomic/GameEconomicComponents/connectorDB.cpp:13:30: fatal error: mysql_connection.h: No such file or directory
compilation terminated.
make[2]: *** [Source/GameEconomic/GameEconomicGameClient/CMakeFiles/GameEconomicGameClient.dir/__/GameEconomicComponents/connectorDB.cpp.obj] Error 1
make[1]: *** [Source/GameEconomic/GameEconomicGameClient/CMakeFiles/GameEconomicGameClient.dir/all] Error 2
make: *** [all] Error 2
[/code]

-------------------------

weitjong | 2017-01-02 01:07:55 UTC | #5

I have not used Mysql-Connector-C++ library before. So, what I am saying below may not be correct at all. If the CMake module you pasted here is not written by you, i.e. it is shipped as part of the said library then most probably you have not followed all the installation instructions provided by the library.

[code]if(WIN32)
   set(MYSQLCONNECTORCPP_INCLUDE_DIR "/usr/local/include")
   set(MYSQLCONNECTORCPP_ROOT_DIR "/usr/local/include")
   set(MYSQLCONNECTORCPP_LIBRARY "/usr/local/lib")[/code]
These lines of code suggests that the CMake module expect the library has been locally installed. So, have you installed the Mysql-connector to your local filesystem? Have you manually check those locations to see if the files you are looking for are actually there?

-------------------------

vivienneanthony | 2017-01-02 01:07:55 UTC | #6

[quote="weitjong"]I have not used Mysql-Connector-C++ library before. So, what I am saying below may not be correct at all. If the CMake module you pasted here is not written by you, i.e. it is shipped as part of the said library then most probably you have not followed all the installation instructions provided by the library.

[code]if(WIN32)
   set(MYSQLCONNECTORCPP_INCLUDE_DIR "/usr/local/include")
   set(MYSQLCONNECTORCPP_ROOT_DIR "/usr/local/include")
   set(MYSQLCONNECTORCPP_LIBRARY "/usr/local/lib")[/code]
These lines of code suggests that the CMake module expect the library has been locally installed. So, have you installed the Mysql-connector to your local filesystem? Have you manually check those locations to see if the files you are looking for are actually there?[/quote]

Yup. I tried that. I tried using the find_path and find_library which works fine under the linux if part but the win32 it does not detect. 

In MinGW compile it does not work.

-------------------------

weitjong | 2017-01-02 01:07:56 UTC | #7

Where did you run the MinGW build? On a Windows host or on a Linux box? If it is the former, for sure it won't work.

-------------------------

weitjong | 2017-01-02 01:07:56 UTC | #8

Actually, no cross that. I think it won't work for MinGW build on linux host as well, provided that you have pasted exactly what you have in your CMake module in the previous post. Assuming the said library has a portable code, so that it can be built using MinGW cross-compiling compiler toolchain, you have to install the cross-compiled binaries in the MinGW "rooted" installation location in your filesystem. Then you have to double check if the CMake module to find the library and its headers also works in this rooted location. If you look at our CMake/MinGW toolchain file (mingw.toolchain.cmake), you can see how this system root path is being set. For sure, you cannot expect MinGW cross-compiling toolchain to just reuse the library binary file that is built for Linux platform. HTH.

-------------------------

