ghidra | 2017-01-02 01:04:05 UTC | #1

It was mentioned to me that I am looking for a "factory".

When making a new scriptInstance in scripting with a base class of "example". I can pass a string "example1" and make a instance like so:
[code]
//pseudo code
void make_example(String c){
     example@ ex1_ = cast<example>(node.CreateScriptObject(scriptFile, c));
}
make_example("example1");
make_example("example2");
make_example("example3");
make_example("example4");
//assuming i have 4 other example classes that extend the base example class
[/code]

Now what I need at the moment is something similar, however, I am not making scriptinstances. I am trying to add a class ONTO my script instance for supplemental information. I have attached my class like the above example. And after words I pass in another string for it to trigger creating another class onto itself. But I am uncertain how to create that class with a string the same way I can a scriptInstance.

NOT WORKING CODE EXAMPLE:
[code]
void make_class(String c){
     new [c]();
}
make_class("classA");
make_class("classB");
make_class("classC");
[/code]

currently my solution is a little meh:
[code]
make_class(String c){
     if(c=="class") mc_ = class();
     if(c=="classA") mc_ = classA();
     if(c=="classB") mc_ = classB();
     if(c=="classC") mc_ = classC();
}
[/code]

-------------------------

