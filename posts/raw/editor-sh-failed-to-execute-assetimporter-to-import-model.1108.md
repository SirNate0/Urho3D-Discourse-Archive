gabdab | 2017-01-02 01:05:30 UTC | #1

Editor.sh crashes on 
Urho3D-1.4-Linux-64bit-STATIC
after issueing the import model command , stating : Editor.sh  Failed to execute AssetImporter to import model
The Resource Path being correct .
[SOLUTION]
..importing models trough Resource Browser does the job .

-------------------------

cadaver | 2017-01-02 01:05:31 UTC | #2

In Linux packaged builds the tool subdirectory didn't exist, right? I've now inserted code in the master branch to execute AssetImporter either from the executable directory or executable directory/tool

-------------------------

