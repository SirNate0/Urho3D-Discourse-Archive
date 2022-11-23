miz | 2017-03-18 02:16:23 UTC | #1

I want to load in some data from a csv for a minigame.

I have code that will do it using std libraries:

    	std::ifstream file2("instructions.csv");

    	for (int row = 0; row < 10; ++row)
    	{
    		std::string line;
    		std::getline(file2, line);
    		if (!file2.good())
    			break;

    		std::stringstream iss(line);

    		for (int col = 0; col < 10; ++col)
    		{
    			std::string val;
    			std::getline(iss, val, ',');
    			if (!iss.good())
    				break;

    			instructionSet[row][col] = val.c_str();
    		}
    	}

Can I do the same thing with the Urho3d File Class? 

I want to use GetSubsystem<ResourceCache>()->GetFile() so I can get the csv from within a package file I've added to the resource cache.

How can I do this?

-------------------------

1vanK | 2017-01-13 09:29:50 UTC | #2

from void StaticModel::ApplyMaterialList(const String& fileName)

```
    SharedPtr<File> file = cache->GetFile(useFileName, false);
    while (!file->IsEof())
    {
           file->ReadLine());
    }
```

-------------------------

SirNate0 | 2017-01-12 19:00:18 UTC | #3

If you want to continue using your std library code you can also use the wrapper I made for File [http://discourse.urho3d.io/t/file-as-an-std-istream/2197](http://discourse.urho3d.io/t/file-as-an-std-istream/2197).
It's probably better to rewrite it for Urho, though. 
Also, if you have any text csv cells that contain comma's your parser will break (and normally text entries are wrapped in double quotes, though csv is a loose standard, so it varies).

-------------------------

