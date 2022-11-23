itisscan | 2017-01-02 01:09:13 UTC | #1

In my project I try to use MariaDB Connector/ODBC. I downloaded MariaDB Connector 1.0 from [url]https://mariadb.com/kb/en/mariadb/about-mariadb-connector-odbc/[/url] for Win64 and ODBC driver 3.5 for Win64 from  [url]https://dev.mysql.com/downloads/connector/odbc/3.51.html[/url]

Then  I created DSN through  ODBC Data Source Administration.[url]http://imgur.com/FMunxtI[/url] As you see connection is successful.

Also when I run this code -

[code]
Database* database  = GetSubsystem<Database>();
DbConnection* connection = database->Connect("DSN=HangarsDSN");
[/code]

I get valid DbConnection pointer and code

[code]connection->IsConnected()[/code]

returns true. So I assume that connection to database is established.

But when I try to execute statement like - 
[code]
DbResult result = connection->Execute("select * from test", true);[/code]

I always get error - 

[code][Sun Jan 03 12:45:01 2016] ERROR: Could not execute: nanodbc:\Programming\Projec
ts\GameEconomics\Source\VS2013\Engine\3thParty\Urho3D-Hangars\Source\ThirdParty\
nanodbc\src\nanodbc.cpp:1036[/code]

In nanodbc.cpp on 1036 line is following code - 

[code] void open(class connection& conn)
    {
        close();
        RETCODE rc;
        NANODBC_CALL_RC(
            SQLAllocHandle
            , rc
            , SQL_HANDLE_STMT
            , conn.native_dbc_handle()
            , &stmt_);
        open_ = success(rc);
        if(!open_)
            NANODBC_THROW_DATABASE_ERROR(stmt_, SQL_HANDLE_STMT);
        conn_ = conn;
    }[/code]

I can't figure out why it can't execute. Is it invalid connection to database, or something wrong with ODBC driver. Also I tried to pass different statements, but got the same error.

SQL server locates on web hosting - [url]https://www.host.sk/[/url]

Maybe someone knows what the problem is ?

-------------------------

itisscan | 2017-01-02 01:09:13 UTC | #2

I have found out that it is problem with connection. If I run MySql server locally, statement's execution works. 

Does anyone have any ideas why remote connection does not work ?

-------------------------

gwald | 2017-01-02 01:09:13 UTC | #3

try an ip address or fully qualified name ie: host.domain
Check firewall settings/ip settings etc

-------------------------

shlomok | 2017-01-02 01:09:13 UTC | #4

Did you enable remote access on MariaDB?
See: [cyberciti.biz/tips/how-do-i- ... erver.html](http://www.cyberciti.biz/tips/how-do-i-enable-remote-access-to-mysql-database-server.html)

-------------------------

