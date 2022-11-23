huminzheng | 2021-07-22 09:40:48 UTC | #1

Hi guys!
  I  bulid Urho with emscripten on Windows success,but I still have some troubles,pls give some advise.Thanks a lot!
   *.js:1 POST http://localhost:5000/stdio.html 404 (Not Found)

-------------------------

Bluemoon | 2021-07-22 12:09:19 UTC | #2

Hello @huminzheng 

I have some questions:

Was your build successful?
If it was successful could you run any of the html samples?
At which point in build/run do you get the error you specified?

-------------------------

huminzheng | 2021-07-23 01:17:18 UTC | #3

Yes,thanks for you reply! I bulid successfull. This is the  section in *.js file. It containts the "stdio.xml".

var emrun_should_close_itself=false;var postExit=function(msg){var http=new XMLHttpRequest;http.open("POST","stdio.html",false);http.send(msg);try{window.close()}catch(e){}};var post=function(msg){var http=new XMLHttpRequest;++emrun_num_post_messages_in_flight;http.onreadystatechange=function(){if(http.readyState==4){if(--emrun_num_post_messages_in_flight==0&&emrun_should_close_itself)postExit("^exit^"+EXITSTATUS)}};http.open("POST","stdio.html",true);http.send(msg)};if(document.URL.search("localhost")!=-1||document.URL.search(":6931/")!=-1){var emrun_http_sequence_number=1;var prevPrint=out;var prevErr=err;Module["addOnExit"](function(){if(emrun_num_post_messages_in_flight==0)postExit("^exit^"+EXITSTATUS);else emrun_should_close_itself=true});out=function(text){post("^out^"+emrun_http_sequence_number+++"^"+encodeURIComponent(text));prevPrint(text)};err=function(text){post("^err^"+emrun_http_sequence_number+++"^"+encodeURIComponent(text));prevErr(text)};var tryToSendPageload=function(){try{post("^pageload^")}catch(e){setTimeout(tryToSendPageload,50)}};tryToSendPageload()}};if(typeof Module!=="undefined"&&typeof document!=="undefined")emrun_register_handlers()}

-------------------------

weitjong | 2021-07-24 06:49:54 UTC | #4

Don't just show us the error you got, instead show us how you got there in the first place. Show us the steps to reproduce your issue.

-------------------------

huminzheng | 2021-08-02 08:00:14 UTC | #5

Hello @weitjong .It seems likes this issue. https://github.com/emscripten-core/emscripten/issues/5888. But I still do not know how to handle this .

-------------------------

weitjong | 2021-08-02 14:26:46 UTC | #6

I am afraid I am not able to help until I have more context.

-------------------------

