vivienneanthony | 2017-01-02 00:59:31 UTC | #1

Hello

Is this line of code correct?

Vivienne

[quote]
void ExistenceClient::LoadAccount(void)
{
    string accountconfigfilename=ACCOUNTFILE;

    XMLFile * accountconfig =  new XMLFile(context_);
    accountconfig -> Load(File((const string &) accountconfigfilename,FILE_READ));

}[/quote]

-------------------------

aster2013 | 2017-01-02 00:59:41 UTC | #2

[code]void ExistenceClient::LoadAccount(void)
{
    String accountconfigfilename=ACCOUNTFILE;

    ResoruceCache* cache = GetSubsystem<ResoruceCache>();
    XMLFile* accountconfig = cache->GetResource<XMLFile>(accountconfigfilename);

    // ...

}[/code]

-------------------------

vivienneanthony | 2017-01-02 00:59:42 UTC | #3

[quote="aster2013"][code]void ExistenceClient::LoadAccount(void)
{
    String accountconfigfilename=ACCOUNTFILE;

    ResoruceCache* cache = GetSubsystem<ResoruceCache>();
    XMLFile* accountconfig = cache->GetResource<XMLFile>(accountconfigfilename);

    // ...

}[/code][/quote]

Thanks. I'll give it a try tomorrow.

-------------------------

vivienneanthony | 2017-01-02 00:59:42 UTC | #4

[quote="aster2013"][code]void ExistenceClient::LoadAccount(void)
{
    String accountconfigfilename=ACCOUNTFILE;

    ResoruceCache* cache = GetSubsystem<ResoruceCache>();
    XMLFile* accountconfig = cache->GetResource<XMLFile>(accountconfigfilename);

    // ...

}[/code][/quote]

I tried the code it seems to work. I am trying the opposite instead of reading now writing. I'm getting a compiliation error. I understand the XML is in a resource path. From what I see, there's 2 or 3 ways to write a file so I think I'm getting confused and putting it all together somehow.

This is the response code.  I am thinking of keeping the format xml but making all the account information highly encrypted.

[quote]// load account info
void ExistenceClient::SaveAccount(void)
{
    String accountconfigfilename=ACCOUNTFILE;

    ResourceCache* cache = GetSubsystem<ResourceCache>();

    XMLFile * accountconfig = cache->GetResource<XMLFile>(accountconfigfilename);


    XMLElement configElem = accountconfig -> CreateRoot("account");
    XMLElement idElement = configElem.CreateChild("uniqueid");
    XMLElement emailElement= configElem.CreateChild("email");
    XMLElement firstnameElement  = configElem.CreateChild("firstname");
    XMLElement middlenameElement  = configElem.CreateChild("middlename");
    XMLElement lastnameElement  = configElem.CreateChild("lastname");
    XMLElement passwordElement = configElem.CreateChild("password");

    idElement.SetString("uniqueid", "test");
    emailElement.SetString("email", "test");
    firstnameElement.SetString("firstname", "test");
    middlenameElement.SetString("middlename", "test");
    lastnameElement.SetString("lastname", "test");
    passwordElement.SetString("passord", "test");

	accountconfig -> Save(File(cache->GetResourceFileName<XMLFile>(accountconfigfilename), FILE_WRITE));


	return;
}
[/quote]

-------------------------

Mike | 2017-01-02 00:59:42 UTC | #5

Try this:

[code]
File saveFile(context_, cache->GetResourceFileName<XMLFile>(accountconfigfilename), FILE_WRITE);
accountconfig->Save(saveFile);
[/code]

-------------------------

vivienneanthony | 2017-01-02 00:59:42 UTC | #6

[quote="Mike"]Try this:

[code]
File saveFile(context_, cache->GetResourceFileName<XMLFile>(accountconfigfilename), FILE_WRITE);
accountconfig->Save(saveFile);
[/code][/quote]

This is the message I get now in response to the "File savefile(...)". Everything else seems correct. So, if anyone knows whats wrong. It will be appreciated. I'll take a crack at it much later this evening.

[quote]/media/home2/vivienne/Existence/Source/ExistenceApps/ExistenceClient/ExistenceClient.cpp|1262|error: expected primary-expression before ?>? token|[/quote]


[code]// load account info
void ExistenceClient::SaveAccount(void)
{
    String accountconfigfilename=ACCOUNTFILE;

    ResourceCache * cache = GetSubsystem<ResourceCache>();

 File saveFile(context_, cache->GetResourceFileName<XMLFile>(accountconfigfilename), FILE_WRITE);

    XMLFile * accountconfig = cache->GetResource<XMLFile>(accountconfigfilename);

    XMLElement configElem = accountconfig -> CreateRoot("account");
    XMLElement idElement = configElem.CreateChild("uniqueid");
    XMLElement emailElement= configElem.CreateChild("email");
    XMLElement firstnameElement  = configElem.CreateChild("firstname");
    XMLElement middlenameElement  = configElem.CreateChild("middlename");
    XMLElement lastnameElement  = configElem.CreateChild("lastname");
    XMLElement passwordElement = configElem.CreateChild("password");

    idElement.SetString("uniqueid", "test");
    emailElement.SetString("email", "test");
    firstnameElement.SetString("firstname", "test");
    middlenameElement.SetString("middlename", "test");
    lastnameElement.SetString("lastname", "test");
    passwordElement.SetString("passord", "test");

    accountconfig->Save(saveFile);

	return;
}
[/code]

-------------------------

vivienneanthony | 2017-01-02 00:59:44 UTC | #7

[quote="Mike"]Try this:

[code]
File saveFile(context_, cache->GetResourceFileName<XMLFile>(accountconfigfilename), FILE_WRITE);
accountconfig->Save(saveFile);
[/code][/quote]

I redid the code. I was using Urho3D - String similiar to the standard string class. Additionally, realized I cannot use resource because it's blank. Basically causing a segmentation error.  This code seems to work.

[code]// save account info
void ExistenceClient::SaveAccount(void)
{
    String accountconfigfilename;

    ResourceCache * cache = GetSubsystem<ResourceCache>();
    FileSystem * filesystem = GetSubsystem<FileSystem>();

    //cout << filesystem->GetProgramDir().CString()+"CoreData/"+accountconfigfilename.CString();

    accountconfigfilename.Append(filesystem->GetProgramDir().CString());
    accountconfigfilename.Append("CoreData/");
    accountconfigfilename.Append(ACCOUNTFILE);

    File saveFile(context_, accountconfigfilename.CString(), FILE_WRITE);

    // check if account file exist
    if(!filesystem->FileExists(accountconfigfilename.CString()))
    {
        cout << "\r\nAccount file ("<< accountconfigfilename.CString() << ") does not exist.";
    }

    XMLFile * accountconfig  = new XMLFile(context_);

    XMLElement configElem = accountconfig -> CreateRoot("account");
    XMLElement idElement = configElem.CreateChild("uniqueid");
    XMLElement emailElement= configElem.CreateChild("email");
    XMLElement firstnameElement  = configElem.CreateChild("firstname");
    XMLElement middlenameElement  = configElem.CreateChild("middlename");
    XMLElement lastnameElement  = configElem.CreateChild("lastname");
    XMLElement passwordElement = configElem.CreateChild("password");

    idElement.SetString("uniqueid", "test");
    emailElement.SetString("email", "test");
    firstnameElement.SetString("firstname", "test");
    middlenameElement.SetString("middlename", "test");
    lastnameElement.SetString("lastname", "test");
    passwordElement.SetString("passord", "test");

    accountconfig->Save(saveFile);

    return;
}[/code]

-------------------------

