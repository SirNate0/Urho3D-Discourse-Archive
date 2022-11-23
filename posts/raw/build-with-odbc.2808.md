anako126n | 2017-02-20 18:13:15 UTC | #1

After several hours (nearly two days) I'm giving up on trying to work out why it doesn't work, hopefully asking for some help/ guidances on how to build with ODBC will help me get through the building process.

Currently I'm on Windows building with Cmake-Gui 3.8.0 with the following installed:

MariaDB 10.1
MariaDB Connector C 64-bit
MariaDB ODBC Driver 64-bit
MySQL - Connector ODBC 3.51
SQLite ODBC Driver


Compiler used VS 2013

Cmake doesn't give me an option to build with ODBC, whenever I build via command line with ODBC flag nothing happens.

There has to be something I'm missing and I just simply cannot work it out.

Many thanks in advance

-------------------------

weitjong | 2017-02-21 00:40:48 UTC | #2

You need VS 2015 or better, otherwise that option is simply ignored even when passed by force. CMake-GUI does not show it as a valid option for a good reason.

-------------------------

