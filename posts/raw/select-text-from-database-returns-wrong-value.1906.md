itisscan | 2017-01-02 01:11:23 UTC | #1

I use MariaDB 5.5 (x64) on Windows 7 and MariaDB ODBC driver 1.0 in order to make connection. 

I have table 'location' with 4 columns (Id, World, Location, Scene). 'Scene' column saves text as LONGTEXT datatype. Let's say it contains this value - 

[url]http://pastebin.com/h70h83gf[/url]

When I try to get this value from the program with command - 

[code]DbConnection connection->Execute("SELECT A.Scene FROM location A WHERE A.Name = "EarthBaseStation";", true)[/code]

I get wrong value like this - [url]http://pastebin.com/21ZitRnV[/url]

It seems that result was splitted into two chunks. First chunk was duplicated from the [b]29 line[/b] . In the result i get 2 first chunks. 

I have tried to execute  query -

[code]SELECT A.Scene FROM location A WHERE A.Name = "EarthBaseStation";[/code] 
from the command prompt. Then all works fine.  

Also if i reduce value size, it is text size, at least on half, then i get the right result. 

How i can fix it, in order to get the right value from the program ? 

Thanks.

-------------------------

weitjong | 2017-01-02 01:11:23 UTC | #2

I could not make head nor tail of your pastebin. The DbConnection::Execute() method returns DbResult object. So, have you use a debugger to check on this returned object directly? If you did and the problem was really coming from the text size of the LONGTEXT datatype then you can file a bug to nanodbc project, assuming if there is nothing wrong with our thin wrapper implementation. If you look at the DbConnection class for ODBC then you can see there is really nothing much in it (only wrapper code).

-------------------------

vivienneanthony | 2017-01-02 01:11:24 UTC | #3

[quote="itisscan"]I use MariaDB 5.5 (x64) on Windows 7 and MariaDB ODBC driver 1.0 in order to make connection. 

I have table 'location' with 4 columns (Id, World, Location, Scene). 'Scene' column saves text as LONGTEXT datatype. Let's say it contains this value - 

[url]http://pastebin.com/h70h83gf[/url]

When I try to get this value from the program with command - 

[code]DbConnection connection->Execute("SELECT A.Scene FROM location A WHERE A.Name = "EarthBaseStation";", true)[/code]

I get wrong value like this - [url]http://pastebin.com/21ZitRnV[/url]

It seems that result was splitted into two chunks. First chunk was duplicated from the [b]29 line[/b] . In the result i get 2 first chunks. 

I have tried to execute  query -

[code]SELECT A.Scene FROM location A WHERE A.Name = "EarthBaseStation";[/code] 
from the command prompt. Then all works fine.  

Also if i reduce value size, it is text size, at least on half, then i get the right result. 

How i can fix it, in order to get the right value from the program ? 

Thanks.[/quote]

It seems to be a problem with NanoOdbc side. I'm going look at the source code see what the results string type or is there some limit.

-------------------------

vivienneanthony | 2017-01-02 01:11:24 UTC | #4

This might be useful.

[github.com/lexicalunit/nanodbc/issues/38](https://github.com/lexicalunit/nanodbc/issues/38)

[github.com/lexicalunit/nanodbc/issues/32](https://github.com/lexicalunit/nanodbc/issues/32)

I'm going install the latest GCC on Ubuntu 14.04 and maybe port the in the latest nanoodbc which might help.

-------------------------

weitjong | 2017-01-02 01:11:24 UTC | #5

I don't think they are related.  In any case our nanodbc subtree was rebased last Jan, so it is quite recent.

-------------------------

itisscan | 2017-01-02 01:11:24 UTC | #6

[quote="weitjong"]I could not make head nor tail of your pastebin. The DbConnection::Execute() method returns DbResult object. So, have you use a debugger to check on this returned object directly? If you did and the problem was really coming from the text size of the LONGTEXT datatype then you can file a bug to nanodbc project, assuming if there is nothing wrong with our thin wrapper implementation. If you look at the DbConnection class for ODBC then you can see there is really nothing much in it (only wrapper code).[/quote]

I get DbResult object, check if it returns some rows (vector's size != 0), then get first value as String. Look,

[code]
DbResult result = m_pConnection->Execute("SELECT A.Scene FROM location A WHERE A.Name = "EarthBaseStation";", true);
const Vector<VariantVector>& rows = result.GetRows();
if (rows.Size() == 0)
{
	success = false;
}
else
{
	for (auto it = rows.Begin(); it != rows.End(); it++)
	{
		// get scene as string
		sceneStr = it->Begin()->GetString();
	}
}

URHO3D_LOGDEBUG(sceneStr);

[/code]

When I debug the program, I see that sceneStr has wrong value, in our case this one with duplicate - [url]http://pastebin.com/21ZitRnV[/url], 
but should has - [url]http://pastebin.com/h70h83gf[/url]

-------------------------

weitjong | 2017-01-02 01:11:24 UTC | #7

Have you tried to step into the nanodbc method call? What I am trying to say is, you can help to first isolate the problem. If it is inside nanodbc the file a bug in nanodbc project. If it is inside Urho3D then file a bug in Urho3D project.

-------------------------

itisscan | 2017-01-02 01:11:24 UTC | #8

[quote="weitjong"]Have you tried to step into the nanodbc method call? What I am trying to say is, you can help to first isolate the problem. If it is inside nanodbc the file a bug in nanodbc project. If it is inside Urho3D then file a bug in Urho3D project.[/quote]

Okey, I will try to step into the nanodbc method.

-------------------------

itisscan | 2017-01-02 01:11:24 UTC | #9

[quote="weitjong"]Have you tried to step into the nanodbc method call? What I am trying to say is, you can help to first isolate the problem. If it is inside nanodbc the file a bug in nanodbc project. If it is inside Urho3D then file a bug in Urho3D project.[/quote]

I have debugged nanodbc method call. 

I think the bug is in nanodbc, because when query was successfully executed and urho3d try to bind primitive data type that Variant class support, it's called this method

[code]  
// All other types are stored using their string representation in the Variant
colValues[i] = result.resultImpl_.get<nanodbc::string_type>((short)i).c_str();[/code]  

in the result we step into below method, where nanodbc reads row's data in the buffer, look -  

[code] 
template<>
inline void result::result_impl::get_ref_impl<string_type>(short column, string_type& result) const
{
    const bound_column& col = bound_columns_[column];
    const SQLULEN column_size = col.sqlsize_;

    switch(col.ctype_)
    {
        case SQL_C_CHAR:
        {
            if(col.blob_)
            {
                // Input is always std::string, while output may be std::string or std::wstring
                std::stringstream ss;
                char buff[1024] = {0};
                std::size_t buff_size = sizeof(buff);
                SQLLEN ValueLenOrInd;
                SQLRETURN rc;
                void* handle = native_statement_handle();
                do
                {
                    NANODBC_CALL_RC(
                        SQLGetData
                        , rc
                        , handle            // StatementHandle
                        , column + 1        // Col_or_Param_Num
                        , SQL_C_CHAR        // TargetType
                        , buff              // TargetValuePtr
                        , buff_size         // BufferLength
                        , &ValueLenOrInd);  // StrLen_or_IndPtr
                    if (ValueLenOrInd > 0)
                        ss << buff;
                } while(rc > 0);
                convert(ss.str(), result);
            }
            else
            {
                const char* s = col.pdata_ + rowset_position_ * col.clen_;
                const std::string::size_type str_size = std::strlen(s);
                result.assign(s, s + str_size);
            }
            return;
        }
....
....
....
[/code]

I have checked the [b]do { ...  } while(rc > 0); loop[/b]. I noticed that if text's size is 1787 character, then in the first iteration we get 1024 first characters and remains to read 715 characters. 
However it looks like in the second iteration we do not start reading from 1025 character, but start reading from the beginning. In the result we get the wrong result that I have described previous.

I suppose the bug is how nanodbc reads the row's data in the buffer or it just consequence to wrong executing of query. 

I will file a bug in nanodbc project.

-------------------------

vivienneanthony | 2017-01-02 01:11:25 UTC | #10

[quote="weitjong"]Have you tried to step into the nanodbc method call? What I am trying to say is, you can help to first isolate the problem. If it is inside nanodbc the file a bug in nanodbc project. If it is inside Urho3D then file a bug in Urho3D project.[/quote]

Thanks to  Itisscan. Numerous issues been found with Nanodbc. Maybe the Urho3D repo can be updated to the current master or release. I was able to merge the copy to build and is testing out. It seems to be okay.

[github.com/lexicalunit/nanodbc/issues/117](https://github.com/lexicalunit/nanodbc/issues/117)

Vivienne

-------------------------

weitjong | 2017-01-02 01:11:26 UTC | #11

Our nanodbc subtree has been rebased against upstream 2.12.4 and push to our master branch.

-------------------------

weitjong | 2017-01-02 01:11:26 UTC | #12

My apology. I realized I forgot to do a subtree push before rebasing and had to do merging work all over again. Fortunately the redo part can be done rather quickly with substree. However, I have to force push the changes one more time to our master branch. So, for those who have pulled down master branch earlier, you may find that your Urho3D project source tree is out of sync with remote master now. To recover that, simply reset your local master branch to a last known good commit, say 23c8af64c777090c6d38b9c063c498f9336784fb, then git pull again as per normal. For those that need explicit instruction, see below.

[code]$ git reset --hard 23c8af64c777090c6d38b9c063c498f9336784fb && git pull[/code]
I hope I don't have to create a youtube video for that  :wink: .

-------------------------

