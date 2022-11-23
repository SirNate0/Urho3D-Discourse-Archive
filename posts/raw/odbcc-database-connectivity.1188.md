vivienneanthony | 2017-01-02 01:05:58 UTC | #1

Hello

Did someone make a OBCC/database component that can work natively with Urho3D? Could I see it. I finally got to the point of being to build executables sharing the same Urho3D added components.

So, easy, client, server, editor setup. Just now if I do the server I need it to be headless and be able to connect to a DB.

Vivienne

-------------------------

friesencr | 2017-01-02 01:05:58 UTC | #2

I highly recommend sqlite over odbc.  If you need more concurrency/throughput than sqlite you are asking for trouble.  sqlite is super portable.

[sqlite.org/](https://www.sqlite.org/)

-------------------------

weitjong | 2017-01-02 01:06:02 UTC | #3

I am currently working on an Android project that requires database query. So, I would take a shot for this. No promise. I will only push it when it is clean enough to meet Urho3D standard. I have some experience with big boys database products (Sybase and Oracle) from my previous works, but I have never used SQLite in an embedded environment before. So, any pointers would be much appreciated.

What I understand is this. ODBC is a standard API for database connection. It allows the application to connect to "any" database products that provide ODBC driver. I believe even SQLite also has one. But that is by no means the only way to connect to a database. There are other APIs such as JDBC for Java and DBI for Perl, not counting the native APIs provided by each database vendors.

I think I will have a quick look first on the native C/C++ API for SQLite. My goal is to be able make a query against a local SQLite database and falling back to send the query remotely over the network against the central DB server (not using SQLite) when local query gives empty resultset and if so, replicate (cache) the resultset into the local SQLite database so future similar query would be faster. That's all I can say for now.

-------------------------

rasteron | 2017-01-02 01:06:02 UTC | #4

I did some experimental port of Urho3D of sqlite3 back then through adding it as a component. It was just basic initialization and this was during Google Groups days. I'm still trying to confirm if I have lost the copy or just buried to my dev archives.  :unamused: 

One thing I do know that it is quite easy and what I have used is the [b]amalgamated[/b] version.

-------------------------

weitjong | 2017-01-02 01:06:02 UTC | #5

I can confirm that building the amalgamated SQLite library is a non-issue. I can also confirm that building the nanodbc (an ODBC library with MIT license) could be done easily as well. After some research, this is what I plan to do. Add new build option(s) to enable database subsystem support. The SQLite library will be built-in for both game engine deployment on the client and server side. On the server side, however, there is another option to use ODBC for database connection. This way individual application could integrate with any back-end database products with their own ODBC drivers. Of course, the game server is not mandatory as the client could just use REST to connect to any RESTful web service to get data from a central database (and this is beyond the scope of this discussion).

The devil is in the implementation details. Note that now the engine will have to deal with two kinds of API (SQLite native and ODBC), but I don't want the engine user to deal with two APIs as well for doing simple db query. The idea is to create yet another wrapper API similar to how Urho3D currently wraps other thirdparty libraries. However, it would probably be a good idea to still expose the underlying APIs by making the headers of SQLite and nanodbc available to library user so that user could still do more advanced things by invoking the underlying API directly if necessary. I hope the performance is still acceptable after adding this wrapper "layer", I reckon the db query performance will be determined more by how performant  the db itself.

Back to my Android project I am currently working on, I realize that I could just use the SDK provided SQLiteDatabase class to connect to a SQLite database and be done with it. End of story. However, this won't be of any use to other platforms though. So, I am avoiding this at the moment until I am running out of time.  :slight_smile: 

Any other thought and feedback are welcome before I am too far in the implementation.

-------------------------

vivienneanthony | 2017-01-02 01:06:03 UTC | #6

[quote="weitjong"]I can confirm that building the amalgamated SQLite library is a non-issue. I can also confirm that building the nanodbc (an ODBC library with MIT license) could be done easily as well. After some research, this is what I plan to do. Add new build option(s) to enable database subsystem support. The SQLite library will be built-in for both game engine deployment on the client and server side. On the server side, however, there is another option to use ODBC for database connection. This way individual application could integrate with any back-end database products with their own ODBC drivers. Of course, the game server is not mandatory as the client could just use REST to connect to any RESTful web service to get data from a central database (and this is beyond the scope of this discussion).

The devil is in the implementation details. Note that now the engine will have to deal with two kinds of API (SQLite native and ODBC), but I don't want the engine user to deal with two APIs as well for doing simple db query. The idea is to create yet another wrapper API similar to how Urho3D currently wraps other thirdparty libraries. However, it would probably be a good idea to still expose the underlying APIs by making the headers of SQLite and nanodbc available to library user so that user could still do more advanced things by invoking the underlying API directly if necessary. I hope the performance is still acceptable after adding this wrapper "layer", I reckon the db query performance will be determined more by how performant  the db itself.

Back to my Android project I am currently working on, I realize that I could just use the SDK provided SQLiteDatabase class to connect to a SQLite database and be done with it. End of story. However, this won't be of any use to other platforms though. So, I am avoiding this at the moment until I am running out of time.  :slight_smile: 

Any other thought and feedback are welcome before I am too far in the implementation.[/quote]

If you need help testing this. I wouldn't mind. Someone some integration into the event system would be nice. Once I can figure out while the drone in my code goes nuts (Left a message in the support.) I might be focusing on creating some form of game based economic system and someone might help me be a multi-game compatible network API which I might integrate the event system with.

-------------------------

rasteron | 2017-01-02 01:06:03 UTC | #7

[b]@weitjong[/b]

I know this could start again from square one with the integration but I was thinking maybe instead of just using sqlite just for database connectivity, why not use the modern ORM approach and port an existing C++ library. This way it will abstract database connections and could make use of other known and preferred drivers.

Some C++ ORM libraries out there, both under MIT.

[b]YB-ORM[/b] (MySQL, Oracle, SQLite, Firebird, Postgres)
[github.com/vnaydionov/yb-orm](https://github.com/vnaydionov/yb-orm)

[b]StactiveRecord[/b] (MySQL, SQLite, Postgres)
[findingscience.com/StactiveRecord/](http://findingscience.com/StactiveRecord/)
[github.com/bmuller/StactiveRecord](https://github.com/bmuller/StactiveRecord) 

Cheers. :slight_smile:

-------------------------

weitjong | 2017-01-02 01:06:03 UTC | #8

@rasteron. Thanks for feedback and the links. I am sure they are good although I have not used or heard of them before  :wink: . I use Hibernate on Java project when I need ORM. For me, those are the stuffs for the middle tier app server. IMHO, we should not lose focus of Urho3D library here. It is a game engine library. I don't think our library user would use Urho to build "business" application where object's state persists longer than the application itself. I believe for a simple in-game inventory system, a few immediate and/or prepared SQL statements are sufficient.

-------------------------

rasteron | 2017-01-02 01:06:03 UTC | #9

Hey no worries just throwing this by you. :slight_smile: .. and if you already made some progress with the sqlite integration then I guess it would be better to use that and btw ORMs are not just for business, it's a common misconception. :wink:

keep it up!

-------------------------

weitjong | 2017-01-02 01:06:09 UTC | #10

I have just pushed now both SQLite API and ODBC API support for database connection. Use the new build options URHO3D_DATABASE_SQLITE or URHO3D_DATABASE_ODBC to enable the database subsystem with the corresponding API. URHO3D_DATABASE_ODBC has higher precedence. Both underlying DB APIs are wrapped using a unified URHO3D_API. I haven't got time to expose those new URHO3D_API to our scripting subystems yet. So only C++ demo for now.

Currently my implementation just supports immediate SQL statement execution. Prepared statements will be added later when I have more time. Nevertheless the sample demo has been tested to be working fine with both underlying DB API on my Linux box. As usual I have not tested on other platforms yet. It will be great if you can help to test run it against your host system.

rake cmake URHO3D_DATABASE_SQLITE=1
rake make

or

rake cmake URHO3D_DATABASE_ODBC=1
rake make

For the latter, you need to install the SQLite-ODBC driver into your system ODBC driver manager. The driver can be downloaded from [ch-werner.de/sqliteodbc/](http://www.ch-werner.de/sqliteodbc/). Linux users need to build the driver from source (may need to tinker with the build script to make it work with your build environment). I have managed to do that but YMMV. Alternatively, install any ODBC driver that your OS currently provides and modify the ODBC connection string accordingly before running the demo.

-------------------------

vivienneanthony | 2017-01-02 01:06:09 UTC | #11

That's cool.  I have working a class to use Mysql Connector which seems to work so far. So, definitely I'll be able to do SQLite, ODBC, or MySQL connectivity.

-------------------------

weitjong | 2017-01-02 01:06:11 UTC | #12

I managed to install the mysql-connector-odbc driver to my system ODBC driver manager and tested successfully to connect to a mariadb (fork of mysql) database using a DSN connection string. I have enhanced the database demo to take a db connection string, so I can change the db connection to other database by issuing this command in the console input: "set connstr DSN=mytestmariadb". All the user/password/host/port and other details are stored in my local "~/.odbc.ini".

-------------------------

vivienneanthony | 2017-01-02 01:06:11 UTC | #13

[quote="weitjong"]I managed to install the mysql-connector-odbc driver to my system ODBC driver manager and tested successfully to connect to a mariadb (fork of mysql) database using a DSN connection string. I have enhanced the database demo to take a db connection string, so I can change the db connection to other database by issuing this command in the console input: "set connstr DSN=mytestmariadb". All the user/password/host/port and other details are stored in my local "~/.odbc.ini".[/quote]


This is my very simple component class. Basically, I can set the host and/or database, execute prepared or plain queries with or without results, run a simple check table exist. I want to add some functions to change the connectivity type and more advance logging including. I left preparing statements to code outside the class  because it can vary and allows this code to be a bit portable as long as MySql and Connector necessary files are installed.

[github.com/vivienneanthony/Urho ... ctorDB.cpp](https://github.com/vivienneanthony/Urho3D-gameeconomic/blob/master/Source/GameEconomic/GameEconomicComponents/connectorDB.cpp)

-------------------------

weitjong | 2017-01-02 01:06:11 UTC | #14

Thanks for sharing your code. All roads lead to Rome. In my approach, the new database subsystem is coupled with two DBAPIs: SQLite3 and ODBC. The native SQLite3 API is necessary if we want to embed and use SQLite database into the app itself without extra dependency. On the other hand, the ODBC API is designed for open possibility. We could connect to any ODBC-compliant databases like MySQL, PostgreSQL, Sybase, or even Oracle without changing much of the code because the new database subsystem interfaces with them using a standard ODBC layer. In this context, ODBC becomes a dependency, so this DBAPI should only be used for native application. What you have done coupled your code with MySQL native API and hence your app can only connect to MySQL database as the result. I am not saying this is wrong or bad. If you only intend to use just MySQL in your project then go for it.

-------------------------

vivienneanthony | 2017-01-02 01:06:11 UTC | #15

[quote="weitjong"]Thanks for sharing your code. All roads lead to Rome. In my approach, the new database subsystem is coupled with two DBAPIs: SQLite3 and ODBC. The native SQLite3 API is necessary if we want to embed and use SQLite database into the app itself without extra dependency. On the other hand, the ODBC API is designed for open possibility. We could connect to any ODBC-compliant databases like MySQL, PostgreSQL, Sybase, or even Oracle without changing much of the code because the new database subsystem interfaces with them using a standard ODBC layer. In this context, ODBC becomes a dependency, so this DBAPI should only be used for native application. What you have done coupled your code with MySQL native API and hence your app can only connect to MySQL database as the result. I am not saying this is wrong or bad. If you only intend to use just MySQL in your project then go for it.[/quote]

The intent in the future was t o create a overall DB Api after the first iteration I probably want to make it you any specific database system type can be used. MSQLite, Sybase, PostgreSQL, MySQL, Oracle, and Microsoft SQL. I just messed with this database type before so it's more familiarity.  So, like you said all roads lead to Rome. So, I think Urho is going have a serious DB api which is pretty good.

The only thing I have to figure out is setting up the network so it can be a both client/server at the same time. So, you can have a pool of servers, that connects to one master server.

-------------------------

weitjong | 2017-01-02 01:06:13 UTC | #16

I have attempted to expose the new C++ API for the database subsystem to the scripting side. Database demo in AngelScript is now in working condition. The demo in Lua, however, is still WIP. If any one with Lua expertise could help me to bind the VariantVector and StringVector from C++ to Lua side, I would be really greatful. At least the Lua demo can already establish a database connection. Currently it just does not know how to dump those values out due incomplete bindings.

-------------------------

cadaver | 2017-01-02 01:06:17 UTC | #17

Vector<String> should be exposed in LuaScript/ToluaUtils.cpp, see for example Resource/ResourceCache.pkg bindings. Can't help with Vector<Variant> though, as it's a non-POD type and so far every vector (except strings) that we push to Lua are either POD types or pointers.

-------------------------

weitjong | 2017-01-02 01:06:20 UTC | #18

Thanks for the pointer. Earlier I had already looked into ToluaUtils class but I was hoping Aster or someone else would come up after hearing my plea. :wink: Anyways, it looks like if you want a thing done well then do it yourself.

In the branch the only thing not yet implemented is the DbConnection::Finalize() method. However, that could wait until when the database subsystem later supports prepared statements and transaction management. I do not need those now so I will probably stop working on this branch for now. @cadaver, if you are OK with it then I will merge this branch into the master as it is now. The good news is the database demos in all three languages: C++, AS, and Lua, now have feature parity. I have tested Lua version using both SQLite and ODBC DBAPI. As usual all tests were done on Linux host system.

-------------------------

cadaver | 2017-01-02 01:06:20 UTC | #19

Yes, it's fine by me.

-------------------------

weitjong | 2017-01-02 01:06:22 UTC | #20

I am about to merge the branch anytime now once Travis CI builds all cleared. As mentioned in [github.com/urho3d/Urho3D/issues/820](https://github.com/urho3d/Urho3D/issues/820), the branch includes changes that will break existing Lua scripts as the VariantMap getter function signatures have been changed. For Linux and Mac users, you can use this one liner to migrate the scripts to use the new signature. Execute this in a terminal after cd-ing into the parent directory containing all your Lua scripts.

[code]
find . -type f -exec grep -lP "eventData:Get.+?\(.+?\)" {} \; |xargs -n 1  perl -pi.bak -e 's/eventData:Get(.+?)\((?:([^,)]+),\s*(.*?)|(.+?))\)/eventData[\3\4]:Get\1(\2)/g'
[/code]
It is left as an exercise for users on Windows.

-------------------------

cadaver | 2017-01-02 01:06:23 UTC | #21

Congrats on merging this rather major work!

-------------------------

vivienneanthony | 2017-01-02 01:07:54 UTC | #22

[quote="weitjong"]I have just pushed now both SQLite API and ODBC API support for database connection. Use the new build options URHO3D_DATABASE_SQLITE or URHO3D_DATABASE_ODBC to enable the database subsystem with the corresponding API. URHO3D_DATABASE_ODBC has higher precedence. Both underlying DB APIs are wrapped using a unified URHO3D_API. I haven't got time to expose those new URHO3D_API to our scripting subystems yet. So only C++ demo for now.

Currently my implementation just supports immediate SQL statement execution. Prepared statements will be added later when I have more time. Nevertheless the sample demo has been tested to be working fine with both underlying DB API on my Linux box. As usual I have not tested on other platforms yet. It will be great if you can help to test run it against your host system.

rake cmake URHO3D_DATABASE_SQLITE=1
rake make

or

rake cmake URHO3D_DATABASE_ODBC=1
rake make

For the latter, you need to install the SQLite-ODBC driver into your system ODBC driver manager. The driver can be downloaded from [ch-werner.de/sqliteodbc/](http://www.ch-werner.de/sqliteodbc/). Linux users need to build the driver from source (may need to tinker with the build script to make it work with your build environment). I have managed to do that but YMMV. Alternatively, install any ODBC driver that your OS currently provides and modify the ODBC connection string accordingly before running the demo.[/quote]


Any luck on the SQL lite database. I'm having trouble cross=compiling my MySql on Linux/Mingw or Windows. It seems to work on Linux fine but having hiccups getting it to run in a cross-compile environment. I mean my MySQL component/connector.

Vivienne

-------------------------

weitjong | 2017-01-02 01:07:55 UTC | #23

I think you have to be very clear in defining your issue. Is the issue with the code in the master branch when URHO3D_DATABASE_SQLITE enabled or is the issue with your code (component/connector whatever)? The URHO3D_DATABASE_SQLITE build option has been tested in our CI builds for all the Urho3D supported target platforms, including HTML5 using Emscripten. We do not have CI builds testing the URHO3D_DATABASE_ODBC build option so far because our Travis-CI server only has "ancient" C++ compiler toolchain and that we don't have client/server environment for running our tests should we able to build ODBC in the first place. For the issue in your own code, however, may I suggest to keep it in your own thread which you already created it. I think there is a rule in our forum to forbid double/cross posting. Thanks.

-------------------------

