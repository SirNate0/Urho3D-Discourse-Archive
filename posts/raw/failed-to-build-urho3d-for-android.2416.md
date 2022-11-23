att | 2017-01-02 01:15:17 UTC | #1

Hi, I just updated the last code, and compiled it, but failed for android platform, following is the errors:

......
error: ISO C90 forbids mixed declarations and code [-Werror=declaration-after-statement]
const char *str;
str = (*mEnv)->GetStringUTFChars(mEnv, filesDir, 0);
error: ISO C90 forbids mixed declarations and code [-Werror=declaration-after-statement]
size_t length = strlen(str) + 1;
......
error: ISO C90 forbids mixed declarations and code [-Werror=declaration-after-statement]
jobject assetManager = (*mEnv)->CallObjectMethod(mEnv, context, mid);
......

-------------------------

weitjong | 2017-01-02 01:15:18 UTC | #2

This is now fixed in master branch.

-------------------------

