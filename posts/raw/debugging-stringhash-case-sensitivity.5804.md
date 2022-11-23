SirNate0 | 2020-01-04 17:07:49 UTC | #1

I recently rebuilt some older game code with a newer version of the library, and found a number of things broken by the (good) choice to switch to a case-sensitive StringHash implementation rather than a case-insensitive one. I thought I'd share some of the things I did to debug this and fix the problems I encountered.

Firstly, I rebuilt the library with URHO3D_HASH_DEBUG to enable the StringHash::Reverse() functionality, with one important change: I added the following to the StringHash constructors so that the old (lower-case) hashes are also added to the map. (Edit: It occured to me after I'd finished that instead of doing this the same behavior could be accomplished without modifying the engine beyond setting the flag by adding the lower case of every string as a hash in a for loop before going through and printing all of them)
```
    // Add the lowercase form as well
    Urho3D::String lower = String(str).ToLower();
    if (lower != str)
    {
        auto hash = StringHash(lower);
    }
```
[details='Full constructors with the above code']
```
StringHash::StringHash(const char* str) noexcept :
    value_(Calculate(str))
{
#ifdef URHO3D_HASH_DEBUG
    Urho3D::GetGlobalStringHashRegister().RegisterString(*this, str);
    // Add the lowercase form as well
    Urho3D::String lower = String(str).ToLower();
    if (lower != str)
    {
        auto hash = StringHash(lower);
    }
#endif
}

StringHash::StringHash(const String& str) noexcept :
    value_(Calculate(str.CString()))
{
#ifdef URHO3D_HASH_DEBUG
    Urho3D::GetGlobalStringHashRegister().RegisterString(*this, str.CString());
    Urho3D::String lower = str.ToLower();
    if (lower != str)
    {
        auto hash = StringHash(lower);
    }
#endif
}
```
[/details]

I then added the following code to the Stop() method of my application:
```

    auto reg = StringHash::GetGlobalStringHashRegister();
    if (reg)
    {
        LOGINFO("String Hashes At Close:");
        for (auto& hashStr : reg->GetInternalMap())
        {
//            LOGRAW(FormatString("{}: '{}',\n",hashStr.first_.Value(), hashStr.second_));
            String val = hashStr.second_;
            val.Replace("\n","\\n");
            val.Replace("\\","\\\\");
            val.Replace("\t","\\t");
            val.Replace("'","\\'");
            LOGRAW(FormatString("hashes[{}] = '{}'\n",hashStr.first_.Value(), val));
        }
    }
```
Copying the results from the end of the log to the following python script, I was able to lookup the required hashes that I had saved in some old ValueAnimation XML files.
```
#!/usr/bin/python3
hashes = {}

# ADD THE HASHES HERE (or in the {} above) as, for example hashes[9]='\t'

inv_map = {v: k for k, v in hashes.items()}

def urhohash(s):
    def SDBMHash(hash, c):
        return (0xffffffff&(0xffffffff&(c + (0xffffffff&(hash << 6)) + (0xffffffff&(hash << 16)))) - hash)
    h = 0;
    for c in map(ord,s):
        h = SDBMHash(h,c)
    return h

import sys
if len(sys.argv) == 1:
    print('Usage: hashLookup.py HASH_INTEGER_OR_STRING...')
    exit()
for arg in sys.argv[1:]:
    try:
        print(arg+':')
        print('  ' + repr(hashes[int(arg)]))
    except KeyError:
        print('HASH {} Not Found'.format(arg))
    except ValueError:
        #print('Could not convert {} to integer'.format(arg))
        try:
            print('  ' + str(inv_map[arg]))
            print('  %d' % urhohash(arg))
        except KeyError:
            print('Could not convert {} to integer & not found as hash'.format(arg))
            print('As hash: %d' % urhohash(arg))

```

<strike>Note that for some reason (I don't know if it was the log skipping some lines or some hashes not being added to the reverse map or if some code had been optimized out or what) but a few hashes that should have been in the list seemed to have been missed (but I was able to work out what they were, as there were only a few possibilities given my code).</strike> Edit: I figured it out. I had some conditional logic that depended on matching some of the other hashes that was never actually matched and it was coincidental (due to some other code setting some values rather than loading from XML) that any of the hashes inside the if statement were reversible, not due to any other errors.

-------------------------

